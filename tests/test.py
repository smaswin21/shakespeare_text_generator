import unittest
from src.preprocess import TextPreprocess
from src.ngram_model import NGramModel

class TestNGramModel(unittest.TestCase):

    def setUp(self):
        # Example small token list for testing
        self.example_tokens = [
            "to", "be", "or", "not", "to", "be", 
            "that", "is", "the", "question"
        ]

    def test_bigram_counts(self):
        model = NGramModel(self.example_tokens, n=2)
        # We can test if certain bigrams are present in the dictionary
        self.assertIn(("to", "be"), model.ngram_to_next_token_counts)
        self.assertIn(("be", "or"), model.ngram_to_next_token_counts)

    def test_trigram_counts(self):
        model = NGramModel(self.example_tokens, n=3)
        # Check if certain trigrams are in the dictionary
        self.assertIn(("to", "be", "or"), model.ngram_to_next_token_counts)
        self.assertIn(("be", "or", "not"), model.ngram_to_next_token_counts)

    def test_sampling(self):
        model = NGramModel(self.example_tokens, n=2)
        # We know ("to", "be") is followed by "or", "that" in the example
        next_tokens = model.ngram_to_next_token_counts[("to", "be")]
        self.assertTrue("or" in next_tokens or "that" in next_tokens)

        sampled_token = model.sample_next_token(("to", "be"))
        # The sampled token should be among the possible next tokens
        self.assertIn(sampled_token, next_tokens.keys())

    def test_text_generation(self):
        model = NGramModel(self.example_tokens, n=2)
        generated_text = model.generate_text(("to", "be"), num_tokens=5)
        # We should have at least 2 (initial) + 5 (generated) = 7 tokens
        self.assertGreaterEqual(len(generated_text.split()), 7)

if __name__ == "__main__":
    unittest.main()
