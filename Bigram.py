from collections import defaultdict, Counter
import math

# Corpus provided
sentences = [
    "ADBD",
    "CAAB",
    "DABD",
    "CCAD",
    "BABB"
]

# Adding start (<s>) and end (</s>) symbols to each sentence
processed_sentences = [["<s>"] + list(sentence) + ["</s>"] for sentence in sentences]

# Determine all unique characters
unique_chars = set()
for sentence in sentences:
    unique_chars.update(sentence)
unique_chars.update(["<s>", "</s>"])  # Include sentence boundary symbols

# Initialize all possible bigrams with Laplace smoothing
all_bigrams = defaultdict(lambda: defaultdict(lambda: 1))  # Start with 1 for Laplace smoothing
total_counts = defaultdict(lambda: len(unique_chars))  # Initial count for smoothing

# Update bigram counts with actual data
for sentence in processed_sentences:
    for i in range(len(sentence) - 1):
        first, second = sentence[i], sentence[i+1]
        all_bigrams[first][second] += 1
        total_counts[first] += 1

# Calculate bigram probabilities with Laplace smoothing and calculate perplexities
smoothed_perplexities = []

for sentence in processed_sentences:
    sentence_bigram_probs = []
    for i in range(len(sentence) - 1):
        first, second = sentence[i], sentence[i+1]
        bigram_prob_smoothed = all_bigrams[first][second] / total_counts[first]
        sentence_bigram_probs.append(bigram_prob_smoothed)

    # Calculating perplexity for the sentence with smoothing
    N = len(sentence) - 1  # number of bigrams in the sentence
    log_prob_sum_smoothed = sum(math.log2(p) for p in sentence_bigram_probs)
    perplexity_smoothed = 2 ** (-log_prob_sum_smoothed / N)
    smoothed_perplexities.append(perplexity_smoothed)

# Output the perplexity results
for i, perplexity in enumerate(smoothed_perplexities):
    print(f"Perplexity of sentence {i+1}: {perplexity:.4f}")

# Print the bigram probabilities matrix
print("\nBigram Probability Matrix:")
sorted_chars = sorted(unique_chars)
print("   " + "\t".join(sorted_chars))
for first in sorted_chars:
    row = [f"{all_bigrams[first][second] / total_counts[first]:.4f}" for second in sorted_chars]
    print(f"{first}: " + "\t".join(row))
