## Dropout
### February 17, 2016

---

Dropout is a technique used to prevent overfitting in Deep Neural Networks. In this method, some of the activation functions (or neurons) are randomly dropped forcing the network to learn the multiple independent representation of the same data. This is how it works: during learning phase, ignore some units and their associate weights by a probability _p, train with back propagation, repeat the same for other training sample and average the weights across all the structures thus obtained and use those new weights to perform the predictions.

---
