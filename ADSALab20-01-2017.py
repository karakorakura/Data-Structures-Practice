

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def printarr(arr):
    for passnum in range(0,len(arr)):
            print arr[passnum],


def binarysearch(arr,n):
    beg=0
    end=len(arr)-1
    mid=int((beg+end)/2)
    while((beg<=end)):
       if(n<arr[mid]):
           end = mid-1
           mid=int((beg+end)/2)
       elif n>arr[mid]:
           beg=mid+1
           mid=int((beg+end)/2)
       else :
           return mid

    return -1


def meanarr(arr):
    mean =0
    for passnum in range(0,len(arr)):
            mean = mean + arr[passnum]

    mean /= len(arr)
    return mean



n= int(raw_input('how many numbers in array?'));

#arr = [-1 for x in range(0,n-1,1)]
arr = []
#printarr(arr)
for i in range(0,n,1):
    t= int(raw_input('enter number'))
    arr.append(t)
    #print "its {} ".format(arr[i])

bubbleSort(arr)
printarr(arr)

x = (raw_input('enter search number '))
while(x!='e'):


    nx = int(x)
    print binarysearch(arr,nx)
    x = (raw_input('enter search number e to exit '))

print "mean of array ",
print meanarr(arr)
