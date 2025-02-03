from preprocess import TextPreprocess
from ngram_model import NGramModel

def main():
    
    # Step 1: Data Preparation
    
    filepath = "../data/shakesspeare.txt"  
    preprocessor = TextPreprocess(filepath)
    tokens = preprocessor.process_text()

    # ----- Bigrams (n=2) -----
    
    print("----------Bigram Model-------------")
    bigram_model = NGramModel(tokens, n=2)

    # Generate 50 tokens starting with a sample bigram
    
    initial_bigram = ("to", "be")
    generated_text_bigram = bigram_model.generate_text(initial_bigram, num_tokens=50)
    print(f"Generated Text (Bigram):\n{generated_text_bigram}\n")

    # ----- Trigrams (n=3) -----
    print("---------- TRIGRAM MODEL----------")
    trigram_model = NGramModel(tokens, n=3)

    # Generate 50 tokens starting with a sample trigram
    
    initial_trigram = ("to", "be", "or")  
    generated_text_trigram = trigram_model.generate_text(initial_trigram, num_tokens=50)
    print(f"Generated Text (Trigram):\n{generated_text_trigram}\n")

    # ----- Quadgrams (n=4) -----
    
    print("----------  QUADGRAM MODEL---------- ")
    quadgram_model = NGramModel(tokens, n=4)

    # Generate 50 tokens starting with a sample quadgram
    
    initial_quadgram = ("to", "be", "or", "not")  
    generated_text_quadgram = quadgram_model.generate_text(initial_quadgram, num_tokens=50)
    print(f"Generated Text (Quadgram):\n{generated_text_quadgram}\n")

if __name__ == "__main__":
    main()
