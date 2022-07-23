# Graduation data

These are the [source data](https://drive.google.com/drive/folders/1C67aJRFVLu_cyeMYJ0CJLeOLEBYtjW2b) for a table exercise. I thought it would be interesting to get actual pre-pandemic higher-education data for *all*, *STEM*, and *computing* degrees awarded &mdash; including race and sex demographics whereever possible.It took a lot to cook these data into a .CSV file and then a Python script to create the table. The table is available at [https://codepen.io/psb-david-petty/pen/dymvrNQ](https://codepen.io/psb-david-petty/pen/dymvrNQ?editors=1000).

## NCES &mdash; National Center for Education Statistics

- [https://www.pewresearch.org/fact-tank/2021/04/14/6-facts-about-americas-stem-workforce-and-those-training-for-it/](https://www.pewresearch.org/fact-tank/2021/04/14/6-facts-about-americas-stem-workforce-and-those-training-for-it/)
- [https://nces.ed.gov/programs/digest/current_tables.asp](https://nces.ed.gov/programs/digest/current_tables.asp)

## Tables 318

- [https://nces.ed.gov/programs/digest/d21/tables/dt21_318.10.asp](https://nces.ed.gov/programs/digest/d21/tables/dt21_318.10.asp) Table 318.10. Degrees conferred by postsecondary institutions, by level of degree and sex of student: Selected years, 1869-70 through 2030-31
- [https://nces.ed.gov/programs/digest/d21/tables/dt21_318.20.asp](https://nces.ed.gov/programs/digest/d21/tables/dt21_318.20.asp) Table 318.20. Bachelor's, master's, and doctor's degrees conferred by postsecondary institutions, by field of study: Selected years, 1970-71 through 2019-20
- [https://nces.ed.gov/programs/digest/d20/tables/dt20_318.30.asp](https://nces.ed.gov/programs/digest/d20/tables/dt20_318.30.asp) Table 318.30. Bachelor's, master's, and doctor's degrees conferred by postsecondary institutions, by sex of student and field of study: 2018-19
- [https://nces.ed.gov/programs/digest/d21/tables/dt21_318.45.asp](https://nces.ed.gov/programs/digest/d21/tables/dt21_318.45.asp) Table 318.45. Number and percentage distribution of science, technology, engineering, and mathematics (STEM) degrees/certificates conferred by postsecondary institutions, by race/ethnicity, level of degree/certificate, and sex of student: 2010-11 through 2019-20
- [https://nces.ed.gov/programs/digest/d20/tables/dt20_318.50.asp](https://nces.ed.gov/programs/digest/d20/tables/dt20_318.50.asp) Table 318.50. Degrees conferred by postsecondary institutions, by control of institution, level of degree, and field of study: 2018-19

## Tables 322

- [https://nces.ed.gov/programs/digest/d21/tables/dt21_322.20.asp](https://nces.ed.gov/programs/digest/d21/tables/dt21_322.20.asp) Table 322.20. Bachelor's degrees conferred by postsecondary institutions, by race/ethnicity and sex of student: Selected years, 1976-77 through 2019-20
- [https://nces.ed.gov/programs/digest/d21/tables/dt21_322.40.asp](https://nces.ed.gov/programs/digest/d21/tables/dt21_322.40.asp) Table 322.40. Bachelor's degrees conferred to males by postsecondary institutions, by race/ethnicity and field of study: 2018-19 and 2019-20
- [https://nces.ed.gov/programs/digest/d21/tables/dt21_322.50.asp](https://nces.ed.gov/programs/digest/d21/tables/dt21_322.50.asp) Table 322.50. Bachelor's degrees conferred to females by postsecondary institutions, by race/ethnicity and field of study: 2018-19 and 2019-20
323

## Tables 323

- [https://nces.ed.gov/programs/digest/d21/tables/dt21_323.20.asp](https://nces.ed.gov/programs/digest/d21/tables/dt21_323.20.asp) Table 323.20. Master's degrees conferred by postsecondary institutions, by race/ethnicity and sex of student: Selected years, 1976-77 through 2019-20
- [https://nces.ed.gov/programs/digest/d21/tables/dt21_323.40.asp](https://nces.ed.gov/programs/digest/d21/tables/dt21_323.40.asp) Table 323.40. Master's degrees conferred to males by postsecondary institutions, by race/ethnicity and field of study: 2018-19 and 2019-20
- [https://nces.ed.gov/programs/digest/d21/tables/dt21_323.50.asp](https://nces.ed.gov/programs/digest/d21/tables/dt21_323.50.asp) Table 323.50. Master's degrees conferred to females by postsecondary institutions, by race/ethnicity and field of study: 2018-19 and 2019-20

## Tables 324

- [https://nces.ed.gov/programs/digest/d21/tables/dt21_324.20.asp](https://nces.ed.gov/programs/digest/d21/tables/dt21_324.20.asp) Table 324.20. Doctor's degrees conferred by postsecondary institutions, by race/ethnicity and sex of student: Selected years, 1976-77 through 2019-20
- [https://nces.ed.gov/programs/digest/d21/tables/dt21_324.30.asp](https://nces.ed.gov/programs/digest/d21/tables/dt21_324.30.asp) Table 324.30. Doctor's degrees conferred to males by postsecondary institutions, by race/ethnicity and field of study: 2018-19 and 2019-20
- [https://nces.ed.gov/programs/digest/d21/tables/dt21_324.35.asp](https://nces.ed.gov/programs/digest/d21/tables/dt21_324.35.asp) Table 324.35. Doctor's degrees conferred to females by postsecondary institutions, by race/ethnicity and field of study: 2018-19 and 2019-20

## `table.py`

```
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
```
