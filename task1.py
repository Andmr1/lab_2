import csv


def annotation(path: str, count_good: int, count_bad: int):
    columns = ("Path1", "Path2", "Class")
    with open("data.csv", "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(columns)
        for i in range(count_good + 1):
            cont = (path + "/good" + str(i).zfill(4) + ".txt", "dataset/good" + str(i).zfill(4) + ".txt", "good")
            writer.writerow(cont)
        for i in range(count_bad + 1):
            cont = (path + "/bad" + str(i).zfill(4) + ".txt", "dataset/bad" + str(i).zfill(4) + ".txt", "bad")
            writer.writerow(cont)


if __name__ == "__main__":
    annotation("C:/Users/Андрей/PycharmProjects/pythonProject8/dataset", 849, 849)