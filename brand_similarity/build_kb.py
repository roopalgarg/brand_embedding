import wikipedia
import numpy as np
import fire
import json
import codecs

from string import punctuation
from nltk.corpus import stopwords

from brand_similarity import DEFAULT_SET_BRANDS, DEFAULT_KB_SAVE_FPATH, logger
from brand_similarity.embeddings.GloveEmbeddings import GloveEmbeddings

__author__ = "roopal_garg"

SET_IGNORE_WORDS = set(stopwords.words())


def build(fpath_save=DEFAULT_KB_SAVE_FPATH, set_brands=DEFAULT_SET_BRANDS, set_ignore_words=SET_IGNORE_WORDS):

    logger.info("building knowledge base")
    dict_brand_name_emb = dict()

    wrd2emb = GloveEmbeddings.get_dict_word_embedding()

    for brand_name in set_brands:
        wiki_obj = wikipedia.page(brand_name)
        logger.info("{brand_name}: {wiki_url}".format(brand_name=brand_name, wiki_url=wiki_obj.url))
        text = wiki_obj.content

        text_tokens = text.split()
        list_emb = list()
        for token in text_tokens:
            token = token.lower()
            token = token.strip(punctuation)
            if token in set_ignore_words:
                continue

            emb = wrd2emb.get(token, None)
            if emb is not None:
                list_emb.append(emb)

        brand_array = np.array(list_emb)
        brand_emb = brand_array.mean(axis=0)

        dict_brand_name_emb[brand_name] = brand_emb.tolist()

    logger.info("saving knowledge base to: `{}`".format(fpath_save))
    with codecs.open(fpath_save, 'w', encoding='utf-8') as fp:
        json.dump(dict_brand_name_emb, fp, separators=(',', ':'), indent=4)

    logger.info("knowledge base compiled")


if __name__ == '__main__':

    fire.Fire()
