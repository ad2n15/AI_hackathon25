




module load apptainer

""""
apptainer exec -H $PWD \
--bind /iridisfs/ddnb/Ahmed/AI_hackathon25:/iridisfs/ddnb/Ahmed/AI_hackathon25 \
--nv --fakeroot /iridisfs/ddnb/Ahmed/AI_hackathon25/helical/helical_container.sif \
pip install jupyter

chmod -R 700 .local/share/jupyter/runtime/
""""

apptainer exec -H $PWD \
--bind /iridisfs/ddnb/Ahmed/AI_hackathon25:/iridisfs/ddnb/Ahmed/AI_hackathon25 \
--nv --fakeroot /iridisfs/ddnb/Ahmed/AI_hackathon25/helical/helical_container.sif \
python3 ci/download_all.py
