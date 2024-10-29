# Neural Network Equations for Mind and Consciousness

---

## 1. Foundational Equations in Neural Networks

### Activation Functions
- **Sigmoid**: `σ(x) = 1 / (1 + e^(-x))`
- **Tanh (Hyperbolic Tangent)**: `tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))`
- **ReLU (Rectified Linear Unit)**: `f(x) = max(0, x)`
- **Softmax**: `softmax(x_i) = e^(x_i) / Σ e^(x_j)`

### Loss Functions
- **Mean Squared Error (MSE)**: `MSE = (1/n) Σ (y_i - ŷ_i)^2`
- **Cross-Entropy Loss**: `L = - Σ y_i * log(ŷ_i)`
- **KL Divergence**: `D_KL(P||Q) = Σ P(i) * log(P(i) / Q(i))`

### Optimization Algorithms
- **Gradient Descent**: `w := w - η ∇_w L(w)`
- **Adam Optimizer**: Combination of momentum and RMSProp for adaptive learning rates.

---

## 2. Network Architectures and Memory Equations

### Feedforward Networks
- **Forward Propagation**: `a^(l+1) = f(W^(l) * a^(l) + b^(l))`

### Recurrent Neural Networks (RNNs)
- **Simple RNN Cell**: `h_t = f(W_x * x_t + W_h * h_(t-1) + b)`
- **LSTM Cell**
  - **Forget Gate**: `f_t = σ(W_f * [h_(t-1), x_t] + b_f)`
  - **Input Gate**: `i_t = σ(W_i * [h_(t-1), x_t] + b_i)`
  - **Output Gate**: `o_t = σ(W_o * [h_(t-1), x_t] + b_o)`

### Hopfield Networks
- **Energy Function**: `E = - (1/2) Σ Σ w_(ij) * s_i * s_j + Σ θ_i * s_i`

### Boltzmann Machines
- **Energy Function**: `E = - Σ a_i * s_i - Σ Σ w_(ij) * s_i * s_j`

---

## 3. Attention and Consciousness Modeling Equations

### Attention Mechanisms
- **Scaled Dot-Product Attention**:  
  `Attention(Q, K, V) = softmax((Q * K^T) / √d_k) * V`

### Transformer Models
- **Self-Attention**: Each token attends to every other token in the input.

### Global Workspace Theory Equations
- **Global Neuronal Workspace Activation**: Modeled as weighted summations across neuron layers, representing conscious awareness activation through recurrent loops.

---

## 4. Probabilistic and Cognitive Modeling Equations

### Markov Chains
- **Transition Matrix**: `P(X_(t+1) = j | X_t = i) = p_(ij)`

### Bayesian Inference Models
- **Posterior Probability**: `P(θ | X) = (P(X | θ) * P(θ)) / P(X)`

### Restricted Boltzmann Machines (RBMs)
- **Free Energy**: `F(v) = - Σ a_i * v_i - Σ log(1 + exp(b_j + Σ v_i * w_(ij)))`

---

## 5. Equations for Modeling Memory and Consciousness

### Hebbian Learning Rule
- **Weight Update**: `Δw_(ij) = η * x_i * y_j`

### Attractor Dynamics (Used in Memory and Consciousness Models)
- **Lyapunov Stability Equations** for determining stable points or “attractors” in neural systems, where `ẋ = f(x)` shows points of stability.

### Integrated Information Theory (IIT)
- **Φ Calculation**: Measures integration across information channels.

---

## 6. Emergent Properties and Qualia Representation Equations

### Graph Theory for Network Consciousness
- **Graph Centrality Measures**: Calculations for node importance, like Eigenvector centrality, help in defining hubs of conscious awareness.
- **Information Flow (Entropy)**: `H(X) = -Σ p(x) * log(p(x))`

### Quantum Neural Networks
- **Superposition State Representation**: Extends neural states to qubits, where states are `|ψ⟩ = α|0⟩ + β|1⟩`

### Qualia and Information Representation
- **Information Partitioning** in networks, measuring qualia as complex, stable patterns in high-dimensional space.

---

This outline provides structured categories and sub-categories of equations relevant to neural networks, cognitive modeling, and consciousness studies.
