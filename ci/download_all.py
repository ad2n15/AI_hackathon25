from helical.utils.downloader import Downloader
from pathlib import Path
import logging
from datasets import load_dataset

LOGGER = logging.getLogger(__name__)


def download_geneformer_models():
    downloader = Downloader()
    versions = ["v1", "v2"]

    # We can decide to download more models by simply adding the model names from the full list as reported in geneformer_config.py
    version_models_dict = {
        "v1": ["gf-12L-30M-i2048", "gf-6L-30M-i2048"],
        "v2": ["gf-12L-95M-i4096", "gf-12L-95M-i4096-CLcancer", "gf-20L-95M-i4096"],
    }

    for version in versions:
        # Download common files for each version
        common_files = [
            f"geneformer/{version}/gene_median_dictionary.pkl",
            f"geneformer/{version}/token_dictionary.pkl",
            f"geneformer/{version}/ensembl_mapping_dict.pkl",
        ]
        for file in common_files:
            downloader.download_via_name(file)

        # Get all model directories
        model_dirs = version_models_dict[version]

        for model_name in model_dirs:
            model_files = [
                f"geneformer/{version}/{model_name}/config.json",
                f"geneformer/{version}/{model_name}/training_args.bin",
            ]

            # Add version-specific files
            if version == "v2":
                model_files.extend(
                    [
                        f"geneformer/{version}/{model_name}/generation_config.json",
                        f"geneformer/{version}/{model_name}/model.safetensors",
                    ]
                )
            else:
                model_files.append(
                    f"geneformer/{version}/{model_name}/pytorch_model.bin"
                )

            # Download all files for the current model
            for file in model_files:
                downloader.download_via_name(file)

    LOGGER.info("All Geneformer models and files have been downloaded.")


def main():
    downloader = Downloader()
    downloader.display = False

    downloader.download_via_name("uce/4layer_model.torch")
    downloader.download_via_name("uce/all_tokens.torch")
    downloader.download_via_name("uce/species_chrom.csv")
    downloader.download_via_name("uce/species_offsets.pkl")




    downloader.download_via_name(
        "uce/protein_embeddings/Homo_sapiens.GRCh38.gene_symbol_to_embedding_ESM2.pt"
    )
    downloader.download_via_name(
        "uce/protein_embeddings/Macaca_fascicularis.Macaca_fascicularis_6.0.gene_symbol_to_embedding_ESM2.pt"
    )
    downloader.download_via_name(
        "uce/protein_embeddings/Danio_rerio.GRCz11.gene_symbol_to_embedding_ESM2.pt"
    )
    downloader.download_via_name(
        "uce/protein_embeddings/Macaca_mulatta.Mmul_10.gene_symbol_to_embedding_ESM2.pt"
    )
    downloader.download_via_name(
        "uce/protein_embeddings/Microcebus_murinus.Mmur_3.0.gene_symbol_to_embedding_ESM2.pt"
    )
    downloader.download_via_name(
        "uce/protein_embeddings/Mus_musculus.GRCm39.gene_symbol_to_embedding_ESM2.pt"
    )
    downloader.download_via_name(
        "uce/protein_embeddings/Sus_scrofa.Sscrofa11.1.gene_symbol_to_embedding_ESM2.pt"
    )
    downloader.download_via_name(
        "uce/protein_embeddings/Xenopus_tropicalis.Xenopus_tropicalis_v9.1.gene_symbol_to_embedding_ESM2.pt"
    )

    downloader.download_via_name("scgpt/scGPT_CP/vocab.json")
    downloader.download_via_name("scgpt/scGPT_CP/best_model.pt")

    download_geneformer_models()

    downloader.download_via_name("hyena_dna/hyenadna-tiny-1k-seqlen.ckpt")
    downloader.download_via_name("hyena_dna/hyenadna-tiny-1k-seqlen-d256.ckpt")
    downloader.download_via_name("hyena_dna/hyenadna-small-32k-seqlen.ckpt")
    downloader.download_via_name("hyena_dna/hyenadna-medium-450k-seqlen.ckpt")
    downloader.download_via_name("hyena_dna/hyenadna-large-1m-seqlen.ckpt")

    downloader.download_via_name(
        "caduceus/caduceus-ph-16L-seqlen-131k-d256/model.safetensors"
    )
    downloader.download_via_name(
        "caduceus/caduceus-ph-16L-seqlen-131k-d256/config.json"
    )
    downloader.download_via_name(
        "caduceus/caduceus-ph-4L-seqlen-1k-d118/model.safetensors"
    )
    downloader.download_via_name("caduceus/caduceus-ph-4L-seqlen-1k-d118/config.json")
    downloader.download_via_name(
        "caduceus/caduceus-ph-4L-seqlen-1k-d256/model.safetensors"
    )
    downloader.download_via_name("caduceus/caduceus-ph-4L-seqlen-1k-d256/config.json")
    downloader.download_via_name(
        "caduceus/caduceus-ps-16L-seqlen-131k-d256/model.safetensors"
    )
    downloader.download_via_name(
        "caduceus/caduceus-ps-16L-seqlen-131k-d256/config.json"
    )
    downloader.download_via_name(
        "caduceus/caduceus-ps-4L-seqlen-1k-d118/model.safetensors"
    )
    downloader.download_via_name("caduceus/caduceus-ps-4L-seqlen-1k-d118/config.json")
    downloader.download_via_name(
        "caduceus/caduceus-ps-4L-seqlen-1k-d256/model.safetensors"
    )
    downloader.download_via_name("caduceus/caduceus-ps-4L-seqlen-1k-d256/config.json")

    downloader.download_via_name("genept/genept_embeddings/genept_embeddings.json")

    downloader.download_via_link(
        Path("yolksac_human.h5ad"),
        "https://huggingface.co/datasets/helical-ai/yolksac_human/resolve/main/data/17_04_24_YolkSacRaw_F158_WE_annots.h5ad?download=true",
    )

    output_path = Path(".cache/pyensembl/GRCh38/ensembl110/Homo_sapiens.GRCh38.110.gtf.gz")
    output_path.parent.mkdir(parents=True, exist_ok=True)  # Create parent dirs if needed

    downloader.download_via_link(
        output_path,
        "https://ftp.ensembl.org/pub/release-110/gtf/homo_sapiens/Homo_sapiens.GRCh38.110.gtf.gz"
    )



    # Download Ensembl GTF and cDNA FASTA files (GRCh38, release 110)
    gtf_output_path = Path(".cache/pyensembl/GRCh38/ensembl110/Homo_sapiens.GRCh38.110.gtf.gz")
    gtf_output_path.parent.mkdir(parents=True, exist_ok=True)
    downloader.download_via_link(
        gtf_output_path,
        "https://ftp.ensembl.org/pub/release-110/gtf/homo_sapiens/Homo_sapiens.GRCh38.110.gtf.gz"
    )

    fasta_output_path = Path(".cache/pyensembl/GRCh38/ensembl110/Homo_sapiens.GRCh38.cdna.all.fa.gz")
    fasta_output_path.parent.mkdir(parents=True, exist_ok=True)
    downloader.download_via_link(
        fasta_output_path,
        "https://ftp.ensembl.org/pub/release-110/fasta/homo_sapiens/cdna/Homo_sapiens.GRCh38.cdna.all.fa.gz"
    )


    # Download Ensembl ncRNA FASTA file (GRCh38, release 110)
    ncrna_output_path = Path(".cache/pyensembl/GRCh38/ensembl110/Homo_sapiens.GRCh38.ncrna.fa.gz")
    ncrna_output_path.parent.mkdir(parents=True, exist_ok=True)
    downloader.download_via_link(
        ncrna_output_path,
        "https://ftp.ensembl.org/pub/release-110/fasta/homo_sapiens/ncrna/Homo_sapiens.GRCh38.ncrna.fa.gz"
    )


    # Download Ensembl protein FASTA file (GRCh38, release 110)
    pep_output_path = Path(".cache/pyensembl/GRCh38/ensembl110/Homo_sapiens.GRCh38.pep.all.fa.gz")
    pep_output_path.parent.mkdir(parents=True, exist_ok=True)
    downloader.download_via_link(
        pep_output_path,
        "https://ftp.ensembl.org/pub/release-110/fasta/homo_sapiens/pep/Homo_sapiens.GRCh38.pep.all.fa.gz"
    )


def download_nucleotide_transformer_dataset():
    # List of dataset splits to download
    dataset_label = "promoter_tata"
    splits = ["train", "test"]

    for split in splits:
        print(f"Downloading and caching split: {split} for dataset: {dataset_label}")
        _ = load_dataset(
            "InstaDeepAI/nucleotide_transformer_downstream_tasks_revised",
            dataset_label,
            split=split,
            trust_remote_code=True,
        )



    return True


if __name__ == "__main__":


    main()
    download_nucleotide_transformer_dataset()
