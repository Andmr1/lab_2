import pandas as pd
import codecs
import os
from task5 import MyIter


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
