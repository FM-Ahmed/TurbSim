# TurbSim v2.00

## Content of repository

### read_dotprofiles.py

Function that returns wind speed array (u) and corresponding height array (z) from .Profiles input file for TurbSim v2.00 (for OpenFAST v3.4.1).

### makefile_Profiles.py

To use a user-defined wind profile as input in TurbSim this filetype and structure is needed. This function creates this file (with extension .Profiles) at a specific folder with a specific name. For TurbSim v2.00, may or may not work for other versions (last updated April 2023). For use for simple wind profiles with no veer and direct wind inflow at turbine (0 deg wind direction). 
