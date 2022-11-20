import csv
import os


def ann(directory: str):
    name = ""
    columns = ("Path1", "Path2", "Class")
    with open("data.csv", "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(columns)
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f) and filename.endswith('.txt'):
                name = f[-12] + f[-11] + f[-10]
                if name == 'bad':
                    cont = (f, 'dataset/' + name + '/' + f[-8] + f[-7] + f[-6] + f[-5], name)
                    writer.writerow(cont)
                else:
                    name = f[-13] + f[-12] + f[-11] + f[-10]
                    cont = (f, "dataset/" + name + '/' + f[-8] + f[-7] + f[-6] + f[-5], name)
                    writer.writerow(cont)


if __name__ == "__main__":
    ann("C:/Users/Андрей/PycharmProjects/pythonProject8/dataset/good")
    ann("C:/Users/Андрей/PycharmProjects/pythonProject8/dataset/bad")
