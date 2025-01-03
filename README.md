# Slang Detection and Identification using BERT

This repository contains the code, datasets, and results for our work on **Slang Detection and Identification** using **BERT**, a transformer-based model. Our research paper, which provides a comprehensive overview of our methodology and findings, is also available in this repository. The project addresses the challenges of understanding the dynamic and informal nature of English slang by fine-tuning BERT for two key tasks: 
1. **Slang Detection** (binary classification at the sentence level).
2. **Slang Identification** (token-level tagging using the BIO scheme).

Our approach leverages the powerful contextual understanding of BERT to process slang across diverse contexts, contributing to advancements in natural language processing (NLP) for informal language.

## Features
- Fine-tuned BERT model for binary slang detection.
- BIO-tagging model for token-level slang identification.
- Comprehensive dataset combining written and spoken slang.
- K-fold cross-validation for robust evaluation.
- Evaluation metrics: accuracy, precision, recall, and F1-score.

## Results

### Slang Detection Model
- **Accuracy:** 88%
- **F1-score:** 0.88

### Slang Identification Model
- **Accuracy:** 97%
- **F1-score:** 0.97

## Credits
### Datasets and code
- https://huggingface.co/datasets/MLBtrio/genz-slang-dataset
- https://www.kaggle.com/datasets/rizdelhi/socialmediaabbrevations
- https://github.com/kaspercools/genz-dataset
- https://github.com/amazon-science/slang-llm-benchmark
- https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/model-compression
- https://github.com/NielsRogge/Transformers-Tutorials/blob/master/BERT/Custom_Named_Entity_Recognition_with_BERT.ipynb
