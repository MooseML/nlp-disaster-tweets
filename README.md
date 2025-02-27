# NLP Disaster Tweets Project  

This repository contains code and models for classifying disaster-related tweets using traditional machine learning models (Logistic Regression, SVM, CatBoost) and deep learning models (GRU, DeBERTa). The goal is to build a robust NLP pipeline to distinguish between real and non-disaster tweets, overcoming challenges like ambiguous keyword usage.  

## Dataset  
The dataset consists of 10,000 tweets labeled as disaster (1) or non-disaster (0). It includes three feature columns: keyword, location, and text. The dataset was analyzed to extract insights on tweet length, keyword importance, and location relevance.  

## Models and Results  

| Model                         | Validation Accuracy | Validation F1 Score | Kaggle Submission Score |
|--------------------------------|---------------------|----------------------|-------------------------|
| Logistic Regression (TF-IDF)   | 0.7991              | 0.7441               | 0.76144                 |
| CatBoost (TF-IDF)              | 0.7833              | 0.7095               | 0.74395                 |
| SVM (TF-IDF)                   | 0.8056              | 0.7487               | 0.75388                 |
| GRU (GloVe Embeddings)         | 0.8116              | 0.7658               | 0.79098                 |
| DeBERTa Transformer            | N/A                 | N/A                  | **0.84033**              |

- **Baseline Models:** TF-IDF with Logistic Regression, SVM, and CatBoost established initial benchmarks.  
- **GRU Model:** Leveraged GloVe embeddings and bidirectional GRUs to capture sequential dependencies.  
- **DeBERTa Transformer:** Achieved the highest performance, utilizing advanced attention mechanisms and contextual embeddings.  

## Folder Structure  
- **Notebooks/**: Jupyter notebooks for experiments  
- **Scripts/**: Python scripts for data preprocessing, training, and evaluation  
- **Data/**: Dataset files (excluded from GitHub via `.gitignore`)  

## How to Use  
Clone the repository and install dependencies:  

```bash
git clone https://github.com/MooseML/nlp-disaster-tweets  
cd nlp-disaster-tweets  
pip install -r requirements.txt  
```

## Key Findings and Future Improvements  
- **Feature Engineering:** Keywords were strong disaster indicators, while location data was inconsistent.  
- **Model Performance:** GRU outperformed traditional ML models, but DeBERTa provided the best results.  
- **Future Work:** Potential improvements include ensembling GRU and DeBERTa, leveraging external datasets, and refining preprocessing.  

## Acknowledgements  
- **Kaggle NLP Disaster Tweets Competition**  
- **Transformer models via Hugging Face**  
- **Word embeddings from GloVe**
- **Full references provided in Jupyter notebook**

---
