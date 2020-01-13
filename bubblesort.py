class BUBBLESORT:

    def bubble_sort(arr):

        if type(arr) != type([]):
            return -1
        length = len(arr)
        if length == 0:
            return "empty array"
        for i in range(length):
            for j in range(0, length-i-1):
                if arr[j] > arr[j+1]:
                    tmp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = tmp

        return arr
