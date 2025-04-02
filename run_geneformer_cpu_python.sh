module load apptainer
apptainer exec -H $PWD \
--bind /iridisfs/ddnb/Ahmed/AI_hackathon25:/iridisfs/ddnb/Ahmed/AI_hackathon25 \
--nv --fakeroot /iridisfs/ddnb/Ahmed/AI_hackathon25/helical/helical_container.sif \
python3 $1
