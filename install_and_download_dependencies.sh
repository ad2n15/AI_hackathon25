# This script is used to install dependencies and download data for the Helical project.
# It uses Apptainer to create a containerized environment for the installation process.
# The script installs the required packages and downloads the necessary data files.
# The script is designed to be run on a system with the Helical project directory mounted at /iridisfs/ddnb/Ahmed/AI_hackathon25.
# The script uses the Apptainer container located at /iridisfs/ddnb/Ahmed/AI_hackathon25/helical/helical_container.sif.
# The script also sets the permissions for the Jupyter runtime directory to ensure that the user has the necessary access rights.
# The script is designed to be run in the directory where the Helical project is located.
# The script uses the --nv and --fakeroot options to enable GPU support and allow for root access within the container.
# The script uses the --bind option to bind the Helical project directory to the container, allowing for access to the data files and directories within the project.
# The script installs the required packages using pip, including jupyter and ontogpt.
# The script also installs the ontogpt package with additional dependencies for documentation and web support.
# The script downloads the necessary data files using the ci/download_all.py script provided in the Helical project.
# The script is designed to be run in a bash shell and uses the apptainer command to execute the installation process within the container.
# Load the Apptainer module

module load apptainer

# install jupyter
apptainer exec -H $PWD \
--bind /iridisfs/ddnb/Ahmed/AI_hackathon25:/iridisfs/ddnb/Ahmed/AI_hackathon25 \
--nv --fakeroot /iridisfs/ddnb/Ahmed/AI_hackathon25/helical/helical_container.sif \
pip install jupyter

# modify permissions for jupyter runtime directory
# This is necessary to avoid permission issues when running Jupyter notebooks
# in the containerized environment.
chmod -R 700 .local/share/jupyter/runtime/

##############################

# install ontogpt and its dependencies
apptainer exec -H $PWD \
--bind /iridisfs/ddnb/Ahmed/AI_hackathon25:/iridisfs/ddnb/Ahmed/AI_hackathon25 \
--nv --fakeroot /iridisfs/ddnb/Ahmed/AI_hackathon25/helical/helical_container.sif \
pip install ontogpt ontogpt[docs] ontogpt[recipes] ontogpt[web]



############################

# download all data files
# This script is used to download all the necessary data files for the Helical project.
apptainer exec -H $PWD \
--bind /iridisfs/ddnb/Ahmed/AI_hackathon25:/iridisfs/ddnb/Ahmed/AI_hackathon25 \
--nv --fakeroot /iridisfs/ddnb/Ahmed/AI_hackathon25/helical/helical_container.sif \
python3 ci/download_all.py
