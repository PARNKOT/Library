# Алгоритм КМП (Кнута-Морриса-Пратта)
# Поиск образа в строке

import typing


class FindString:
    def __init__(self, string: str):
        self.__string = string
        self.__pi_array = self.calculate_pi_array(string)

    @staticmethod
    def calculate_pi_array(string) -> list:
        j, i = 0, 1
        pi_array = [0]*len(string)

        while i < len(string):
            if string[j] == string[i]:
                pi_array[i] = j + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    pi_array[i] = 0
                    i += 1
                else:
                    j = pi_array[j-1]

        return pi_array

    def __len__(self):
        return len(self.__string)

    def __getitem__(self, item):
        return self.__string[item]

    @property
    def value(self):
        return self.__string

    @value.setter
    def value(self, value):
        self.__string = value
        self.__pi_array = self.calculate_pi_array(value)

    @property
    def pi_array(self):
        return self.__pi_array


def kmp(src: str, to_find: typing.Union[str, FindString]):
    n, m = len(src), len(to_find)
    i, j = 0, 0

    if isinstance(to_find, str):
        pi_array = FindString.calculate_pi_array(to_find)
    else:
        pi_array = to_find.pi_array

    while i < n:
        if src[i] == to_find[j]:
            i += 1
            j += 1
            if j == m:
                return True, i - m, i
        else:
            if j > 0:
                j = pi_array[j-1]
            else:
                i += 1

    return False, -1


if __name__ == "__main__":
    fs = FindString("лилила")
    src = "лилилось лилилась"

    res = kmp(src, fs)
    if res[0]:
        print(f"Found: start = {res[1]}, end = {res[2]}")
        print(src[res[1]:res[2]])
    else:
        print("Not found")

