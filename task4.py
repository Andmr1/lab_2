import os


counter = 0


def fnd(cls: str) -> str:
    """
    Функция проверяет наличие файла и возвращает путь к нему, в случае, если данный файл существует.
    """
    path = "C:/Users/Андрей/PycharmProjects/pythonProject8/dataset/" + cls + "/" + str(counter).zfill(4) + ".txt"
    if os.path.isfile(path):
        return path
    else:
        return None


if __name__ == '__main__':
    for i in range(851):
        string = fnd("good")
        counter += 1
        print(string)
