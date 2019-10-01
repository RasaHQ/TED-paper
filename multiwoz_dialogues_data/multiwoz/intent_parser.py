
"""
User intents must be inferred from the information gained by the Wizard.
Therefore, we implement a class `IntentParser` that initializes a baseline metadata set and tracks changes to it.
"""

import json
import multiwoz.domain_info
from multiwoz.domain_info import log_problem
from multiwoz.dialog_turn import DialogIntent
from multiwoz.dialog_turn import DialogSlot
from multiwoz.dialog_turn import DialogAction


class IntentParser:
    def __init__(self, slot_parser, add_status_slots):
        self.baseline = None
        self.slot_parser = slot_parser
        self.add_status_slots = add_status_slots

    def __call__(self, metadata):
        if self.baseline is None:
            # Initialize baseline
            self.baseline = metadata.copy()
            # For the baseline, all values must be "not mentioned", [], or ""
            self.baseline = self.clear_dataset(self.baseline)

        updated_domains = set()

        # Find differences from baseline using depth-first-search
        differences = []
        lookups = []
        self.find_differences(
            self.baseline, metadata, differences, lookups
        )

        # `differences` now contains strings like ['_hotel_book_people_6', '_hotel_semi_parking_yes', ...]
        # The first token specifies the domain, and the third token specifies the slot
        # The second token is either 'book' or 'semi', and can be ignored
        # The last token specifies the slot value, as requested by the user
        intent_string = "* inform{"
        for difference in differences:
            split_difference = difference[1:].split("_")
            if len(split_difference) != 4:
                # A few data in the set yield a difference string like
                # `hotel_book_booked_reference_YF86GE4J`
                # that is, the second token "book_booked" that can be ignored is falsely interpreted as
                # two tokens
                domain, _, _, _slot, value = split_difference
            else:
                domain, _, _slot, value = split_difference

            # Add the information iff `value` is valid
            if self.slot_parser.value_valid(value):
                updated_domains.add(domain)
                slot = domain + "_" + _slot
                value = self.slot_parser.value_simplify(slot, value)
                intent_string += '"' + slot + '": "' + value + '", '

                # Safe slot definition for the domain file
                if slot not in multiwoz.domain_info.slots:
                    multiwoz.domain_info.slots[slot] = set()
                multiwoz.domain_info.slots[slot].add(value)
        if intent_string[-2:] == ", ":  # Drop trailing ", "
            intent_string = intent_string[:-2]
        intent_string += "}"

        # If there was no information gained, then we assume it's just chit chat
        if intent_string == "* inform{}":
            intent_string = "* inform"

        intent = DialogIntent.from_string(intent_string)
        intent.store_in_domain_info()
        result = [intent]

        # Assume that the objects of interest are available
        if self.add_status_slots:
            for domain in sorted(updated_domains):
                slot_name = domain + "_status"
                slot_value = "unique" if lookups else "available"
                slot = DialogSlot({slot_name: slot_value})
                slot.store_in_domain_info()
                result.append(slot)

        # If information was gained because the Wizard looked something up, add an action
        if lookups:
            for lookup in lookups:
                result.append(lookup)

        # Update baseline
        self.baseline = metadata

        # Set `domain_substitute` if a new domain was encountered
        domain_substitute = sorted(list(updated_domains))[-1] if updated_domains else None

        return result, domain_substitute

    @staticmethod
    def clear_dataset(dataset):
        """Ensures that all values in `dataset` are 'not mentioned', [], or ''. """
        if type(dataset) is dict:
            return {k: IntentParser.clear_dataset(dataset[k]) for k in dataset}
        elif type(dataset) is list:
            return [IntentParser.clear_dataset(s) for s in dataset]
        elif type(dataset) is str:
            if dataset == "not mentioned" or dataset == "":
                return dataset
            else:
                return ""

    def find_differences(
        self, baseline, dataset, results, lookups, branch=""
    ):
        """Searches `baseline` and `dataset` synchronously with a depth-first-search and
        appends the location of any difference to `results`."""
        assert type(baseline) is type(dataset)
        if type(baseline) is list:
            if len(baseline) <= len(dataset):
                for i in range(len(baseline)):
                    self.find_differences(
                        baseline[i],
                        dataset[i],
                        results,
                        lookups,
                        branch
                    )
            if len(baseline) < len(dataset):
                # The Wizard looked up something (a booking was made)
                lookups += self.parse_lookup(branch, baseline, dataset)
            if len(baseline) > len(dataset):
                log_problem({
                        "type": "long_baseline",
                        "branch": branch,
                        "baseline": baseline,
                        "dataset": dataset
                    })
        elif type(baseline) is dict:
            for key in baseline:
                self.find_differences(
                    baseline[key],
                    dataset[key],
                    results,
                    lookups,
                    branch + "_" + str(key)
                )
        elif type(baseline) is str:
            if baseline != dataset:
                results.append(branch + "_" + dataset)
        else:
            raise TypeError("Dataset contains objects that is not dict/list/str.")

    def parse_lookup(self, branch, baseline, dataset):
        """Take the new information gained by the Wizard's lookup to generate an action string"""

        # The new information is what is new in `dataset`, compared to `baseline`
        info = [d for d in dataset if d not in baseline]

        # Extract the domain from `branch`
        split_branch = branch[1:].split("_")
        if len(split_branch) != 3:
            raise RuntimeError(f"Bad branch {branch}")
        else:
            domain = split_branch[0]

        lookup_actions = []
        if self.add_status_slots:
            lookup_actions.append(DialogSlot({f"{domain}_status": "unique"}))
        lookup_actions.append(DialogAction("action", domain, ["book"]))
        if self.add_status_slots:
            lookup_actions.append(DialogSlot({f"{domain}_status": "booked"}))

        for i in info:
            # Prepend `domain` to info keys and write the string
            lookup_actions.append(
                DialogSlot({(domain + "_" + k): self.slot_parser.value_simplify(domain + "_" + k, i[k])
                            for k in i if self.slot_parser.value_valid(i[k])}))

        for la in lookup_actions:
            la.store_in_domain_info()

        return lookup_actions
