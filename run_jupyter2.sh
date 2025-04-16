# This script is used to run a Jupyter notebook server inside apptainer.
# it set port 8888 and bind the current directory to the container.


module load apptainer
apptainer exec -H $PWD \
--bind AI_hackathon25:AI_hackathon25 \
--nv --fakeroot helical/helical_container.sif \
/iridisfs/ddnb/Ahmed/AI_hackathon25/.local/bin/jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
