if __name__ == '__main__':
    # list - ordered, indexing.
    print(dir(list))  # or print(dir([]))
    # 1.
    

    elements = ['str', 123, True, [], {}, 10.5]

    del elements[2]  # delete third element
    print(len(elements))  # print length of list
    print(elements[::-1])

    list2 = ['a', 12]

    elements.extend(list2)

    print(elements)
    # 2.
    list1, list3 = [1,2,'3'], [3,2,'1']
    list1 += list3
    print(list1.__add__(list3))
    print(list1)
