import re

def parse_week(week):
    if re.match(r"^[cC][wW][0-5][0-9]$", week) is None:
        return 0
    w = int(week[2:])
    if w < 1 or w > 53:
        return 0
    return w
