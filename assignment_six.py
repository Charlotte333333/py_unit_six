#Charlotte Moore
#January 13
#generate birthday lists and see how often they have a duplicate

import random
def introduction():
    """
    This functioion intoduces the code and its purpose to the user
    """
    print("hey user. This code is to track how many birthdays are duplicated out of a list")
    stuff = input("how many times do you want to run?")
    return stuff



def get_birthday():
    """
    This function generates a list of 23 random numbers ranging from 1-365, representing every day in a year. And it generates as many lists as the user requests

    """
    birthdays = []
    o=23
    for x in range(o):
        birthdays.append(random.randint(1, 365))

    return birthdays

def is_duplicates(list):
    """
    This function calculates the number of duplicates in each list
    :param list: the random list made in get_birthdays function
    :return:
    """

    p = 0
    for element in list:
        p = p +1
        for days in list[p:-1]:
            if element == days:
                return True





def main():

    slay = int(introduction())
    counter = 0
    for x in range(slay):
        list = get_birthday()
        if is_duplicates(list) == True:
            counter +=1
    print("There are", counter,"duplicates in", slay,"lists")
    percentage = counter/slay
    c = percentage*100
    h = round(c, 2)
    print(h,"%")




main()













































