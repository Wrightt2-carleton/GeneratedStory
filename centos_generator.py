import markovify
import os

# Directory containing cleaned text files
INPUT_DIR = "gutenberg_books"
OUTPUT_FILE = "centos_story.txt"

def load_texts():
    """Load all text files in the INPUT_DIR and combine them into one."""
    all_text = []

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".txt"):
            file_path = os.path.join(INPUT_DIR, filename)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read().strip()
                    all_text.append(text)
                print(f"✅ Loaded: {filename}")
            except Exception as e:
                print(f"❌ Error loading {filename}: {e}")

    return "\n".join(all_text)

def generate_centos_story(text):
    """Generate a Centos-style short story using Markov chains."""
    if len(text) < 100:
        print("❌ Error: Not enough text to generate a story.")
        return None
    
    print("🔄 Training Markov model...")
    model = markovify.Text(text, state_size=2)

    story_lines = []
    for _ in range(10):  # Generate 10 sentences for the short story
        sentence = model.make_sentence(tries=100)
        if sentence:
            story_lines.append(sentence)

    return "\n".join(story_lines)

if __name__ == "__main__":
    print("📖 Loading texts...")
    combined_text = load_texts()

    if combined_text:
        story = generate_centos_story(combined_text)
        if story:
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write(story)
            print(f"\n🚀 Centos-style short story saved to `{OUTPUT_FILE}`!\n")
            print("✨ Preview:\n")
            print(story)
        else:
            print("❌ Failed to generate a story.")
