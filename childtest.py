# creating file in child branch

# Mergesort
def mergeSortDivide(num_merge, si, ei):
    if si >= ei:
        return
        
    if si < ei:
        mid = (si +ei)//2
        mergeSortDivide(num_merge, si, mid)
        mergeSortDivide(num_merge, mid+1, ei)
        mergeSortConquer(num_merge, si, mid, ei)


def mergeSortConquer(num_merge, si, mid, ei):
    merged = [0]*(ei-si+1)
    idx1 = si
    idx2 = mid + 1
    x = 0
    while(idx1 <= mid and idx2 <= ei):
        if num_merge[idx1] <= num_merge[idx2]:
            merged[x] = num_merge[idx1]
            x = x + 1
            idx1 = idx1 + 1
        else:
            merged[x] = num_merge[idx2]
            x = x + 1
            idx2 = idx2 + 1

    while(idx1 <= mid):
        merged[x] = num_merge[idx1]
        x = x + 1
        idx1 = idx1 + 1

    while(idx2 <= ei):
        merged[x] = num_merge[idx2]
        x = x + 1
        idx2 = idx2 + 1

    j = si
    for i in range(0, len(merged)):
        num_merge[j] = merged[i]
        j=j+1

if __name__ == '__main__':
    mergeList = []
    n_merge = int(input("Enter the number of elements to be taken in list for merge sort : "))
    for i in range(0, n_merge):
        num = int(input())
        mergeList.append(num)
    mergeSortDivide(mergeList, 0, len(mergeList)-1)
    print(mergeList)

