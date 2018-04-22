# brand_embedding

The repo maps the similarity or closeness between different commercial brands. It builds a `brand embedding` which can 
be queried to find the most similar or the least distant instances representing similar brands.

### Methodology ###

* `version 1`: It is a simple technique which takes the mean of the `Glove` word embedding for each word present on the 
landing page of the brand in `Wikipedia`. The idea is that similar brands talk about overlapping concepts. Working
with word embeddings frees us from worrying about the exact match in jargon or vocab.

### How to build the brand embeddings? ### 

Use the `build` function in `brand_similarity/build_emb.py` scrip to query `Wikipedia` iteratively and generate the 
brand embeddings for the set of brands passed as an argument via `set_brands`. 
The default set of brands are as listed in `brand_similarity/data/brand_list` which is loaded as part of the module 
`__init__`.

### How to query the brand embeddings? ### 

Use the `query` or the `query_list` function in `brand_similarity/query_emb.py` to get most similar brands to a 
particular brand or get the same for a list of brands. The `top_n` parameter can be set to only return the closes `n` 
brands.