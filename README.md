# PlanA
A printable planner generator that uses ISO 216 A series papers.

## dependencies

### click
To implement command line interface.

### Jinja2
Template to generate the intermediate latex document.

### texlive
To convert latex document to pdf using pdflatex

## Use

``` shell
./plan-a.py nov > temp.tex
pdflatex temp.tex
```
