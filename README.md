# **CSCN8020 Assignment 3 - Deep Q-Network for Atari Pong**

**STUDENT NAME:**  SABRINA RONNIE GEORGE KARIPPATT
**Student ID:**    8991911

# **Overview**

This assignment implements a Deep Q-Network (DQN) to train an agent to play Atari Pong using reinforcement learning.

The project demonstrates how deep learning and reinforcement learning can be combined to solve high-dimensional control problems where the agent learns directly from raw image input.

The work follows a structured experimental workflow:

Implementation → Validation → Experimentation → Analysis → Demo

## **Objectives**

The main objectives of this assignment are:

Implement a working DQN agent using PyTorch
Apply image preprocessing and frame stacking for Atari input
Evaluate the impact of training duration and hyperparameters
Analyze learning behavior using reward trends and plots
Demonstrate the trained agent through a final gameplay simulation

## **Methodology**

**Environment Setup**

- Environment: Atari Pong (Gymnasium)
- Input: Raw RGB frames from the game
- Output: Discrete action space

**Preprocessing Pipeline**

To make learning efficient, the following steps are applied:
- Cropping irrelevant regions
- Downsampling image resolution
- Converting to grayscale
- Normalizing pixel values to [-1, 1]
- Frame stacking to capture motion

## **DQN Architecture**

The implementation includes:
- Convolutional Neural Network (CNN) for feature extraction
- Experience Replay Buffer for stable learning
- Target Network to reduce instability
- Epsilon-Greedy Policy for exploration vs exploitation

Core Components:
- DQN → Neural network model
- DQNAgent → Handles learning and action selection
- PongTrainer → Manages training loop and experiments

## **Experiments Conducted**

**Debug Run (5 Episodes)**

Purpose:
- Validate pipeline correctness

**Observation:**
- Rewards remain highly negative
- No meaningful learning trend

**Conclusion:**
- Useful for debugging only 

**Training Duration Experiment**

| Episodes | Observation                          |
|----------|--------------------------------------|
| 250      | Early improvement, unstable          |
| 500      | Clear upward trend and better rewards|


Conclusion:
- Longer training is required to observe meaningful learning

**Batch Size Comparison**

| Batch Size  | Observation                                    |
|-------------|------------------------------------------------|
| 8           | Faster short-term improvement, higher variance |
| 16          | Slightly smoother but similar performance      |

Conclusion:

- Batch size has limited impact under current training scale

**Target Network Update Frequency**

| Update Frequency    | Observation                                             |
|---------------------|---------------------------------------------------------|
| Every 3 episodes    | Faster early learning but more fluctuation              |
| Every 10 episodes   | More stable learning and competitive final performance  |

## **Extended Training for Final Demo**

After identifying the better configuration, an additional experiment was conducted:

- 1000 episodes
- Batch size = 8
- Target update = every 10 episodes

*Purpose:*

- Improve policy quality for final demonstration
- Validate whether longer training improves performance

This extended run is not part of the main comparison, but serves as a refinement step for demonstration.

## **Results and Key Insights**

- Very short runs (5 episodes) are only useful for debugging
- Learning becomes visible only after sufficient training duration
- 500 episodes show meaningful improvement, but not full convergence
- Target network update frequency significantly affects stability
- Batch size has a comparatively smaller effect
- Reinforcement learning exhibits high variance and stochastic behavior

## **Final Demo**

The final demo loads the trained model from the extended 1000-episode run and performs a full gameplay episode using a greedy policy.

- Model file: pong_trained_model_tu10_ext1000.pth
- Example result: reward ≈ 20–21

Note:

- Small variations in reward are expected due to environment stochasticity

## **Limitations**

- The agent does not fully converge within 1000 episodes
- Reward variance remains high
- Only standard DQN is implemented

## **Future Improvements**

- Double DQN → reduce overestimation bias
- Dueling DQN → improve value estimation
- Longer training (2000+ episodes)
- Hyperparameter tuning (learning rate, epsilon decay)

## **Why DQN Works for Pong**

- Pong uses high-dimensional image input → CNN required  
- Traditional Q-learning cannot scale → function approximation needed  
- Experience replay improves sample efficiency  
- Target network stabilizes learning

## **Main File**

- CSCN8020_Assignment3.ipynb — main submission notebook

## **How to Run**

**Install Dependencies**

```
pip install -r requirements.txt
```

**Run Notebook**

- Open CSCN8020_Assignment3.ipynb
- Run all cells sequentially
- The notebook will:
   * Validate the pipeline
   * Run experiments (250, 500 episodes)
   * Compare hyperparameters
   * Train extended model (1000 episodes)
   * Run final demo animation

## **Reproducibility**

- Random seeds are set where applicable
- Results are generally reproducible, but small variations may occur due to:
   * stochastic environment dynamics
   * GPU/CPU differences

## **Conclusion**

This assignment successfully implements a Deep Q-Network (DQN) to solve Atari Pong.

The work demonstrates that:

- Training duration is the most critical factor in reinforcement learning
- Controlled experimentation is necessary for meaningful comparison
- Target network update frequency plays a key role in stability
- Reinforcement learning requires significant training time to achieve strong performance

The additional 1000-episode run confirms that extended training improves policy quality, enabling a strong final gameplay demonstration.

## **GitHub Repository**
https://github.com/Sabrina1911/DQN_Assignment3.git

# **Final Note**

This notebook emphasizes not only implementation correctness, but also structured experimentation, analysis, and interpretation, which are essential for real-world reinforcement learning workflows.