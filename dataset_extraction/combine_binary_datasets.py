import random

def mix_equal_datasets(file_slang, file_non_slang, output_file):
    """
    Mix sentences from slang and non-slang datasets, ensuring an equal number of each.
    The total number of sentences in the output is 2 * the size of the smaller dataset.

    Args:
        file_slang (str): Path to the slang sentences file (tagged with 1).
        file_non_slang (str): Path to the non-slang sentences file (tagged with 0).
        output_file (str): Path to the output file with mixed sentences.
    """
    # Read sentences from both files
    with open(file_slang, 'r', encoding='utf-8') as slang_f:
        slang_sentences = slang_f.readlines()
    
    with open(file_non_slang, 'r', encoding='utf-8') as non_slang_f:
        non_slang_sentences = non_slang_f.readlines()
    
    # Determine the shorter dataset length
    min_length = min(len(slang_sentences), len(non_slang_sentences))
    
    # Randomly shuffle both datasets
    random.shuffle(slang_sentences)
    random.shuffle(non_slang_sentences)
    
    # Select equal numbers of slang and non-slang sentences
    slang_sample = slang_sentences[:min_length]
    non_slang_sample = non_slang_sentences[:min_length]
    
    # Interleave sentences from both datasets
    mixed_sentences = []
    for slang, non_slang in zip(slang_sample, non_slang_sample):
        if random.choice([True, False]):
            mixed_sentences.append(slang)
            mixed_sentences.append(non_slang)
        else:
            mixed_sentences.append(non_slang)
            mixed_sentences.append(slang)
    
    # Write the mixed sentences to the output file
    with open(output_file, 'w', encoding='utf-8') as out_f:
        out_f.writelines(mixed_sentences)

# File paths for input and output
file_slang = "slang_sentences_with_tags.txt"  # Replace with your slang file path
file_non_slang = "wsj_sentences_with_tags.txt"  # Replace with your non-slang file path
output_file = "binary_sentence_tags.txt"  # Output file for mixed sentences

# Mix the datasets and generate the output
mix_equal_datasets(file_slang, file_non_slang, output_file)
