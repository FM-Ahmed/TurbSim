#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
import pandas as pd

def read_dotprofiles(path_to_profile):
#     Inputs:
#         path_to_profile: absolute path to .Profiles file
#     Outputs:
#         umean: mean wind velocity in x-direction [array]
#         zh: corresponding heights [array]
   
    windprof = open(path_to_profile)
    data_windprof = pd.read_csv(windprof, header = 11, sep='\s+', lineterminator = '\n', dtype = str)
    df_windprof = pd.DataFrame(data_windprof)
    df_windprof.loc[-1] = [df_windprof.columns[0], df_windprof.columns[1], df_windprof.columns[2]]
    df_windprof.index = df_windprof.index + 1
    df_windprof = df_windprof.sort_index()
    df_windprof.rename(columns = {df_windprof.columns[0]:'Ht', df_windprof.columns[1]:'Ux', df_windprof.columns[2]:'Dir'}, inplace = True)
    umean = np.array(df_windprof['Ux'].astype(float))
    zh = np.array(df_windprof['Ht'].astype(float))
    windprof.close()
    return umean, zh
