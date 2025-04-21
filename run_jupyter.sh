# This script launches a Jupyter Notebook server inside an Apptainer container.
# It sets the server to run on port 8888 and binds the current directory to the container.

# Load the Apptainer module (required to use apptainer commands)
module load apptainer

# Run the Apptainer container using `exec` to execute a command inside it
apptainer exec \

  # Set the home directory inside the container to the current directory
  -H $PWD \

  # Bind the current working directory to /workspace inside the container
  --bind "$PWD:/workspace" \

  # Enable GPU access (if available) and allow the container to act as root
  --nv --fakeroot \

  # Specify the container image to use
  helical/helical_container.sif \

  # Start the Jupyter Notebook server inside the container
  .local/bin/jupyter notebook \
    --ip=0.0.0.0 \            # Allow access from any IP address
    --port=8888 \             # Set the port to 8888
    --no-browser \            # Do not open a browser automatically
    --allow-root              # Allow running Jupyter as root

