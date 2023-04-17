#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import os
import pandas as pd
import numpy as np

def makefile_Profiles(folderpath, name, u, z):
#     Inputs:
#         folderpath: absolute path to folder where you want to place your file
#         name: name of .Profiles file
#         u: wind speed [array] or (list)
#         z: height [array] or (list)
#     Outputs:
#         None, it just makes a file at a specific folder for you

    line1 = '----------TurbSim v2.00.* Profile Input File-----------------------'
    line2 = 'Made up profiles'
    line3 = '-------- User-Defined Profiles (Used only with USR wind profile or USRVKM spectral model) ----------------'
    line4 = '{}	 NumUSRz	 - Number of Heights'.format(len(z))
    line5 = '1	StdScale1	- u-component scaling factor for the input standard deviation (USRVKM only)'
    line6 = '1	StdScale2	- v-component scaling factor for the input standard deviation (USRVKM only)'
    line7 = '1	StdScale3	- w-component scaling factor for the input standard deviation (USRVKM only)'
    line8 = '-----------------------------------------------------------------------------------'
    line9 = 'Height    Wind Speed       Wind Direction'
    line10 = '(m)        (m/s)       (deg, cntr-clockwise )'
    line11 = '------------------------------------------------------------------------------------------------------------------'

    filestart = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5 + '\n' + line6 + '\n' + line7 + '\n' + line8 + '\n' + line9 + '\n' + line10 + '\n' + line11 

    if os.path.exists(folderpath):
        print('Folder exists. New folder not created.')
    else:
        os.makedirs(folderpath)
        print('Folder not found. New folder created.')
        
    if not len(u) == len(z):
        raise ValueError('Length of arrays {} and {} are not equal.'.format(u, z))
    else:
        None

    df = pd.DataFrame(z)
    df.rename(columns = {df.columns[0]:'z'}, inplace = True)
    df['u'] = u
    df['winddir'] = 0

    filename = str(folderpath) + str('\\') + str('{}'.format(name)) + str('.Profiles')
    np.savetxt(filename, df.values, fmt = '%.2f', delimiter = '\t', header = filestart, comments = '')
    return print('Successfully created file {}.Profiles for TurbSim v2.00.'.format(name))

