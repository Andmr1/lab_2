import codecs
import csv
import os


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


def ann(directory: str):
    name = ""
    columns = ("Path1", "Path2", "Class")
    with open("data1.csv", "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(columns)
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f) and filename.endswith('.txt'):
                name = f[-12] + f[-11] + f[-10]
                if name == 'bad':
                    cont = (f, 'dataset1/' + name + '_' + f[-8] + f[-7] + f[-6] + f[-5], name)
                    writer.writerow(cont)
                else:
                    name = f[-13] + f[-12] + f[-11] + f[-10]
                    cont = (f, "dataset1/" + name + '_' + f[-8] + f[-7] + f[-6] + f[-5], name)
                    writer.writerow(cont)


if __name__ == "__main__":
    d_copy("C:/Users/Андрей/PycharmProjects/pythonProject8/dataset",
           "C:/Users/Андрей/PycharmProjects/pythonProject8/dataset1", 849, 808)
    ann("C:/Users/Андрей/PycharmProjects/pythonProject8/dataset")
