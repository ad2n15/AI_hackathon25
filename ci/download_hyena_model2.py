from datasets import load_dataset

# All task names in the dataset
all_tasks = [
    "H2AFZ",
    "H3K27ac",
    "splice_sites_donors",
    "splice_sites_acceptors",
    "H3K27me3",
    "H3K36me3",
    "H3K4me1",
    "splice_sites_all",
    "H3K4me2",
    "H3K4me3",
    "enhancers_types",
    "promoter_no_tata",
    "H3K9ac",
    "H3K9me3",
    "promoter_tata",
    "enhancers",
    "H4K20me1",
    "promoter_all"
]

# Loop over each task and download both train and test splits
for task in all_tasks:
    print(f"📥 Downloading: {task}")
    _ = load_dataset(
        "InstaDeepAI/nucleotide_transformer_downstream_tasks_revised",
        task,
        split="train",
        trust_remote_code=True
    )
    _ = load_dataset(
        "InstaDeepAI/nucleotide_transformer_downstream_tasks_revised",
        task,
        split="test",
        trust_remote_code=True
    )
    print(f"✅ Finished: {task}")

