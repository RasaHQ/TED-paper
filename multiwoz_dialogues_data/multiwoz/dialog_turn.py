
import re
import ast
import json
import multiwoz.domain_info

default_name_merge_list = {
    "action": {
        # "inform": "advise",
        # "recommend": "advise",
        # "select": "advise",
        "inform": "reply",
        "recommend": "reply",
        "select": "reply",
        "request": "reply",
        "bye": "welcome",
        "greet": "welcome"
    }
}


class DialogTurn:

    def __init__(self, turn_type, name, name_merge_list=None):
        assert turn_type in ["intent", "action", "slot"]

        self.name_merge_list = default_name_merge_list if name_merge_list is None else name_merge_list

        self.turn_type = turn_type
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._merge_names(value)

    def to_string(self):
        pass

    @staticmethod
    def from_string(string):
        t = DialogTurn.type_from_string(string)
        if t == "action":
            return DialogAction.from_string(string)
        elif t == "intent":
            return DialogIntent.from_string(string)
        elif t == "slot":
            return DialogSlot.from_string(string)
        else:
            raise ValueError(f"The string '{string}' is not a valid dialog turn string")

    @staticmethod
    def type_from_string(string):
        regex_action = r"- ([^_\{]+)_([^ ]+_)?([^_*]+)$"  # Groups: name | tags | domain
        regex_intent = r"\* ([^_\{]+)(?:\{([^\}]*)})?$"   # Groups: name | slots
        regex_slot = r"- slot\{([^\}]*)\}$"               # Groups: slots

        if re.search(regex_action, string):
            return "action"
        elif re.search(regex_intent, string):
            return "intent"
        elif re.search(regex_slot, string):
            return "slot"
        else:
            return None

    def store_in_domain_info(self):
        pass

    @property
    def sort_key(self):
        return self.name

    @property
    def full_name(self):
        return self.name

    @property
    def is_action(self):
        return self.turn_type == "action"

    @property
    def is_intent(self):
        return self.turn_type == "intent"

    @property
    def is_slot(self):
        return self.turn_type == "slot"

    def _merge_names(self, name):
        if self.name_merge_list:
            return self.name_merge_list.get(self.turn_type, {}).get(name, name)
        else:
            return name


class DialogIntent(DialogTurn):

    def __init__(self, name, slots=None, name_merge_list=None):
        super(DialogIntent, self).__init__("intent", name, name_merge_list=name_merge_list)
        self.slots = slots

    def to_string(self):
        string = f"* {self.name}"
        if self.slots:
            string += json.dumps(self.slots)
        return string

    @staticmethod
    def from_string(string):
        regex_intent = r"\* ([^_\{]+)(?:\{([^\}]*)})?$"  # Groups: name | slots

        match = re.search(regex_intent, string)
        if match:
            name = match.group(1)
            if match.group(2):
                slots = ast.literal_eval("{" + match.group(2) + "}")
            else:
                slots = None
            return DialogIntent(name, slots)
        else:
            raise ValueError(f"The string '{string}' is not a valid intent string")

    def store_in_domain_info(self):
        # Update global list of slots
        if self.slots:
            for name, value in self.slots.items():
                if name not in multiwoz.domain_info.slots:
                    multiwoz.domain_info.slots[name] = set()
                multiwoz.domain_info.slots[name].update([value])


class DialogAction(DialogTurn):

    def __init__(self, name, domain, tags=None, name_merge_list=None):
        super(DialogAction, self).__init__("action", name, name_merge_list=name_merge_list)
        if tags:
            self.tags = [t.strip("_") for t in tags if t != ""]
        else:
            self.tags = None
        self.domain = domain

    def to_string(self):
        return f"   - {self.full_name}"

    @staticmethod
    def from_string(string):
        regex_action = r"- ([^_\{]+)_([^ ]+_)?([^_*]+)$"  # Groups: name | tags | domain

        match = re.search(regex_action, string)
        if match:
            name = match.group(1)
            domain = match.group(3)
            if match.group(2):
                tags = [t.strip("_") for t in match.group(2).split("_")]
            else:
                tags = None
            return DialogAction(name, domain, tags)
        else:
            raise ValueError(f"The string '{string}' is not a valid action string")

    @property
    def full_name(self):
        string = self.name + "_"
        if self.tags:
            string += "_".join(self.tags) + "_"
        string += self.domain
        return string

    def store_in_domain_info(self):
        if self.domain != "booking":  # Do not store `booking` domain actions, since these are substituted
            # Update global list of slots
            multiwoz.domain_info.actions.update([self.full_name])

    @property
    def sort_key(self):

        domain_prefix = {
            "booking": "a",
            "general": "c"
        }.get(self.domain, "b")

        action_prefix = {
            "greet": "a",
            "welcome": "b",
            "select": "c",
            "inform": "d",
            "advise": "d",  # Merged from inform/select/recommend
            "reply": "d",  # Merged from inform/select/recommend/request
            "recommend": "e",
            "offerbook": "f",
            "book": "g",
            "nobook": "h",
            "nooffer": "i",
            "offerbooked": "j",
            "request": "k",
            "reqmore": "l",
            "bye": "m"
        }.get(self.name)

        return domain_prefix + action_prefix + self.full_name


class DialogSlot(DialogTurn):

    def __init__(self, slots, name_merge_list=None):
        super(DialogSlot, self).__init__("slot", name="slot", name_merge_list=name_merge_list)
        self.slots = slots

    def to_string(self):
        string = f"   - slot" + json.dumps(self.slots)
        return string

    @staticmethod
    def from_string(string):
        regex_slot = r"- slot\{([^\}]*)\}$"  # Groups: slots

        match = re.search(regex_slot, string)
        if match:
            slots = ast.literal_eval("{" + match.group(1) + "}")
            return DialogSlot(slots)
        else:
            raise ValueError(f"The string '{string}' is not a valid slot string")

    def store_in_domain_info(self):
        # Update global list of slots
        for name, value in self.slots.items():
            if name not in multiwoz.domain_info.slots:
                multiwoz.domain_info.slots[name] = set()
            multiwoz.domain_info.slots[name].add(value)


if __name__ == '__main__':
    s = '* inform{"hotel_parking": "yes", "hotel_internet": "yes"}'
    print(s)
    dt = DialogTurn.from_string(s)
    print(dt.to_string())

    s = '   - request_price_hotel'
    print(s)
    dt = DialogTurn.from_string(s)
    print(dt.to_string())

    s = '   - slot{"booking_status": "NA"}'
    print(s)
    dt = DialogTurn.from_string(s)
    print(dt.to_string())
    print(dt.is_slot)
