# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:39:23 2021

@author: Gabo
"""
file = open("devices.txt", "a")
while True:
    newItem = input("Ingrese Un Nuevo Item: ")
    if newItem == "exit":
        print("ALL DONE!!")
        break
    else:
        file.write(newItem + "\n")
file.close()