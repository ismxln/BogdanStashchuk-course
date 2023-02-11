if __name__ == '__main__':


    class Comment:


        def __init__(self, txt):
            self.text = txt
            self.votes_qty = 0


        def upvote(self):
            self.votes_qty += 1


    comment1 = Comment('First comment')

    # print(comment1.__dict__)  # {'text': 'First comment', 'votes_qty': 0}

    # print(comment1.text)  # First comment

    # print(comment1.votes_qty)  # 0

    # print(dir(comment1))  # namespace for comment1 (the own attributes: text, votes_qty and the rest are: inherited from the class)
    """
    [
        '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__',
        '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
        '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'text', 'upvote', 'votes_qty'
    ]
    """

    class Comment2:
        total_comments = 0

        def __init__(self, text):
            self.text = text
            self.votes_qty = 0
            Comment2.total_comments += 1


        def upvote(self):
            self.votes_qty += 1
        
        
        @staticmethod
        def merge_comments(first, second):
            return f'{first} {second}'
        

        def __add__(self, other):
            return (f'{self.text} {other.text}', self.votes_qty + other.votes_qty)
        

    my_comment = Comment2('My comment0')

    m_1 = Comment2.merge_comments('Ty', 'Yosh')
    print(m_1)  # Ty Yosh

    m_2 = my_comment.merge_comments('Like', 'OK')
    print(m_2)  # Like OK

    print(Comment2.total_comments)  # 1

    com1 = Comment2('First comment')
    com1.upvote()

    com2 = Comment2('Second comment')
    com2.upvote()

    print(com1 + com2)  # ('First comment Second comment', 2)


    class ExtendedList(list):


        def print_list_info(self):
            print(f'List has {len(self)} elements')


    # this class is only for 'print(ExtendedList.__subclasses__())' check
    class MyExtendedList(ExtendedList):
        def print_list_info(self):
            print(f'List has {len(self)} elements')

    custom_list = ExtendedList([1, 2, 3])
    custom_list.print_list_info()  # List has 3 elements

    # object attribute search chain=custom list -> ExtendedList -> list -> object
    print(f'list of self-attributes of object name custom_list: {custom_list.__dict__}')  # {}
    print(f'list of self-attributes of class ExtendedList: {ExtendedList.__dict__}\n')  # {'__module__': '__main__', etc...
    print(f'list of self-attributes of class list: {list.__dict__}\n')  # {'__new__': <built-in method __new__ etc...
    print(f'list of self-attributes of class object: {object.__dict__}')  # {'__new__': <built-in method __new__ etc...

    print('\nlist subclasses: ' + str(list.__subclasses__()) + '\n')  # [<class '__main__.ExtendedList'>]

    print(f'object subclasses: {object.__subclasses__()}\n')  # [<class 'type'>, <class 'async_generator'>, <class 'bytearray_iterator'>, etc...

    print(ExtendedList.__subclasses__())  # [<class '__main__.MyExtendedList'>]
    