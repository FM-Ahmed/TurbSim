#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

path1 = r'C:\Users\fahim\OneDrive\Desktop\OpenFAST_v3.4.1\IEA-15-240-RWT-master\OpenFAST\IEA-15-240-RWT\Wind\Profiles_below'
path2 = r'C:\Users\fahim\OneDrive\Desktop\OpenFAST_v3.4.1\IEA-15-240-RWT-master\OpenFAST\IEA-15-240-RWT\Wind\Profiles_rated'
path3 = r'C:\Users\fahim\OneDrive\Desktop\OpenFAST_v3.4.1\IEA-15-240-RWT-master\OpenFAST\IEA-15-240-RWT\Wind\Profiles_above'

paths = [path1, path2, path3]

below_path = os.listdir(path1)
rated_path = os.listdir(path2)
above_path = os.listdir(path3)

p_ = [below_path, rated_path, above_path]

def get_dotprofiles(path_to_profile):
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

labels = ['Below rated (6.8 ms$^{-1}$)', 'Rated (10.59 ms$^{-1}$)', 'Above rated (17.8 ms$^{-1}$)']

fig, ax = plt.subplots(1, 3, figsize = (10, 5))
for i in range(len(paths)):
    for file in p_[i]:
        count = 0
        colors = ['k', 'r', 'b']
        filepath = str(paths[i]) + str('\\') + str(file)
        u, z = get_dotprofiles(filepath)
        ax[i].plot(u, z, color = colors[i], linewidth = 0.8)
        ax[i].set_xlabel('u [ms$^{-1}$]')
        ax[i].set_title(labels[i])
        ax[i].grid(True, 'both')
        # ax[i].axhline(y = 270, linestyle = '--', color = 'black', label = 'Rotor swept area')
        # ax[i].axhline(y = 30, linestyle = '--', color = 'black')
        
ax[0].set_ylabel('z [m]');

# fig_destination = r'C:\Users\fahim\OneDrive\Desktop\windprofiles.eps'
# plt.savefig(fig_destination, format = 'eps', bbox_inches = 'tight')


# In[ ]:


get_dotprofiles

