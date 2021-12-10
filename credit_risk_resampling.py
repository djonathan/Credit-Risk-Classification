#!/usr/bin/env python
# coding: utf-8

# # Credit Risk Classification
# 
# Credit risk poses a classification problem that’s inherently imbalanced. This is because healthy loans easily outnumber risky loans. In this Challenge, you’ll use various techniques to train and evaluate models with imbalanced classes. You’ll use a dataset of historical lending activity from a peer-to-peer lending services company to build a model that can identify the creditworthiness of borrowers.
# 
# ## Instructions:
# 
# This challenge consists of the following subsections:
# 
# * Split the Data into Training and Testing Sets
# 
# * Create a Logistic Regression Model with the Original Data
# 
# * Predict a Logistic Regression Model with Resampled Training Data 
# 
# ### Split the Data into Training and Testing Sets
# 
# Open the starter code notebook and then use it to complete the following steps.
# 
# 1. Read the `lending_data.csv` data from the `Resources` folder into a Pandas DataFrame.
# 
# 2. Create the labels set (`y`)  from the “loan_status” column, and then create the features (`X`) DataFrame from the remaining columns.
# 
#     > **Note** A value of `0` in the “loan_status” column means that the loan is healthy. A value of `1` means that the loan has a high risk of defaulting.  
# 
# 3. Check the balance of the labels variable (`y`) by using the `value_counts` function.
# 
# 4. Split the data into training and testing datasets by using `train_test_split`.
# 
# ### Create a Logistic Regression Model with the Original Data
# 
# Employ your knowledge of logistic regression to complete the following steps:
# 
# 1. Fit a logistic regression model by using the training data (`X_train` and `y_train`).
# 
# 2. Save the predictions on the testing data labels by using the testing feature data (`X_test`) and the fitted model.
# 
# 3. Evaluate the model’s performance by doing the following:
# 
#     * Calculate the accuracy score of the model.
# 
#     * Generate a confusion matrix.
# 
#     * Print the classification report.
# 
# 4. Answer the following question: How well does the logistic regression model predict both the `0` (healthy loan) and `1` (high-risk loan) labels?
# 
# ### Predict a Logistic Regression Model with Resampled Training Data
# 
# Did you notice the small number of high-risk loan labels? Perhaps, a model that uses resampled data will perform better. You’ll thus resample the training data and then reevaluate the model. Specifically, you’ll use `RandomOverSampler`.
# 
# To do so, complete the following steps:
# 
# 1. Use the `RandomOverSampler` module from the imbalanced-learn library to resample the data. Be sure to confirm that the labels have an equal number of data points. 
# 
# 2. Use the `LogisticRegression` classifier and the resampled data to fit the model and make predictions.
# 
# 3. Evaluate the model’s performance by doing the following:
# 
#     * Calculate the accuracy score of the model.
# 
#     * Generate a confusion matrix.
# 
#     * Print the classification report.
#     
# 4. Answer the following question: How well does the logistic regression model, fit with oversampled data, predict both the `0` (healthy loan) and `1` (high-risk loan) labels?
# 
# ### Write a Credit Risk Analysis Report
# 
# For this section, you’ll write a brief report that includes a summary and an analysis of the performance of both machine learning models that you used in this challenge. You should write this report as the `README.md` file included in your GitHub repository.
# 
# Structure your report by using the report template that `Starter_Code.zip` includes, and make sure that it contains the following:
# 
# 1. An overview of the analysis: Explain the purpose of this analysis.
# 
# 
# 2. The results: Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of both machine learning models.
# 
# 3. A summary: Summarize the results from the machine learning models. Compare the two versions of the dataset predictions. Include your recommendation for the model to use, if any, on the original vs. the resampled data. If you don’t recommend either model, justify your reasoning.

# In[1]:


# Import the modules
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import confusion_matrix
from imblearn.metrics import classification_report_imbalanced

import warnings
warnings.filterwarnings('ignore')


# ---

# ## Split the Data into Training and Testing Sets

# ### Step 1: Read the `lending_data.csv` data from the `Resources` folder into a Pandas DataFrame.

# In[2]:


# Read the CSV file from the Resources folder into a Pandas DataFrame
# YOUR CODE HERE!

# Review the DataFrame
# YOUR CODE HERE!


# ### Step 2: Create the labels set (`y`)  from the “loan_status” column, and then create the features (`X`) DataFrame from the remaining columns.

# In[3]:


# Separate the data into labels and features

# Separate the y variable, the labels
# YOUR CODE HERE!]

# Separate the X variable, the features
# YOUR CODE HERE!


# In[4]:


# Review the y variable Series
# YOUR CODE HERE!


# In[5]:


# Review the X variable DataFrame
# YOUR CODE HERE!


# ### Step 3: Check the balance of the labels variable (`y`) by using the `value_counts` function.

# In[6]:


# Check the balance of our target values
# YOUR CODE HERE!


# ### Step 4: Split the data into training and testing datasets by using `train_test_split`.

# In[7]:


# Import the train_test_learn module
from sklearn.model_selection import train_test_split

# Split the data using train_test_split
# Assign a random_state of 1 to the function
# YOUR CODE HERE!


# ---

# ## Create a Logistic Regression Model with the Original Data

# ###  Step 1: Fit a logistic regression model by using the training data (`X_train` and `y_train`).

# In[8]:


# Import the LogisticRegression module from SKLearn
from sklearn.linear_model import LogisticRegression

# Instantiate the Logistic Regression model
# Assign a random_state parameter of 1 to the model
# YOUR CODE HERE!

# Fit the model using training data
# YOUR CODE HERE!


# ### Step 2: Save the predictions on the testing data labels by using the testing feature data (`X_test`) and the fitted model.

# In[9]:


# Make a prediction using the testing data
# YOUR CODE HERE!


# ### Step 3: Evaluate the model’s performance by doing the following:
# 
# * Calculate the accuracy score of the model.
# 
# * Generate a confusion matrix.
# 
# * Print the classification report.

# In[10]:


# Print the balanced_accuracy score of the model
# YOUR CODE HERE!


# In[11]:


# Generate a confusion matrix for the model
# YOUR CODE HERE!


# In[12]:


# Print the classification report for the model
# YOUR CODE HERE!


# ### Step 4: Answer the following question.

# **Question:** How well does the logistic regression model predict both the `0` (healthy loan) and `1` (high-risk loan) labels?
# 
# **Answer:** WRITE YOUR ANSWER HERE!

# ---

# ## Predict a Logistic Regression Model with Resampled Training Data

# ### Step 1: Use the `RandomOverSampler` module from the imbalanced-learn library to resample the data. Be sure to confirm that the labels have an equal number of data points. 

# In[13]:


# Import the RandomOverSampler module form imbalanced-learn
from imblearn.over_sampling import RandomOverSampler

# Instantiate the random oversampler model
# # Assign a random_state parameter of 1 to the model
# YOUR CODE HERE!

# Fit the original training data to the random_oversampler model
# YOUR CODE HERE!


# In[14]:


# Count the distinct values of the resampled labels data
# YOUR CODE HERE!


# ### Step 2: Use the `LogisticRegression` classifier and the resampled data to fit the model and make predictions.

# In[15]:


# Instantiate the Logistic Regression model
# Assign a random_state parameter of 1 to the model
# YOUR CODE HERE!

# Fit the model using the resampled training data
# YOUR CODE HERE!

# Make a prediction using the testing data
# YOUR CODE HERE!


# ### Step 3: Evaluate the model’s performance by doing the following:
# 
# * Calculate the accuracy score of the model.
# 
# * Generate a confusion matrix.
# 
# * Print the classification report.

# In[16]:


# Print the balanced_accuracy score of the model 
# YOUR CODE HERE!


# In[17]:


# Generate a confusion matrix for the model
# YOUR CODE HERE!


# In[18]:


# Print the classification report for the model
# YOUR CODE HERE!


# ### Step 4: Answer the following question

# **Question:** How well does the logistic regression model, fit with oversampled data, predict both the `0` (healthy loan) and `1` (high-risk loan) labels?
# 
# **Answer:** YOUR ANSWER HERE!
