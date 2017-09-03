#Auther Nikhil Hegde

from DataUtility import CreateDataUtility

#Insertion Sort Implementation
class InsertionSort(object):

    def sort(self,input):
        for index in range(1, len(input)):
            currentvalue = input[index]
            position = index

            while position > 0 and input[position - 1] > currentvalue:
                input[position] = input[position - 1]
                position = position - 1

            input[position] = currentvalue
        return input

if __name__=='__main__':
    input = CreateDataUtility().CreateAverageData(1000)
    print "sorting input of size 1000"
    print input
    InsertionSort().sort(input)
    print input
