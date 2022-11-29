# !/user/bin/env.python3
# Created By: Daniel Momoh
# Date: Nov. 24, 2022
# This program asks the user for a grade level,
# then returns the middle percentage.


# this function uses a 'switch case' to
# determine middle percentage of a grade level
def calc_mark(level):
    levels = {
        "4+": "Level {} has a middle percentage of  95% - 100%".format(level),
        "4": "Level {} has a middle percentage of 87% - 94%".format(level),
        "4-": "Level {} has a middle percentage of 80% - 86%".format(level),
        "3+": "Level {} has a middle percentage of 77% - 79%".format(level),
        "3": "Level {} has a middle percentage of 73% - 76%".format(level),
        "3-": "Level {} has a middle percentage of 70% - 72%".format(level),
        "2+": "Level {} has a middle percentage of 67% - 69%".format(level),
        "2": "Level {} has a middle percentage of 63% - 66%".format(level),
        "2-": "Level {} has a middle percentage of 60% - 62%".format(level),
        "1+": "Level {} has a middle percentage of 57% - 59%".format(level),
        "1": "Level {} has a middle percentage of 53% - 56%".format(level),
        "1-": "Level {} has a middle percentage of 50% - 52%".format(level),
        "R": "Level {} has a middle percentage of Below 50%".format(level),

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
