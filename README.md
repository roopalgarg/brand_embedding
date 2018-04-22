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
This should iterate through the brand list giving out logs as pages are processed from wikipedia
```
04/21/2018 21:35:04:INFO: building knowledge base
04/21/2018 21:35:14:INFO: Manchester United: https://en.wikipedia.org/wiki/Manchester_United_F.C.
04/21/2018 21:35:15:INFO: Honda: https://en.wikipedia.org/wiki/Honda
04/21/2018 21:35:16:INFO: Los Angeles Lakers: https://en.wikipedia.org/wiki/Los_Angeles_Lakers
04/21/2018 21:35:18:INFO: Gap Inc.: https://en.wikipedia.org/wiki/Gap_Inc.
04/21/2018 21:35:19:INFO: Ford Motor Company: https://en.wikipedia.org/wiki/Ford_Motor_Company
```
and towards the end:

```
04/21/2018 21:36:05:INFO: saving knowledge base to: `/home/bluefire/workspace/projects/brand_embedding/brand_embedding/data/brand_emb.json`
04/21/2018 21:36:05:INFO: knowledge base compiled
```

The embeddings would be saved to the `fpath_save` path in the `build` function.

* Querying the embeddings for similarity:
```
cd brand_embedding

python brand_embedding/query_emb.py query --target_brand_name=Toyota --top_n=5

["Honda", 0.5642089940473477]
["Ford Motor Company", 0.5905087678182305]
["General Motors", 0.6618795641050003]
["Suzuki", 0.7336843346403088]
["Chevrolet", 0.8425528515308258]
```

```
cd brand_embedding

python brand_embedding/query_emb.py query_list --list_target_brand_name='["Liverpool F.C.", "Google"]' --top_n=5

Liverpool F.C.: [(u'Chelsea F.C.', 0.3479228805034268), (u'Manchester United', 0.37073191660239563), (u'Arsenal F.C.', 0.41666102106971), (u'Cincinnati Bengals', 1.1081518545348459), (u'Los Angeles Rams', 1.171184292207359)]
Google: [(u'Facebook', 0.563797545845138), (u'Amazon Inc', 0.634932045374182), (u'Apple Inc', 0.6743377279657304), (u'Gap Inc.', 1.0265872931260083), (u'Nestle', 1.0296603447159702)]

```