conda create -n myenv
conda config --add channels conda-forge
conda config --set channel_priority strict
conda create -n pythontest python=3.8
conda activate pythontest
conda activate myenv
/opt/conda/bin/activate
conda update conda
conda install getfem
/opt/conda/bin/python
