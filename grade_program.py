# !/user/bin/env.python3
# Created By: Daniel Momoh
# Date: Nov. 24, 2022
# This program asks the user for a grade level,
# then returns the middle percentage.


# this function uses a 'switch case' to
# determine middle percentage of a grade level
def calc_mark(level):
    levels = {
        "4+": "Level {} has a middle percentage of 98%".format(level),
        "4": "Level {} has a middle percentage of 91%".format(level),
        "4-": "Level {} has a middle percentage of 83%".format(level),
        "3+": "Level {} has a middle percentage of 78%".format(level),
        "3": "Level {} has a middle percentage of 75%".format(level),
        "3-": "Level {} has a middle percentage of 71%".format(level),
        "2+": "Level {} has a middle percentage of 68%".format(level),
        "2": "Level {} has a middle percentage of 65%".format(level),
        "2-": "Level {} has a middle percentage of 61%".format(level),
        "1+": "Level {} has a middle percentage of 58%".format(level),
        "1": "Level {} has a middle percentage of 55%".format(level),
        "1-": "Level {} has a middle percentage of 51%".format(level),
        "R": "Level {} has a middle percentage of 25%".format(level),
    }
    return levels.get(level, -1)


# this function gets input from the user
# and calls the next function
def main():

    # gets input from the user
    level_user = input("Enter the level you want converted to a percentage: ")
    print("")

    # assigns variable to function call that gives return value
    percent = calc_mark(level_user)

    # displays results to user
    if calc_mark(level_user) == -1:
        print("Invalid input!")
    else:
        print(percent)


if __name__ == "__main__":
    main()
