# Credit-Risk-Classification
Train and evaluate models with imbalanced, building a model that can identify the creditworthiness of borrowers.

---
## Technologies

Python modules used:

* pandas
* pathlib
* sklearn.metrics
* sklearn.model_selection
* sklearn.linear_model
* imblearn.metrics
* imblearn.over_sampling
---
## In a Jupyter Notebook:
* Split the Data into Training and Testing Sets
* Create a Logistic Regression Model with the Original Data
* Predict a Logistic Regression Model with Resampled Training Data
---
## Credit Risk Analysis Report
### Overview:
Credit risk prediction modeled on historical lending activity is problematic because the data is unbalanced: healthy loans outnumber risky loans. This can lead to results that under-estimate the possibility of loan default.

Using data from a peer-to-peer lending service, this analysis compares the accuracy of logistics regression modeling applied to the original unbalanced data, vs. the model applied to the data after random-oversampling.

The data was first split in to Training and Testing datasets.  A Logistic Regression model was created and fit on the Training dataset, then the model generated predictions using the Testing dataset.

* The pandas value_counts() function was used to show that in the original data, only 3% represented default.
* After random-oversampling value_counts() showed that the data had been adjusted to represent equal numbers of good and bad loans.


---

## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

* Logistic Regression Model 1 -- original data:
<pre>
  * Accuracy:   95%
  * Precision:  85%
  * Recall:     91%
</pre>

* Logistic Regression Model 2 -- over-sampled data:
<pre>
  * Accuracy:       95%
  * Precision:      84% (about the same, meaning we have not increased false positives)
  * Recall:         99% (represents improved prediction of loans that will default)
</pre>
---
## Contributors

[David Jonathan](https://www.linkedin.com/in/david-jonathan-1b9470/)

---

## License

Licensed under the [MIT License](https://github.com/tmbo/questionary/blob/master/LICENSE). Copyright 2021 David Jonathan
