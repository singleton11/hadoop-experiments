#!/usr/bin/env python

import sys
from typing import List, Optional

import re

article_id: Optional[str] = None

for line in sys.stdin:
    text: Optional[str] = None

    try:
        article_id, text = line.strip().split('\t', 1)
    except ValueError as e:
        continue

    article_text: str = re.sub('^\W+|\W+$', '', text)
    words: List[str] = re.split('\W*\s+\W*', text)

    with open('stop_words.txt') as f:
        stop_words = f.read().split('\n')
        counter = 0
        for index, word in enumerate(words):
            if word in stop_words:
                counter += 1
                print(f'reporter:counter:stop_words,stop_words,{counter}', file=sys.stderr)
            print(f'reporter:counter:stop_words,words_total,{index + 1}', file=sys.stderr)
            print(word, 1, sep='\t')
