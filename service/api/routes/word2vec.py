import time
from ...core.preprocessor import Preprocessor
from fastapi.routing import APIRouter

from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action='ignore')

preprocessor = Preprocessor()
word2vec_route = APIRouter()

@word2vec_route.get('/{text}')
def w2v(text: str):
    start_time = time.time()
    
    text = preprocessor.process(text)
    
    data = []
    
    # iterate through each sentence in the file
    for i in sent_tokenize(text):
        temp = []
	    # tokenize the sentence into words
        for j in word_tokenize(i):
            temp.append(j.lower())
            
        data.append(temp)

    # Create CBOW model
    model1 = Word2Vec(
        data,
        min_count=1,
		vector_size=10,
        window=5
        )

    # Create Skip Gram model
    model2 = Word2Vec(
        data,
        min_count=1,
        vector_size=10,
		window=5,
        sg=1
        )
    
    cbow = model1.wv.vectors.tolist()
    skip_gram = model2.wv.vectors.tolist()
    
    count= 0
    
    for w in data[0]:
        count += 1
        
    total_time = time.time() - start_time
    
    return {
        "description": "Word Embedding is a language modeling technique for mapping words to vectors of real numbers. It represents words or phrases in vector space with several dimensions.",
        "extracted_words": data[0],
        "num_words": count,
        "word2vec": {
            "CBOW": {
                "data": cbow,
                "length": len(cbow)
                },
            "Skip-Gram": {
                "data": skip_gram,
                "length": len(skip_gram)
                },
        },
        "response_time": total_time,
    }


