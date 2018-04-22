import fire
import operator
import numpy as np
import json
import codecs

from brand_embedding import logger, DEFAULT_BRAND_EMB_SAVE_FPATH


__author__ = "roopal_garg"


def query(target_brand_name, top_n=None, kb_fpath=DEFAULT_BRAND_EMB_SAVE_FPATH, dict_kb=None):

    if dict_kb is None:
        with codecs.open(kb_fpath, encoding='utf-8') as fp:
            dict_kb = json.load(fp)

    target_brand_emb = np.array(dict_kb[target_brand_name])

    dict_brand_name_emb_distance = dict()
    for candidate_brand_name, candidate_emb in dict_kb.iteritems():

        if candidate_brand_name == target_brand_emb:
            continue

        emb_dist = np.linalg.norm(target_brand_emb - np.array(candidate_emb))
        dict_brand_name_emb_distance[candidate_brand_name] = emb_dist

    sorted_dict = sorted(dict_brand_name_emb_distance.items(), key=operator.itemgetter(1))

    if top_n:
        sorted_dict = sorted_dict[: top_n]

    return sorted_dict


def query_list(list_target_brand_name, top_n=None, kb_fpath=DEFAULT_BRAND_EMB_SAVE_FPATH):

    with codecs.open(kb_fpath, encoding='utf-8') as fp:
        dict_kb = json.load(fp)

    for idx, target_brand_name in enumerate(list_target_brand_name, start=1):
        sorted_dict_candidate_brands = query(target_brand_name, top_n=top_n, dict_kb=dict_kb)

        logger.info("{}: {}".format(target_brand_name, sorted_dict_candidate_brands))


if __name__ == '__main__':

    fire.Fire()
