import random
import os
import json

start = True
while start:
    print("Welcome to Our-People Bank Plc Banking System \n")
    print("1 Staff Login")
    print("2 Close App")
    start_option = input("Please enter your selection [1/2]: ")
    while start_option not in ["1", "2"]:
        start_option = input("kindly enter a valid selection [1 or 2]: ")
    