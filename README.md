# Shakespeare Text Generation Using N-Grams

## Table of Contents
- [Project Overview](#project-overview)
- [Approach](#approach)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
  - [Text Preprocessing](#text-preprocessing)
  - [N-Gram Model](#n-gram-model)
  - [Text Generation](#text-generation)
- [Testing](#testing)
- [Human Evaluation](#human-evaluation)
- [Future Improvements](#future-improvements)
- [Contact](#contact)

---

## Project Overview

This project implements a text generation model that mimics William Shakespeare's style using **N-gram models (bigrams, trigrams, quadgrams, etc.)**. The model is trained on Shakespeare's works and can generate new text based on an initial phrase.

---

## Approach

1. **Preprocess the Text:** Convert to lowercase, remove punctuation, and tokenize.
2. **Create N-Grams:** Construct bigrams, trigrams, and quadgrams from the text.
3. **Compute Token Counts & Probabilities:** Build frequency distributions for next-word predictions.
4. **Generate Text:** Given an initial phrase, predict the next word probabilistically and iteratively build a sequence.
5. **Evaluate Model Performance:** Compare different N-gram models and conduct human evaluations.

---

## Dataset

- **Source:** Project Gutenberg's collection of Shakespeare’s works.
- **Download Link:** [Gutenberg Shakespeare](https://www.gutenberg.org/ebooks/100)
- **File Format:** Plain Text (.txt)
- **Processing:** Convert to lowercase, remove punctuation, and tokenize into words.

---

## Project Structure

```bash
└── smaswin21-shakespeare_text_generator/
    ├── README.md
    ├── data/
    │   └── shakesspeare.txt
    ├── src/
    │   ├── main.py
    │   ├── ngram_model.py
    │   ├── preprocess.py
    │   └── __pycache__/
    └── tests/
        ├── test.py
        └── __pycache__/
```

---

## Installation & Setup

1. **Clone the Repository:**

   ```bash
   git clone 
   cd src

*  Ensure you have Python 3.6+ installed.

2. **Create a Virtual Environment: (optional)** 
    ```bash
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
* No external dependencies needed (uses standard Python libraries).

## Usage

1. **Prepare the Dataset**

* Ensure shakespeare.txt is inside the data/ folder.

* Run the Script:

    ```bash
    python src/main.py

* Example Output:

    ```bash
    === BIGRAM MODEL ===
    Generated Text (Bigram):
    to be or not to be that is the question ...

## Code Explanation

### Text Preprocessing Stage (preprocess.py)

```bash
import re
import string

class TextPreprocessor:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_and_preprocess_text(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            text = file.read().lower()

        text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
        return text.split()
```

####  Explanation:

+ Reads the Shakespeare text file.
+ Converts all text to lowercase.
+ Removes punctuation.
+ Splits text into a list of tokens (words).


### N-Gram Model (ngram_model.py)

```bash
import random
from collections import defaultdict

class NGramModel:
    def __init__(self, tokens, n=2):
        self.tokens = tokens
        self.n = n
        self.ngram_to_next_token_counts = defaultdict(lambda: defaultdict(int))
        self.ngram_to_next_token_probs = defaultdict(dict)
        self._build_ngram_counts()
        self._build_ngram_probs()

    def _build_ngram_counts(self):
        for i in range(len(self.tokens) - self.n):
            ngram = tuple(self.tokens[i : i + self.n])
            next_token = self.tokens[i + self.n]
            self.ngram_to_next_token_counts[ngram][next_token] += 1
```

####  Explanation:

+ Builds frequency counts of the next word given an n-gram context
+ Dictionaries (defaultdict) to store word probabilities.

### Text Generation (main.py)

```bash
from text_preprocessor import TextPreprocessor
from ngram_model import NGramModel

def main():
    filepath = "../data/shakespeare.txt"
    preprocessor = TextPreprocessor(filepath)
    tokens = preprocessor.load_and_preprocess_text()

    bigram_model = NGramModel(tokens, n=2)
    initial_bigram = ("to", "be")
    print("Generated Text (Bigram):", bigram_model.generate_text(initial_bigram, 50))

if __name__ == "__main__":
    main()
```

## Testing

```bash
python -m unittest discover tests
```

### Example test (test.py):

```bash
import unittest
from src.ngram_model import NGramModel

class TestNGramModel(unittest.TestCase):
    def test_bigram_counts(self):
        tokens = ["to", "be", "or", "not", "to", "be"]
        model = NGramModel(tokens, n=2)
        self.assertIn(("to", "be"), model.ngram_to_next_token_counts)

if __name__ == "__main__":
    unittest.main()
```

## Human Evaluation

###  Conduct a Survey:

+ Show participants AI-generated text.
+ Ask them to rate coherence, Shakespearean style, and grammar.
+ Compare scores for bigrams, trigrams, and quadgrams.

### Survey Questions:

+ Are you familiar with Shakespeare’s works?
+ Does the text resemble Shakespearean language?  
+ What is your level of English proficiency?

+ Find more detasils in the link attached here - [Google Forms Survey](https://docs.google.com/forms/d/e/1FAIpQLScIvps5_6atyIEyGuzaM0DUT9JXFuNI9USN3iBmvkAMnXJufQ/viewform)



### Future Improvements

+ Implement smoothing techniques (e.g., Laplace Smoothing).
+ Use neural network models (RNNs, GPT-based) to compare quality.
+ Add more structured datasets (XML, JSON) for better NLP features.

##  Contact

+ Author: Aswin Subramanian MaheswaRAN
+ Email: asubramanian.ieu2022@student.ie.edu
+ GitHub: [Github Repository](https://github.com/smaswin21/shakespeare_text_generator)

#### Enjoy generating Shakespearean text with N-grams! 