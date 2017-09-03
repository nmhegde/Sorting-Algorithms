# Auther Nikhil Hegde
import random

class CreateDataUtility(object):
    #Returns Average Case data
    def CreateAverageCaseData(self,size):
        data = []
        for i in range(0,size-1):
            data.append(random.randint(0,size))
        return data

    #Returns Best Case data
    def CreateBestCaseData(self,size):
        data = []
        for i in range(0,size-1):
            data.append(i)
        return data

    #Returns Worst Case Data
    def CreateWorstCaseData(self,size):
        data = []
        for i in range(size-1,0,-1):
            data.append(i)
        return data

if __name__=='__main__':
    data = CreateDataUtility()
    print "Creating Average case Data"
    input = data.CreateData(1000)
    print input
    print "Creating Best case Data"
    sortedInput = data.CreateBestCaseData(1000)
    print sortedInput
    print "Creating Worst case Data"
    reverseSortedInput = data.CreateWorstCaseData(1000)
    print reverseSortedInput