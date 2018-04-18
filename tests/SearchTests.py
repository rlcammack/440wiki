import unittest
import StageASearch


class Tester:
    tots = 0
    title = ""

    def __init__(self, tots, title):
        self.tots = tots
        self.title = title


class MyTestCase(unittest.TestCase):
    def test_search_creation(self):
        test1 = StageASearch.Search(1, [1, 2, 3])
        self.assertEqual([1, 2, 3], test1.search_area)

    def test_search_clear(self):
        test1 = StageASearch.Search(1, [1, 2, 3])
        test1.simple_search(1)
        test1.clear()
        self.assertEqual([], test1.matches)

    def test_simple_search(self):
        test1 = StageASearch.Search(1, [1, 2, 3])
        test2 = StageASearch.Search(1, [1, 2, 3])

        test1.simple_search(1)
        test2.simple_search(1)

        self.assertEqual(test2.matches, test1.matches)

    def test_attr_search(self):
        a = Tester(5, 'bob')
        b = Tester(6, 'ethan')
        c = Tester(7, 'steve')

        test1 = StageASearch.Search(7, [a, b, c])
        test1.attr_search(7, 'tots')

        self.assertEqual('steve', test1.matches[0].title)

    def test_range_search(self):
        test1 = StageASearch.Search(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        test2 = StageASearch.Search(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        test1.range_search(4, 7)
        test2.range_search(4, 7, True)

        self.assertEqual([5, 6], test1.matches)
        self.assertEqual([4, 5, 6, 7], test2.matches)


if __name__ == '__main__':
    unittest.main()
