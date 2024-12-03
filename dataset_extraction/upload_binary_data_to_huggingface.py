import pandas as pd
from datasets import Dataset, DatasetDict
from sklearn.model_selection import train_test_split

def prepare_and_upload_data(file_path, hf_dataset_name):
    """
    Prepare the data and upload it to Hugging Face with specified splits.
    
    Args:
        file_path (str): Path to the combined dataset file.
        hf_dataset_name (str): Name for the Hugging Face dataset repository.
    """
    # Step 1: Load the data from the file
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:  # Ignore empty lines
                text, label = line.rsplit('\t', 1)  # Split text and label
                data.append({"text": text, "labels": int(label)})

    # Step 2: Convert to a DataFrame
    df = pd.DataFrame(data)

    # Step 3: Split the data into train, dev, and test sets
    train, temp = train_test_split(df, test_size=0.3, random_state=42)
    dev, test = train_test_split(temp, test_size=0.5, random_state=42)

    # Step 4: Convert splits to Hugging Face Dataset format
    train_dataset = Dataset.from_pandas(train)
    dev_dataset = Dataset.from_pandas(dev)
    test_dataset = Dataset.from_pandas(test)

    dataset_dict = DatasetDict({
        "train": train_dataset,
        "dev": dev_dataset,
        "test": test_dataset
    })

    dataset_dict = dataset_dict.remove_columns(["__index_level_0__"])

    # Step 5: Push to Hugging Face Hub
    dataset_dict.push_to_hub(hf_dataset_name)

# File path and Hugging Face dataset name
file_path = "binary_sentence_tags.txt"  # Replace with your local dataset file path
hf_dataset_name = "SohailaMohammed/BERTSlangDetectionInitial"  # Your Hugging Face dataset name

# Prepare and upload the dataset
prepare_and_upload_data(file_path, hf_dataset_name)
