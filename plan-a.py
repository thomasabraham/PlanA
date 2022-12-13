#!/usr/bin/env python3

import click
import calendar
import jinja2
import sys

from datetime import date

@click.group()
def plan_a():
    pass

def parse_month(month):
    months = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12}
    return months.get(month, 0)

def find_start_date(month):
    today = date.today()
    if month < today.month:
        return date(today.year+1, month, 1)
    else:
        return date(today.year, month, 1)

def build_list_of_days(start_date):
    start_week_day, day_count = calendar.monthrange(start_date.year, start_date.month)
    days = []
    for i in range(1,day_count+1):
        day = start_date.replace(day=i)
        days.append({
            'day':day.strftime("%d"),
            'week_days_left': min(7-day.weekday(),day_count+1-i),
            'calendar_week': day.isocalendar().week, # Using python 3.9+ feature
            'week_day':day.strftime("%a")})

    return days

def fill_template(start_date, output):
    env = None
    try:
        env = jinja2.Environment(loader=jinja2.PackageLoader("PlanA"), autoescape=jinja2.select_autoescape())
    except ModuleNotFoundError:
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./templates"), autoescape=jinja2.select_autoescape())

    template = env.get_template("monthly-template.tex.jinja")
    output.write(template.render(month=start_date.strftime("%B - %Y"), days=build_list_of_days(start_date)))


@plan_a.command()
@click.argument('month')
@click.argument('output', default='temp.tex', type=click.File("w"))
def month(month, output):
    """Generate planner for a month. Use three letter code for month jan, feb..."""
    m = parse_month(month)
    if m == 0:
        print(f"Please proved a valid month; eg: jan, feb, mar, etc.", file=sys.stderr)
        return 1
    start_date = find_start_date(m)
    fill_template(start_date, output)

@plan_a.command()
@click.argument('week')
@click.argument('output', default='temp.tex', type=click.File("w"))
def week(week, output):
    """Generate planner for a week. Use calendar week notation like cw45, cw30..."""
    pass

if __name__ == '__main__':
    plan_a()
