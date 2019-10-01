
"""This script parses all stories and creates stories_....md files"""

import os
import random
from multiwoz.parser import MultiWOZParser
import argparse
import multiwoz.dialog_turn
from pathlib import Path
from tqdm import tqdm

#################################################
# Command line argument specification
#################################################

arg_parser = argparse.ArgumentParser(description="Parse MultiWOZ 2.0 or 2.1 to story file.")
arg_parser.add_argument("directory", type=str, help="Data directory")
arg_parser.add_argument("--dataset-version", "-d", default="2.0", const="2.1", choices=["2.0", "2.1"],
                        nargs="?", help="MultiWOZ version", type=str)
arg_parser.add_argument("--subset", "-s", default="all", const="test", choices=["all", "test", "val"],
                        nargs="?", help="MultiWOZ version", type=str)
arg_parser.add_argument("--add-status-slots", action="store_true", default=False,
                        help="Add status slots to stories.")
arg_parser.add_argument("--slot-simplification", type=int, default=1, const=2,
                        choices=[0, 1, 2, 3, 4],
                        nargs="?", help="Degree of slot simplification (0 = no simplification)")


if __name__ == '__main__':

    random.seed(2019)
    args = arg_parser.parse_args()
    data_dir = os.path.abspath(args.directory)

    # Do not combine actions
    multiwoz.dialog_turn.default_name_merge_list = {}

    # Use `debug=True` for smaller data set
    parser = MultiWOZParser(
        directory=data_dir,
        version=args.dataset_version,
        simplification_level=args.slot_simplification,
        add_status_slots=args.add_status_slots
    )

    assert len(parser.data) == len(parser.acts)
    print(f"Parsing {len(parser.data)} stories...")

    all_problems = []
    count = 0
    count_good = 0

    pbar = tqdm(parser.story_names, desc="Stories")
    if args.subset == "all":
        # Write all stories
        with open(Path(data_dir) / "stories_all.md", "w+") as story_file:
            with open(Path(data_dir) / "stories_vallist.md", "w+") as val_file:
                with open(Path(data_dir) / "stories_testlist.md", "w+") as test_file:
                    for name in parser.story_names:
                        story = parser.parse_story(name)
                        count += 1
                        if story:
                            count_good += 1
                            story_file.write(story)

                            if name in parser.validation_list:
                                val_file.write(story)

                            if name in parser.test_list:
                                test_file.write(story)

        # Inform about number of bad stories
        assert count == len(parser.story_names)
        print(f"{count_good}/{count} = {100.0 * count_good / count:.2f}% of all stories were sufficiently labeled.")
    elif args.subset == "test":
        # Write stories in test list
        with open(Path(data_dir) / "stories_all.md", "w+") as test_file:
            for name in pbar:
                if name in parser.test_list:
                    story = parser.parse_story(name)
                    count += 1
                    if story:
                        count_good += 1
                        test_file.write(story)
        # Inform about number of bad stories
        assert count == 1000
        print(f"{count_good}/{count} = {100.0 * count_good / count:.2f}% of all "
              f"test stories were sufficiently labeled.")
    elif args.subset == "val":
        # Write stories in validation list
        with open(Path(data_dir) / "stories_all.md", "w+") as val_file:
            for name in pbar:
                if name in parser.validation_list:
                    story = parser.parse_story(name)
                    count += 1
                    if story:
                        count_good += 1
                        val_file.write(story)
        # Inform about number of bad stories
        assert count == 1000
        print(f"{count_good}/{count} = {100.0 * count_good / count:.2f}% of all "
              f"validation stories were sufficiently labeled.")

    print("Exporting domain file...")
    import multiwoz.domain_info

    with open(Path(data_dir) / "domain.yml", "w+") as domain_file:

        # Intents
        domain_file.write("intents:\n")
        domain_file.write("  - inform\n")
        domain_file.write("  - bye\n")
        domain_file.write("\n")

        # Entities
        domain_file.write("entities:\n")
        for slot in sorted(list(multiwoz.domain_info.slots)):
            domain_file.write(f"  - {slot}\n")
        domain_file.write("\n")

        # Actions
        domain_file.write("actions:\n")
        for a in sorted(list(multiwoz.domain_info.actions)):
            domain_file.write(f"  - {a}\n")
        domain_file.write("\n")

        # Templates
        domain_file.write("templates:\n")
        for a in sorted(list(multiwoz.domain_info.actions)):
            domain_file.write(f"  {a}:\n")
            domain_file.write(f'  - text: "{a}"\n')
        domain_file.write("\n")

        # Slots
        domain_file.write("slots:\n")
        for slot in sorted(list(multiwoz.domain_info.slots)):
            domain_file.write(f"  {slot}:\n")
            if len(multiwoz.domain_info.slots[slot]) > 1:
                domain_file.write(f"    type: categorical\n")
                domain_file.write(f"    values:\n")
                for value in sorted(multiwoz.domain_info.slots[slot]):
                    domain_file.write(f"    - {value}\n")
            else:
                domain_file.write(f"    type: text\n")

    print()
    print("Tally of problems:")
    problem_tally = {}
    for problem in multiwoz.domain_info.problems:
        if problem["type"] in problem_tally:
            problem_tally[problem["type"]] += 1
        else:
            problem_tally[problem["type"]] = 1
    for t, c in problem_tally.items():
        print(f"  {t}: {c}")

    print("Done.")
