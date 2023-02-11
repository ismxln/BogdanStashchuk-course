if __name__ == '__main__':
    # tuple - ordered, indexing.
    print(dir(tuple))  # ()
    # .count() - count element in tuple, .index() - index element in tuple
    tuple1 = (1, "hello", [1, 2, 3], (4, 5, 6), {'a': 1, 'b': 2})
    tuple2 = (7, 8.5, True, "world", {'c': 3, 'd': 4})

    print(tuple1 + tuple2)