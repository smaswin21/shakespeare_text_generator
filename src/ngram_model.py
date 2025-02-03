import random
from collections import defaultdict

class NGramModel:
    def __init__(self, tokens, n=2):
        self.tokens = tokens
        self.n = n
        self.ngram_to_next_token_counts = defaultdict(lambda: defaultdict(int))
        self.ngram_to_next_token_probs = defaultdict(dict)

        # Build the dictionaries
        self._build_ngram_counts()
        self._build_ngram_probs()

    def _build_ngram_counts(self):
        for i in range(len(self.tokens) - self.n):
            ngram = tuple(self.tokens[i : i + self.n])  # current n-gram
            next_token = self.tokens[i + self.n]        # the token that follows
            self.ngram_to_next_token_counts[ngram][next_token] += 1

    def _build_ngram_probs(self):
        for ngram, next_token_dict in self.ngram_to_next_token_counts.items():
            total_count = sum(next_token_dict.values())
            for token, count in next_token_dict.items():
                self.ngram_to_next_token_probs[ngram][token] = count / total_count

    def sample_next_token(self, context):
        # If the context is not in the dictionary, return None or a fallback.
        if context not in self.ngram_to_next_token_probs:
            return None

        # Get the dict of possible next tokens + probabilities
        next_token_prob_dict = self.ngram_to_next_token_probs[context]

        tokens = list(next_token_prob_dict.keys())
        probs = list(next_token_prob_dict.values())

        next_token = random.choices(tokens, weights=probs, k=1)[0]
        return next_token

    def generate_text(self, initial_context, num_tokens=50):
        # Generated text with the initial context
        current_context = list(initial_context)
        generated_tokens = list(initial_context)

        # Generate next tokens iteratively
        for _ in range(num_tokens):
            context_tuple = tuple(current_context[-(self.n):])  # the last n tokens
            next_token = self.sample_next_token(context_tuple)

            if not next_token:
                # If we can't find a next token, break early
                break

            generated_tokens.append(next_token)
            current_context.append(next_token)

        return " ".join(generated_tokens)
