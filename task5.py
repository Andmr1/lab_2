import os


class MyIter:
    def __init__(self, cls: str):
        self.mark = cls
        self.path_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if os.path.isfile("dataset/" + self.mark + "/" + str(self.path_num).zfill(4) + ".txt"):
            self.path_num += 1
            return "dataset/" + self.mark + "/" + str(self.path_num-1).zfill(4) + ".txt"
        else:
            print("None")
            raise StopIteration


if __name__ == '__main__':
    s_itr = MyIter("good")
    for pt in s_itr:
        print(pt)
    s_itr1 = MyIter("bad")
    for pt1 in s_itr1:
        print(pt1)
