# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:14:32 2020

@author: Showmic
"""

import os
path = os.getcwd()

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for folder in d:
        direc=os.path.join(r, folder)
        print(direc)
        for root_name, folder_name, file_name in os.walk(direc):
            for ii in file_name:
                if '.sh' in ii:
                    os.chdir(direc)
                    os.system('sbatch '+direc+'/'+ii)