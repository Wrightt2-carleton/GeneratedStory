import spacy
import os

# Function to download spaCy model if not available
def load_spacy_model():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        print("SpaCy model 'en_core_web_sm' not found. Downloading now...")
        import subprocess
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
        return spacy.load("en_core_web_sm")

# Load spaCy NLP model
nlp = load_spacy_model()

def get_noun_replacement(word, noun_list):
    """Find the noun 7 places after the given noun in the noun list."""
    try:
        index = noun_list.index(word)
        return noun_list[index + 7] if index + 7 < len(noun_list) else word
    except ValueError:
        return word  # Return original if not found

def n_plus_7_replace(text):
    """Perform the N+7 transformation on nouns in the given text."""
    doc = nlp(text)

    # Extract all nouns from the text in order
    noun_list = sorted(set(token.text.lower() for token in doc if token.pos_ == "NOUN"))

    # Replace nouns in the text
    replaced_text = [
        get_noun_replacement(token.text.lower(), noun_list) if token.pos_ == "NOUN" else token.text
        for token in doc
    ]

    return " ".join(replaced_text)

def process_file(input_file, output_file):
    """Reads input file, applies N+7 replacement, and saves output."""
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found. Please check the path.")
        return
    
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    transformed_text = n_plus_7_replace(text)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(transformed_text)

    print(f"✅ N+7 replacement complete! Check '{output_file}' for results.")

if __name__ == "__main__":
    # Define file paths
    input_file = "cleaned_text.txt"  # Make sure this file exists in the same folder
    output_file = "n_plus_7_text.txt"

    print("🔄 Processing N+7 replacement...")
    process_file(input_file, output_file)
    print("🚀 Done! Open VS Code and check 'n_plus_7_text.txt'.")

