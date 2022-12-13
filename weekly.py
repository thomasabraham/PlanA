import re
import jinja2

from datetime import date
from datetime import timedelta

def parse_week(week: str) -> int:
    if re.match(r"^[cC][wW][0-5][0-9]$", week) is None:
        return 0
    w = int(week[2:])
    if w < 1 or w > 53:
        return 0
    return w

def _find_target_week_date(week: int)-> date:
    today = date.today()
    this_week = today.isocalendar().week
    if week >= this_week:
        return today + timedelta(weeks=week-this_week)
    else:
        return today.replace(year=today.year+1) + timedelta(weeks=week-this_week)

def find_start_date(week: int) -> date:
    target_week = _find_target_week_date(week)
    start_week = target_week - timedelta(days=target_week.weekday())
    return start_week

def render_template(start_date: date) -> str:
    env = None
    try:
        env = jinja2.Environment(loader=jinja2.PackageLoader("PlanA"), autoescape=jinja2.select_autoescape())
    except ModuleNotFoundError:
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./templates"), autoescape=jinja2.select_autoescape())

    template = env.get_template("weekly-template.tex.jinja")
    return template.render(start_date=start_date)
