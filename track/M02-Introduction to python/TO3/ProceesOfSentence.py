sentence = input()

# Clean and normalize the sentence
cleaned = sentence.strip()
normalized = cleaned.lower().replace(".", "")

# Split the sentence and create the slug
words = normalized.split()
slug = "-".join(words)

# Produce the uppercase form and search result
uppercase = normalized.upper()
python_position = normalized.find("python")

# Display all processed values
print(f"Cleaned: {cleaned}")
print(f"Normalized: {normalized}")
print(f"Words: {words}")
print(f"Slug: {slug}")
print(f"Uppercase: {uppercase}")
print(f"Python Position: {python_position}")