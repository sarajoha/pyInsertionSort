def Insert(array, rightIndex, value):
#    rInd = int(rightIndex)
#   val = int(value)
    
    for i in range(rightIndex, -1, -1):      
        if i>= 0 and value < array[i]:
            array[i+1] = array[i]
        else:
            array[i+1] = value
            break    
    #print array
    
def InsertionSort(array):

    for j in range(1, len(array)):
        Insert(array, j-1, array[j])
    print array

array = [1,4,25,10,14,5,3]

InsertionSort(array)
