import unittest
from random import randint
from sorting_algorithm import shell_sort


class ShellSortTesting(unittest.TestCase):
    """A class that implements ShellSort sorting algorithm testing"""
    def test_sorting_empty_array(self) -> None:
        """A method to test empty array sorting"""
        array = []
        self.assertEqual(shell_sort(array), [])

    def test_sorting_int_filled_array(self) -> None:
        """A method to test sorting ints filled array"""
        for i in range(10):
            array = [randint(0, 100) for _ in range(100)]
            self.assertEqual(shell_sort(array), sorted(array))


if __name__ == "__main__":
    unittest.main()
