# This script is used to run a Jupyter notebook server inside apptainer.
# it set port 8888 and bind the current directory to the container.


module load apptainer
apptainer exec -H $PWD \
--bind "$PWD:/workspace" \
--nv --fakeroot helical/helical_container.sif /bin/bash $1
