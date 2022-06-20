#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for elem in range(0, x):
            print(my_list[elem], end="")
    except IndexError:
        count = 0
        for elem in my_list:
            count += 1
        return count
    else:
        return x
    finally:
        print(end="\n")
