def mergeOverlappingIntervals(intervals)->list[list]:
    sortedIntervals=sorted(intervals,key=lambda x:x[0])
    
    mergedIntervals=[]
    currentInterval=sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _,currentIntervalEnd=currentInterval #unpacking the array
        nextIntervalStart, nextIntervalEnd=nextInterval
        if(currentIntervalEnd>=nextIntervalStart):
            currentIntervalEnd=max(currentIntervalEnd,nextIntervalEnd)
        else:
            currentInterval=nextInterval
            mergedIntervals.append(currentInterval)
    return mergedIntervals

if __name__=="__main__":
    noOfValues=int(input("Enter the number of values under consideration"))
    intervals=[]
    for i in range(noOfValues):
        inputList=[]
        for j in range(2):
            dummy=int(input(f"Enter {j}th value of {i+1}th element in the list"))
            inputList.append(dummy)
        intervals.append(inputList)
    print(intervals)
    result=mergeOverlappingIntervals(intervals)
    print(result)