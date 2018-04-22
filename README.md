# brand_embedding

The repo maps the similarity or closeness between different commercial brands. It builds a `brand embedding` which can 
be queried to find the most similar or the least distant instances representing similar brands.

### Download Glove Embeddings ###
Download `Glove` word embeddings from [glove.6B.zip](http://nlp.stanford.edu/data/glove.6B.zip) to 
`brand_embedding/data/glove_embeddings`.


### Methodology ###

* `release 1`: It is a simple technique which takes the mean of the `Glove` word embedding for each word present on the 
landing page of the brand in `Wikipedia`. The idea is that similar brands talk about overlapping concepts. Working
with word embeddings frees us from worrying about the exact match in jargon or vocab.

### How to build the brand embeddings? ### 

Use the `build` function in `brand_embedding/build_emb.py` scrip to query `Wikipedia` iteratively and generate the 
brand embeddings for the set of brands passed as an argument via `set_brands`. 
The default set of brands are as listed in `brand_embedding/data/brand_list` which is loaded as part of the module 
`__init__`. The listings in `brand_embedding/data/brand_list` must match the brand name as on `Wikipedia` otherwise 
ambiguous results may arise.

### How to query the brand embeddings? ### 

Use the `query` or the `query_list` function in `brand_embedding/query_emb.py` to get most similar brands to a 
particular brand or get the same for a list of brands. The `top_n` parameter can be set to only return the closes `n` 
brands.


### Examples ### 
* Building the embeddings: 
```
cd brand_embedding
python brand_embedding/build_emb.py build
```

* Querying the embeddings for similarity:
```
cd brand_embedding
python brand_embedding/query_emb.py query --target_brand_name=Toyota --top_n=5

["Toyota", 0.0]
["Honda", 0.5642089940473477]
["Ford Motor Company", 0.5905087678182305]
["General Motors", 0.6618795641050003]
["Suzuki", 0.7336843346403088]
```