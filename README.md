# CSCN8020 Assignment 3 - Deep Q-Network for Atari Pong

**STUDENT NAME:**  SABRINA RONNIE GEORGE KARIPPATT
**Student ID:**    8991911

## Overview

This project implements a **Deep Q-Network (DQN)** agent for **Atari Pong** in Python using **PyTorch** and **Gymnasium/ALE**.

The notebook covers the full reinforcement learning workflow:
- environment setup and reproducibility
- Atari frame preprocessing
- frame stacking
- replay buffer implementation
- convolutional DQN model
- DQN agent with epsilon-greedy exploration
- trainer class for running experiments
- duration comparison experiments
- batch size comparison
- target network update frequency comparison
- observations, limitations, and conclusion

## Main File

- `CSCN8020_Assignment3.ipynb` — main submission notebook

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not yet present, the main packages used in this notebook are:

- numpy
- matplotlib
- torch
- gymnasium
- ale-py

Depending on your local environment and helper utilities, you may also need:
- opencv-python
- jupyter

## How to Run

1. Open the notebook in Jupyter Notebook or JupyterLab.
2. Ensure the required packages are installed.
3. Run the cells in order from top to bottom.
4. The notebook will:
   - validate the DQN pipeline with a short debug run
   - run longer experiments at 250 and 500 episodes
   - compare selected hyperparameters
   - generate plots and summary observations

## Experimental Structure

The notebook follows this progression:

1. **Debug validation**
   - 5-episode run to confirm that preprocessing, replay memory, training updates, and plotting all work correctly

2. **Training duration comparison**
   - 5 episodes
   - 250 episodes
   - 500 episodes

3. **Hyperparameter comparison**
   - Batch size: 8 vs 16
   - Target update frequency: every 3 episodes vs every 10 episodes

## Key Findings

- Very short runs are useful for debugging, but not for evaluating performance.
- Longer training durations reveal clearer learning trends.
- The 500-episode run showed the strongest evidence of learning.
- Batch size had only a modest effect under the current training budget.
- More frequent target network updates produced better results in this setup.

## Limitations

- Pong is a difficult Atari environment, and 250-500 episodes are still limited for full DQN convergence.
- Results are based on single runs and may vary because reinforcement learning is stochastic.
- Only a small subset of hyperparameters was explored.

## Notes

- Rewards in Atari Pong typically range from **-21 to +21**, where higher values indicate better performance.
- The notebook is designed to emphasize **structured experimentation** as well as implementation correctness.

## Author

Prepared for **CSCN8020 - Reinforcement Learning Programming**
