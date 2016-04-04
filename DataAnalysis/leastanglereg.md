## Least Angle Regression Algorithm

* Start with all coefficients b<sub>j</sub> equals to zero
* Find the predictor x<sub>j</sub> most correlated with y
* Increase the predictor coefficient b<sub>j</sub> in the same direction as its correlation with y. Compute the residual r = y - yhat. Continue until another predictor x<sub>k</sub> has as much correlation to r as x<sub>j</sub> has.
* Increase coefficients (b<sub>j</sub>, b<sub>k</sub>) in the direction of their joint least squares until some other predictor x<sub>m</sub> has same correlation with residual r.
* Continue until all the predictors are included in the model.

Source: http://statweb.stanford.edu/~tibs/lasso/simple.html
