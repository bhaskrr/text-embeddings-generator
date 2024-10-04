from scipy.sparse import coo_matrix
from core.preprocessor import Preprocessor
from fastapi.routing import APIRouter
from sklearn.feature_extraction.text import TfidfVectorizer

preprocessor = Preprocessor()
vect = TfidfVectorizer()

tfidf_route = APIRouter()

@tfidf_route.get('/{text}')
def tfidf(text: str):
    text = preprocessor.process(text)
    tfidf_matrix = vect.fit_transform([text])
    tfidf_coo = coo_matrix(tfidf_matrix)
    
    shape = tfidf_coo.shape
    data = tfidf_coo.data.tolist()
    rows = tfidf_coo.row.tolist()
    cols = tfidf_coo.col.tolist()
    # print(data, rows, cols)
    
    return {
        "description": "A sparse matrix in COOrdinate format and of type scipy.sparse.coo_matrix. To reconstruct the csr_matrix, import coo_matrix from scipy.sparse and do coo_matrix((data, (rows, cols)), [shape=(shape[0], shape[1]))])",
        "preprocessed_text": text,
        "matrix": {
            "data": data,
            "rows": rows,
            "cols": cols,
            "shape": shape
            }
        }