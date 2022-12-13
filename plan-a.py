#!/usr/bin/env python3

import click
import sys
import monthly
import weekly


@click.group()
def plan_a():
    pass


@plan_a.command()
@click.argument('month')
@click.argument('output', default='temp.tex', type=click.File("w"))
def month(month, output):
    """Generate planner for a month. Use three letter code for month jan, feb..."""
    m = monthly.parse_month(month)
    if m == 0:
        click.echo(f"Please proved a valid month; eg: jan, feb, mar, etc.", file=sys.stderr)
        return 1
    start_date = monthly.find_start_date(m)
    click.echo(f"Generating monthly planner for month starting on {start_date}")
    output.write(monthly.render_template(start_date))


@plan_a.command()
@click.argument('week')
@click.argument('output', default='temp.tex', type=click.File("w"))
def week(week, output):
    """Generate planner for a week. Use calendar week notation like cw45, cw30..."""
    w = weekly.parse_week(week)
    if w == 0:
        click.echo(f"Calendar week {week} is not valid!")
        return 1
    pass


if __name__ == '__main__':
    plan_a()
