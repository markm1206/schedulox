import random
import sys
import os
import json
from pprint import pprint
from decimal import Decimal

with open('spring2018.json') as f:#this one becomes a list
    data = json.load(f)

with open('utdCSS18.json') as f:#this one becomes a dict
    cs = json.load(f)


def find_Name_location(Name):
    i = 0
    while(i< len(data)):

        check = data[i]['prof']

        if Name == check:
            return i
        i+=1

    return -1



def find_Total(Name):
    if not(find_Name_location(Name) == -1) :

        Total = 0

        try:
            Total += int(data[find_Name_location(Name)]['grades']['A+'])
        except(KeyError, IndexError):
            pass
        try:
            Total += int(data[find_Name_location(Name)]['grades']['A'])
        except(KeyError, IndexError):
            pass
        try:
            Total += int(data[find_Name_location(Name)]['grades']['A-'])
        except(KeyError, IndexError):
            pass
        try:
            Total += int(data[find_Name_location(Name)]['grades']['B+'])
        except(KeyError, IndexError):
            pass
        try:
            Total += int(data[find_Name_location(Name)]['grades']['B'])
        except(KeyError, IndexError):
            pass
        try:
            Total += int(data[find_Name_location(Name)]['grades']['B-'])
        except(KeyError, IndexError):
            pass
        try:
            Total += int(data[find_Name_location(Name)]['grades']['C+'])
        except(KeyError, IndexError):
            pass
        try:
            Total += int(data[find_Name_location(Name)]['grades']['C'])
        except(KeyError, IndexError):
            pass
        try:
            Total += int(data[find_Name_location(Name)]['grades']['C-'])
        except(KeyError, IndexError):
            pass
        try:
            Total += int(data[find_Name_location(Name)]['grades']['D+'])
        except(KeyError, IndexError):
            pass
        try:
            Total += int(data[find_Name_location(Name)]['grades']['D'])
        except(KeyError, IndexError):
            pass
        try:
            Total += int(data[find_Name_location(Name)]['grades']['D-'])
        except(KeyError, IndexError):
            pass
        try:
            Total += int(data[find_Name_location(Name)]['grades']['F'])
        except(KeyError, IndexError):
            pass

        return Total

    else: print("name not found ")
    return -1




def get_GPA(Name):
    if not (find_Name_location(Name) == -1):

        GPA = 0

        try:
            GPA += ((int(data[find_Name_location(Name)]['grades']['A+']) * 4.0))
        except(KeyError, IndexError):
            pass
        try:
            GPA += (int(data[find_Name_location(Name)]['grades']['A']) * 4.0)
        except(KeyError, IndexError):
            pass
        try:
            GPA += (int(data[find_Name_location(Name)]['grades']['A-']) * 3.67)
        except(KeyError, IndexError):
            pass
        try:
            GPA += (int(data[find_Name_location(Name)]['grades']['B+']) * 3.33)
        except(KeyError, IndexError):
            pass
        try:
            GPA += (int(data[find_Name_location(Name)]['grades']['B']) * 3.0)
        except(KeyError, IndexError):
            pass
        try:
            GPA += (int(data[find_Name_location(Name)]['grades']['B-']) * 2.67)
        except(KeyError, IndexError):
            pass
        try:
            GPA += (int(data[find_Name_location(Name)]['grades']['C+']) * 2.33)
        except(KeyError, IndexError):
            pass
        try:
            GPA += (int(data[find_Name_location(Name)]['grades']['C']) * 2.0)
        except(KeyError, IndexError):
            pass
        try:
            GPA += (int(data[find_Name_location(Name)]['grades']['C-1']) * 1.67)
        except(KeyError, IndexError):
            pass
        try:
            GPA += (int(data[find_Name_location(Name)]['grades']['D+']) * 1.33)
        except(KeyError, IndexError):
            pass
        try:
            GPA += (int(data[find_Name_location(Name)]['grades']['D']) * 1.0)
        except(KeyError, IndexError):
            pass
        try:
            GPA += (int(data[find_Name_location(Name)]['grades']['D-']) * .67)
        except(KeyError, IndexError):
            pass
        try:
            GPA += (int(data[find_Name_location(Name)]['grades']['F']) * 0)
        except(KeyError, IndexError):
            pass

        return round( GPA / find_Total(Name), 2)

    else:
        print("name not found ")
    return -1



def find_name_by_class(subject, classNum):
    List_professor = []
    for count in range(0, 2705):
        temp = {}
        sub = (data[count]['subj'])
        num = (data[count]['num'])

        if (subject == sub) and (classNum == num) :
            temp = {data[count]['prof']:get_GPA(data[count]['prof'])}
            List_professor.append(temp)

    return List_professor


def Remove_duplicates(List_Of_Names):
    final_list = []
    for num in List_Of_Names:
        if num not in final_list:
            final_list.append(num)
    return final_list


# def swap(List_Of_Names, i, j):
#     temp = List_Of_Names[i]
#     List_Of_Names[i] = List_Of_Names[j]
#     List_Of_Names[j] = temp
#
#     return List_Of_Names
#
def Sort_List(List_Of_Names):
    Sorted_List = []
    item = float(str(List_Of_Names[0].values())[13:17])
    num =1
    while num < len(List_Of_Names):
        if item > float(str(List_Of_Names[num].values())[13:17]):
            #num+=1
            print("larger")
        else: item = float(str(List_Of_Names[num].values())[13:17])
    List_Of_Names.append(item)
    print( Sorted_List)


def insertionSort(my_list):
    # for every element in our array
    for index in range(1, len(my_list)):
        current = float(str(my_list[index].values())[13:17])
        position = index

        while position > 0 and float(str(my_list[index].values())[13:17]) > current:
            print("Swapped {} for {}".format(my_list[position], my_list[position-1]))
            my_list[position] = my_list[position-1]
            print(my_list)
            position -= 1

        my_list[position] = current

    return my_list
#
#
#     return List_Of_Names


           # > List_Of_Names[num].vlaues():
           #print(List_Of_Names[num2].values())
            #else: print("not >")

#print(Remove_duplicates(find_name_by_class("ACCT", "2302")))
print(Remove_duplicates(insertionSort(find_name_by_class("ACCT", "2302"))))

#print(Remove_duplicates(find_name_by_class("ACCT", "2302")))

#
# print(Remove_duplicates(find_name_by_class("ACCT", "2302")))
# print(find_name_by_class("ACCT", "2302"))
# find_name_by_class = Remove_duplicates(find_name_by_class("ACCT", "2302"))
# print(find_name_by_class)


#create a function to change the professor name
#use the coursebook catalog to sign up for classes
#use times part of the json file for the
#use days in order to insert the days
#use instructor_netid for the professor input in the file
#replace location with location
#replace description with section_address (make it capital though)


#print(find_name_by_class('ACCT'))
# for count in range (0,2706):
#     try:
#         print(data[count]['prof'])
#
#     except(KeyError, IndexError):
#             pass

# print(Professor_GPA)
# print(find_Total("Sun, Yan"))
