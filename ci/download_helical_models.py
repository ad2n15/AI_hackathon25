from helical.models.geneformer import GeneformerConfig, GeneformerFineTuningModel
import anndata as ad

# Load the data
ann_data = ad.read_h5ad("yolksac_human.h5ad")

# Get the column for fine-tuning
cell_types = list(ann_data.obs["LVL1"][:10])
label_set = set(cell_types)

# Create a GeneformerConfig object
geneformer_config = GeneformerConfig(model_name="gf-12L-95M-i4096", batch_size=10)

# Create a GeneformerFineTuningModel object
geneformer_fine_tune = GeneformerFineTuningModel(geneformer_config=geneformer_config, fine_tuning_head="classification", output_size=len(label_set))

