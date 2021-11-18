#!/bin/python3
import sys

def prepMyFruit():
    fruit = "Strawberry"
    quantity = 420
    pie_crust = "filled with delicious strawberry"
    print(f"You  put {quantity} {fruit} on the crust")
    return pie_crust

def main():
    pie_crust = prepMyFruit()
    print(f"my pie is {pie_crust}")
    return

main()