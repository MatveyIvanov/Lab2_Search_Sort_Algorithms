import unittest, copy

import Lab2_Sort_Search_Algorithms as alg


class Test_TestSearch(unittest.TestCase):

    def setUp(self): # Initialisation for tests
        self.lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_binary_search(self):
        self.assertEqual(alg.binary_search(self.lst, 5), 4)

    def test_binary_search_first(self): # Case for searching the first element
        self.assertEqual(alg.binary_search(self.lst, 1), 0)
    
    def test_binary_search_last(self): # Case for searching the last element
        self.assertEqual(alg.binary_search(self.lst, 10), 9)

    def test_binary_search_exception(self): # Case for searching the element that doesn't exist in list
        try:
            alg.binary_search(self.lst, 50)
        except Exception as e:
            self.assertEqual(str(e), 'Value does not exist in the list')

    def test_binary_search_empty_list(self): # Case for searching an element in empty list
        temp_list = []
        try:
            alg.binary_search(temp_list, 2)
        except Exception as e:
            self.assertEqual(str(e), 'List is empty')

    
class Test_TestAlgorithms(unittest.TestCase):

    def setUp(self): # Initialisation for tests
        self.unsorted_lst = [5, 1, 6, 2, 8, 12, 25, 9, 76, 15]
        self.sorted_lst = [1, 2, 5, 6, 8, 9, 12, 15, 25, 76]
        self.unsorted_string = 'Hello world'
        self.sorted_string = 'dehllloorw'

    def test_insertion_sort(self):
        temp_lst = copy.deepcopy(self.unsorted_lst) # Using deepcopy to make a new object and don't create a ling to an existing one
        alg.insertion_sort(temp_lst)
        self.assertListEqual(temp_lst, self.sorted_lst)
    
    def test_insertion_sort_empty_list(self): # Case for sorting an empty list
        temp_list = []
        try:
            alg.insertion_sort(temp_list)
        except Exception as e:
            self.assertEqual(str(e), 'List is empty')

    def test_bogo_sort(self):
        temp_lst = copy.deepcopy(self.unsorted_lst)
        alg.bogo_sort(temp_lst)
        self.assertListEqual(temp_lst, self.sorted_lst)

    def test_bogo_sort_empty_list(self): # Case for sorting an empty list
        temp_list = []
        try:
            alg.bogo_sort(temp_list)
        except Exception as e:
            self.assertEqual(str(e), 'List is empty')

    def test_counting_sort(self):
        self.assertListEqual(list(alg.counting_sort(self.unsorted_string)), list(self.sorted_string))

    def test_counting_sort_empty_list(self): # Case for sorting an empty list
        temp_string = ''
        try:
            alg.counting_sort(temp_string)
        except Exception as e:
            self.assertEqual(str(e), 'String is empty')

    def test_quick_sort(self):
        temp_lst = copy.deepcopy(self.unsorted_lst)
        alg.quick_sort(temp_lst, 0, len(temp_lst) - 1)
        self.assertListEqual(temp_lst, self.sorted_lst)

    def test_quick_sort_empty_list(self): # Case for sorting an empty list
        temp_list = []
        try:
            alg.quick_sort(temp_list, 0, len(temp_list) - 1)
        except Exception as e:
            self.assertEqual(str(e), 'List is empty')


if __name__ == '__main__':
    unittest.main()