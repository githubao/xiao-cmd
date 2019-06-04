#!/usr/bin/env python
# encoding: utf-8

"""
@description: 去重统计

@author: baoqiang
@time: 2019-06-04 12:01
"""

import re

exists = set()
ordered = []

filename = 'day01.md'


def dup():
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if not line.startswith('1. '):
                continue

            cmd = line.lstrip('1. ').strip()

            if cmd in exists:
                print('dup: {}'.format(cmd))
            else:
                exists.add(cmd)
                ordered.append(cmd)

    print('len: {}'.format(len(exists)))
    # print('\n'.join(sorted(list(exists))))

    for item in ordered:
        item = re.sub('\\(.*', '', item)
        print('tldr {} >> 1.txt'.format(item))


if __name__ == '__main__':
    dup()
