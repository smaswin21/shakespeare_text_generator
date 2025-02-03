import re
import string

class TextPreprocess:
    
    def __init__(self, filepath):
        
        self.filepath = filepath
        
    def process_text(self):
        
        with open(self.filepath, 'r', encoding='utf-8') as file:
            text = file.read()
        text = text.lower()
        
        # A regex substitution to remove punctuation
        text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)

        # split on whitespace
        tokens = text.split()

        return tokens