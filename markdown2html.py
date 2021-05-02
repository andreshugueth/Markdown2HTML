#!/usr/bin/python3
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as markdown:
            sys.exit(0)
    except FileNotFoundError:
        sys.stderr.write('Missing {}\n'.format(sys.argv[1]))
        sys.exit(1)
