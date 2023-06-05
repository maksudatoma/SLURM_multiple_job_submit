# SLURM Multiple Job Submit

This repository shows some example scripts to submit multiple jobs in a Slurm cluster for different software. The current examples are suitable for running jobs on the `swan` cluster of the Holland Computing Center (HCC). <br /> 

## DREAM.3D
For DREAM3D there are multiple examples for submitting a `.json` file created by DREAM.3D. Python is very good for reading and modifying `.json` files. Most of the cases for modifying DREAM.3D pipeline the python code is lightweight enough to run directly on the login node. Some specifics commands are presented with a comment.

## Abaqus
Abaqus is a licenced well-known finite element solver. In order to run Abaqus on HCC, the administrators of HCC has to add you to the `Abaqus group`. Every request in the script is commented throughout.

## MATLAB
HCC offers different versions of MATLAB. The `-nodisplay` command tells the system to run MATLAB in non-GUI format. the `-r` tag is the command for running a matlab script from a terminal. 

## Paraview
A python script can be run so that everything that is done in the paraview GUI is recorded and can be automated. The code is generated in Python and the Slurm script just runs Python and executes the paraview script. 
