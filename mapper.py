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

    for word in words:
        print(word, 1, sep='\t')
