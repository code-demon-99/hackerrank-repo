#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    result =  meal_cost + (tip_percent/100)*meal_cost +(tax_percent/100)*meal_cost
    print(int(round(result)))
    return result

if __name__ == '__main__':
    # base cost of meal
    meal_cost = float(input().strip())  

    # (the percentage of the meal price being added as tip)
    tip_percent = int(input().strip()) 

    # (the percentage of the meal price being added as tax)
    tax_percent = int(input().strip()) 

    solve(meal_cost, tip_percent, tax_percent)
