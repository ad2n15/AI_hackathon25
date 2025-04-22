# AI Hackathon 25 Challenges

---

## Overview:
Each group should tackle one of the following three different challenges related to biology foundation models or LLMs. The challenges are designed to be solvable within a 2:30-hour time limit.

---

### General Notes for Participants:
1. **Time Limit:** You have 2 hours and 30 minutes to complete the challenge, including model development, training, and testing.
2. **Hardware Availability:**
   - **AMD CPUs:** All models are compatible with AMD CPUs, and participants are encouraged to use them as needed.
   - **A100 GPUs:** Available for more intensive tasks, but access may be impacted by long queues. Please be prepared to use CPUs if GPU access is delayed.
3. **Collaboration:** Each group will use a single account for development. All group members can collaborate on the design and discussions.
4. **No Internet Access:** Both AMD and A100 nodes do not have internet access, so ensure that all necessary datasets, dependencies, and libraries are preloaded onto the system.

---

## Challenge 1: Classifying Single Cells by Cell Type

### Objective:
Develop a machine learning approach to process scRNA-seq dataset and classify cells based on their cell type.

### Steps:
1. **Dataset:** Select a dataset from the cellxgene database or any other publicly available dataset related to single-cell gene expression.
2. **Model Selection:** Choose one of the pretrained Geneformer models.
3. **Approach:**
   - **Zero-shot Learning:** Use the model to classify cell types without training on specific labels.
   - **Fine-tuning:** Optionally, fine-tune the model on a subset of labeled data if performance needs improvement.
4. **Optimization:** Experiment with hyperparameter tuning (e.g., learning rate, batch size) and evaluate the model's performance based on metrics like accuracy and F1-score.

### Deliverables:
- A Python script or Jupyter notebook for model training, fine-tuning (if applicable), and evaluation.
- A summary of results showing classification accuracy for the selected cell types.

---

## Challenge 2: Classifying DNA Features

### Objective:
Develop an approach to classify DNA features like regulatory elements, splicing sites, or other genomic sequences.

### Steps:
1. **Dataset:** Use one of the InstaDeepAI datasets for DNA features or choose a publicly available genomic dataset.
2. **Model Selection:** Choose a HyenaDNA model or any other model designed for genomic sequence classification. HyenaDNA models are well-suited for DNA-related data.
3. **Approach:**
   - **Zero-shot Learning:** Use the model without fine-tuning, relying on pretrained knowledge.
   - **Fine-tuning:** Optionally fine-tune the model for better performance on your specific dataset.
4. **Optimization:** Adjust hyperparameters (e.g., learning rate, optimizer choice) and evaluate performance based on metrics like precision, recall, and accuracy.

### Deliverables:
- A Python script or Jupyter notebook for training and testing the model.
- A report with model performance and accuracy on the DNA feature classification task.

---

## Challenge 3: Extracting and Structuring Biological Information from Text

### Objective:
Develop a system to extract and structure biological or medical information from textual datasets, such as publications or abstracts.

### Steps:
1. **Dataset:** Use textual data from sources like PubMed articles, abstracts, or other bioinformatics-related text datasets.
2. **LLM Model Selection:** Download an appropriate Large Language Model (LLM) using ollama, to extract structured biological information from unstructured text.
3. **OntoGPT Schema:** Design an OntoGPT schema to guide the extraction of entities (e.g., genes, diseases, drugs) and their relationships (e.g., "causes," "treats," "affects"). Define output formats like RDF, OWL, or JSON for structured data.
4. **Optimization:** Use the OntoGPT schema to guide the extraction and structuring of information.

### Deliverables:
- A Python script or Jupyter notebook for extracting and structuring biological information.
- A structured output (e.g., RDF, OWL, JSON) containing extracted entities and relationships.

---

