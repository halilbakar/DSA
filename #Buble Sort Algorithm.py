#Buble Sort Algorithm
def swap(array,index1,index2):
    a=array[index1]
    b=array[index2]
    array[index1]=b
    array[index2]=a
    if a>b:
        swapped=1
    else:
        swapped=0
    return array,swapped

    
    return
def bublesort(arr):
    
    
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            swap(arr,i-1,i)
            


        
    return arr
print(bublesort(eval(input())))

