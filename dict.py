"""
print(dict1['model'])
# KeyError: 'model'

print(dict1.get('model'))
# None
"""

if __name__ == '__main__':
    # dict - unordered, indexing.
    print(dir(dict))

    d = {}
    for i in range(6):
        key = input("Enter a key: ")
        value = input("Enter a value: ")
        d[key] = value

    print(d)  # {'s': 's', '2': 'x', 'x': '1', '1234': '234', 'xzfds': 'asdasd', 'sdf79sdf79': '98asd89asd8'}