if __name__ == '__main__':
    # 1
    print('\t\t1')
    n = 5
    squares = (num * num for num in range(n))
    print(squares)
    for num in squares:
        print(num)
    
    # 2
    print('\t\t2')
    from sys import getsizeof
    squares_gen = (num * num for num in range(10000))
    print(getsizeof(squares_gen), type(squares_gen))

    squares_list = [num * num for num in range(10000)]
    print(getsizeof(squares_list), type(squares_list))