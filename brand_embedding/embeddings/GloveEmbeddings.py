import numpy as np

from brand_embedding import ENV_EMBEDDING_GLOVE_6B_FPATH

__author__ = "roopal_garg"


class GloveEmbeddings:
    GLOVE_DIR = ENV_EMBEDDING_GLOVE_6B_FPATH
    EMBEDDING_DIM = 200

    @staticmethod
    def get_dict_word_embedding(path=GLOVE_DIR, embedding_dim=EMBEDDING_DIM):
        f = open(path.format(dim=embedding_dim))

        word2emb = dict()
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            word2emb[word] = coefs
        f.close()
        return word2emb


GloveEmbeddings.get_dict_word_embedding()