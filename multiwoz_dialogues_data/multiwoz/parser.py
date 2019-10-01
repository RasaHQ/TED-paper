import os
import json
from termcolor import colored
import random
import re

from multiwoz.domain_info import log_problem
import multiwoz.domain_info

from multiwoz.downloader import multiwoz_download
from multiwoz.intent_parser import IntentParser
from multiwoz.slot_parser import SlotParser
from multiwoz.dialog_turn import DialogTurn
from multiwoz.dialog_turn import DialogAction
from multiwoz.dialog_turn import DialogSlot
from multiwoz.dialog_turn import DialogIntent


class MultiWOZParser:

    def __init__(self, directory="", version="2.0", simplification_level=2,
                 add_status_slots=True):
        """
        Downloads the MultiWOZ-2 data set and stores all the interesting file names.
        This does not load the data into RAM.
        :param directory:
        """
        self.directory = directory
        unpacked_dir = multiwoz_download(directory, version=version)

        self.data_file_name = os.path.abspath(
            os.path.join(unpacked_dir, "data.json")
        )
        self.ontology_file_name = os.path.abspath(
            os.path.join(unpacked_dir, "ontology.json")
        )
        self.acts_file_name = os.path.abspath(
            os.path.join(unpacked_dir, "dialogue_acts.json")
        )
        self.testlist_file_name = os.path.abspath(
            os.path.join(unpacked_dir, "testListFile.json")
        )
        self.vallist_file_name = os.path.abspath(
            os.path.join(unpacked_dir, "valListFile.json")
        )

        self.add_status_slots = add_status_slots
        self.slot_parser = SlotParser(simplify=simplification_level)

        assert os.path.exists(self.data_file_name)
        assert os.path.exists(self.acts_file_name)
        assert os.path.exists(self.testlist_file_name)
        assert os.path.exists(self.vallist_file_name)

        self._data = None
        self._ontology = None
        self._names = None
        self._acts = None
        self._test_list = None
        self._validation_list = None
        self._domain_substitute = None

        self._sub_ontology = None
        self._pattern_ontology = None
        self._pattern_time = None
        self._pattern_number = None
        self._pattern_weekday = None
        self._pattern_refnumber = None
        self._pattern_pricerange = None
        self._pattern_area = None
        self._pattern_hotel_type = None
        self._pattern_hotel_name = None
        self._pattern_attraction_type = None
        self._pattern_attraction_name = None
        self._pattern_restaurant_name = None
        self._pattern_restaurant_food = None
        self._pattern_location = None

    @property
    def data(self):
        # Load data on demand
        if self._data is None:
            with open(self.data_file_name, "r") as read_file:
                self._data = json.load(read_file)

        # Return the data
        return self._data

    @property
    def ontology(self):
        # Load data on demand
        if self._ontology is None:
            with open(self.ontology_file_name, "r") as read_file:
                self._ontology = json.load(read_file)

        # Return the data
        return self._ontology

    @property
    def story_names(self):
        if self._names is None:
            self._names = list(self.data)
        return self._names

    @property
    def acts(self):
        # Load data on demand
        if self._acts is None:
            with open(self.acts_file_name, "r") as read_file:
                self._acts = json.load(read_file)

        # Return the data
        return self._acts

    @property
    def validation_list(self):
        # Load data on demand
        if self._validation_list is None:
            with open(self.vallist_file_name, "r") as read_file:
                self._validation_list = read_file.read().split()

        # Return the data
        return self._validation_list

    @property
    def test_list(self):
        # Load data on demand
        if self._test_list is None:
            with open(self.testlist_file_name, "r") as read_file:
                self._test_list = read_file.read().split()

        # Return the data
        return self._test_list

    def __call__(self, story_name, verbose=0):
        return self.parse_story(story_name, verbose)

    def parse_action(self, action_list):
        actions = self._parse_action_aggregated(action_list)

        # Substitute booking domain
        for action in actions:
            if action.domain == "booking":
                if self._domain_substitute:
                    action.domain = self._domain_substitute
                    if action.name not in ["advise", "reply"]:
                        if action.tags:
                            action.tags.append("booking")
                        else:
                            action.tags = ["booking"]
                    else:
                        # Let `reply_booking_DOMAIN` be just `reply_DOMAIN`
                        action.tags = None
                    action.store_in_domain_info()
                else:
                    log_problem({"type": "unclear_booking_domain"})
                    return []

        # Sort actions
        actions.sort(key=lambda a: a.sort_key)

        # Post-process
        actions2 = []
        for action in actions:

            # Remove repetitions of actions
            if actions2 == [] or action.to_string() != actions2[-1].to_string():

                # Insert status slots when appropriate
                if self.add_status_slots:
                    if (action.name == "inform" and action.tags and "booking" in action.tags) or \
                            (action.name in ["offerbook"]):
                        slot = DialogSlot({f"{action.domain}_status": "unique"})
                        slot.store_in_domain_info()
                        actions2.append(slot)
                        actions2.append(action)
                    elif action.name in ["nobook", "nooffer"]:
                        slot = DialogSlot({f"{action.domain}_status": "NA"})
                        slot.store_in_domain_info()
                        actions2.append(slot)
                        actions2.append(action)
                    elif action.name in ["book", "offerbooked"]:
                        actions2.append(action)
                        slot = DialogSlot({f"{action.domain}_status": "booked"})
                        slot.store_in_domain_info()
                        actions2.append(slot)
                    else:
                        actions2.append(action)
                else:
                    actions2.append(action)
        actions = actions2

        return actions

    def _parse_action_aggregated(self, action_list):
        action_infos = []
        if type(action_list) is not dict:
            if type(action_list) is str and action_list == "No Annotation":
                log_problem({"type": "no_annotation"})
            else:
                log_problem({"type": "bad_action_list_type", "action_list": action_list})
            return []
        for base_action, slots in action_list.items():
            # Parse key (basic action and domain)
            if "-" in base_action:
                domain, action_name = base_action.split("-")
            else:
                # Single-letter actions like "A" or "N" are actually never requested
                log_problem({"type": "bad_action_format", "base_action": base_action})
                return []

            action_name = action_name.lower()

            # Parse value (slots)
            for slot in slots:
                if slot == ["none", "none"]:
                    spec = ""
                else:
                    slot_name = slot[0].lower()
                    spec = slot_name.strip()

                action_info = {"activity": action_name,
                               "spec": spec,
                               "domain": domain.lower()}

                action_infos += [action_info]

        # Combine all `action_infos` entries to strings of aggregated actions
        # for each domain and activity
        action_groups = {}
        for info in action_infos:
            head = info["domain"] + "_" + info["activity"]
            if head not in action_groups:
                action_groups[head] = set()
            action_groups[head].update([info["spec"]])

        actions = []
        for head, specs in action_groups.items():
            domain, activity = head.split("_")
            string = "   - " + activity
            string += "_" + domain
            action = DialogTurn.from_string(string)
            action.store_in_domain_info()
            actions.append(action)

        return actions

    def _substitute_entity(self, string):
        """
        Replaces times, numbers, locations, weekdays, etc. in the given string with special tokens
        :param string: A string
        :return: The input string with replaced substrings
        """
        if not self._pattern_time:
            regex_time = r"(\d|\d\d):\d\d|noon"
            regex_number = r"\b(\d+[\.,; -]+\d+\b|\b\d+|one|two|three|four|five|six|seven|eight|nine|ten)\b"
            regex_weekday = r"\b(mon|tues|wednes|thurs|fri|satur|sun|Mon|Tues|Wednes|Thurs|Fri|Satur|Sun)day\b"
            regex_refnumber = r"\b[\dA-Z][\dA-Z][\dA-Z]+\b"
            regex_color = r"(?i)(\byellow\b|\bwhite\b|\bblack\b|\bgrey\b|\bblue\b|\bred\b)"
            regex_cartype = r"(?i)(\bvolkswagen\b|\btoyota\b|\bvolvo\b|\btesla\b|\blexus\b|\bhonda\b|\bford\b|\baudi" \
                            r"\b|\bbmw\b|\bvw\b|\bskoda\b)"
            regex_pricerange = r"(?i)(\bexpensive\b|\bmoderate\b|\bcheap\b)"
            regex_area = r"(?i)(\bsouth\b|\bnorth\b|\bwest\b|\beast\b)"
            regex_hotel_type = r"(?i)(\bguest\s+house\b|\bhotel\b)"
            regex_hotel_name = r"(?i)(\bexpress\s+by\s+holiday\s+inn\s+cambridge\b|\bdoubletree\s+by\s+hilton\s" \
                               r"+cambridge\b|\bcity\s+centre\s+north\s+b\s+and\s+b\b|\baylesbray\s+lodge\s+guest\s" \
                               r"+house\b|\balexander\s+bed\s+and\s+breakfast\b|\bcarolina\s+bed\s+and\s+breakfast\b" \
                               r"|\bfinches\s+bed\s+and\s+breakfast\b|\balexander\s+bed\s+&\s+breakfast\b|\brosa's\s" \
                               r"+bed\s+and\s+breakfast\b|\barbury\s+lodge\s+guest\s+house\b|\bhuntingdon\s+marriott" \
                               r"\s+hotel\b|\bhuntingdon\s+marriot\s+hotel\b|\bhuntingdon\s+marriott\b|\balpha-milton" \
                               r"\s+guest\s+house\b|\ba\s" \
                               r"+and\s+b\s+guest\s+house\b|\buniversity\s+arms\s+hotel\b|\bthe\s+cambridge\s+belfry" \
                               r"\b|\bthe\s+lensfield\s+hotel\b|\bbridge\s+guest\s+house\b|\bcity\s+center\s+north\b" \
                               r"|\bacorn\s+guest\s+house\b|\bnorth\s+b\s+and\s+b\b|\bwandlebury\s+coutn\b" \
                               r"|\bhuntingdon\s+hotel\b|\bhome\s+from\s+home\b|\bcity\s+stop\s+rest\b|\bcambridge\s" \
                               r"+belfry\b|\bwarkworth\s+house\b|\btandoori\s+palace\b|\blensfield\s+hotel\b" \
                               r"|\bcaridge\s+belfrey\b|\baylesbray\s+lodge\b|\bthe\s+allenbell.\b|\bleverton\s+house" \
                               r"\b|\bkirkwood\s+house\b|\bhamilton\s+lodge\b|\bgonville\s+hotel\b|\bthe\s+allenbell" \
                               r"\b|\bhobsons\s+house\b|\bdo\s+n't\s+care\b|\bautumn\s+house.\b|\barchway\s+house\b" \
                               r"|\blovell\s+lodge\b|\bla\s+margherit\b|\bautumn\s+house\b|\bashley\s+hotel\b|\bworth" \
                               r"\s+house\b|\broyal\s+spice\b|\bacorn\s+house\b|\bexpress\s+by\b|\bel\s+shaddai\b" \
                               r"|\bcity\s+roomz\b|\blimehouse\b|\blensfield\b|\bcityroomz\b|\bcambridge\b" \
                               r"|\ballenbell\b|\balexander\b|\bkirkwood\b|\bhuntingd\b|\bgonville\b|\bcambridg\b" \
                               r"|\banatolia\b|\blevert\b|\bavalon\b|\bwhale\b|\bnusha\b|\bclare\b|\bcherr" \
                               r"\b|\bcaffe\b|\bacorn\b|\bgall\b)"
            regex_attraction_type = r"(?i)(\bmultiple\s+sports\b|\bswimming\s+pool\b|\bconcert\s+hall\b" \
                                    r"|\bentertainment\b|\blocal\s+site\b|\barchitecture\b|\bnightclub\b|\bspecial\b" \
                                    r"|\bhotspot\b|\bcollege\b|\bmuseum\b|\bcinema\b|\bchurch\b|\bpark\b|\bboat\b)"
            regex_attraction_name = r"(?i)(\bwhipple\s+museum\s+of\s+the\s+history\s+of\s+science\b|\bcambridge\s" \
                                    r"+university\s+botanic\s+gardens\b|\bgallery\s+at\s+twelve\s+a\s+high\s+street\b" \
                                    r"|\bcambridge\s+book\s+and\s+print\s+gallery\b|\bcambridge\s+and\s+county\s+folk" \
                                    r"\s+museum\b|\bcherry\s+hinton\s+hall\s+and\s+grounds\b|\bcambridge\s+museum\s" \
                                    r"+of\s+technology\b|\bsaint\s+barnabas\s+press\s+gallery\b|\bthe\s+cambridge\s" \
                                    r"+corn\s+exchange\b|\blittle\s+saint\s+mary's\s+church\b|\bwilliams\s+art\s+and" \
                                    r"\s+antiques\b|\bkings\s+hedges\s+learner\s+pool\b|\bgreat\s+saint\s+mary's\s" \
                                    r"+church\b|\bjesus\s+green\s+outdoor\s+pool\b|\bcherry\s+hinton\s+water\s+play\b" \
                                    r"|\bcambridge\s+contemporary\s+art\b|\bthe\s+man\s+on\s+the\s+moon\b|\bcorn\s" \
                                    r"+cambridge\s+exchange\b|\bcontemporary\s+art\s+museum\b|\bcambridge\s+temporary" \
                                    r"\s+art\b|\bcambridge\s+corn\s+exchange\b|\bcollege\s+in\s+the\s+north\b" \
                                    r"|\bsidney\s+sussex\s+college\b|\bthe\s+cambridge\s+punter\b|\bsaint\s+john's\s" \
                                    r"+college\b|\bno\s+specific\s+location\b|\barchitectural\s+churches\b|\bsoul\s" \
                                    r"+tree\s+nightclub\b|\bmilton\s+country\s+park\b|\bholy\s+trinity\s+church\b" \
                                    r"|\bscott\s+polar\s+museum\b|\bcafe\s+jello\s+gallery\b|\ball\s+saint's\s+church" \
                                    r"\b|\bwhale\s+of\s+a\s+time\b|\bman\s+on\s+the\s+moon\b|\ball\s+saints\s+church" \
                                    r"\b|\briverboat\s+georgina\b|\bcambridge\s+artworks\b|\bmagdalene\s+college\b" \
                                    r"|\bfunky\s+fun\s+house\b|\bchurchill\s+college\b|\bpembroke\s+college\b|\bhome" \
                                    r"\s+from\s+home\b|\bemmanuel\s+college\b|\bchrist's\s+college\b|\bcastle\s" \
                                    r"+galleries\b|\bcambridge\s+punter\b|\btrinity\s+college\b|\bregency\s+gallery\b" \
                                    r"|\bqueen's\s+college\b|\bdowning\s+college\b|\bthe\s+fez\s+club\b|\bruskin\s" \
                                    r"+gallery\b|\bolder\s+churches\b|\bking's\s+college\b|\bcorpus\s+christi\b" \
                                    r"|\bchrist\s+college\b|\bswimming\s+pool\b|\bkettle's\s+yard\b|\bjesus\s+college" \
                                    r"\b|\bclare\s+college\b|\bthe\s+junction\b|\bbangkok\s+city\b|\bworth\s+house\b" \
                                    r"|\bscott\s+polar\b|\bold\s+schools\b|\bhughes\s+hall\b|\bold\s+school\b|\bclub" \
                                    r"\s+salsa\b|\bclare\s+hall\b|\bcafe\s+jello\b|\bthe\s+place\b|\bfez\s+club\b" \
                                    r"|\bcollege\b|\bboating\b|\btenpin\b|\bschool\b|\bmuseum\b|\bthanh" \
                                    r"\b|\bpizza\b|\bcarol\b|\buniv\b|\bnusha\b)"
            regex_restaurant_name = r"(?i)(\bthe\s+good\s+luck\s+chinese\s+food\s+takeaway\b|\bthe\s+river\s+bar\s" \
                                    r"+steakhouse\s+and\s+grill\b|\bstazione\s+restaurant\s+and\s+coffee\s+bar\b" \
                                    r"|\bthe\s+cow\s+pizza\s+kitchen\s+and\s+bar\b|\bdarrys\s+cookhouse\s+and\s+wine" \
                                    r"\s+shop\b|\banatolia\s+and\s+efes\s+restaurant\b|\bmaharajah\s+tandoori\s" \
                                    r"+restaurant\b|\bseasame\s+restaurant\s+and\s+bar\b|\bsesame\s+restaurant\s+and" \
                                    r"\s+bar\b|\bhotel\s+du\s+vin\s+and\s+bistro\b|\bgolden\s+house\s+golden\s+house" \
                                    r"\b|\bthe\s+cambridge\s+chop\s+house\b|\bshanghai\s+family\s+restaurant\b" \
                                    r"|\bpizza\s+express\s+fen\s+ditton\b|\bmidsummer\s+house\s+restaurant\b|\bde\s" \
                                    r"+luca\s+cucina\s+and\s+bar\b|\bcambridge\s+lodge\s+restaurant\b|\bshanghi\s" \
                                    r"+family\s+restaurant\b|\bpizza\s+hut\s+cherry\s+hinton\b|\bsaint\s+johns\s+chop" \
                                    r"\s+house\b|\bgrafton\s+hotel\s+restaurant\b|\bpizza\s+hut\s+city\s+centre\b" \
                                    r"|\bchiquito\s+restaurant\s+bar\b|\bthe\s+varsity\s+restaurant\b|\bthe\s+slug\s" \
                                    r"+and\s+lettuce\b|\bpizza\s+hut\s+fen\s+ditton\b|\bgourmet\s+burger\s+kitchen\b" \
                                    r"|\bthe\s+dojo\s+noodle\s+bar\b|\bdon\s+pasquale\s+pizzeria\b|\brestaurant\s+one" \
                                    r"\s+seven\b|\bfitzbillies\s+restaurant\b|\bcity\s+stop\s+restaurant\b" \
                                    r"|\bcambridge\s+chop\s+house\b|\bmeze\s+bar\s+restaurant\b|\bbloomsbury\s" \
                                    r"+restaurant\b|\brestaurant\s+two\s+two\b|\brestaurant\s+alimentum\b|\bnandos\s" \
                                    r"+city\s+centre\b|\bmahal\s+of\s+cambridge\b|\bjinling\s+noodle\s+bar\b" \
                                    r"|\bfrankie\s+and\s+bennys\b|\byippee\s+noodle\s+bar\b|\bthe\s+copper\s+kettle\b" \
                                    r"|\briverside\s+brasserie\b|\bmolecular\s+gastonomy\b|\bda\s+vinci\s+pizzeria\b" \
                                    r"|\bthe\s+missing\s+sock\b|\bthe\s+golden\s+curry\b|\bslug\s+and\s+lettuce\b" \
                                    r"|\bpipasha\s+restaurant\b|\bshiraz\s+restaurant\b|\bsaffron\s+brasserie\b" \
                                    r"|\bpeking\s+restaurant\b|\bmichaelhouse\s+cafe\b|\bkitchen\s+and\s+bar\b|\bdojo" \
                                    r"\s+noodle\s+bar\b|\bbackstreet\s+bistro\b|\bthe\s+oak\s+bistro\b|\bthe\s+lucky" \
                                    r"\s+star\b|\blan\s+hong\s+house\b|\bian\s+hong\s+house\b|\bzizzi\s+cambridge\b" \
                                    r"|\btravellers\s+rest\b|\btandoori\s+palace\b|\bscudamores\s+punt\b|\befes\s" \
                                    r"+restaurant\b|\bcambridge\s+lodge\b|\bsitar\s+tandoori\b|\broyal\s+standard\b" \
                                    r"|\bparkside\s+pools\b|\bhamilton\s+lodge\b|\bugly\s+duckling\b|\bpizza\s" \
                                    r"+express\b|\bla\s+margherita\b|\bdo\s+n't\s+care\b|\bcopper\s+kettle\b|\bthe\s" \
                                    r"+gardenia\b|\btang\s+chinese\b|\btaj\s+tandoori\b|\bnot\s+metioned\b|\bmissing" \
                                    r"\s+sock\b|\blittle\s+seoul\b|\bj\s+restaurant\b|\bhobson\s+house\b|\bgolden\s" \
                                    r"+house\b|\bgolden\s+curry\b|\bcurry\s+prince\b|\bcurry\s+garden\b|\bcharlie\s" \
                                    r"+chan\b|\bcambridge\s+be\b|\bbangkok\s+city\b|\bworth\s+house\b|\bsaigon\s+city" \
                                    r"\b|\broyal\s+spice\b|\bindia\s+house\b|\bcurry\s+queen\b|\bclowns\s+cafe\b" \
                                    r"|\bthe\s+nirala\b|\bthe\s+hotpot\b|\bthe\s+gandhi\b|\bthanh\s+binh\b|\bsala\s" \
                                    r"+thong\b|\brice\s+house\b|\bold\s+school\b|\boak\s+bistro\b|\blucky\s+star\b" \
                                    r"|\bgolden\s+wok\b|\bel\s+shaddai\b|\bcurry\s+king\b|\byu\s+garden\b|\brice\s" \
                                    r"+boat\b|\bpizza\s+hut\b|\bone\s+seven\b|\bloch\s+fyne\b|\bla\s+mimosa\b|\bhk\s" \
                                    r"+fusion\b|\bfitzbillies\b|\bcow\s+pizza\b|\bcity\s+stop\b|\bcaffe\s+uno\b|\bthe" \
                                    r"\s+alex\b|\bmargherita\b|\bla\s+tasca\b|\bali\s+baba\b" \
                                    r"|\blimehouse\b|\bla\s+raza\b|\bgastropub\b|\bwagamama\b|\btandoori\b|\brajmahal" \
                                    r"\b|\bkohinoor\b|\bgraffiti\b|\bgardenia\b|\bgalleria\b|\bcamboats" \
                                    r"\b|\banatolia\b|\bpipasha\b|\bpanahar\b|\bgrafton\b|\bcharlie\b|\bbedouin\b" \
                                    r"|\barchway\b|\bprezzo\b|\bnirala\b|\bnandos\b|\bmeghna\b|\bkymmoy\b" \
                                    r"|\bhotpot\b|\beraina\b|\bclowns\b|\bashley\b|\bnusha\b" \
                                    r"|\blovel\b|\bindia\b|\bhobso\b|\bhakka\b|\bfunky\b|\bcotto\b|\bcocum\b|\bcityr" \
                                    r"\b|\badden\b|\befes\b|\bcott\b|\bcote\b)"
            regex_restaurant_food = r"(?i)(\bmolecular\s+gastronomy\b|\bnorthern\s+european\b|\beastern\s+european\b" \
                                    r"|\bmodern\s+european\b|\bmodern\s+eclectic\b|\bmodern\s+american\b|\bnorth\s" \
                                    r"+american\b|\bmodern\s+english\b|\bmiddle\s+eastern\b|\blatin\s+american\b" \
                                    r"|\basian\s+oriental\b|\bsouth\s+african\b|\bnorth\s+african\b|\bmodern\s+global" \
                                    r"\b|\bafternoon\s+tea\b|\bthe\s+americas\b|\bsouth\s+indian\b|\bnorth\s+indian\b" \
                                    r"|\bbritish\s+food\b|\bmediterranean\b|\blight\s+bites\b|\binternational\b" \
                                    r"|\bscandinavian\b|\baustralasian\b|\btraditional\b|\bsingaporean\b|\bvietnamese" \
                                    r"\b|\bvegetarian\b|\bsteakhouse\b|\bportuguese\b|\bpolynesian\b|\bindonesian\b" \
                                    r"|\baustralian\b|\bmalaysian\b|\bhungarian\b|\bcrossover\b|\bchristmas\b" \
                                    r"|\bcaribbean\b|\bcantonese\b|\bbrazilian\b|\bvenetian\b|\bscottish\b|\bromanian" \
                                    r"\b|\bmoroccan\b|\blebanese\b|\bjapanese\b|\bjamaican\b|\beuropean\b|\beritrean" \
                                    r"\b|\bcreative\b|\bbarbeque\b|\baustrian\b|\bamerican\b|\bunusual\b|\bturkish\b" \
                                    r"|\bswedish\b|\bspanish\b|\bseafood\b|\brussian\b|\bpersian\b|\bmexican\b" \
                                    r"|\bitalian\b|\benglish\b|\bcorsica\b|\bchinese\b|\bcatalan\b|\bcanapes\b" \
                                    r"|\bbritish\b|\bbelgian\b|\bafrican\b|\btuscan\b|\bpolish\b|\bkosher\b|\bkorean" \
                                    r"\b|\bindian\b|\bgerman\b|\bfusion\b|\bfrench\b|\bdanish\b|\bbistro\b|\bbasque\b" \
                                    r"|\bafghan\b|\bworld\b|\bwelsh\b|\bswiss\b|\bpizza\b|\birish\b|\bhalal\b|\bgreek" \
                                    r"\b|\bcuban\b|\basian\b|\bthai\b|\bital\b)"
            regex_location = r"(?i)(\bcambridge\s+county\s+fair\s+next\s+to\s+the\s+city\s+tourist\s+museum\b" \
                             r"|\bwhipple\s+museum\s+of\s+the\s+history\s+of\s+science\b|\bthe\s+good\s+luck\s" \
                             r"+chinese\s+food\s+takeaway\b|\blondon\s+liverpool\s+street\s+train\s+station\b|\bthe\s" \
                             r"+river\s+bar\s+steakhouse\s+and\s+grill\b|\bbirmingham\s+new\s+street\s+train\s" \
                             r"+station\b|\bcambridge\s+university\s+botanic\s+gardens\b|\bgallery\s+at\s+twelve\s+a" \
                             r"\s+high\s+street\b|\blondon\s+kings\s+cross\s+train\s+station\b|\bexpress\s+by\s" \
                             r"+holiday\s+inn\s+cambridge\b|\bcambridge\s+book\s+and\s+print\s+gallery\b|\bcambridge" \
                             r"\s+and\s+county\s+folk\s+museum\b|\bthe\s+cow\s+pizza\s+kitchen\s+and\s+bar\b|\bthe\s" \
                             r"+alexander\s+bed\s+and\s+breakfast\b|\bcambridge\s+road\s+church\s+of\s+christ\b|\bman" \
                             r"\s+on\s+the\s+moon\s+concert\s+hall\b|\bcherry\s+hinton\s+hall\s+and\s+grounds\b|\bthe" \
                             r"\s+regent\s+street\s+city\s+center\b|\bcambridge\s+museum\s+of\s+technology\b|\bsaint" \
                             r"\s+barnabas\s+press\s+gallery\b|\bcherry\s+hinton\s+village\s+center\b|\bthe\s" \
                             r"+cambridge\s+corn\s+exchange\b|\bmaharajah\s+tandoori\s+restaurant\b|\balexander\s+bed" \
                             r"\s+and\s+breakfast\b|\blittle\s+saint\s+mary's\s+church\b|\bcarolina\s+bed\s+and\s" \
                             r"+breakfast\b|\bwilliams\s+art\s+and\s+antiques\b|\bsesame\s+restaurant\s+and\s+bar\b" \
                             r"|\bkings\s+hedges\s+learner\s+pool\b|\bgreat\s+saint\s+mary's\s+church\b|\bfinches\s" \
                             r"+bed\s+and\s+breakfast\b|\bthe\s+cambridge\s+chop\s+house\b|\bshanghai\s+family\s" \
                             r"+restaurant\b|\brosa's\s+bed\s+and\s+breakfast\b|\bmidsummer\s+house\s+restaurant\b" \
                             r"|\bkings\s+lynn\s+train\s+station\b|\bjesus\s+green\s+outdoor\s+pool\b|\bcherry\s" \
                             r"+hinton\s+water\s+play\b|\bcambridge\s+lodge\s+restaurant\b|\bcambridge\s+contemporary" \
                             r"\s+art\b|\bpizza\s+hut\s+cherry\s+hinton\b|\bsaint\s+johns\s+chop\s+house\b|\bgrafton" \
                             r"\s+hotel\s+restaurant\b|\bthe\s+man\s+on\s+the\s+moon\b|\bthe\s+gallery\s+at\s+twelve" \
                             r"\b|\blondon\s+liverpool\s+street\b|\bleicester\s+train\s+station\b|\bcambridge\s+train" \
                             r"\s+station\b|\ba\s+and\s+b\s+guest\s+house\b|\bthe\s+varsity\s+restaurant\b|\bthe\s" \
                             r"+slug\s+and\s+lettuce\b|\bgourmet\s+burger\s+kitchen\b|\buniversity\s+arms\s+hotel\b" \
                             r"|\bst\s+johns\s+chop\s+house\b|\bsidney\s+sussex\s+college\b|\bnorwich\s+train\s" \
                             r"+station\b|\bdon\s+pasquale\s+pizzeria\b|\bbirmingham\s+new\s+street\b|\bthe\s" \
                             r"+cambridge\s+punter\b|\bthe\s+cambridge\s+belfry\b|\bsaint\s+john's\s+college\b" \
                             r"|\brestaurant\s+one\s+seven\b|\bcity\s+stop\s+restaurant\b|\bcambridge\s+chop\s+house" \
                             r"\b|\bsoul\s+tree\s+nightclub\b|\bmilton\s+country\s+park\b|\bholy\s+trinity\s+church\b" \
                             r"|\bcountry\s+folk\s+museum\b|\bbloomsbury\s+restaurant\b|\bscott\s+polar\s+museum\b" \
                             r"|\brestaurant\s+two\s+two\b|\blondon\s+kings\s+cross\b|\bcafe\s+jello\s+gallery\b" \
                             r"|\bbridge\s+guest\s+house\b|\byippee\s+noodle\s+bar\b|\bwhale\s+of\s+a\s+time\b|\bthe" \
                             r"\s+copper\s+kettle\b|\briverside\s+brasserie\b|\bhuntington\s+marriott\b|\ball\s" \
                             r"+saints\s+church\b|\bacorn\s+guest\s+house\b|\bthe\s+missing\s+sock\b|\bthe\s+golden\s" \
                             r"+curry\b|\briverboat\s+georgina\b|\bcambridge\s+artworks\b|\bshiraz\s+restaurant\b" \
                             r"|\bsaffron\s+brasserie\b|\bpeking\s+restaurant\b|\bmagdalene\s+college\b|\bfunky\s+fun" \
                             r"\s+house\b|\bchurchill\s+college\b|\bbackstreet\s+bistro\b|\bthe\s+oak\s+bistro\b" \
                             r"|\bthe\s+lucky\s+star\b|\bpembroke\s+college\b|\bhome\s+from\s+home\b|\bemmanuel\s" \
                             r"+college\b|\bchrist's\s+college\b|\bcastle\s+galleries\b|\bcambridge\s+belfry\b" \
                             r"|\btrinity\s+college\b|\bthe\s+soul\s+tree\b|\btandoori\s+palace\b|\bregency\s+gallery" \
                             r"\b|\bqueen's\s+college\b|\bdowning\s+college\b|\bthe\s+fez\s+club\b|\bsitar\s+tandoori" \
                             r"\b|\bsaint\s+barnabas\b|\bruskin\s+gallery\b|\broyal\s+standard\b|\bking's\s+college\b" \
                             r"|\bhamilton\s+lodge\b|\bdowning\s+street\b|\bcorpus\s+christi\b|\bugly\s+duckling\b" \
                             r"|\bpizza\s+express\b|\bkings\s+college\b|\bkettle's\s+yard\b|\bjesus\s+college\b" \
                             r"|\bclare\s+college\b|\barchway\s+house\b|\bthe\s+junction\b|\bthe\s+gardenia\b|\bthe\s" \
                             r"+galleria\b|\bthe\s+anatolia\b|\btang\s+chinese\b|\bstation\s+road\b|\blittle\s+seoul" \
                             r"\b|\bj\s+restaurant\b|\bgolden\s+house\b|\bcurry\s+prince\b|\bcurry\s+garden\b" \
                             r"|\bcharlie\s+chan\b|\bbangkok\s+city\b|\bautumn\s+house\b|\bashley\s+hotel\b|\bworth\s" \
                             r"+house\b|\bsaint\s+johns\b|\bsaigon\s+city\b|\broyal\s+spice\b|\bold\s+schools\b|\bnew" \
                             r"\s+england\b|\bindia\s+house\b|\bhughes\s+hall\b|\bcurry\s+queen\b|\bclowns\s+cafe\b" \
                             r"|\bacorn\s+house\b|\bthe\s+hotpot\b|\bthe\s+gandhi\b|\bthe\s+avalon\b|\brice\s+house\b" \
                             r"|\bkings\s+lynn\b|\bgolden\s+wok\b|\bcurry\s+king\b|\bclub\s+salsa\b|\bclare\s+hall\b" \
                             r"|\bclair\s+hall\b|\bthe\s+place\b|\brice\s+boat\b|\bpizza\s+hut\b|\bla\s+mimosa\b" \
                             r"|\bcity\s+hall\b|\bbournemouth\b|\bbirmingham\b" \
                             r"|\bliverpool\b|\bleicester\b|\bkohinoor\b|\bgraffiti\b|\bgalleria\b" \
                             r"|\banatolia\b|\bnorwich\b|\bfinches\b|\bbedouin\b|\btenpin\b|\bmuseum\b|\blondon\b" \
                             r"|\bgandhi\b|\bcinema\b|\bavalon\b|\bnorth\b|\bhakka\b|\blens\b" \
                             r"|\bcote\b)"
            self._pattern_time = re.compile(regex_time, flags=re.IGNORECASE)
            self._pattern_number = re.compile(regex_number, flags=re.IGNORECASE)
            self._pattern_weekday = re.compile(regex_weekday, flags=re.IGNORECASE)
            self._pattern_pricerange = re.compile(regex_pricerange, flags=re.IGNORECASE)
            self._pattern_area = re.compile(regex_area, flags=re.IGNORECASE)
            self._pattern_hotel_name = re.compile(regex_hotel_name, flags=re.IGNORECASE)
            self._pattern_attraction_name = re.compile(regex_attraction_name, flags=re.IGNORECASE)
            self._pattern_restaurant_name = re.compile(regex_restaurant_name, flags=re.IGNORECASE)
            self._pattern_restaurant_food = re.compile(regex_restaurant_food, flags=re.IGNORECASE)
            self._pattern_location = re.compile(regex_location, flags=re.IGNORECASE)
            self._pattern_color = re.compile(regex_color, flags=re.IGNORECASE)
            self._pattern_cartype = re.compile(regex_cartype, flags=re.IGNORECASE)
            self._pattern_attraction_type = re.compile(regex_attraction_type, flags=re.IGNORECASE)
            self._pattern_hotel_type = re.compile(regex_hotel_type, flags=re.IGNORECASE)
            self._pattern_refnumber = re.compile(regex_refnumber)

        string = re.sub(self._pattern_time, lambda k: "_time_ ", string)
        string = re.sub(self._pattern_number, lambda k: "_number_ ", string)
        string = re.sub(self._pattern_weekday, lambda k: "_weekday_ ", string)
        string = re.sub(self._pattern_refnumber, lambda k: "_reference_ ", string)
        string = re.sub(self._pattern_pricerange, lambda k: "_pricerange_ ", string)
        string = re.sub(self._pattern_area, lambda k: "_area_ ", string)
        string = re.sub(self._pattern_hotel_name, lambda k: "_hotel_name_ ", string)
        string = re.sub(self._pattern_hotel_type, lambda k: "_hotel_type_ ", string)
        string = re.sub(self._pattern_attraction_name, lambda k: "_attraction_name_ ", string)
        string = re.sub(self._pattern_attraction_type, lambda k: "_attraction_type_ ", string)
        string = re.sub(self._pattern_restaurant_food, lambda k: "_food_type_ ", string)
        string = re.sub(self._pattern_restaurant_name, lambda k: "_restaurant_name_ ", string)
        string = re.sub(self._pattern_location, lambda k: "_location_ ", string)
        string = re.sub(self._pattern_color, lambda k: "_color_ ", string)
        string = re.sub(self._pattern_cartype, lambda k: "_cartype_ ", string)

        return string

    def parse_story_e2e(self, name, verbose=0):
        """
        Parse a MultiWOZ story for end-to-end training.
        :param name: Name of the story (e.g. MUL0129.json)
        :param verbose: Level of output (0 = no print, 1 = print parsed story, 2 = also print utterances)
        :return:
        """
        initial_num_problems = len(multiwoz.domain_info.problems)
        dialog = self.data[name]
        log = dialog["log"]
        num_turns = len(log)

        story = ""
        parse_intent = IntentParser(self.slot_parser, add_status_slots=self.add_status_slots)
        name = name[:-5]

        story += f"## story_{name}" + "\n"
        if verbose > 0:
            print(colored(f"## story_{name}", "green"))

        count_use = 0  # How often the user spoke
        count_wiz = 0  # How often the wizard replied (consecutive actions count as one)
        self._domain_substitute = None
        intent_name = None
        for step in log:
            if len(step["metadata"]) == 0:  # User-texts don't have metadata
                # User's text
                if verbose > 0:
                    print("U:  " + step["text"].strip())

                intent_name = step["text"]

                count_use += 1
            else:
                turns_from_wizard = []
                count_wiz += 1

                # Infer user intent from new information
                # This includes the user intent + possible additional slots that come from the wizard
                # looking up information during booking
                turns_from_user, domain_substitute = parse_intent(step["metadata"])

                if domain_substitute:
                    self._domain_substitute = domain_substitute

                if verbose > 1:
                    for turn in turns_from_user:
                        print(colored(turn.to_string(), "blue"))

                # Wizard's information
                if str(count_wiz) in self.acts[name]:
                    action = self.acts[name][str(count_wiz)]
                    turns_from_wizard = self.parse_action(action)

                    if verbose > 1:
                        for turn in turns_from_wizard:
                            print(colored(turn.to_string(), "red"))
                else:
                    log_problem({
                        "type": "no_action",
                        "count_wiz": count_wiz,
                        "story": name,
                        "actions": self.acts[name]
                    })

                if self.add_status_slots:
                    # Merge all slots
                    all_slots = DialogSlot({})
                    for turn in turns_from_user + turns_from_wizard:
                        if not turn.is_action and turn.slots:
                            all_slots.slots.update(turn.slots)

                    status_slots = DialogSlot({
                        k: v for k, v in all_slots.slots.items() if k.endswith("status")
                    })
                else:
                    status_slots = None

                action_name = step["text"]

                # Substitute entities
                intent_name = self._substitute_entity(intent_name)
                action_name = self._substitute_entity(action_name)

                # Remove line breaks, `/`, and redundant whitespaces or tabs
                intent_name = re.sub(r"[/:\"'`#]+", lambda k: " ", intent_name)
                intent_name = intent_name.replace("\n", "").strip(" \t/")
                intent_name = re.sub(r"\s\s+", lambda k: " ", intent_name)
                action_name = re.sub(r"[/:\"'`#]+", lambda k: " ", action_name)
                action_name = action_name.replace("\n", "").strip(" \t/")
                action_name = re.sub(r"\s\s+", lambda k: " ", action_name)

                if verbose > 0:
                    print(f"U: {intent_name}")
                    print(f"W: {step['text'].strip()}")
                    print(f"W: {action_name}")

                # Store action for domain (if no errors occurred)
                if len(multiwoz.domain_info.problems) == initial_num_problems:
                    multiwoz.domain_info.e2e_actions.update({
                        action_name: sorted([a.to_string()[5:] for a in turns_from_wizard if a.is_action])})

                story += f"* {intent_name}\n"
                if self.add_status_slots:
                    if status_slots.slots:
                        story += status_slots.to_string() + "\n"
                story += f"   - {action_name}\n"

        story += "\n"

        if len(multiwoz.domain_info.problems) > initial_num_problems:
            story = None

        return story

    def parse_story(self, name, verbose=0, infuse_chitchat_callback=None, chitchat_variability=1):
        """
        Parse a MultiWOZ story.
        :param name: Name of the story (e.g. MUL0129.json)
        :param verbose: Level of output (0 = no print, 1 = print parsed story, 2 = also print utterances)
        :param infuse_chitchat_callback: Function that takes the current story name, present and maximum number of
        turns and returns the number of chitchats that should be infused at this point.
        :param chitchat_variability: How many different chitchat intents/actions should be created
        :return:
        """
        initial_num_problems = len(multiwoz.domain_info.problems)
        dialog = self.data[name]
        log = dialog["log"]
        num_turns = len(log)

        story = ""
        parse_intent = IntentParser(self.slot_parser, add_status_slots=self.add_status_slots)
        name = name[:-5]

        story += f"## story_{name}" + "\n"
        if verbose > 0:
            print(colored(f"## story_{name}", "green"))

        # If we infuse chitchat, then add the chitchat action to the domain file
        # The intent is added in the parse_stories.py script
        if infuse_chitchat_callback is not None:
            if chitchat_variability > 1:
                for v in range(chitchat_variability):
                    DialogAction(f"chitchat_{v + 1}", "general").store_in_domain_info()
            else:
                DialogAction("chitchat", "general").store_in_domain_info()

        count_use = 0  # How often the user spoke
        count_wiz = 0  # How often the wizard replied (consecutive actions count as one)
        self._domain_substitute = None
        for step in log:
            if len(step["metadata"]) == 0:  # User-texts don't have metadata
                # Possibly infuse a chitchat detour
                if infuse_chitchat_callback is not None:
                    # Determine how many chitchats should be added
                    req_num_chitchat = infuse_chitchat_callback(name, count_use + count_wiz + 1, num_turns)
                    # Create the intent/action pairs
                    turns = []
                    for _ in range(req_num_chitchat):
                        # Determine the chitchat type
                        if chitchat_variability > 1:
                            cc_name = f"chitchat_{random.randint(1, chitchat_variability)}"
                        else:
                            cc_name = "chitchat"
                        turns.append(DialogIntent(cc_name))
                        turns.append(DialogAction(cc_name, "general"))
                    # Add the turns to the story
                    for turn in turns:
                        story += turn.to_string() + "\n"

                # User's text
                if verbose > 1:
                    print("U:  " + step["text"])

                count_use += 1
            else:
                turns_from_wizard = []
                count_wiz += 1

                # Infer user intent from new information
                # This includes the user intent + possible additional slots that come from the wizard
                # looking up information during booking
                turns_from_user, domain_substitute = parse_intent(step["metadata"])

                if domain_substitute:
                    self._domain_substitute = domain_substitute

                # If this is the end of the dialog, then we assume the user's `inform{}` (no slots) is actually a `bye`
                if count_wiz * 2 == len(log) and len(turns_from_user) == 1 and not turns_from_user[0].slots:
                    turns_from_user[0].name = "bye"

                if verbose > 0:
                    for turn in turns_from_user:
                        print(colored(turn.to_string(), "blue"))

                # Wizard's text
                if verbose > 1:
                    print("W:  " + step["text"])

                # Wizard's information
                if str(count_wiz) in self.acts[name]:
                    action = self.acts[name][str(count_wiz)]
                    turns_from_wizard = self.parse_action(action)

                    if verbose > 0:
                        for turn in turns_from_wizard:
                            print(colored(turn.to_string(), "red"))
                else:
                    log_problem({
                        "type": "no_action",
                        "count_wiz": count_wiz,
                        "actions": self.acts[name]
                    })

                # Merge adjacent slots
                all_turns = []
                last_slot = None
                for turn in turns_from_user + turns_from_wizard:
                    if turn.is_slot or turn.is_intent:
                        if last_slot:
                            if last_slot.slots:
                                last_slot.slots.update(turn.slots)
                            else:
                                last_slot.slots = turn.slots
                        else:
                            last_slot = turn
                    else:
                        if last_slot:
                            all_turns.append(last_slot)
                            last_slot = None
                        all_turns.append(turn)
                if last_slot:
                    all_turns.append(last_slot)

                for turn in all_turns:
                    story += turn.to_string() + "\n"

        story += "\n"

        if len(multiwoz.domain_info.problems) > initial_num_problems:
            story = None

        return story
