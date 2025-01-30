import markovify
import os

# Load the combined corpus
CORPUS_FILE = "markov_corpus.txt"

def train_markov_model():
    """Train a Markov chain model from the text corpus."""
    if not os.path.exists(CORPUS_FILE):
        print(f"❌ Error: Corpus file '{CORPUS_FILE}' not found. Run the preprocessing script first.")
        return None
    
    with open(CORPUS_FILE, "r", encoding="utf-8") as file:
        text = file.read().strip()
    
    if len(text) < 500:  # Ensure enough text for training
        print("⚠️ Warning: Corpus file is too short. Try adding more text.")
        return None
    
    print("🔄 Training Markov model...")
    return markovify.Text(text, state_size=1)  # Lower state size for more flexible generation

def generate_sentence(model):
    """Generate a random sentence from the Markov model."""
    if not model:
        return "❌ No model available."

    sentence = model.make_sentence(tries=10)  # Try 10 times to generate a sentence
    if not sentence:
        sentence = model.make_short_sentence(120, tries=10)  # Fallback to short sentence

    return sentence if sentence else "⚠️ Could not generate a valid sentence."

if __name__ == "__main__":
    model = train_markov_model()
    
    if model:
        print("\n✨ Generated Sentences:\n")
        for _ in range(5):
            print("📝", generate_sentence(model))
    else:
        print("❌ Could not generate sentences due to model training failure.")
