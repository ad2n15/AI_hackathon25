#If you don't have root access, you can first build a sandbox directory and then convert it into a .sif file



module load apptainer





#apptainer build --sandbox helical_container/ helical_singularity.def
#apptainer build helical_container.sif helical_container/
#rm -rf helical_container/

cd ../


module load apptainer
apptainer exec -H $PWD \
--bind /iridisfs/ddnb/Ahmed/AI_hackathon25:/iridisfs/ddnb/Ahmed/AI_hackathon25 \
--nv --fakeroot /iridisfs/ddnb/Ahmed/AI_hackathon25/helical/helical_container.sif pip install jupyter
