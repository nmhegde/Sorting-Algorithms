#Auther Nikhil Hegde


from DataUtility import CreateDataUtility

#Merge Sort Implementation
class MergeSort(object):

    def sort(self, input):
        if len(input) > 1:
            mid = len(input) // 2
            leftHalf = input[:mid]
            rightHalf = input[mid:]

            self.sort(leftHalf)
            self.sort(rightHalf)

            i = 0
            j = 0
            k = 0
            while i < len(leftHalf) and j < len(rightHalf):
                if leftHalf[i] < rightHalf[j]:
                    input[k] = leftHalf[i]
                    i = i + 1
                else:
                    input[k] = rightHalf[j]
                    j = j + 1
                k = k + 1

            while i < len(leftHalf):
                input[k] = leftHalf[i]
                i = i + 1
                k = k + 1

            while j < len(rightHalf):
                input[k] = rightHalf[j]
                j = j + 1
                k = k + 1
        return input

if __name__ == '__main__':
    input = CreateDataUtility().CreateWorstCaseData(1000)
    print input
    MergeSort().sort(input)
    print input