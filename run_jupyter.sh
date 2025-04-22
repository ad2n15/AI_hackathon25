# This script is used to run a Jupyter notebook server inside apptainer.
# it set port 8888 and bind the current directory to the container.


module load apptainer

apptainer exec -H $PWD \
--bind "$PWD:/workspace" \
--nv --fakeroot helical/helical_container.sif \
.local/bin/jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

