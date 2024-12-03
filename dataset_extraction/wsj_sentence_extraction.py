import os
import re

def is_title_case(line):
    """
    Check if a line is entirely in title case (e.g., "In Washington and on Wall Street").
    Args:
        line (str): The line to evaluate.
    Returns:
        bool: True if the line is entirely title case, False otherwise.
    """
    words = line.strip().split()
    # List of lowercase exceptions that often appear in title case lines
    lowercase_exceptions = {"and", "an", "the", "on", "of", "in", "for", "&"}
    
    # If every word is capitalized or is a lowercase exception, it's title case
    return all(word.istitle() or word.lower() in lowercase_exceptions for word in words)

def clean_line(line):
    """
    Clean a line by removing leading uppercase words followed by a colon.
    
    Args:
        line (str): The line to clean.

    Returns:
        str: The cleaned line.
    """
    # Remove leading uppercase words followed by a colon
    cleaned_line = re.sub(r'^[A-Z\s]+:\s', '', line)
    return cleaned_line

def is_valid_sentence(line):
    """
    Determine if a line is a valid sentence based on stricter heuristics.

    Args:
        line (str): The line to evaluate.

    Returns:
        bool: True if the line is a valid sentence, False otherwise.
    """
    # Remove leading/trailing whitespace
    line = line.strip()

    # Exclude empty lines or lines starting with ".START"
    if not line or line.startswith(".START"):
        return False

    # Exclude lines starting with single letters or numbers
    if re.match(r'^[A-Z]\.\s|^\d', line):
        return False

    # Exclude lines with financial or measurement patterns
    if re.search(r'[\d,]+%|[\$\€\£]\d|Fees|CALL MONEY|Guarantee|Source:|Stocks:|Commodities:|Dollar:', line, re.IGNORECASE):
        return False

    # Exclude proper noun-like patterns (e.g., "Brown & Sons Inc.")
    if re.match(r'^[A-Z][a-z]+(\s+[A-Z][a-z]+)*(\s+&\s+[A-Z][a-z]+)*$', line):
        return False

    # Exclude all-uppercase titles or headers
    if line.isupper():
        return False

    # Exclude title-case lines (e.g., "In Washington and on Wall Street.")
    if is_title_case(line):
        return False

    # Exclude short lines (fewer than three words)
    if len(line.split()) < 3:
        return False

    # Exclude lines like "Ad Notes. . . ."
    if line == "Ad Notes. . . .":
        return False

    # Ensure the line starts with an uppercase letter and ends with terminal punctuation
    if re.match(r'^[A-Z].*[.!?]$', line):
        return True

    return False

def extract_wsj_sentences(wsj_dir, output_file):
    """
    Extract valid sentences from WSJ corpus and write to a file with a tag of 0.

    Args:
        wsj_dir (str): Path to the WSJ directory containing subfolders 00 to 24.
        output_file (str): Path to the output file.
    """
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for folder_num in range(25):
            folder_name = f"{folder_num:02d}"  # Format folder number as two digits
            folder_path = os.path.join(wsj_dir, folder_name)

            if not os.path.exists(folder_path):
                print(f"Folder not found: {folder_path}")
                continue

            for file_num in range(1, 100):
                file_name = f"wsj_{folder_num:02d}{file_num:02d}"
                file_path = os.path.join(folder_path, file_name)

                if not os.path.isfile(file_path):
                    print(f"File not found: {file_path}")
                    continue

                # Process the file
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as in_f:
                    for line in in_f:
                        # Remove leading uppercase words followed by a colon
                        cleaned_line = clean_line(line)
                        # Validate if the cleaned line is a proper sentence
                        if is_valid_sentence(cleaned_line):
                            out_f.write(f"{cleaned_line.strip()}\t0\n")

# Set the directory path for WSJ and the output file path
wsj_directory = "wsj"  # Replace with the actual path
output_file_path = "new_wsj_sentences_with_tags.txt"

# Extract sentences and write to output
extract_wsj_sentences(wsj_directory, output_file_path)