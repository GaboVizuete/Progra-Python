# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:28:16 2021

@author: Jorge
"""

lista1=['R1','R2','R3','S1','S2','S3']
switches=[]
routers=[]
for i in lista1:
   if 'S' in i:
        switches.append(i)  
        print(i)
   if 'R' in i:
        routers.append(i)
        print(i)