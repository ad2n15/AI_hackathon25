which jupyter
find / -name "jupyter" 2>/dev/null
/tmp/rootfs-565854257/root/usr/local/bin/jupyter
/tmp/rootfs-565854257/root/usr/local/bin/jupyteR
/tmp/rootfs-565854257/root/usr/local/bin/jupyter
./tmp/rootfs-565854257/root/usr/local/bin/jupyter
ls /tmp/
ls -ltr /tmp/
find / -name "jupyter" 2>/dev/null
exit
runoa
runoaK
runoak
exit
ontogpt 
ontogpt
pip show ontogpt
python
pip install ontogpt[docs]
pip install ontogpt[recipes]
pip install ontogpt[web]
runoak
python
exit() exit
exit
python3
runoak 
which runoak
find / -name runoak 2>/dev/null
/iridisfs/ddnb/Ahmed/AI_hackathon25/.local/bin/runoak
.local/bin/runoak
.local/bin/runoak set-apikey -e openai <your openai api key>
.local/bin/runoak set-apikey -e openai "your openai api key"
ontogpt --help
find / -name ontogpt 2>/dev/null
export PATH=$PATH:.local/bin
ontogpt 
runoak
import os
# Prepend ../.local/bin to the current PATH
os.environ["PATH"] = os.path.join("../.local/bin") + ":" + os.environ.get("PATH", "")
export PATH="../.local/bin:$PATH"
ontogpt complete --help
import os
# Prepend ../.local/bin to the current PATH
os.environ["PATH"] = os.path.join(".local/bin") + ":" + os.environ.get("PATH", "")
export PATH=".local/bin:$PATH"
ontogpt complete --help
ontogpt list-templates
#!/bin/bash
# Get all template names (first column of output)
templates=$(ontogpt list-templates | awk 'NR>1 {print $1}')
# Loop over each template and extract example output
for template in $templates; do     echo "Fetching template: $template";     ontogpt extract -t "$template" -i ~/path/to/abstract.txt > "${template}.json"; done
ls -ltr
exit
