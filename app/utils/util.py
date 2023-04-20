from typing import Tuple


def duration_string_formatter(seconds: int) -> str:
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    hour_str: str = ""
    minute_str: str = ""
    second_str: str = "00"
    if not h == 0:
        hour_str = f"{h}:"
    if not m == 0:
        minute_str = f"{m}:"
    if s > 9:
        second_str = f"{s}"
    else:
        second_str = f"0{s}"
    return hour_str + minute_str + second_str
