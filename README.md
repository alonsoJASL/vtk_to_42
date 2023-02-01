# vtk_to_42
Convert VTK legacy files version 5.1 to 4.2

Simple python script to convert vtk legacy ascii files from 
5.1 to 4.2. 

To use directly on your computer, you can set up a conda environment: 
```sh
conda create -n vtk910 python=3.8 -y
conda install -c conda-forge vtk==9.1.0 -n vtk910 -y 
conda clean -afy
```

Alternatively, you can use the docker container, which is easily accessible by the `run.sh` script.
A useful way to install this in your machine would be to soft link it to your `/usr/local/bin` 
folder.

+ Open a terminal
+ Navigate to the folder you saved this project on: `cd /path/to/this/project`
+ Give running permissions to the script `chmod +x run.sh`
+ Create link `sudo ln -s $(pwd)/run.sh /usr/local/bin/convert_vtk_42`

You will then be able to use the docker container without the need to setup the conda environment.
