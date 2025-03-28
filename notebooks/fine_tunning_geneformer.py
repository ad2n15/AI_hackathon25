from helical.models.geneformer import GeneformerConfig, GeneformerFineTuningModel
import anndata as ad

# Load the data
print("Loading data...")
ann_data = ad.read_h5ad("../data/yalk_sac_data.h5ad")
print("Data loaded successfully.")

# Get the column for fine-tuning
print("Extracting cell types...")
cell_types = list(ann_data.obs["LVL1"][:10])
label_set = set(cell_types)
print(f"Extracted cell types: {cell_types}")
print(f"Unique labels: {label_set}")

# Create a GeneformerConfig object
print("Creating GeneformerConfig...")
geneformer_config = GeneformerConfig(model_name="gf-12L-95M-i4096", batch_size=10)
print("GeneformerConfig created.")

# Create a GeneformerFineTuningModel object
print("Creating GeneformerFineTuningModel...")
geneformer_fine_tune = GeneformerFineTuningModel(geneformer_config=geneformer_config, fine_tuning_head="classification", output_size=len(label_set))
print("GeneformerFineTuningModel created.")

# Process the data
print("Processing data...")
dataset = geneformer_fine_tune.process_data(ann_data[:10])
print(f"Processed dataset length: {len(dataset)}")
print(f"Cell types length: {len(cell_types)}")

# Add column to the dataset
print("Adding cell_types column to the dataset...")
dataset = dataset.add_column('cell_types', cell_types)
print("Column added successfully.")

# Create a dictionary to map cell types to ids
print("Creating class_id_dict...")
class_id_dict = dict(zip(label_set, [i for i in range(len(label_set))]))
print(f"Class ID dictionary: {class_id_dict}")

def classes_to_ids(example):
    example["cell_types"] = class_id_dict[example["cell_types"]]
    return example

# Convert cell types to ids
print("Mapping cell types to IDs...")
dataset = dataset.map(classes_to_ids, num_proc=1)
print("Mapping completed.")

# Fine-tune the model
print("Starting fine-tuning...")
geneformer_fine_tune.train(train_dataset=dataset, label="cell_types")
print("Fine-tuning completed.")

# Get logits from the fine-tuned model
print("Getting logits from the fine-tuned model...")
outputs = geneformer_fine_tune.get_outputs(dataset)
print(f"Logits: {outputs[:10]}")

# Get embeddings from the fine-tuned model
print("Getting embeddings from the fine-tuned model...")
embeddings = geneformer_fine_tune.get_embeddings(dataset)
print(f"Embeddings: {embeddings[:10]}")
