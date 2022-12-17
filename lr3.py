import re

import pandas as pd
import codecs
from task5 import MyIter
import nltk
import matplotlib
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from pymorphy2 import MorphAnalyzer
from nltk.corpus import stopwords
from pymystem3 import Mystem


def create_hist(df: pd, mark: str):
    df_n = filter_by_mark(df, mark)
    lemmatizer = Mystem()
    text = df_n["rev_text"]
    text = list(text)
    for sent in text:
        sent_lemmas = lemmatizer.lemmatize(sent)
        print(sent_lemmas)




def filter_by_mark(df: pd, mark: str) -> pd:
    return df[df["rev_type"] == mark]


def filter_by_number(df: pd, w_num: int) -> pd:
    return df[df["word_num"] <= w_num]


def read_all_data() -> pd:
    rev_types = []
    rev_text = []
    word_num = []
    it_good = MyIter("good")
    it_bad = MyIter("bad")
    for data in it_good:
        rev_types.append("good")
        f = codecs.open(u'' + data, "r", "utf-8")
        txt = f.read()
        word_num.append(len(txt.split()))
        rev_text.append(txt)
        f.close()
    for data in it_bad:
        rev_types.append("bad")
        f = codecs.open(u'' + data, "r", "utf-8")
        txt = f.read()
        word_num.append(len(txt.split()))
        rev_text.append(txt)
        f.close()
    dt = pd.DataFrame(
        {
            "rev_type": rev_types,
            "rev_text": rev_text,
            "word_num": word_num
        }
    )
    return dt


if __name__ == '__main__':
   data1 = read_all_data()
   print(data1)
   print(data1.isnull().sum())
   data_good = filter_by_mark(data1, "good")
   data_bad = filter_by_mark(data1, "bad")
   good_max = data_good["word_num"].max()
   good_min = data_good["word_num"].min()
   good_avg = data_good["word_num"].mean()
   bad_max = data_bad["word_num"].max()
   bad_min = data_bad["word_num"].min()
   bad_avg = data_bad["word_num"].mean()
   print(data_good)
   print("maximum:", good_max)
   print("minimum:", good_min)
   print("average:", good_avg)
   print(data_bad)
   print("maximum:", bad_max)
   print("minimum:", bad_min)
   print("average:", bad_avg)
   create_hist(data1, "good")
