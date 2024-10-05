# Word Embeddings Generator
A hobby project built to learn Python FastAPI framework. 

# Table of contents

- [Word Embeddings Generator](#word-embeddings-generator)
- [Table of contents](#table-of-contents)
    - [Natural Language Processing](#natural-language-processing)
    - [Vectors and Embeddings](#vectors-and-embeddings)
  - [**API Documentation**](#api-documentation)
    - [Getting Started](#getting-started)
      - [Base URL](#base-url)
      - [Endpoints](#endpoints)

### Natural Language Processing

    Natural language processing (NLP) is a field of computer science and a subfield of artificial intelligence that aims to make computers understand human language. NLP uses computational linguistics, which is the study of how language works, and various models based on statistics, machine learning, and deep learning. These technologies allow computers to analyze and process text or voice data, and to grasp their full meaning, including the speaker’s or writer’s intentions and emotions.

    NLP powers many applications that use language, such as text translation, voice recognition, text summarization, and chatbots. You may have used some of these applications yourself, such as voice-operated GPS systems, digital assistants, speech-to-text software, and customer service bots. NLP also helps businesses improve their efficiency, productivity, and performance by simplifying complex tasks that involve language.

[Click Here](https://www.google.com/search?q=natural+language+processing) to learn more using a pre-filled query.

### Vectors and Embeddings

    Vectors: A vector is a mathematical approach for expressing and organizing data. The vectorization of data, such as word vectorization, is one of the initial phases in the creation of an ML model.

    Embeddings: Word Embeddings are a method of extracting features out of text so that we can input those features into a machine learning model to work with text data. They try to preserve syntactical and semantic information. The methods such as Bag of Words (BOW), CountVectorizer and TFIDF rely on the word count in a sentence but do not save any syntactical or semantic information. In these algorithms, the size of the vector is the number of elements in the vocabulary. We can get a sparse matrix if most of the elements are zero. Large input vectors will mean a huge number of weights which will result in high computation required for training. Word Embeddings give a solution to these problems.

[Click Here](https://www.google.com/search?q=what+are+vectors+in+nlp) to learn more using a pre-filled query.

## **API Documentation**

**Version**: 0.0.1

### Getting Started
  The frontend of the application has not yet been built. To try out the API, use a tool like CURL or POSTMAN.

#### Base URL

```
https://text-embeddings-generator.onrender.com/
```

#### Endpoints

- `/embeddings` - This route serves all the available text embeddings.
  - `/tfidf` - This endpoint takes a string parameter and returns the Term Frequency-Inverse Document Frequency representation in a COOrdinate Matrix format.
    - Example:
      - Request:
  
        ```
          https://text-embeddings-generator.onrender.com/embeddings/tfidf/hello%20world
        ```
      - Response:
        ```python
          {
            "description": "A sparse matrix in COOrdinate format and of type scipy.sparse.coo_matrix. To reconstruct the csr_matrix, import coo_matrix from scipy.sparse and do coo_matrix((data, (rows, cols)), [shape=(shape[0], shape[1]))])",
            "preprocessed_text": "hello world",
            "matrix": {
                "data": [
                    0.7071067811865475,
                    0.7071067811865475
                    ],
                "rows": [
                    0,0
                    ],
                "cols": [
                    0,1
                    ],
                "shape": [
                    1,2
                    ]
                }
            }
        ```
  - `/word2vec` - This endpoint takes a string parameter and returns the Continuous-Bag-of-Words(CBOW) and Skip-Gram representations of WordToVec.
    - Example:
      - Request:

        ```
          https://text-embeddings-generator.onrender.com/embeddings/word2vec/hello%20world
        ```

      - Response:

        ```python
            {
              "description": "Word Embedding is a language modeling technique for mapping words to vectors of real numbers. It represents words or phrases in vector space with several dimensions.",
              "extracted_words": [
                "hello",
                "world"
              ],
              "num_words": 2,
              "word2vec": {
                "CBOW": {
                  "data": [
                    [
                      -0.005362272262573242,
                      0.0023643136955797672,
                      0.05103349685668945,
                      0.090092733502388,
                      -0.09302949905395508,
                      -0.07116808742284775,
                      0.06458872556686401,
                      0.08972988277673721,
                      -0.05015427991747856,
                      -0.03763371706008911
                    ],
                    [
                      0.07380504906177521,
                      -0.015334713272750378,
                      -0.04536613076925278,
                      0.06554051488637924,
                      -0.048601604998111725,
                      -0.018160175532102585,
                      0.02876579761505127,
                      0.009918737225234509,
                      -0.08285214751958847,
                      -0.09448818117380142
                    ]
                  ],
                  "length": 2
                },
                "Skip-Gram": {
                  "data": [
                    [
                      -0.005362272262573242,
                      0.0023643136955797672,
                      0.05103349685668945,
                      0.090092733502388,
                      -0.09302949905395508,
                      -0.07116808742284775,
                      0.06458872556686401,
                      0.08972988277673721,
                      -0.05015427991747856,
                      -0.03763371706008911
                    ],
                    [
                      0.07380504906177521,
                      -0.015334713272750378,
                      -0.04536613076925278,
                      0.06554051488637924,
                      -0.048601604998111725,
                      -0.018160175532102585,
                      0.02876579761505127,
                      0.009918737225234509,
                      -0.08285214751958847,
                      -0.09448818117380142
                    ]
                  ],
                  "length": 2
                }
              },
              "response_time": 0.009032011032104492
            }
        ```
    - Example with CURL:
      ```
        curl -X 'GET' \
        'https://text-embeddings-generator.onrender.com/embeddings/word2vec/hello%20world' \
        -H 'accept: application/json'
      ```

If you are a stranger to these api testing tools, then you can make use of the swagger UI by visiting the `/docs` endpoint.

For any query, ping me on [Linkedin](https://www.linkedin.com/in/bhaskar-bordoloi-0a7473210) 
