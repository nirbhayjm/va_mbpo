
# Model-Advantage and Value-Aware Models for Model-Based Reinforcement Learning: Bridging the Gap in Theory and Practice

Code for the MBPO experiments in [Model-Advantage and Value-Aware Models for Model-Based Reinforcement Learning: Bridging the Gap in Theory and Practice](https://arxiv.org/abs/2106.14080). This repository is a clone of
[MBRL-Lib](https://github.com/facebookresearch/mbrl-lib).

## Install

Please see the [original README of MBRL-Lib](MBRL-LIB-README.md) for
installing all the requirements of mbrl-lib. `PyTorch>=1.7` is required
by mbrl-lib and the experiments for this paper were ran with `PyTorch==1.9.1`.
Additionally, this repository uses [Weights and Biases](https://wandb.ai/) for tracking experiments on top of mbrl-lib. After installing PyTorch and `mbrl-lib`, the run the following commands to install extra dependencies.

```
# Patchelf required for mujoco-py==2.1.2.14
conda install patchelf=0.12
pip install -r requirements/va_mbpo_requirements.txt
```

Alternatively, the file `requirements/conda_va_mbpo.yaml` is provided to reproduce the conda environment for this code.

## Run

In order to run MBPO with a value-aware model learning objective, the following example command may be called (in this case, with the `mbrl/examples/conf/overrides/mbpo_halfcheetah` config file). Two new arguments are used for selecting amongst value-aware objectives and MLE. `overrides.model_loss_type` can either be `va` for value-aware or `mle` for the default maximum-likelihood model learning objective. `dynamics_model.va_norm` can be set to `l1` for the MA-L1 objective or `l2` for the [VAML](http://www.sologen.net/papers/IterVAML(NeurIPS2018)(extended).pdf) objective.

```
python -m mbrl/examples/main.py algorithm=mbpo action_optimizer=cem overrides=mbpo_halfcheetah dynamics_model=gaussian_mlp_ensemble +overrides.model_loss_type=va experiment=halfcheetah_va_l1
```

If tracking experiments with Weights and Biases (`wandb`), edit `mbrl/examples/conf/main.yaml` to set the `wandb_project_name`. For example, the following command activates `wandb` for tracking with the `use_wandb=1` option.

```
python -m mbrl/examples/main.py algorithm=mbpo action_optimizer=cem overrides=mbpo_halfcheetah dynamics_model=gaussian_mlp_ensemble +overrides.model_loss_type=va experiment=halfcheetah_va_l1 use_wandb=1 wandb_group_name=mbpo_mle_true_l1_0.01
```

### Additional hyper-parameters for value-aware losses

1. `dynamics_model.va_loss_coeff` (default `0.01`): Sets the scaling coefficient for value-aware model learning losses.
1. `overrides.value_update_interval` (default `5`): Sets the interval for number of model updates in between value function refitting in the model learning loop of training. Setting this to `0` deactivates value network refitting within model learning.
1. `overrides.num_v_updates_in_model` (default `5`): Hyper-parameter for value-refitting. Sets the number of value updates during refitting.
1. `overrides.v_update_batch_size` (default `5`): Hyper-parameter for value-refitting. Sets the batch size per update during value network refitting.
