# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:25:40 2017

@author: py15asm
"""

import os, os.path
import glob
import numpy as np
from os import listdir
import numpy as np
import matplotlib.pyplot as plt
import pylab
import matplotlib.pyplot as plt
import datetime
import csv

paths=[]
path=[]
counter=0

#folder where the data will be exported
folder='C:\Users\py15asm\Desktop\Playing_with_python'
#folder where the code will scan
day_folder='W:\\Formatted Correctly'

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]
            


for name in glob.glob(day_folder+'/*'): 
    if os.path.isdir(name):
        paths.append(name)
    else:
        continue

paths.sort()    


#if there are folders corresponding to something that it is not a day, they will appear at the end. The next command removes the last folder, in the initial case, the folder "Don't use"
counter=0
header=''
paths=paths[:-1]
number_days=len(paths)
for i in range(0,number_days):
    path=paths[i]
    excels = find_csv_filenames(path)
    number_excels=len(excels)
    
    if number_excels==0:
        print('no excels on the '+str(path[-6:]))
        continue
    daily_reading=0
    
    excels.sort()
    
    for j in range(0,number_excels):
        if excels[j][0:19].find('Blan')==-1:
            name=excels[j]
            counter=counter+1
            print counter
            header=header+str(name)+', ,'
            
       
number=counter
counter=0

data=np.ones((100,2*number))*9999  


for i in range(0,number_days):
    path=paths[i]
    excels = find_csv_filenames(path)
    number_excels=len(excels)
    
    if number_excels==0:
        print('no excels on the '+str(path[-6:]))
        continue
    daily_reading=0
    
    excels.sort()
    
    for j in range(0,number_excels):
        if excels[j][0:19].find('Blan')==-1:
            name=excels[j]
            
            
            importing=np.genfromtxt(path+'\\'+excels[j],delimiter=',',skip_header=1,dtype=np.float64,usecols=(0,1,2))
            
            
            data[0:len(importing),counter]=importing[:,0]
            data[0:len(importing),counter+1]=importing[:,1]
            
            counter=counter+2
            
#
        
np.savetxt(folder+'\\Data '+'.csv',data,header=header,delimiter=',')       