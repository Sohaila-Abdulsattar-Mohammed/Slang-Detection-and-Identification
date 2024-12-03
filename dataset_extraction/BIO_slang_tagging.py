import pandas as pd
import re
from datasets import load_dataset

# Load dataset
ds = load_dataset("MLBtrio/genz-slang-dataset")
df = ds["train"].to_pandas()

# Function to check for punctuation
def has_punctuation(slang):
    return bool(re.search(r'[^\w\s]', slang))

# Filter out slangs with punctuation
df = df[~df["Slang"].apply(has_punctuation)]

# BIO tagging function
def bio_tagging(sentence, slang):
    sentence = sentence.lower()
    slang = slang.lower()

    # Split sentence into words and keep punctuation as separate tokens
    words = re.findall(r"\w+|[^\w\s]", sentence)
    tags = ["O"] * len(words)

    # Split slang into words and tag them
    slang_words = slang.split()
    for i in range(len(words) - len(slang_words) + 1):
        if words[i:i+len(slang_words)] == slang_words:
            tags[i] = "B"
            for j in range(1, len(slang_words)):
                tags[i+j] = "I"
            break
    return list(zip(words, tags))

# Apply BIO tagging
df["BIO_Tagged"] = df.apply(lambda row: bio_tagging(row["Example"], row["Slang"]), axis=1)

# Prepare the output DataFrame
output_df = df[["Slang", "Example", "BIO_Tagged"]].rename(columns={
    "Slang": "slang",
    "Example": "untagged_sentence",
    "BIO_Tagged": "bio_tagged_sentence"
})

# Save to TSV
output_df.to_csv("bio_tagged_dataset.tsv", sep="\t", index=False)

print("Slang terms with punctuation have been omitted, and the updated dataset has been saved.")
