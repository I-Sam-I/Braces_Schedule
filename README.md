# Braces_Schedule
A python script that prints a schedule of my braces.
The schedule is for my InvisAlign braces that I have to change every 10 days.

## main.py
* The main program that prints the schedule.

## helpers.py
* Helper functions that are used in `main.py`
    + ### build_schedule()
        Returns a list of dictionaries that represent the schedule. <br>
        Each dictionary has the keys: 
        - **Set**: Represents which braces I should be wearing.
        - **Day**: Is the day of the week when I should change my braces.
        - **Date Words**: Is the date when I should change my braces in words.
        - **Date No.**: Is the date when I should change my braces in numbers.
    
    + ### tabulate_schedule()
        Tabulates the list of dictionaries, using the `tabulate` module, into a table that is returned.

## constants.py
* Constants that are used in `helpers.py`
    + **TOTAL_SETS**: Is the number of sets of braces I should wear.
    + **START_DATE**: Is the date I started wearing the braces.
    + **DAYS_INTERVAL**: Is the number of days I should wear a set of braces before changing them.