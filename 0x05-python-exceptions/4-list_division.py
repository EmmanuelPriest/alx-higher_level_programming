#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    try:
        list_length = [x / y for x, y in zip(len(my_list_1), len(my_list_2))]
    except ValueError:
        list_length = 0
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        return list_length
