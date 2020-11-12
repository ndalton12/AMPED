
from ray import tune

from src.algos.mu_zero.mu_zero_trainer import MuZeroTrainer
from src.common.env_wrappers import register_super_mario_env


def train():
    register_super_mario_env()

    tune.run(MuZeroTrainer, config={
        "env": "super_mario",
        "framework": "torch",
        "num_workers": 4,
        "log_level": "DEBUG",
        "seed": 1337,
        "num_envs_per_worker": 5,
        "entropy_coeff": 0.01,
        "kl_coeff": 0.0,
        "vf_share_layers": True,
        "train_batch_size": 256,
        "num_sgd_iter": 2,
        "num_simulations": 25,
    })


if __name__ == "__main__":
    train()
