#!/usr/bin/env python3

# Copyright  2017  Jian Wang
#            2017  Daniel Povey
# License: Apache 2.0.

import argparse
import sys
import random
import math

parser = argparse.ArgumentParser(description="This script is used to randomly initialize "
                                 "Kaldi-format matrices, with supplied dimensions and "
                                 "standard deviation.",
                                 epilog="E.g. " + sys.argv[0] + " --num-rows=10 --num-cols=20 "
                                 "--param-stddev=0.05 > exp/rnnlm1/embedding.mat",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("--num-rows", type=int, required=True,
                    help="Number of rows for the matrix ")
parser.add_argument("--num-cols", type=int, required=True,
                    help="Number of columns for the matrix ")
parser.add_argument("--stddev", type=float, default=-1.0,
                    help="Standard deviation of individual parameters.  If not "
                    "set to a value >= 0.0, defaults to 1/sqrt(num-cols).")
parser.add_argument("--srand", type=int, default=0,
                    help="Number of columns for the matrix ")


args = parser.parse_args()


if args.num_rows <= 0:
    sys.exit("--num-rows must be >0.")
if args.num_cols <= 0:
    sys.exit("--num-rows must be >0.")
if args.stddev < 0.0:
    stddev = 1.0 / math.sqrt(args.num_cols)
else:
    stddev = args.stddev

random.seed(args.srand)

print("[ ", end="")
for _ in range (args.num_rows):
    for _ in range(args.num_cols):
        if args.stddev == 0.0:
            r = 0.0
        else:
            r = random.gauss(0.0, stddev)
        print("{0:0.2g} ".format(r), end="")
    print("")  # newline
print("]")
