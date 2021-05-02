#!/usr/bin/python3
"""
This file transform Markdown to HTML
"""
import sys
import re


def headings(data, count):
    """heading tags"""
    write = []
    content = ' '.join([str(elem) for elem in re.split(' |\n', data)[1:-1]])
    if 1 <= count <= 6:
        write.append('<h{}>{}</h{}>'.format(count, content, count))
    return write


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        sys.exit(1)

    try:
        # Opens a markdown file and gets a list of lines to be added to a html file
        with open(sys.argv[1], 'r') as markdown:
            data = markdown.readlines()
            write = []

            for line in data:
                headings_number = len(line) - len(line.lstrip('#'))

                if 1 <= headings_number <= 6:
                    new_list = headings(line, headings_number)
                write.append(new_list)
        # Write into an html file
        with open(sys.argv[2], 'w', encoding="utf-8") as html:
            content = '\n'.join([str(char)
                                 for elem in write for char in elem])
            html.write(content + '\n')
        sys.exit(0)
    except FileNotFoundError:
        sys.stderr.write('Missing {}\n'.format(sys.argv[1]))
        sys.exit(1)
