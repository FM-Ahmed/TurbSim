#!/usr/bin/env python
# coding: utf-8

# In[ ]:


raise NameError('Dont run this cell unless you want to make TurbSim .profiles input files ')

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

folderpath = r'C:\Users\fahim\OneDrive\Desktop\OpenFAST_v3.4.1\IEA-15-240-RWT-master\OpenFAST\IEA-15-240-RWT\Wind\Profiles_extra'

if os.path.exists(folderpath):
    print('Folder \'Profiles\' exists. New folder not created.')
else:
    os.makedirs(folderpath)
    print('Folder not found. New folder \'Profiles\' created.')

for i in range(len(windA)):
    df = pd.DataFrame(z)
    df.rename(columns = {df.columns[0]:'z'}, inplace = True)
    df['u'] = windA[i]
    df['winddir'] = 0
    
    filename = str(folderpath) + str('\\') + str('LLJ_{}'.format(i)) + str('.Profiles')
    np.savetxt(filename, df.values, fmt = '%.2f', delimiter = '\t', header = filestart, comments = '')

