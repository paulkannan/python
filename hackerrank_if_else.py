#!/bin/python3

import math
import os
import random
import re
import sys

is_between = 6 <=20

if __name__ == '__main__':
    n = int(input().strip())
    
    if (n>0 & n<=100):
        if (n % 2 == 0 and n>20):
            print("Not Weird")
        elif (n % 2 == 0 and n>5) and (n<=20):
            print("Weird")
        elif(n % 2 == 0 and n>1) and (n <=5):
            print("Not Weird")
        elif(n%2 !=0):
            print("Weird")
    else:
        print("pls enter > 100")
