# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 21:53:16 2020

@author: Showmic
"""

import os
from collections import OrderedDict
import json
import math
import numpy as np
mean_dia=[25, 26, 27, 28, 29, 30, 31]
var_dia=9
#mu=math.log(mean_dia**2/math.sqrt(var_dia+mean_dia**2))
#sigma=math.sqrt(math.log(var_dia/(mean_dia**2)+1))
#print(mu)
#print(sigma)

def lognstat(mu, sigma):
    """Calculate the mean of and variance of the lognormal distribution given
    the mean (`mu`) and standard deviation (`sigma`), of the associated normal 
    distribution."""
    m = np.exp(mu + sigma**2 / 2.0)
    v = np.exp(2 * mu + sigma**2) * (np.exp(sigma**2) - 1)
    return m, v

#[M,V]= lognstat(mu,sigma);
#print(M,V)
with open('two_phase_Fe_25_Cu_75_150_cube_hcc.json', 'r+') as f:
    data = json.load(f)
    data=OrderedDict(data)
    #phase_frac=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    #print(len(phase_frac))
    for ii in range(len(mean_dia)):
        path=os.getcwd()
        path=path + '\mean_dia'+str(mean_dia[ii])
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
        mu=math.log(mean_dia[ii]**2/math.sqrt(var_dia+mean_dia[ii]**2))
        sigma=math.sqrt(math.log(var_dia/(mean_dia[ii]**2)+1))
        data['00']['StatsDataArray']['2']['FeatureSize Distribution']['Standard Deviation']=sigma
        data['00']['StatsDataArray']['2']['FeatureSize Distribution']['Average']=mu
        data['12']['OutputFile']='/mnt/phase_fraction_'+str(mean_dia[ii])+'.dream3d'
        test=open(path+'two_phase_mean'+ str(mean_dia[ii])+'.json','w')
        json.dump(data,test, indent =2)
        test.close()