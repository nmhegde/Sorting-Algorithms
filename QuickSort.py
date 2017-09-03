#Auther Nikhil Hegde


import sys
from DataUtility import CreateDataUtility

#In Place Quick Sort Implementation
class QuickSort(object):
    def sort(self,input):
        #Choosing the first number as the pivot
        self.quickSortHelper(input, 0, len(input) - 1)
        return input

    def quickSortHelper(self, input, first, last):
        if first < last:
            splitpoint = self.partition(input, first, last)
            self.quickSortHelper(input, first, splitpoint - 1)
            self.quickSortHelper(input, splitpoint + 1, last)

    def partition(self, input, first, last):
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
                temp = input[leftMark]
                input[leftMark] = input[rightMark]
                input[rightMark] = temp

        temp = input[first]
        input[first] = input[rightMark]
        input[rightMark] = temp

        return rightMark

if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    print "sorting input of size 1000"
    input = CreateDataUtility().CreateWorstCaseData(10000)
    print input
    QuickSort().sort(input)
    print input