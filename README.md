# AI From Scratch

> Implementing Machine Learning and Deep Learning algorithms completely **from scratch** using only **Python**, **NumPy**, and **Matplotlib**.

The purpose of this repository is to understand the mathematics and implementation details behind Machine Learning algorithms before relying on high-level frameworks such as **Scikit-Learn**, **TensorFlow**, or **PyTorch**.

---

# Features

- Pure Python implementation
- NumPy-based numerical computation
- No Machine Learning libraries
- Mathematical implementation
- Gradient Descent optimization
- Visualization using Matplotlib
- Educational code with clean structure

---

# Current Implementations

| Algorithm | Description | Status |
|-----------|-------------|--------|
| Linear Regression | Predict continuous values using Gradient Descent | ✅ |
| Logistic Regression | Binary Classification using Sigmoid Function | ✅ |

---

# Planned Implementations

| Algorithm | Status |
|-----------|--------|
| K-Nearest Neighbors (KNN) | ⏳ |
| Decision Tree | ⏳ |
| Random Forest | ⏳ |
| Naive Bayes | ⏳ |
| Support Vector Machine (SVM) | ⏳ |
| Perceptron | ⏳ |
| Neural Networks | ⏳ |
| Convolutional Neural Networks (CNN) | ⏳ |
| Recurrent Neural Networks (RNN) | ⏳ |
| Attention Mechanism | ⏳ |
| Transformer | ⏳ |

---

# Implemented Algorithms

## Linear Regression

Linear Regression predicts **continuous numerical values** by fitting a straight line to the training data.

### Mathematical Model

$$
\hat{y}=wx+b
$$

### Loss Function

Mean Squared Error (MSE)

### Optimizer

Gradient Descent

---

### Example Result



<img src="https://raw.githubusercontent.com/Farnaztr/AI-From-Scratch/master/linear.png" width="400">

---

## Logistic Regression

Logistic Regression is a **binary classification** algorithm that predicts probabilities using the **Sigmoid** activation function.

### Linear Model

$$
z=wx+b
$$

### Activation Function

Sigmoid

$$
\sigma(z)=\frac1{1+e^{-z}}
$$

### Loss Function

Binary Cross Entropy (BCE)

### Optimizer

Gradient Descent

---

### Example Result


<img src="https://raw.githubusercontent.com/Farnaztr/AI-From-Scratch/master/sigmoid.png" width="400">  <img src="https://raw.githubusercontent.com/Farnaztr/AI-From-Scratch/master/curve.png" width="390">




---


# Goal

This repository is part of my journey to deeply understand Artificial Intelligence by implementing every Machine Learning and Deep Learning algorithm from scratch.

Instead of using high-level Machine Learning libraries, every model is built step by step using only Python and NumPy to better understand the underlying mathematics and optimization process.

The repository will continue to grow as more algorithms are implemented.
