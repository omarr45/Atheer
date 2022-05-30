from TAO_Arabic_Stemmer.tokenization import ArabicTokenizer as arabic_tokenizer
from TAO_Arabic_Stemmer.stemming import LightStemmer as arabic_processing_cog_stemmer


def stem(string, full):

    stems_list = []
    # split given string into words (tokens) using ArabicTokenizer
    for token in arabic_tokenizer.tokenize(string):
        stem_word = arabic_processing_cog_stemmer.stem_token(token, full)
        stems_list.append(stem_word)

    return stems_list


def root(string):

    stems_list = []
    # split given string into words (tokens) using ArabicTokenizer
    for token in arabic_tokenizer.tokenize(string):
        stem_word = arabic_processing_cog_stemmer.get_root(token)
        stems_list.append(stem_word)

    return stems_list
