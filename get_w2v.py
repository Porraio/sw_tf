import os
import gensim


def read_all_articles(path_name):
    f2 = open("./data/sentences/all_sentences.txt", "w+")
    path_dir = os.listdir(path_name)
    for i in path_dir:
        article_path = os.path.join(path_name, i)
        if os.path.isfile(article_path):
            lines = read_articles(article_path)
            f2.writelines(lines)
    f2.close()

def read_articles(article_path):
    f = open(article_path)
    lines = f.readlines()
    f.close()
    return lines


class MySentences():
    def __init__(self, fname):
        self.fname = fname

    def __iter__(self):
        with open(self.fname, "r") as files:
            for line in files:
                yield line.split()


sentences = MySentences("./data/sentences/all_sentences.txt")
model = gensim.models.Word2Vec(size=200, sg =1, min_count=2)
model.build_vocab(sentences)
model.train(sentences=sentences, total_examples=model.corpus_count, epochs=10)
model.save("./data/word2vec_model/articles_model")
