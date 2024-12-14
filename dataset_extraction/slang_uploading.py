from datasets import Dataset, DatasetDict
from huggingface_hub import HfApi
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
file_path = "slang_detection_final_dataset.csv"
dataset = pd.read_csv(file_path)

# Split the dataset into train (85%) and test (15%) sets
train_data, test_data = train_test_split(dataset, test_size=0.15, random_state=42)

# Convert the train and test DataFrames to Hugging Face Dataset format
train_dataset = Dataset.from_pandas(train_data)
test_dataset = Dataset.from_pandas(test_data)

# Combine into a DatasetDict
dataset_dict = DatasetDict({
    "train": train_dataset,
    "test": test_dataset
})

dataset_dict = dataset_dict.remove_columns(["__index_level_0__"])

# Push the dataset to Hugging Face Hub
dataset_name = "SohailaMohammed/BERTSlangDetection"
dataset_dict.push_to_hub(dataset_name)

print(f"Dataset successfully uploaded to Hugging Face Hub: {dataset_name}")
