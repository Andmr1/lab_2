import codecs
import csv
import os
from random import randint


def rand_cpy(path: str, path_new: str):
    name = ""
    new_name = ""
    columns = ("Path1", "Path2", "Class")
    with open("data2.csv", "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(columns)
        for filename in os.listdir(path):
            f = os.path.join(path, filename)
            if os.path.isfile(f) and filename.endswith('.txt'):
                new_name = str(randint(0, 9999)).zfill(4)
                name = f[-12] + f[-11] + f[-10]
                if name == 'bad':
                    cont = (path_new + "/" + new_name, 'dataset3/' + new_name, name)
                    writer.writerow(cont)
                else:
                    name = f[-13] + f[-12] + f[-11] + f[-10]
                    cont = (path_new + "/" + new_name, "dataset3/" + new_name, name)
                    writer.writerow(cont)
                file = codecs.open(u'' + f, "r", "utf-8")
                ln = file.read()
                file.close()
                file = codecs.open(u'' + path_new + "/" + new_name + ".txt", "w", "utf-8")
                file.write(ln)
                file.close()


if __name__ == '__main__':
    rand_cpy("C:/Users/Андрей/PycharmProjects/pythonProject8/dataset/good",
             "C:/Users/Андрей/PycharmProjects/pythonProject8/dataset3")
    rand_cpy("C:/Users/Андрей/PycharmProjects/pythonProject8/dataset/bad",
             "C:/Users/Андрей/PycharmProjects/pythonProject8/dataset3")
