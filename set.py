if __name__ == '__main__':
    # set - unordered, unindexing
    print(dir(set))
    # only unique.
    set1 = {1123, 1234, 4231}
    set1.add(1)
    # set1.union(45234)
    # set1.update(46189)
    set2 = {1123, 1234, 52352}

    print(f'difference: {set1.difference(set2)}, intersection: {set1.intersection(set2)}')

    set3 = set1.intersection(set2)

    print(f'set1 {set1}, set3 {set3}')
    
    # convert tuple to a list
    set3 = list(set3)
    print(set3, type(set3))