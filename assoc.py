import argparse
import subprocess
import yaml

ANY_PATTERN="."

def assoc_open(file, openers):
    subprocess.call([openers[0], file], stdout=subprocess.PIPE)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A file association manager")
    parser.add_argument("file", type=str);
    parser.add_argument("--open", action="store_true");
    args = parser.parse_args()

    # load the 
    config = yaml.load(open(".assocrc"));

    for [patterns, exes] in config["global"]:
        # get file extension
        extension = ".".join(args.file.split(".")[1:])
        # make sure pattern is in listed patterns
        if extension in patterns or ANY_PATTERN in patterns:
            if args.open:
                # open it if argument is set
                assoc_open(args.file, exes)
            else:
                # otherwise print the list of openers
                for exe in exes:
                    print(exe)
