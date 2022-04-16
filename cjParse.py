#!/usr/bin/env python

# Simple CSV to JSON converter.
# No files, just stdin and stdout like a real tool should be
# Jim Sander

import csv
import json
import sys

data = []

with sys.stdin as csvf:
    csvReader = csv.DictReader(csvf)
    for row in csvReader:
        data.append(row)

print(json.dumps(data, indent=4))

