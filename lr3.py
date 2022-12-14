import pandas as pd
import codecs
from task5 import MyIter
import matplotlib
import matplotlib.pyplot as plt
from pymystem3 import Mystem
import numpy as np


def create_hist(mark: str) -> plt:
    '''
     Функция считывает использование слов в обзорах и возвращает столбичную диаграмму
    '''
    keys = []
    vals = []
    if mark == "good":
        fl = codecs.open("new1.txt", "r", "utf-8")
        for i in fl.readlines():
            key, val = i.strip().split(":")
            val = int(val)
            if val > 800:
                keys.append(key)
                vals.append(val)
    else:
        fl = codecs.open("new2.txt", "r", "utf-8")
        for i in fl.readlines():
            key, val = i.strip().split(":")
            keys.append(key)
            vals.append(val)
    position = np.arange(len(vals))
    fig, ax = plt.subplots()
    ax.bar(position, vals)
    ax.set_xticks(position)
    ax.set_xticklabels(keys)
    fig.set_figwidth(1000)
    fig.set_figheight(1000)
    return fig


def lemmatize_and_count(df: pd, mark: str, ing: str):
    '''
    Функция производит токенизацию и лемматизацию обзоров из датафрейма по заданной метке и записывает полученную
    информацию в файл
    '''
    words = {}
    df_n = filter_by_mark(df, mark)
    lemmatizer = Mystem()
    text = df_n["rev_text"]
    text = list(text)
    for sent in text:
        sent_lemmas = lemmatizer.lemmatize(sent)
        print(sent_lemmas)
        for word in sent_lemmas:
            if word not in words and (len(word) >= 3 or word == "я"):
                words[word] = 1
            if word in words:
                words[word] += 1
        print(words)
    f = codecs.open(u'' + "new" + ing + ".txt", "a", "utf-8")
    for word in words:
        f.write(word + ": " + str(words[word] + "\n"))
    f.close()


def filter_by_mark(df: pd, mark: str) -> pd:
    return df[df["rev_type"] == mark]


def filter_by_number(df: pd, w_num: int) -> pd:
    return df[df["word_num"] <= w_num]


def read_all_data() -> pd:
    '''
    С использованием класса итератора из предыдущей работы записывает обзоры в датафрейм.
    '''
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
   m = 0
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
   fig = create_hist(data_good, "good")
   plt.show()
