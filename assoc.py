import argparse
import subprocess
import yaml
import sys

ANY_PATTERN="."

def read_constrained(prompt, type_f):
    try:
        return type_f(raw_input(prompt))
    except ValueError:
        print("not valid, try again")
        return read_constrained(prompt, type_f)

def assoc_open(file, openers):
    if len(openers) == 1:
        subprocess.call([openers[0], file])
    else:
        print("multiple options:")
        for i, exe in enumerate(openers):
            print(" : ".join([str(i), exe]))
        try:
            def valid_pick(pick):
                pick = int(pick)
                if pick >= len(openers):
                    raise ValueError();
                return pick
            entry = read_constrained("pick opener (or ^C to exit): ", valid_pick)
            assoc_open(file, [openers[entry]])
        except KeyboardInterrupt:
            print("")
            return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A file association manager")
    parser.add_argument("file", type=str);
    parser.add_argument("--list", action="store_true");
    args = parser.parse_args()

    # load the 
    config = yaml.load(open(".assocrc"));

    for [patterns, exes] in config["global"]:
        # get file extension
        extension = ".".join(args.file.split(".")[1:])
        # make sure pattern is in listed patterns
        if extension in patterns or ANY_PATTERN in patterns:
            if args.list:
                # list openers
                for exe in exes:
                    print(exe)
            else:
                assoc_open(args.file, exes)
