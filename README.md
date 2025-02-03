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



---

## Installation & Setup

1. **Clone the Repository:**

   ```bash
   git clone 
   cd "inside the directory"

*  Ensure you have Python 3.6+ installed.
