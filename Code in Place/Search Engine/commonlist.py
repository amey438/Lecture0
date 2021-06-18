import os
import sys
import string

def common(list1, list2):  #MILESTONE 1
    """
    PRE: list1 and list 2 are a list
    POST: returns new_list
    This function is passed two lists and returns a new list containing
    those elements that appear in both of the lists passed in.
    """
    new_list = []
    list1_length = len(list1)
    list2_length = len(list2)
    for i in range (list1_length):
        for j in range (list2_length):
            if list1[i] == list2[j]:
                new_list_length = len(new_list)
                new_list.append(format(list1[i]))
                for x in range(new_list_length):
                    if new_list[x] == list1[i]:
                        new_list.pop()
    return new_list