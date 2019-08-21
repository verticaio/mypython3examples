#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import sys
def process_input(a, b, operation):
   if operation == "add":
       return a + b
   if operation == "subtract":
       return a - b
   if operation == "multiple":
       return a * b
   if operation == "divide":
       if b == 0:
           return "Invalid Input"
       return a / b
if __name__ == "__main__":
   print(process_input(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]))