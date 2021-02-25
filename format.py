#!/usr/bin/python3
"""
Farbod Shahinfar
25/02/2021
Format my latex files with 80 line limit constraint.

For ease of use create a link to this scrip
ln -s ./format.py ~/.local/bin/fmtex
"""
import os
import argparse
from string import whitespace


conf = {
        'line_length': 80,
        }


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    return args


def apply_line_length_limit(line, length):
    # TODO(farbod): this may break the latex commands
    limit = conf['line_length']
    result = []
    prev = 0
    while length > 0:
        delta = min(limit, length)
        start = prev
        end = start + delta
        while end > 1 and line[end - 1] not in whitespace:
            end -= 1
            delta -= 1
        tmp = line[start:end]
        if tmp[-1] != '\n':
            tmp += '\n'
        result.append(tmp)
        length -= delta
        prev = end
    return result


def main(args):
    file_path = args.file
    if not os.path.exists(file_path):
        return
    if not os.path.isfile(file_path):
        return

    limit = conf['line_length']
    result = []
    with open(file_path) as f:
        for line in f:
            length = len(line)
            if length > limit:
                broken_lines = apply_line_length_limit(line, length)
                result.extend(broken_lines)
            else:
                result.append(line)

    for line in result:
        print(line, end='')


if __name__ == '__main__':
    args = parse_args()
    main(args)
