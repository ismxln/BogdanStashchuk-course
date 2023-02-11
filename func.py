if __name__ == '__main__':

    print('Hello, World!')

    def merge_lists_to_dict(keys, values):
        """
        Merging lists to dictionary

        Args:
            keys (list): key from list1 to dict look key:value
            values (list): value from list2 to dict look key:value
        """
        d = dict(zip(keys, values))
        print(f'Your new dict: {d}')
    
    merge_lists_to_dict(['a', 'b', 'c'], [1, 2, 3])