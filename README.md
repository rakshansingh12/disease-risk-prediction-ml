# disease-risk-prediction-mlOverview

This project implements an end-to-end bioinformatics and machine learning pipeline to predict disease status from gene expression data. Using publicly available datasets from the NCBI Gene Expression Omnibus (GEO), the project covers data preprocessing, feature selection, model training, evaluation, and biological interpretation of results.

The goal is to classify biological samples as disease vs healthy control (or disease subtypes) based on their gene expression profiles.

# Dataset

Source: NCBI Gene Expression Omnibus (GEO)

Dataset ID: GSEXXXXX

Organism: Homo sapiens

Technology: Microarray / RNA-Seq (processed expression matrix)

Samples:

Disease: N

Control: M

Features: ~20,000 genes

The dataset consists of a gene expression matrix where rows represent genes and columns represent samples, along with metadata describing disease status.

# Project Pipeline

Data Acquisition

Downloaded processed gene expression matrix from GEO

Extracted disease/control labels from sample metadata

Preprocessing

Log₂ transformation to stabilize variance

Feature scaling using standardization

Basic handling of missing values

Feature Selection

Variance-based gene filtering

(Optional) Statistical testing to identify differentially expressed genes

Modeling

Baseline model: Logistic Regression

Advanced models: Random Forest / Support Vector Machine (optional)

Evaluation

Accuracy

ROC-AUC score

Confusion matrix

# Biological Interpretation

Identification of top predictive genes

Literature-based validation of biologically relevant genes

# Methods
Preprocessing

Gene expression values were log-transformed using log2(x + 1) to reduce skewness and standardized to ensure comparable scales across genes.

Feature Selection

Due to the high dimensionality of gene expression data, low-information genes were removed using variance-based filtering and statistical significance testing between disease and control groups.

Machine Learning Models

Logistic Regression: Used as a baseline model due to simplicity and interpretability

Random Forest / SVM: Used to capture non-linear relationships in the data (optional)

# Results
Model	Accuracy	ROC-AUC
Logistic Regression	XX%	XX
Random Forest	XX%	XX

The baseline logistic regression model achieved strong performance, indicating that a subset of genes contains meaningful predictive signal for disease status.

Biological Interpretation

The most influential genes identified by the model include:

GENE1 – Associated with disease-related cellular pathways

GENE2 – Implicated in immune response and inflammation

GENE3 – Previously reported as a disease biomarker

These findings are consistent with existing biological literature, supporting the relevance of the selected features.
