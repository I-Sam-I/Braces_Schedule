from datetime import date, timedelta
from tabulate import tabulate
import constants


def build_schedule() -> list:
    """Builds a list of dictionaries representing the schedule.
    Each dictionary has the set number, day, and dates.

    Returns:
        list: list of dictionaries.
    """

    schedule: list = []
    for set in range(constants.TOTAL_SETS):
        date_to_change: date = timedelta(
            days=constants.DAYS_INTERVAL * set) + constants.START_DATE

        schedule.append({
            "Set": set + 1,
            "Day": date_to_change.strftime('%A').upper(),
            "Date Words": date_to_change.strftime('%d %B, %Y').upper(),
            "Date No.": date_to_change.strftime('%m-%d-%Y')
        })

    return schedule


def tabulate_schedule(schedule: list) -> str:
    """Return a tabular representation of the schedule.

    Args:
        schedule (list): A list of dictionaries representing the schedule.

    Returns:
        str: tabulate() formatted string.
    """

    return tabulate(
        tabular_data=schedule,
        headers="keys",
        stralign="center",
        tablefmt="fancy_grid"
    )
