#!/bin/python3
import sys

def prepMyFruit():
    fruit = "Strawberry"
    quantity = 420
    pie_crust = "filled with delicious strawberry"
    is_oven_on = False
    print(f"You  put {quantity} {fruit} on the crust")

    return is_oven_on, pie_crust

def turn_on_oven(is_oven_on):
    is_oven_on = turn_on_oven(is_oven_on)
    if is_oven_on == False:
        is_oven_on == True
    print(f"Is the hoven turned on ?", is_oven_on)
    return is_oven_on

def main():
    pie_crust = prepMyFruit()
    print(f"my pie is {pie_crust}")
    return


main()