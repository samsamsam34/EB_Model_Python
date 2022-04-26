# -*- coding: utf-8 -*-
"""Shortwave.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d2gzef-3EFKF_j26qAkaYRy3hiEY-cIF
"""

/content/CENMET_INPUT_data.csv

import pandas as pd
import numpy as np

url= 'https://github.com/LiamCFenn/EB_Models/blob/758d9443d7aff14df6aa5a1db57387078188b135/matlabEB_lab/CENMET_INPUT_data.csv?raw=true'
inMet= pd.read_csv(url, index_col=0)

inMet

##This calculates the shortwave radiation

# SWin is the measured shortwave radiation 
# Look in energy_balance.m to see how it is read in.

def shortwave (inMet):
  ALBvis = np.empty(len(inMet.index))
  ALBnir = np.empty(len(inMet.index))
  for i in range(1,len(inMet["T_C"])):
      if inMet.iloc[i][" SWEmm"] == 0:
          ALBvis[i] = 0.2   
      else:
          ALBvis[i] = 0.9
 
  for i in range(1,len(inMet["T_C"])):
      if inMet.iloc[i][" SWEmm"] == 0: 
          ALBnir[i] = 0.2
        
      else:
          ALBnir[i] = 0.9

# This assumes that the incoming shortwave radiation will be evenly split between the visable and NIR.
# We need to split the incoming

# Preallocate space

  SWvisI = np.empty(len(inMet.index)) # Preallocate space for incoming SW visible
  SWvisO = np.empty(len(inMet.index)) # Preallocate space for outgoing SW visible
  SWnirI = np.empty(len(inMet.index)) # Preallocate space for incoming SW NIR
  SWnirO = np.empty(len(inMet.index)) # Preallocate space for outgoing SW NIR

# calculate the visible Shortwave
  for i in range(1,len(inMet["T_C"])):
      SWvisI[i] = inMet.iloc[i][" inSR"] * 0.5
    

# calculate the nir SW
  for i in range(1,len(inMet["T_C"])):
      SWnirI[i] = inMet.iloc[i][" inSR"] * 0.5
    

# calculate the outgoing visible SW
# 0.9 is the albedo of snow in the visible

  for i in range(1,len(inMet["T_C"])):
      SWvisO[i] = SWvisI[i] * 0.9
    

# calculate the outgoing nir SW
# 0.7 is the albedo of snow in the nir
  for i in range(1,len(inMet["T_C"])):
      SWnirO[i] = SWnirI[i] * 0.7
    

# Compute the net shortwave radiation flux

# Qsw = (SWvisI - SWvisO) + (SWnirI - SWnirO)
  Qsw= np.empty(len(inMet.index))

  for i in range(1,len(inMet["T_C"])):
    
      Qsw[i] = (SWvisI[i] - SWvisO[i]) + (SWnirI[i] - SWnirO[i])
  inMet['Qsw'] = Qsw.tolist() #Add to array
  return inMet

list(inMet.columns)