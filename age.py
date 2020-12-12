#!/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
# This program uses a compound boolean statement


def main():

    # input
    age = print("Enter your age  ")
    age_string = input("Enter Here plz : ")
    # process & output
    try:
        age = int(age_string)
        if age >= 25 and age <= 40:
            print("You can date.")
        else:
            print("You  can't date .")

    except Exception:
        print("This was an invalid number ")


if __name__ == "__main__":
    main()
