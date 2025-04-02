module load apptainer
apptainer exec -H $PWD \
--bind /iridisfs/ddnb/Ahmed/AI_hackathon25:/iridisfs/ddnb/Ahmed/AI_hackathon25 \
--nv --fakeroot /iridisfs/ddnb/Ahmed/AI_hackathon25/helical/helical_container.sif \
/iridisfs/ddnb/Ahmed/AI_hackathon25/.local/bin/jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
