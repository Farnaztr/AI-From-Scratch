# AI From Scratch

Implementing Machine Learning and Deep Learning algorithms **from scratch** using only **Python** and **NumPy**.

The purpose of this repository is to understand the mathematical foundations of Machine Learning instead of relying on high-level libraries such as scikit-learn or TensorFlow.

---


# Current Implementations

* ✅ Linear Regression (Gradient Descent)

---

# Planned Implementations

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree
* Random Forest
* Naive Bayes
* Support Vector Machine (SVM)
* Perceptron
* Neural Networks
* Convolutional Neural Networks (CNN)
* Recurrent Neural Networks (RNN)
* Attention Mechanism
* Transformer

---

# Linear Regression

## Mathematical Model

The hypothesis function is defined as

[
\hat{y}=wx+b
]

where

* **x** : input feature
* **w** : weight (slope)
* **b** : bias (intercept)
* **ŷ** : predicted value

---

## Objective Function

The objective is to minimize the Mean Squared Error (MSE):

[
MSE=\frac1n\sum_{i=1}^{n}(y_i-\hat y_i)^2
]

where

* (y_i) is the true value
* (\hat y_i) is the predicted value
* (n) is the number of samples

---

## Gradient Descent

Gradient Descent updates the parameters iteratively to minimize the loss function.

### Gradient with respect to Weight

[
\frac{\partial J}{\partial w}
=============================

-\frac{2}{n}
\sum_{i=1}^{n}
x_i(y_i-\hat y_i)
]

### Gradient with respect to Bias

[
\frac{\partial J}{\partial b}
=============================

-\frac{2}{n}
\sum_{i=1}^{n}
(y_i-\hat y_i)
]

---

## Parameter Update

After computing the gradients, the parameters are updated using

[
w=w-\alpha\frac{\partial J}{\partial w}
]

[
b=b-\alpha\frac{\partial J}{\partial b}
]

where

* **α** is the learning rate.

---

# Training Procedure

1. Initialize weight and bias.
2. Predict the output.
3. Compute the Mean Squared Error.
4. Compute the gradients.
5. Update parameters.
6. Repeat until convergence.

---

# Time Complexity

| Operation            | Complexity |
| -------------------- | ---------: |
| Prediction           |       O(n) |
| Loss Calculation     |       O(n) |
| Gradient Calculation |       O(n) |
| One Training Epoch   |       O(n) |



---

# Technologies

* Python
* NumPy
* Matplotlib

---

# Future Improvements

* Mini-Batch Gradient Descent
* Stochastic Gradient Descent (SGD)
* Feature Scaling
* L1 & L2 Regularization
* Polynomial Regression
* Multiple Linear Regression
* Early Stopping
* Model Evaluation Metrics

---

# Goal

This repository is part of my journey to deeply understand Artificial Intelligence by implementing every algorithm from scratch before using high-level Machine Learning frameworks.

