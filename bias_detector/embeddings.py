from gensim.downloader import load
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


def load_embeddings():
    """
    Load the GloVe embeddings from Gensim's downloader into memory.
    """
    return load("glove-wiki-gigaword-300")


def get_vector(word, embedding):
    """
    Retrieve the vector for a given word from the embedding.
    :param word: The word for which to retrieve the vector.
    :param embedding: The word embedding model.
    :return:
    """
    word = word.lower()
    if word in embedding:
        return embedding[word]
    lemma = lemmatizer.lemmatize(word)
    if lemma in embedding:
        return embedding[lemma]
    return None
