#Auther Nikhil Hegde


from DataUtility import CreateDataUtility
from InsertionSort import InsertionSort
from MergeSort import MergeSort
from QuickSort import QuickSort
from ModifiedQuickSort import ModifiedQuickSort
import timeit
import csv
import sys

#Helps find the run time sort method of a instatiation of a sorting implementatiom
def recordTime(sortObject,input):
    start_time = timeit.default_timer()
    sortObject.sort(input)
    elapsed = timeit.default_timer() - start_time
    return elapsed*100

#Input Sizes
inputSizes = [100,500,1000,2000,5000,10000,15000,20000]

#Creating objects of sorting implementation and data Creation utility
data = CreateDataUtility()
insertionSort = InsertionSort()
mergeSort = MergeSort()
quickSort = QuickSort()
modifiedQuickSort = ModifiedQuickSort()

#Creating a csv file with results in "Results/" folder
with open('Results/Running-times-Worst-case.csv',mode='w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['Sort Algorithm', 'input Size', 'Time Taken'])
    for inputSize in inputSizes:
        input = data.CreateWorstCaseData(inputSize)
        sys.setrecursionlimit(max(sys.getrecursionlimit(), len(input) + 50000))
        insertionSortInput = []
        insertionSortInput.extend(input)
        mergeSortInput = []
        mergeSortInput.extend(input)
        quickSortInput = []
        quickSortInput.extend(input)
        modifiedQuickSortInput = []
        modifiedQuickSortInput.extend(input)
        print "Sorting data of size {0} using Insertion Sort".format(inputSize)
        writer.writerow(['Insertion Sort', inputSize, recordTime(insertionSort,insertionSortInput)])
        print "Sorting data of size {0} using Merge Sort".format(inputSize)
        writer.writerow(['Merge Sort', inputSize, recordTime(mergeSort,mergeSortInput)])
        print "Sorting data of size {0} using Quick Sort".format(inputSize)
        writer.writerow(['Quick Sort', inputSize, recordTime(quickSort,quickSortInput)])
        print "Sorting data of size {0} using Modified Quick Sort".format(inputSize)
        writer.writerow(['Modified Quick Sort', inputSize, recordTime(modifiedQuickSort,modifiedQuickSortInput)])