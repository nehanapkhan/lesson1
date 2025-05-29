from datetime import datetime
from zoneinfo import ZoneInfo  # Available in Python 3.9+

def is_daylight_saving(date: datetime, timezone_str: str) -> bool:
    """
    Check if the given date is in daylight saving time (summer time)
    using the zoneinfo module.

    Args:
        date (datetime): The date to check.
        timezone_str (str): Timezone name (e.g., 'Europe/London', 'America/New_York').

    Returns:
        bool: True if the date is in daylight saving time, False otherwise.
    """
    try:
        tz = ZoneInfo(timezone_str)
        localized_date = date.replace(tzinfo=tz)
        return bool(localized_date.dst())
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    user_input = input("Enter date (YYYY-MM-DD): ")
    timezone_input = input("Enter timezone (e.g., Europe/London): ")

    try:
        date_obj = datetime.strptime(user_input, "%Y-%m-%d")
        in_dst = is_daylight_saving(date_obj, timezone_input)
        print(f"{user_input} in {timezone_input} is {'in' if in_dst else 'not in'} daylight saving time (summer time).")
    except ValueError as ve:
        print(f"Invalid date format: {ve}")
