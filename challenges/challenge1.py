#!/usr/bin/python

import sys

var1 = "Pfizer"
var2 = "Girls Who Code"
output = ""

for letter in var1:
    output += letter
    output += " "
    output += var2
    output += " "

x = len(var1)
y = len(var2)

key1 = x*y
key2 = len(output)
