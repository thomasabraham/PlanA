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
### To generate a monthly planner
``` shell
./plan-a.py month nov && pdflatex temp.tex
```
### To generate a weekly planner

``` shell
./plan-a.py week cw33 && pdflatex temp.tex
```

