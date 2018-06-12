import gensim

model = gensim.models.Word2Vec.load("./data/word2vec_model/articles_model")
startups = model.most_similar("startup")
print(startups)