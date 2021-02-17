#!/usr/bin/env python3

import sys
import os
#  import getopt

def exec(args):
    link, name, path = args[0:]

    os.system(f"youtube-dl -x {link} -o {name}.opus --audio-format opus")
    os.system(f"mv {name}.opus {path}")

    print(f"[ok] {name}.opus")

if __name__ == "__main__":
    exec(sys.argv[1:])
