#!/usr/bin/env python

import argparse
import re

#DATA_PATTERN = '(\d+(\.\d+)?)(,(\d+(\.\d+)))+'
DATA_PATTERN = '(\d+(\.\d+)?)'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, nargs='+',
                        help="file(s) to scan")
    return parser.parse_args()


data_re = re.compile(DATA_PATTERN)

## Main ####################

if __name__=='__main__':
    args = parse_args()
    prev_ts = 0
    ts_interval = 0
    for fn in sorted(args.file):
        print("scanning {}...".format(fn))
        with open(fn, 'r') as f:
            for line in f:
                match = data_re.match(line.rstrip()) 
                if not match:
                    print("MISMATCH({0}): {1}".format(fn, line.rstrip()))
                    continue
                ts = float(match.group(1))
                if prev_ts == 0:
                    prev_ts = ts
                    continue
                if ts_interval == 0:
                    ts_interval = round( ts - prev_ts )
                    prev_ts = ts
                    print("Interval set to {0}s".format(ts_interval))
                    continue
                if round( ts - prev_ts ) != ts_interval:
                    print("*** GAP({0}): {1} - {2}".format(fn, prev_ts, ts))
                prev_ts = ts

    print("done.")





## Local Variables:
## mode: python
## End:
