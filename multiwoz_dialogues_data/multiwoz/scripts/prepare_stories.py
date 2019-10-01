
"""The purpose of this script is to split a list of stories into training and testing stories."""

import argparse
import os

arg_parser = argparse.ArgumentParser(description="Split a list of stories into training and testing stories.")

arg_parser.add_argument("input", type=str, help="Input story file name")
arg_parser.add_argument("--train", default=None, type=str, help="Output story file name for training")
arg_parser.add_argument("--test", default=None, type=str, help="Output story file name for testing")
arg_parser.add_argument("--insights", action="store_true", help="Display information about the input stories")
arg_parser.add_argument("--num-train", type=int, default=-1,
                        help="Number of training examples (default: train_test_ratio)")
arg_parser.add_argument("--num-test", type=int, default=-1,
                        help="Number of testing examples (default: 1 - train_test_ratio)")
arg_parser.add_argument("--train-test-ratio", type=float, nargs=1, default=0.80,
                        help="Ratio of training to testing examples (default: 0.80)")
arg_parser.add_argument("--train-domains", type=str, nargs="+", metavar="A",
                        help="Domains allowed in the training set (default: all)")
arg_parser.add_argument("--test-domains", type=str, nargs="+", metavar="B",
                        help="Domains allowed in the testing set (default: all)")
arg_parser.add_argument("--filter", default=None, type=str, help="File containing a list of allowed story names ("
                                                                 "including .json)")


def print_insights():

    print(f"Story file: {os.path.abspath(story_file_name)}")

    domains = {}
    unique_domains = {}
    current_domains = set()
    num_lines = 0
    num_stories = 0

    with open(story_file_name, "r") as story_file:
        for line in story_file:
            num_lines += 1
            if line.startswith("##"):
                num_stories += 1
                # Increment domain counters for each domain that has occurred in the last story
                for domain in current_domains:
                    if domain in domains:
                        domains[domain] += 1
                    else:
                        domains[domain] = 1
                if len(current_domains) == 1:
                    domain = list(current_domains)[0]
                    if domain in unique_domains:
                        unique_domains[domain] += 1
                    else:
                        unique_domains[domain] = 1
                current_domains = set()
            elif line.lstrip().startswith("- ") and not line.lstrip().startswith("- slot"):
                domain = line.strip().split("_")[-1]
                current_domains.add(domain)

    print(f"Domains (appears (uniquely) in _ stories)")
    for domain in sorted(domains):
        print(f"  {domain} ({domains[domain]}, {unique_domains.get(domain, 0)} unique)")
    print(f"# Domains : {len(domains)}")
    print(f"# Stories : {num_stories}")
    print(f"# Lines   : {num_lines}")


def count_stories():
    num_stories = 0
    with open(story_file_name, "r") as story_file:
        for line in story_file:
            if line.startswith("##"):
                num_stories += 1
    return num_stories


class StoryFilter:
    """
    Loads the given file (e.g. valList.json) and, when called,
    returns True only iff the given story was in this list.
    """
    def __init__(self, filter_file_name: str):
        if filter_file_name is None:
            self.no_filter = True
        else:
            self.no_filter = False

            if not os.path.exists(filter_file_name):
                raise ValueError(f"The filter file '{filter_file_name}' does not exist.")
            if not os.path.isfile(filter_file_name):
                raise ValueError(f"The filter '{filter_file_name}' is not a file.")

            if filter_file_name.endswith(".json"):
                # This is one of the testlist.json or vallist.json files

                # Read all story names from the file
                with open(filter_file_name, "r") as file:
                    self.whitelist = file.readlines()

                # Remove ".json" ending and add "story_" beginning
                self.whitelist = ["story_" + s.strip()[:-5] for s in self.whitelist]

            elif filter_file_name.endswith(".md"):
                # This is a Rasa story file

                self.whitelist = []
                with open(filter_file_name, "r") as input_stories:
                    for line in input_stories:
                        if line.startswith("##"):
                            current_story_name = line[2:].strip()
                            self.whitelist += [current_story_name]
            else:
                # Read all story names from the file
                with open(filter_file_name, "r") as file:
                    self.whitelist = file.readlines()

                # Remove \n from story names
                self.whitelist = [s.strip() for s in self.whitelist]

            print(f"Filter: {len(self.whitelist)} stories allowed")

    def __call__(self, story_name):
        if self.no_filter:
            return True
        else:
            return story_name in self.whitelist


def split_file():
    global train_count
    global test_count

    num_stories_train = 0
    num_stories_test = 0
    num_stories_unused = 0

    story_allowed = StoryFilter(args.filter)

    if args.num_train == -1 and args.num_test == -1 and not story_allowed.no_filter:
        train_count = round(0.80 * len(story_allowed.whitelist))
        test_count = round(0.20 * len(story_allowed.whitelist))

    with open(story_file_name, "r") as input_stories:
        with open(train_file_name, "w") as output_train:
            with open(test_file_name, "w") as output_test:
                domains = set()
                story = []
                current_story_name = ""
                for line in input_stories:
                    if line.startswith("##"):
                        # A new story begins
                        story += [line]
                        current_story_name = line[2:].strip()
                    elif line.strip() == "":
                        # The story ends
                        story += [line]

                        # Check what we can use this story for
                        usage = None
                        if story_allowed(current_story_name):
                            if train_count < 0 or num_stories_train < train_count:
                                # We need more training stories
                                if train_domains is None or all(domain in train_domains for domain in domains):
                                    # This story could be used for training
                                    usage = "training"
                            if usage is None and (test_count < 0 or num_stories_test < test_count):
                                # We need more testing stories
                                if test_domains is None or all(domain in test_domains for domain in domains):
                                    # This story could be used for testing
                                    usage = "testing"

                        # Write to the appropriate output file
                        if usage is None:
                            # This story is useless
                            num_stories_unused += 1
                        elif usage == "training":
                            # This story should be used for training
                            output_train.writelines(story)
                            num_stories_train += 1
                        elif usage == "testing":
                            # This story should be used for testing
                            output_test.writelines(story)
                            num_stories_test += 1

                        # Reset the story
                        domains = set()
                        story = []
                    elif line.lstrip().startswith("- ") and not line.lstrip().startswith("- slot"):
                        # An action is taken, so we can infer the domain
                        domain = line.strip().split("_")[-1]
                        domains.add(domain)
                        story += [line]
                    else:
                        # User utterance or anything else
                        story += [line]

    if num_stories_train < train_count:
        print(f"WARNING: Only {num_stories_train} out of {train_count} stories found for training.")
    if num_stories_test < test_count:
        print(f"WARNING: Only {num_stories_test} out of {test_count} stories found for testing.")

    print(f"{num_stories_train + num_stories_test + num_stories_unused} stories processed")
    print(f"Training output: {os.path.abspath(train_file_name)}")
    print(f"Testing output : {os.path.abspath(test_file_name)}")


if __name__ == '__main__':

    args = arg_parser.parse_args()

    # Parse input file name
    story_file_name = args.input

    # Parse output file names
    train_file_name = args.train
    if train_file_name is None:
        train_file_name = "auto-stories_train.md"
    test_file_name = args.test
    if test_file_name is None:
        test_file_name = "auto-stories_test.md"

    # Process files
    if args.insights:
        # Print insights and quit
        print_insights()
    else:
        # Parse remaining parameters
        train_domains = args.train_domains
        test_domains = args.test_domains

        train_count = None
        test_count = None
        if args.num_train > 0:
            train_count = args.num_train
        if args.num_test > 0:
            test_count = args.num_test

        if train_count is None or test_count is None:
            if train_count is None and test_count is None:
                count = count_stories()
                train_count = round(count * args.train_test_ratio)
                test_count = round(count * (1.0 - args.train_test_ratio))
            elif train_count is None:
                # noinspection PyTypeChecker
                train_count = round(test_count * args.train_test_ratio / (1.0 - args.train_test_ratio))
            else:
                test_count = round(train_count * (1.0 - args.train_test_ratio) / args.train_test_ratio)

        assert type(train_count) is int
        assert type(test_count) is int
        assert train_count > 0
        assert test_count > 0

        # Split input file into training and testing stories
        print(f"Number of requested training stories: {train_count}")
        print(f"Number of requested testing stories : {test_count}")
        split_file()
