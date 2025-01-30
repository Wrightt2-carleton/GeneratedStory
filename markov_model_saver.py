import markovify
import os
import json

# File paths
CORPUS_FILE = "markov_corpus.txt"
MODEL_FILE = "markov_model.json"

def train_markov_model():
    """Train a Markov chain model from the text corpus."""
    if not os.path.exists(CORPUS_FILE):
        print(f"❌ Error: Corpus file '{CORPUS_FILE}' not found. Run the preprocessing script first.")
        return None
    
    with open(CORPUS_FILE, "r", encoding="utf-8") as file:
        text = file.read().strip()
    
    if len(text) < 100:  # If the corpus is too short, warn the user
        print("⚠️ Warning: Corpus file is too short. Try adding more text.")
        return None
    
    print("🔄 Training Markov model...")
    return markovify.Text(text, state_size=2)

def save_model(model):
    """Save the Markov model to a JSON file."""
    if not model:
        print("❌ No model available to save.")
        return
    
    model_json = model.to_json()
    
    with open(MODEL_FILE, "w", encoding="utf-8") as file:
        json.dump(model_json, file)
    
    print(f"✅ Markov model saved as '{MODEL_FILE}'.")

def load_model():
    """Load the Markov model from a JSON file."""
    if not os.path.exists(MODEL_FILE):
        print(f"❌ Error: Model file '{MODEL_FILE}' not found. Train and save a model first.")
        return None
    
    with open(MODEL_FILE, "r", encoding="utf-8") as file:
        model_json = json.load(file)
    
    return markovify.Text.from_json(model_json)

def generate_sentence(model):
    """Generate a random sentence from the Markov model."""
    if not model:
        return "❌ No model available."
    
    for _ in range(10):  # Try multiple times to get a valid sentence
        sentence = model.make_sentence(tries=100)
        if sentence:
            return sentence
    
    return "⚠️ Could not generate a valid sentence."

if __name__ == "__main__":
    model = train_markov_model()
    
    if model:
        save_model(model)
        
        # Reload model and test sentence generation
        loaded_model = load_model()
        if loaded_model:
            print("\n✨ Generated Sentence from Saved Model:\n")
            print("📝", generate_sentence(loaded_model))
    else:
        print("❌ Could not generate a model.")
