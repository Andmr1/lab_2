import os


counter = 0


def fnd(cls: str) -> str:
    path = "C:/Users/Андрей/PycharmProjects/pythonProject8/dataset/" + cls + "/" + str(counter).zfill(4) + ".txt"
    if os.path.isfile(path) and path.endswith('.txt'):
        return path
    else:
        return None


if __name__ == '__main__':
    for i in range(851):
        string = fnd("good")
        counter += 1
        print(string)
