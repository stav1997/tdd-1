import unittest
import bubblesort

class bubblesort_test(unittest.TestCase):

    def bubble_sort_test(self):
        arry1 = []

        arry2 = "afasfd"

        arry3 = 132

        arry4 = [1, 2, 3, 4]

        arry5 = [4, 3, 2, 1]

        arry6 = [1]

        arry7 = [5, 5]

        arry8 = [5, 5, 2]

        arry9 = [5,6]

        arry10 = [5, 23, 1, 90, 54, 23, 12, 52]

        expected_result1 = "empty array"
        expected_result2 = -1
        expected_result3 = -1
        expected_result4 = [1, 2, 3, 4]
        expected_result5 = [1, 2, 3, 4]
        expected_result6 = [1]
        expected_result7 = [5, 5]
        expected_result8 = [2, 5, 5]
        expected_result9 = [5, 6]
        expected_result10 = [1, 5, 12, 23, 23, 52, 54, 90]
        expected_result11 = 1
        expected_result12 = 2
        expected_result13 = 3

        actual_result1 = bubblesort.BUBBLESORT.bubble_sort(arry1)
        actual_result2 = bubblesort.BUBBLESORT.bubble_sort(arry2)
        actual_result3 = bubblesort.BUBBLESORT.bubble_sort(arry3)
        actual_result4 = bubblesort.BUBBLESORT.bubble_sort(arry4)
        actual_result5 = bubblesort.BUBBLESORT.bubble_sort(arry5)
        actual_result6 = bubblesort.BUBBLESORT.bubble_sort(arry6)
        actual_result7 = bubblesort.BUBBLESORT.bubble_sort(arry7)
        actual_result8 = bubblesort.BUBBLESORT.bubble_sort(arry8)
        actual_result9 = bubblesort.BUBBLESORT.bubble_sort(arry9)
        actual_result10 = bubblesort.BUBBLESORT.bubble_sort(arry10)
        actual_result11 = len(bubblesort.BUBBLESORT.bubble_sort(arry6))
        actual_result12 = len(bubblesort.BUBBLESORT.bubble_sort(arry7))
        actual_result13 = len(bubblesort.BUBBLESORT.bubble_sort(arry8))


        self.assertEqual(expected_result1, actual_result1)
        self.assertEqual(expected_result2, actual_result2)
        self.assertEqual(expected_result3, actual_result3)
        self.assertEqual(expected_result4, actual_result4)
        self.assertEqual(expected_result5, actual_result5)
        self.assertEqual(expected_result6, actual_result6)
        self.assertEqual(expected_result7, actual_result7)
        self.assertEqual(expected_result8, actual_result8)
        self.assertEqual(expected_result9, actual_result9)
        self.assertEqual(expected_result10, actual_result10)
        self.assertEqual(expected_result11, actual_result11)
        self.assertEqual(expected_result12, actual_result12)
        self.assertEqual(expected_result13, actual_result13)
        if __name__ == '__main__':
            unittest.main()



