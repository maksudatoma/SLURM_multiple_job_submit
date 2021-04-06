# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:56:38 2020

@author: Showmic
"""

import os
#print(os.listdir(os.getcwd()))
path = os.getcwd()

folders = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for folder in d:
        folders.append(os.path.join(r, folder))
        direc=os.path.join(r, folder)
        print(direc)
        print(os.walk(direc))
        for root_name, folder_name, file_name in os.walk(direc):
            for ii in file_name:
                if '.json' in ii:
                    print('inside')
                    submit_file=open(direc+'/test_submit.sh','w')
                    submit_file.write('#!/bin/sh\n') 
                    submit_file.write('#SBATCH --array=1-10\n')
                    submit_file.write('#SBATCH --nodes=1\n')
                    submit_file.write('#SBATCH --time=6:00:00\n')
                    submit_file.write('#SBATCH --mem=20G\n')
                    submit_file.write('#SBATCH -o slurm-%A_%a.out --array=1-10\n\n')
                    submit_file.write('module load singularity\n')
                    submit_file.write('mkdir $SLURM_ARRAY_TASK_ID\n')
                    submit_file.write('cd $SLURM_ARRAY_TASK_ID\n')
                    submit_file.write('singularity exec -B ' +path+'/$SLURM_ARRAY_TASK_ID:/mnt docker://unlhcc/dream3d PipelineRunner -p ' + path+'/'+folder+'/'+ii)
                    submit_file.close()
for f in folders:
    print(f)
    