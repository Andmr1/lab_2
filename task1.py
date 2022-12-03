import csv
import os


def create_main_ann(directory: str):
    """
    Функция создания файла-аннотации для изначального датасета. Принимает на вход абсолютный путь к одной из папок
    изначального датасета и, пробегая по всем файлам составляет аннотацию.
    """
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
    create_main_ann("C:/Users/Андрей/PycharmProjects/pythonProject8/dataset/good")
    create_main_ann("C:/Users/Андрей/PycharmProjects/pythonProject8/dataset/bad")
