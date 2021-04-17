# Built-in imports
import datetime


def formatted_now(include_date=False):
    """
    Pretty-prints the current time float

    Returns:
        str: formatted now time string in "HH:MM:SS:_MS"
    """
    now = datetime.datetime.now()
    return f"{now.month}/{now.day}/{now.year} {now.hour:02d}:{now.minute:02d}:{now.second:02d}:{int(now.microsecond / 1000):03d}"


def format_time(time_float):
    """
    Pretty-prints the time float

    Args:
        time_float (float): float representing seconds from epoch

    Returns:
        str: formatted time string in "HH:MM:SS:_MS"
    """
    minute, second = divmod(time_float, 60)
    hour, minute = divmod(minute, 60)
    millisecond = time_float % 1 * 100
    return f"{int(hour):02d}:{int(minute):02d}:{int(second):02d}:{int(millisecond):03d}"


def get_now_weekday():
    """
    Get current time's weekday

    Returns:
        int: integer ranged [0, 6] representing current weekday (Monday=0, Sunday=6)
    """
    return datetime.datetime.today().weekday()


if __name__ == "__main__":
    print(formatted_now(True))
