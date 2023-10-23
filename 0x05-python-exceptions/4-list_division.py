#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    i = 0
    while i < list_length:
        try:
            a = 0
            a = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            i += 1
            newlist.append(a)
    return newlist
