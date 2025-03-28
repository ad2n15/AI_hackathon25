#If you don't have root access, you can first build a sandbox directory and then convert it into a .sif file



module load apptainer





apptainer build --sandbox helical_container/ helical_singularity.def
apptainer build helical_container.sif helical_container/
rm -rf helical_container/
