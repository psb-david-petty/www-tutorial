#!/usr/bin/env python3
#
# table.py
#
import csv, os

# Constants
filename = 'nces-table-data.csv'
indent, nl = ' ' * 2, '\n'
caption = f"{indent * 1}<caption>2015-2016 NCES Computing / STEM degrees</caption>"
header, footer = f"{indent * 0}<table>", f"{indent * 0}</table>"
thead_header, thead_footer = f"{indent * 1}<thead>", f"{indent * 1}</thead>"
tbody_header, tbody_footer = f"{indent * 1}<tbody>", f"{indent * 1}</tbody>"
tfoot_header, tfoot_footer = f"{indent * 1}<tfoot>", f"{indent * 1}</tfoot>"

def main(path, n, m):
    """Return path .CSV file formatted as an HTML table w/ n rows in <thead>
    and m rows in <tfoot>."""
    cell_start, cell_end, i = '<th>', '</th>', 0
    with open(path, newline='') as csvfile:
        html = f"{header}\n{caption}\n{thead_header}\n"
        reader = csv.reader(csvfile)
        rows = [ row for row in reader ]    # read entire .CSV
        assert n + m <= len(rows), f"n ({n}) + m ({m}) > #rows ({len(rows)})"
        for row in rows:
            if i == n:
                html += f"{thead_footer}\n{tbody_header}\n"
                cell_start, cell_end = '<td>', '</td>'
            # https://twitter.com/dabeaz/status/810217326293479425
            line = f"{cell_start}{f'{cell_end}{cell_start}'.join(row)}{cell_end}"
            html += f"{indent * 2}<tr>{line}</tr>\n"
            if i == len(rows) - 1 - m:
                html += f"{tbody_footer}\n{tfoot_header}\n"
            i += 1
        html += f"{tfoot_footer}\n{footer}\n"
    return html

if __name__ == '__main__':
    doctype_header = '<!DOCTYPE html><html lang="en"><head><title>TABLE</title></head><body>'
    print(doctype_header)   # for W3 Validator

    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)
    head_lines = 2          # number of lines from beginning before switching to <tbody>
    foot_lines = 0          # number of lines from end before switching to <tfoot>
    print(main(path, head_lines, foot_lines))
