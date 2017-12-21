#!/usr/bin/env python

import sys
from typing import Optional

current_word: Optional[str] = None
word_count = 0
word: Optional[str] = None
count: Optional[str] = None

for line in sys.stdin:

    word, count = line.split('\t', 1)

    int_count: int = int(count)

    if word == current_word:
        word_count += int_count
    else:
        if current_word:
            print(current_word, word_count, sep='\t')
        current_word = word
        word_count = int_count

if current_word:
    print(current_word, word_count, sep='\t')
