#!/usr/bin/env python3
import os
import shutil
import sys


def main(argv):
    source = ""
    output = ""
    depfile = ""
    skip_next = False

    for index, arg in enumerate(argv):
        if skip_next:
            skip_next = False
            continue
        if arg == "-o" and index + 1 < len(argv):
            output = argv[index + 1]
            skip_next = True
        elif arg == "-MF" and index + 1 < len(argv):
            depfile = argv[index + 1]
            skip_next = True
        elif not arg.startswith("-") and os.path.exists(arg):
            source = arg

    if not source:
        print("preproc_passthrough: source file not found", file=sys.stderr)
        return 1

    if output and output not in (os.devnull, "/dev/null", "NUL"):
        output_dir = os.path.dirname(output)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        shutil.copyfile(source, output)

    if depfile:
        dep_dir = os.path.dirname(depfile)
        if dep_dir:
            os.makedirs(dep_dir, exist_ok=True)
        target = output or os.devnull
        with open(depfile, "w", encoding="utf-8") as dep:
            dep.write(f"{target}: {source}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
