import os
import re

# Directory containing downloaded Gutenberg books
INPUT_DIR = "gutenberg_books"
OUTPUT_FILE = "markov_corpus.txt"

def clean_text(text):
    """
    Preprocess text by:
    - Removing Gutenberg license headers and footers
    - Removing special characters
    - Lowercasing everything
    """
    # Remove Gutenberg header/footer
    start_marker = "*** START OF"
    end_marker = "*** END OF"
    lines = text.split("\n")
    
    inside_book = False
    cleaned_lines = []

    for line in lines:
        if start_marker in line:
            inside_book = True
            continue
        if end_marker in line:
            inside_book = False
            break
        if inside_book:
            cleaned_lines.append(line)

    # Join and clean text
    text = "\n".join(cleaned_lines)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)  # Remove special characters
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    return text.lower()  # Convert to lowercase

def merge_text_files():
    """Read all .txt files in INPUT_DIR, clean, and merge them into one."""
    all_text = []

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".txt"):
            file_path = os.path.join(INPUT_DIR, filename)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()
                    cleaned_text = clean_text(text)
                    all_text.append(cleaned_text)
                print(f"✅ Processed: {filename}")
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")

    # Write to a single output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(all_text))

    print(f"\n🚀 All books processed! Merged text saved in `{OUTPUT_FILE}`.")

if __name__ == "__main__":
    merge_text_files()
