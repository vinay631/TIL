## Rectfied Linear Units (RELU)
### Date: Feb 18, 2016

Rectified linear unit computes the function *f(x) = max(0, x)*. It thresholds activation at 0.

- Efficient computation unlike tanh/sigmoid neurons
- Speeds up the convergence of sgd compared to tanh/sigmoid
- Solves the problem of vanishing gradient (?) and exploding gradient (?)
