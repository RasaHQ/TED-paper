import os
import sys
from termcolor import colored

compute_dir = os.path.abspath("./compute/")


def status(name: str):
    if os.path.exists(os.path.join(compute_dir, name, "test-train.out")):
        if os.path.exists(os.path.join(compute_dir, name, "test-test.out")):
            return "tested"
        else:
            return "unclear"

    if os.path.exists(os.path.join(compute_dir, name, "train.out")):
        return "trained"

    return "new"


if __name__ == '__main__':

    if not os.path.exists(compute_dir):
        raise ValueError(f"Cannot find compute path '{compute_dir}'.")

    experiments = {d: {"date": d[:15], "title": d[16:], "status": status(d)}
                   for d in os.listdir(compute_dir) if d.startswith("2") and not d.endswith("zip")}

    if len(sys.argv) <= 1:
        print()
        print(f"     {'Date':>16}", f"{'Title':>24}", f"{'Status':>12}")
        i = 1
        for experiment, values in sorted(experiments.items(),
                                         key=lambda kv: [
                                             kv[1]["status"],
                                             kv[1]["date"],
                                             kv[1]["title"]],
                                         reverse=False)[:12]:
            if values["status"] == "new":
                color = "green"
            elif values["status"] == "tested":
                color = "blue"
            elif values["status"] == "trained":
                color = "yellow"
            elif values["status"] == "unclear":
                color = "red"
            else:
                color = "white"

            if len(sys.argv) < 2 or sys.argv[1] == values["status"]:
                print(
                    f"{i:>2}: ",
                    colored(f"{values['date']:>16}", color),
                    colored(f"{values['title']:>24}", color),
                    colored(f"{values['status']:>12}", color))

            i += 1
    else:
        options = [experiment for experiment, _ in sorted(experiments.items(),
                                                          key=lambda kv: [
                                                              kv[1]["status"],
                                                              kv[1]["date"],
                                                              kv[1]["title"]],
                                                          reverse=False)]

        indices = sys.argv[1:]
        for i in indices:
            print(options[int(i) - 1])
