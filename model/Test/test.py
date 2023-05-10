from operator import itemgetter


if __name__ == '__main__':
    l = [{"x": 1}, {"x": 100}]
    print(l)

    l = sorted(l, key=itemgetter("x"))
    print(l)