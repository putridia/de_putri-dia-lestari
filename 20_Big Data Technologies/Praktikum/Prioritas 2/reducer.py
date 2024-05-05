#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
current_sum = 0

for line in sys.stdin:
    # Remove tab character
    line = line.strip()
    # Split line into key and value
    key, value = line.split('\t', 1)

    if current_word == key:
        current_count += 1
        current_sum += float(value)
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_sum / current_count))
            current_count = 1
            current_sum = float(value)
            current_word = key

if current_word == key:
    print('%s\t%s' % (current_word, current_sum / current_count))