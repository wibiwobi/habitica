# ! ADD A BACK FEATURE

default_print = print

from rich import print
import time
import sys
from rich.prompt import Prompt
import calendar
import random
import json
import traceback

# TODO: JSON FEATURE
    # DISPLAY - output all habits for log_habit, output_one...streak, delete_habit
    # READING - output one and output all habit streak funtion

def add_all_habits_to_json(habits):
    try:
        # load all the data from habit_data.json
        # perform read and write of habit_data.json
        with open("habit_data.json", "r+") as file:
            habit_data = json.load(file)

            for habit in habits:
                habit_data[habit] = {}

            file.seek(0)
            json.dump(habit_data, file, indent=2)
    except Exception as e:
        print(e)

def log_streak_to_json(habit_key, month, day):
    # all keys in json when fetched are all strings
    habit_key = str(habit_key)
    month = str(month)

    try:    
        with open("habit_data.json", "r+") as file:
            habit_data = json.load(file)

            if month in habit_data[habit_key] and day not in habit_data[habit_key][month]: # month is already existing in the dictionary
                habit_data[habit_key][month].append(day) # only add the day 
            elif month not in habit_data[habit_key]:
                habit_data[habit_key][month] = [day] # create a month key and add the day inside a dictionary

            file.seek(0)
            json.dump(habit_data, file, indent=2)

    except Exception as e:
        print(e)

def fetch_all_habit_data():
    with open("habit_data.json", "r") as file:
        habit_records = json.load(file)
    return habit_records


def display_all_habits(bright_colors):
    habit_records = fetch_all_habit_data()
    
    print("[bold bright_blue]Habit(s):[/bold bright_blue]")
    for i, habit in enumerate(habit_records):
        bright_color = random.choice(bright_colors)
        print(f"[{bright_color}][{i}] {habit}[/{bright_color}]")
    print()

def fetch_all_habit_keys():
    habit_records = fetch_all_habit_data()
    
    key_habit_records_list = []
    for i, habit in enumerate(habit_records):
        key_habit_records_list.append(habit)

    return key_habit_records_list

    

 

def add_habit():
    print("[bold red]█   █  ███  ████  ███ █████ ███  ███   ███[/bold red]")  
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█████ █████ ████   █    █    █  █     █████[/bold red]") 
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█   █ █   █ ████  ███   █   ███  ███  █   █[/bold red]\n")
    while True:     
        # ask what habit to add (only string, dont accept empty string)
        try:
            print("[magenta bold]ADD A HABIT TO TRACK IT LATER![/magenta bold]")
            print("To exit the prompt type \"x\" without the double quotes")
            print("\'To add more than one habit separate them by spaces\'\n")

            # ask what habit to add (only string, dont accept empty string)
            habits = str(Prompt.ask("[light_cyan1 bold]Habit(s) [/light_cyan1 bold]")).split()
            if habits == []: 
                raise Exception("Input is empty!") 

            elif habits[0] == "x": # exit if the user inputs 'x'
                delete_lines(11)
                break
            
            else: # add the habit
                add_all_habits_to_json(habits)
                delete_lines(11)
                break
        except:
            print("Input is [magenta bold]EMPTY![/magenta bold]")
            time.sleep(2)
            delete_lines(6)


def log_habit(bright_colors): 
    from datetime import datetime
    
    print("[bold red]█   █  ███  ████  ███ █████ ███  ███   ███[/bold red]")  
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█████ █████ ████   █    █    █  █     █████[/bold red]") 
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█   █ █   █ ████  ███   █   ███  ███  █   █[/bold red]\n\n")

    habit_records = fetch_all_habit_data()

    # prevent the user from inputting anything if the habit_records is empty
    if not habit_records:
        print("There are no habits to log...")
        input("Press \'enter\' to continue..")
        default_print("\033[2J]\033[3J]\033[H")
        return

    print("type \'x\' if you want to exit\n")
  
    key_habit_records_list = fetch_all_habit_keys()
    display_all_habits(bright_colors)


    # ask what habit to log
    while True:
        try:
            decision_number = str(Prompt.ask(f"[light_cyan1 bold]Pick a habit from [0 - {len(key_habit_records_list) - 1}] [/light_cyan1 bold]"))
            if decision_number == 'x': # exit the function
                default_print("\033[2J]\033[3J]\033[H")
                return 
            else:
                decision_number = int(decision_number)

            if decision_number < 0 or decision_number > len(key_habit_records_list) - 1: # number does NOT ranges from 0 to the last habit index
                raise ValueError(f"decision_number is not valid, it should range only from 0 - {len(key_habit_records_list) - 1}")
            else:
                delete_lines(3 + len(key_habit_records_list))
                break
        except:
            print(f"Input should be an [bold red]integer[/bold red] and [bold red]ranges from 0 to {len(key_habit_records_list) - 1}![/bold red]")
            time.sleep(2)
            delete_lines(2)

    # Adding a date to log the habit
    while True:
        try:
            date_decision = input("Manually input date [y/n]? ")

            if date_decision == 'x': # exit the function
                default_print("\033[2J]\033[3J]\033[H")
                return 

            if date_decision == 'y': # manually input the month and day
                while True:
                    try:
                        month = input("Month [1 - 12]: ")

                        if month == 'x': # exit the function
                            default_print("\033[2J]\033[3J]\033[H")
                            return 
                        else:
                            month = int(month) 


                        if month < 1 or month > 12:
                            raise ValueError("Invalid month input")
                        else:
                            delete_lines(1)
                            break
                    except:
                        print("Invalid [bold blue]month[/bold blue]!")
                        time.sleep(2)
                        delete_lines(2)

                
                total_days_in_month = calendar.monthrange(2026, month)[1] # get the total days in a month

                while True:
                    try:
                        # input the nth day of the month
                        day = input(f"Day [1 - {total_days_in_month}]: ")

                        if day == 'x': 
                            default_print("\033[2J]\033[3J]\033[H")
                            return 
                        else:
                            day = int(day)

                        if day < 1 or day > total_days_in_month:
                            raise ValueError("Invalid day input")
                        else:
                            delete_lines(1)
                            break
                    except:
                        print("Invalid [bold blue]day[/bold blue]!")
                        time.sleep(2)
                        delete_lines(2)
                

                # log it
                habit_key = key_habit_records_list[decision_number]
                log_streak_to_json(habit_key, month, day)
                delete_lines(12)
                break
                   
            elif date_decision == 'n': # automatic date (current date)
                present_day = datetime.now().day
                present_month = datetime.now().month
                habit_key = key_habit_records_list[decision_number]
                log_streak_to_json(habit_key, present_month, present_day)
                delete_lines(10)
                break
            else:
                raise ValueError("date decision should be either a y/n")
            
        except Exception as e:
            print("Input should either be a [bold blue]y[/bold blue] or [bold red]n[/bold red]!")
            time.sleep(2)
            delete_lines(2)
    


def output_one_habit_streak(bright_colors):
    print("[bold red]█   █  ███  ████  ███ █████ ███  ███   ███[/bold red]")  
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█████ █████ ████   █    █    █  █     █████[/bold red]") 
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█   █ █   █ ████  ███   █   ███  ███  █   █[/bold red]\n")

    habit_records = fetch_all_habit_data()

    # prevent the user from inputting anything if the habit_records is empty
    if not habit_records:
        print("There are no habits to display...")
        input("Press \'enter\' to continue..")
        default_print("\033[2J]\033[3J]\033[H")
    
        return

    key_habit_records_list = fetch_all_habit_keys()
    display_all_habits(bright_colors)

    # ask what habit to display its streak (2026)
    while True:
        try:
            decision_number = Prompt.ask(f"[light_cyan1 bold]Pick a habit streak to display from [0 - {len(key_habit_records_list) - 1}] [/light_cyan1 bold]")

            if decision_number == "x": # exit the function
                default_print("\033[2J]\033[3J]\033[H")
                return 
            else:
                decision_number = int(decision_number)


            if decision_number < 0 or decision_number > len(key_habit_records_list) - 1:
                raise ValueError(f"decision_number is not valid, it should range only from 0 - {len(key_habit_records_list) - 1}")
            else:
                delete_lines(3 + len(key_habit_records_list))
                break
        except:
            print(f"Input should be an [bold red]integer[/bold red] and [bold red]ranges from 0 to {len(key_habit_records_list) - 1}![/bold red]")
            time.sleep(2)
            delete_lines(2)

    habit_key = key_habit_records_list[decision_number]

    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    days = {1: "Su", 2: "Mo", 3: "Tu", 4: "We", 5: "Th", 6: "Fr", 7: "Sa"}
    
    month = 1 # starting index for the month (January)
    cal = calendar.Calendar(firstweekday=6) # cal object, gives a lot of functions out of the box

    print(f"\n\n[bold hot_pink]{habit_key:^70}[/bold hot_pink]")
    print(f"\n{"2026":^70}\n")

    for i in range(4): # four rows total
                       # row1 = jan, feb, march 
                       # row2 = april, may, june
                       # row3 = july, august, september
                       # row4 = october, november, december

        # Output: Ex (Changes overtime, this is just an example format) --> January          February             March
        print(f"{months[month]:^20}{months[month + 1]:^30}{months[month+2]:^20}")

        # Output: Su Mo Tu We Th Fr Sa       Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
        for i in range(3):
            print(f"{days[1]:^3}{days[2]:^3}{days[3]:^3}{days[4]:^3}{days[5]:^3}{days[6]:^3}{days[7]:^3}", end=f"{"":<4}")

        print()

        # month1, month2 and month3's values is a 2d array, each index is an array containing days in one row
        # [[0, 1, 2, 3], [4, 5, 6, 7]]
        month1 = cal.monthdayscalendar(2026, month) 
        month2 = cal.monthdayscalendar(2026, month + 1) 
        month3 = cal.monthdayscalendar(2026, month + 2) 


        # errors are catched if index is out of bounds, if it happens then just ignore it and output a space
        for j in range(6): # six rows of days
            for k in range(7): # seven days per row
                try:
                    if month1[j][k] != 0:
                        if str(month) in habit_records[habit_key] and month1[j][k] in habit_records[habit_key][str(month)]: 
                            print(f"[black on white]{month1[j][k]:^2}[/black on white]", end=" ")
                        else:
                            print(f"{month1[j][k]:^3}", end="")
                    else: 
                        print(f"{" ":^3}", end="")
                except:
                    print(f"{" ":^3}", end="")


            print(end="    ")

            for l in range(7): # month 2
                try:
                    if month2[j][l] != 0:
                        # highlight the specific date in this month if month is existing in the habit records and specific day is in a month in habit records
                        if str(month + 1) in habit_records[habit_key] and month2[j][l] in habit_records[habit_key][str(month + 1)]:
                            print(f"[black on white]{month2[j][l]:^3}[/black on white]", end="")
                        else:
                            print(f"{month2[j][l]:^3}", end="")
                    else:
                        print(f"{" ":^3}", end="")
                except:
                        print(f"{" ":^3}", end="")

            print(end="    ")

            for m in range(7): # month 3
                try:
                    if month3[j][m] != 0:
                        # highlight the specific date in this month if month is existing in the habit records and specific day is in a month in habit records
                        if str(month + 2) in habit_records[habit_key] and month3[j][m] in habit_records[habit_key][str(month + 2)]:
                            print(f"[black on white]{month3[j][m]:^3}[/black on white]", end="")
                        else:
                            print(f"{month3[j][m]:^3}", end="")
                    else:
                        print(f"{" ":^3}", end="")
                except Exception:
                        print(f"{" ":^3}", end="")

            print()


        month += 3
        print("\n\n")

    input("Press enter to continue")
    default_print("\033[2J]\033[3J]\033[H")

    return


def output_all_habit_streak():

    print("[bold red]█   █  ███  ████  ███ █████ ███  ███   ███[/bold red]")  
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█████ █████ ████   █    █    █  █     █████[/bold red]") 
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█   █ █   █ ████  ███   █   ███  ███  █   █[/bold red]\n")

    habit_records = fetch_all_habit_data()

    # check if there are habits to log
    if not habit_records:
        print("There are no habits to display...")
        input("Press \'enter\' to continue..")
        default_print("\033[2J]\033[3J]\033[H")
    
        return

    print(f"\n{"2026":^70}\n")


    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    days = {1: "Su", 2: "Mo", 3: "Tu", 4: "We", 5: "Th", 6: "Fr", 7: "Sa"}
    month = 1
    cal = calendar.Calendar(firstweekday=6)


    for habit_key in habit_records:
        print(f"\n\n[bold hot_pink]{habit_key:^70}[/bold hot_pink]")
        for i in range(4):
                # Output: Ex (Changes overtime, this is just an example format) --> January          February             March
                print(f"{months[month]:^20}{months[month + 1]:^30}{months[month+2]:^20}")
                # Output: Su Mo Tu We Th Fr Sa       Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
                for i in range(3):
                    print(f"{days[1]:^3}{days[2]:^3}{days[3]:^3}{days[4]:^3}{days[5]:^3}{days[6]:^3}{days[7]:^3}", end=f"{"":<4}")
        
                print()

                # month1, month2 and month3's values is a 2d array, each index is an array containing days in one row
                # [[0, 1, 2, 3], [4, 5, 6, 7]]
                month1 = cal.monthdayscalendar(2026, month)
                month2 = cal.monthdayscalendar(2026, month + 1)
                month3 = cal.monthdayscalendar(2026, month + 2)

                # errors are catched if index is out of bounds, if it happens just ignore it and output a space
                for j in range(6): # six rows of days
                    for k in range(7): # seven days in one row
                        try:
                            if month1[j][k] != 0:
                                # highlight the specific date in this month if month is existing in the habit records and specific day is in a month in habit records
                                if str(month) in habit_records[habit_key] and month1[j][k] in habit_records[habit_key][str(month)]:
                                    print(f"[black on white]{month1[j][k]:^2}[/black on white]", end=" ")
        
                                else:
                                    print(f"{month1[j][k]:^3}", end="")
                            else:
                                print(f"{" ":^3}", end="")
                        except:
                            print(f"{"":^3}", end="")
        
        
                    print(end="    ")
        
                    for l in range(7): # month 2
                        try:
                            if month2[j][l] != 0:
                                # highlight the specific date in this month if month is existing in the habit records and specific day is in a month in habit records
                                if str(month + 1) in habit_records[habit_key] and month2[j][l] in habit_records[habit_key][str(month + 1)]:
                                    print(f"[black on white]{month2[j][l]:^2}[/black on white]", end=" ")
                                else:
                                    print(f"{month2[j][l]:^3}", end="")
                            else:
                                print(f"{" ":^3}", end="")
                        except:
                                print(f"{" ":^3}", end="")
        
                    print(end="    ")
        
                    for m in range(7): # month 3
                        try:
                            if month3[j][m] != 0:
                                # highlight the specific date in this month if month is existing in the habit records and specific day is in a month in habit records
                                if str(month + 2) in habit_records[habit_key] and month3[j][m] in habit_records[habit_key][str(month + 2)]:
                                    print(f"[black on white]{month3[j][m]:^2}[/black on white]", end=" ")
                                else:
                                    print(f"{month3[j][m]:^3}", end="")
                            else:
                                print(f"{" ":^3}", end="")
                        except Exception:
                                print(f"{" ":^3}", end="")
        
                    print()
        
        
                month += 3
                print("\n\n")

        month = 1        
        
    input("Press enter to continue")
    default_print("\033[2J]\033[3J]\033[H")

# deletes lines in the terminal n number of times
def delete_lines(n):
    if n < 1: print("n should be greater than 0!") # TODO: Error handling
    else:
        for i in range(n):
            sys.stdout.write("\033[1A") # move cursor up
            sys.stdout.write("\x1b[2K") # delete line


def delete_habit(bright_colors):
    print("[bold red]█   █  ███  ████  ███ █████ ███  ███   ███[/bold red]")  
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█████ █████ ████   █    █    █  █     █████[/bold red]") 
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█   █ █   █ ████  ███   █   ███  ███  █   █[/bold red]\n")

    habit_records = fetch_all_habit_data()

    # check if there are habits to log
    if not habit_records:
        print("There are no habits to delete...")
        input("Press \'enter\' to continue..")
        default_print("\033[2J]\033[3J]\033[H")
        return

    print("Delete a habit.\n\n")

    key_habit_records_list = fetch_all_habit_keys()
    display_all_habits(bright_colors)

    # ask what habit to delete
    while True:
            try:
                decision_number = str(Prompt.ask(f"[light_cyan1 bold]Pick a habit to [bold red]delete[/bold red] from [0 - {len(key_habit_records_list) - 1}] [/light_cyan1 bold]"))
                if decision_number == 'x': 
                    default_print("\033[2J]\033[3J]\033[H")
                    return 
                else:
                    decision_number = int(decision_number)
    
                if decision_number < 0 or decision_number > len(key_habit_records_list) - 1:
                    raise ValueError(f"decision_number is not valid, it should range only from 0 - {len(key_habit_records_list) - 1}")
                else:
                    delete_lines(3 + len(key_habit_records_list))
                    break
            except:
                print(f"Input should be an [bold red]integer[/bold red] and [bold red]ranges from 0 to {len(key_habit_records_list) - 1}![/bold red]")
                time.sleep(2)
                delete_lines(2)


    # delete habit
    del habit_records[key_habit_records_list[decision_number]]

    with open("habit_data.json", "w") as file:
        json.dump(habit_records, file, indent=2)

    delete_lines(9)
    
# starting point of the program
def main_flow():

    # colors used to highlight text
    bright_colors = [
    "red1",
    "green1",
    "yellow1",
    "blue1",
    "magenta1",
    "cyan1",
    "orange1",
    "deep_pink1",
    "hot_pink",
    "chartreuse1",
    "spring_green1",
    "dodger_blue1",
    "purple",
    "gold1",
    "orchid1",
    "turquoise2",
    "sea_green1",
    "salmon1",
    "violet",
    "medium_orchid1",
    ]

    default_print("\033[2J]\033[3J]\033[H")
    while True:

        delete_lines(1)
        # display decision_numbers
        print("[bold red]█   █  ███  ████  ███ █████ ███  ███   ███[/bold red]")  
        print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
        print("[bold red]█████ █████ ████   █    █    █  █     █████[/bold red]") 
        print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
        print("[bold red]█   █ █   █ ████  ███   █   ███  ███  █   █[/bold red]") 

        print("\n\n[bold green][0][/bold green] [bold bright_white]Add a habit[/bold bright_white]")
        print("[bold yellow][1][/bold yellow] [bold bright_white]Log a habit[/bold bright_white]")
        print("[bold cyan][2][/bold cyan] [bold bright_white]See streak of a specific habit[/bold bright_white]")
        print("[bold magenta][3][/bold magenta] [bold bright_white]See all habit streak[/bold bright_white]")
        print("[bold yellow][4][/bold yellow] [bold bright_white]Delete a habit[/bold bright_white]\n")

        # ask what feature to use
        while True:
            try:
                decision_number = int(Prompt.ask("[light_cyan1 bold]What do you want to do? [0 - 4] [/light_cyan1 bold]"))
                if decision_number < 0 or decision_number > 4: # not a valid decision_number
                    raise ValueError("decision_number is not valid, it should range only from 1 - 4")
                else:
                    delete_lines(14)
                    break
            except:
                print("Input should be an [bold red]integer[/bold red] and [bold red]ranges from 0 to 4![/bold red]")
                time.sleep(2)
                delete_lines(2)

        if decision_number == 0:
            add_habit()
        elif decision_number == 1:
            log_habit(bright_colors)
        elif decision_number == 2:
            output_one_habit_streak(bright_colors)
        elif decision_number == 3:
            output_all_habit_streak()   
        elif  decision_number == 4:
            delete_habit(bright_colors)



main_flow()







