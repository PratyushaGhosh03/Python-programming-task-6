from collections import Counter

def word_frequency(text):
    words = text.lower().split()
    return dict(Counter(words))

# Example usage
text = "Hello world! Hello everyone."
print(word_frequency(text))
