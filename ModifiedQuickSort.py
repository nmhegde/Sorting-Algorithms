#Auther Nikhil Hegde


from DataUtility import CreateDataUtility
from InsertionSort import InsertionSort

#Modified QUick Sort implementation
class ModifiedQuickSort(object):

    def sort(self, input):
        self.quickSortHelper(input, 0, len(input) - 1)
        return input

    def quickSortHelper(self, input, first, last):
        if first + 15 <= last:
            splitpoint = self.partition(input, first, last)

            self.quickSortHelper(input, first, splitpoint - 1)
            self.quickSortHelper(input, splitpoint + 1, last)
        else:
            input[first:last] = InsertionSort().sort(input[first:last])

    #Choosing Median
    def median(self, a, i, j, k):
        if a[i] < a[j]:
            return j if a[j] < a[k] else k
        else:
            return i if a[i] < a[k] else k

    def swap(self, input, leftMark, rightMark):
        temp = input[leftMark]
        input[leftMark] = input[rightMark]
        input[rightMark] = temp

    def partition(self, input, first, last):
        pivotindex = self.median(input, first, last, (first + last) / 2)
        input[first], input[pivotindex] = input[pivotindex], input[first]
        pivotvalue = input[first]

        leftMark = first + 1
        rightMark = last

        done = False
        while not done:

            while leftMark <= rightMark and input[leftMark] <= pivotvalue:
                leftMark = leftMark + 1

            while input[rightMark] >= pivotvalue and rightMark >= leftMark:
                rightMark = rightMark - 1

            if rightMark < leftMark:
                done = True
            else:
                self.swap(input,leftMark,rightMark)

        self.swap(input,leftMark,rightMark)
        return rightMark

if __name__ == '__main__':
    input = CreateDataUtility().CreateAverageData(1000)
    print "sorting input of size 1000"
    print input
    output = ModifiedQuickSort().sort(input)
    print output