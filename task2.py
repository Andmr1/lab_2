import codecs


def d_copy(path_old: str, path_new: str, count_good: int, count_bad: int):
    for i in range(count_good+1):
        f = codecs.open(u'' + path_old + "/good/" + str(i).zfill(4) + ".txt", "r", "utf-8")
        ln = f.read()
        f.close()
        f = codecs.open(u'' + path_new + "/good_" + str(i).zfill(4) + ".txt", 'w', "utf-8")
        f.write(ln)
        f.close()
    for i in range(count_bad+1):
        f = codecs.open(u'' + path_old + "/bad/" + str(i).zfill(4) + ".txt", "r", "utf-8")
        ln = f.read()
        f.close()
        f = codecs.open(u'' + path_new + "/bad_" + str(i).zfill(4) + ".txt", "w", "utf-8")
        f.write(ln)
        f.close()


if __name__ == "__main__":
    d_copy("C:/Users/Андрей/PycharmProjects/pythonProject8/dataset", "C:/Users/Андрей/Desktop/tst", 849, 808)
