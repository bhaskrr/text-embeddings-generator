from starlette.middleware.base import BaseHTTPMiddleware


import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

class Preprocessor():
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
    
    def remove_stopwords(self, text):
        filtered_words = [word for word in text.split() if word not in self.stop_words]
        return ' '.join(filtered_words)
    
    def lemmatize_text(self, text):
        tokens = word_tokenize(text)
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        return ' '.join(lemmatized_tokens)
    
    def process(self, text):
        text = text.lower().strip()

        # Remove URLs and unwanted characters
        text = re.sub(r'http\S+|www.\S+', '', text)
        text = re.sub(r'\(.*?\)|\[.*?\]', '', text)
        text = re.sub(r'[\(\)\[\]]', '', text)
        text = re.compile('<.*?>').sub('', text)
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text)

        # Uncomment this line if you want to remove stopwords
        # text = self.remove_stopwords(text)
        text = self.lemmatize_text(text)
        
        return text