from helical.models.hyena_dna import HyenaDNAFineTuningModel, HyenaDNAConfig
import hydra
from omegaconf import DictConfig


@hydra.main(
    version_base=None,
    config_path="../run_models/configs",
    config_name="hyena_dna_config",
)
def preload_dependencies(cfg: DictConfig):
    # ✅ Minimal example inputs (not used for training)
    input_sequences = ["ACT" * 10]

    # ✅ Load config
    hyena_dna_config = HyenaDNAConfig(**cfg)

    # ✅ Initialize model (this will trigger download of model/tokenizer if needed)
    hyena_dna_fine_tune = HyenaDNAFineTuningModel(
        hyena_config=hyena_dna_config,
        fine_tuning_head="classification",
        output_size=3  # Dummy label count
    )

    # ✅ Run minimal preprocessing (triggers any tokenizer/model preprocessing download)
    _ = hyena_dna_fine_tune.process_data(input_sequences)

    print("✅ HyenaDNA model and dependencies downloaded.")


if __name__ == "__main__":
    preload_dependencies()

