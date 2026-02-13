disease-risk-prediction-ml
# Overview

This project implements an end-to-end bioinformatics and machine learning pipeline to predict Alzheimer’s disease status from gene expression data.

Using publicly available datasets from the NCBI Gene Expression Omnibus (GEO), the project covers data preprocessing, feature selection, model training, evaluation, biological interpretation of results, and deployment as a live web application.

The goal is to classify biological brain tissue samples as Alzheimer’s disease vs healthy control based on their gene expression profiles.

# Dataset

Source: NCBI Gene Expression Omnibus (GEO)
Dataset ID: GSE5281
Organism: Homo sapiens
Platform: GPL570 (Affymetrix Human Genome U133 Plus 2.0 Array)
Technology: Microarray (processed expression matrix)

# Samples

Disease (Alzheimer’s): 74

Control: 87

Total: 161 samples

Features

~54,000 microarray probe features

Reduced to top 1000 genes after feature selection

The dataset consists of a gene expression matrix where rows represent genes (probes) and columns represent samples, along with metadata describing disease status.

# Project Pipeline
Data Acquisition

Downloaded processed gene expression matrix from GEO

Extracted disease/control labels from sample metadata

Parsed phenotype information directly from GEO annotation fields

# Preprocessing

Log₂ transformation to stabilize variance:

log2(expression + 1)

Feature scaling using standardization (StandardScaler)

Conversion of matrix to Samples × Genes format

No missing values detected in dataset

# Feature Selection

Due to the high dimensionality (p ≫ n), feature reduction was necessary.

Variance-based gene filtering

Selected top 1000 most variable genes

Reduced dimensionality from ~54,000 → 1000 features

This step improves generalization and prevents overfitting.

# Modeling

Models trained and compared:

Logistic Regression (baseline, interpretable)

Random Forest

Support Vector Machine (SVM)

# Evaluation

Performance was evaluated using:

Accuracy

ROC-AUC score

Confusion matrix

Stratified train-test split (80/20)

# Results
Model	Accuracy	ROC-AUC
Logistic Regression	~93–94%	~0.99
Random Forest	~91%	~0.98
SVM	~93–94%	~0.98

The logistic regression model was selected as the final model due to:

Strong performance

Stability in high-dimensional data

Interpretability of gene coefficients

Biological interpretability

# Biological Interpretation

Logistic regression coefficients were mapped from microarray probe IDs to gene symbols using the GPL570 platform annotation file.

The most influential genes identified by the model include:

FBXL5 – Linked to oxidative stress regulation

FXR2 – Associated with RNA regulation in neurons

FAM168B – Implicated in neuronal cellular processes

KCNIP3 – Related to neuronal signaling mechanisms

OGFRL1 – Potential role in neuronal pathways

Several identified genes are associated with:

Synaptic function

Neuronal regulation

RNA processing

Cellular stress mechanisms

These findings align with known molecular mechanisms involved in Alzheimer’s disease, supporting the biological relevance of the model.

# Deployment

The trained model was deployed as a Streamlit web application.

Users can:

Upload a CSV file containing gene expression values

Receive predicted class (Alzheimer’s / Control)

View predicted probability score

# Live App:
https://disease-risk-prediction-ml-ezzq7ikzgw7vcxtohviapp2.streamlit.app/

# Methods
Preprocessing

Gene expression values were log-transformed using log2(x + 1) to reduce skewness and standardized to ensure comparable scales across genes.

Feature Selection

Low-information genes were removed using variance-based filtering to address the high dimensionality of transcriptomic data.

Machine Learning Models

Logistic Regression: Selected as final model due to interpretability and strong performance.

Random Forest / SVM: Used for comparison to evaluate potential non-linear modeling improvements.

# Key Skills Demonstrated

Transcriptomic data preprocessing

High-dimensional feature selection

Model comparison and evaluation

Interpretable machine learning

Probe-to-gene annotation mapping

End-to-end ML deployment
