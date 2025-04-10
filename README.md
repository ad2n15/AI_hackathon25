# 🧠 AI Hackathon 2025

Welcome to the **AI Hackathon 2025**! This project focuses on fine-tuning and prompt engineering using state-of-the-art models in a containerized environment.

---

## 🚀 Setup Instructions

### 1. Prepare the Container Environment

You can either:
- **Build the container yourself**, or
- **Request access** to a pre-built `.sif` container from the hackathon organizers.

To build the container:

```bash
cd helical
./build_helical_container.sh
```

### 2. Install Required Dependencies

Once the container is ready, install the necessary Python packages:

```bash
cd ../
./install_and_download_dependencies.sh
```

---

## 📓 Running Jupyter Notebooks

1. **Login to Open OnDemand** (University of Southampton):
   - Open [https://iridisondemand.soton.ac.uk/pun/sys/dashboard](https://iridisondemand.soton.ac.uk/pun/sys/dashboard) in your browser.
2. **Launch a Desktop session**:
   - Select **Desktop**, adjust the number of hours and cores (we recommend **32 cores**), and launch the session.
3. **Open a terminal emulator** inside the desktop.
4. **Navigate to the project folder and start Jupyter**:

```bash
cd AI_hackathon25
./run_jupyter.py
```

5. **Copy the Jupyter URL** from the terminal and open it in your browser.
6. Open an existing notebook or create a new one to start coding.

---

## 🧪 Enabling Command-Line Tools in Jupyter

To access command-line tools like `ontogpt` inside Jupyter notebooks, run this command in the first cell (if you're in the `notebooks/` directory):

```python
%env PATH=../.local/bin:$PATH
```

---

## 🤖 Using OntoGPT with Ollama (Local LLM Inference)

To run OntoGPT with a locally hosted Ollama model:

1. Open a **new terminal**.
2. Navigate to the project directory:

```bash
cd AI_hackathon25
```

3. Load the Ollama module and start the server:

```bash
module load ollama
ollama serve
```

4. (Optional) Download a model (e.g., `gemma:7b`):

```bash
ollama pull gemma:7b
```

### Example Usage from a Notebook:

```python
!ontogpt complete -m ollama/gemma:7b "Why did the squid cross the coral reef?"
```

---

## ✅ Project Status & Next Steps

- [x] Ahmed: Integrate OntoGPT
- [x] Ahmed: Download LLaMA model
- [ ] Alex: Test notebooks
- [ ] Ahmed & Alex: Prepare 30-minute presentation
- [ ] Ahmed & Alex: Define competition & marking criteria