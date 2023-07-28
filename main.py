from helpers import build_schedule, tabulate_schedule
from time import sleep


def main() -> None:
    schedule: list = build_schedule()
    print(tabulate_schedule(schedule))
    while True:
        sleep(1)


if __name__ == "__main__":
    main()
 