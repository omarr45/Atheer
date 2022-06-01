from .stemming import LightStemmer


def tokenize(text):
    # strip removes leading and trailing whitespace
    return text.strip().split()


def text2stem(text, full):

    stems_list = []

    for token in tokenize(text):
        stem_word = LightStemmer.get_stem(token, full)
        stems_list.append(stem_word)

    return stems_list


def text2root(text):

    stems_list = []

    for token in tokenize(text):
        stem_word = LightStemmer.get_root(token)
        stems_list.append(stem_word)

    return stems_list
