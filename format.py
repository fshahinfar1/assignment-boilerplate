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
    total_length = length
    result = []
    prev = 0
    while length > 0:
        delta = min(limit, length)
        start = prev
        end = start + delta
        while end > start and line[end - 1] not in whitespace:
            end -= 1
            delta -= 1
        if end == start:
            # Use whole line
            # TODO: what is this condition??
            tmp = line[start:] + '\n'
            delta = total_length - start
        else:
            tmp = line[start:end]
            if tmp[-1] != '\n':
                tmp += '\n'
        result.append(tmp)
        length -= delta
        prev = end
    return result


def get_left_over(lines):
    count = len(lines)
    if count == 1:
        return '', 0
    last_line = lines[-1]
    length = len(last_line)
    if last_line[-1] == '\n':
        last_line = last_line[:-1]
        length -= 1
    return last_line, length


def may_connect_to_prev_line(line):
    tmp = line.lstrip()
    if not tmp:
        return False
    elif tmp.startswith('\\'):
        return False
    return True


def main(args):
    file_path = args.file
    if not os.path.exists(file_path):
        return
    if not os.path.isfile(file_path):
        return

    limit = conf['line_length']
    result = []
    left_line = ''
    left_line_len = 0
    with open(file_path) as f:
        for line in f:
            # Check if should connect to the prev line
            if left_line_len > 0:
                # If there exists line from previous operations
                if may_connect_to_prev_line(line):
                    line = left_line + ' ' + line
                else:
                    result.append(left_line + '\n')
                    left_line = ''
                    left_line_len = 0

            # Check if line should be formated
            length = len(line)
            if length > limit:
                broken_lines = apply_line_length_limit(line, length)
                left_line, left_line_len = get_left_over(broken_lines)
                if left_line_len > 0:
                    # if there is left over line then remove if
                    # from the list before commiting to the results
                    broken_lines.pop()
                result.extend(broken_lines)
            else:
                result.append(line)

        if left_line_len > 0:
            result.append(left_line)

    for line in result:
        print(line, end='')


if __name__ == '__main__':
    args = parse_args()
    main(args)
