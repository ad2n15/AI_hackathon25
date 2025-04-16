from helical.models.geneformer import GeneformerConfig, GeneformerFineTuningModel
from helical.utils import get_anndata_from_hf_dataset
from datasets import load_dataset
import anndata as ad
import hydra
from omegaconf import DictConfig


@hydra.main(
    version_base=None,
    config_path="../run_models/configs",
    config_name="geneformer_config",
)
def preload_dependencies(cfg: DictConfig):
    # ✅ Download dataset from Hugging Face (5% split is enough)
    hf_dataset = load_dataset(
        "helical-ai/yolksac_human",
        split="train[:5%]",
        trust_remote_code=True,
        download_mode="reuse_cache_if_exists"
    )

    # ✅ Convert to AnnData to trigger loading of necessary assets
    ann_data = get_anndata_from_hf_dataset(hf_dataset)

    # ✅ Load the Geneformer config
    geneformer_config = GeneformerConfig(**cfg)

    # ✅ Initialize the model (this will download any model/tokenizer files)
    _ = GeneformerFineTuningModel(
        geneformer_config=geneformer_config,
        fine_tuning_head="classification",
        output_size=2  # dummy value
    )

    print("✅ All required files and models should now be downloaded and cached.")


if __name__ == "__main__":
    preload_dependencies()

