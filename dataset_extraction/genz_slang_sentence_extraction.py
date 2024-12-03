from datasets import load_dataset

def extract_slang_sentences(dataset_name, output_file):
    """
    Extract sentences containing slang from the Hugging Face dataset
    and write to a file with a tag of 1.

    Args:
        dataset_name (str): Name of the Hugging Face dataset to load.
        output_file (str): Path to the output file.
    """
    # Load the dataset
    ds = load_dataset(dataset_name)

    # Open the output file for writing
    with open(output_file, 'w', encoding='utf-8') as out_f:
        # Iterate over the dataset (defaulting to the "train" split)
        for example in ds['train']:
            # Get the sentence from the 'example' field
            sentence = example['Example']
            if sentence:  # Ensure it's not empty
                # Write sentence with tag 1
                out_f.write(f"{sentence}\t1\n")

# Set the dataset name and output file path
dataset_name = "MLBtrio/genz-slang-dataset"
output_file_path = "slang_sentences_with_tags.txt"

# Extract slang sentences and write to output
extract_slang_sentences(dataset_name, output_file_path)