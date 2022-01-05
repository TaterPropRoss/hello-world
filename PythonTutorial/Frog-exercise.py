#Frog exercise

# given an array representing a skyline of blocks, 
# what is the largest attainable distance if you're 
# only allowed to travel upwards?

class Solution():
    #find the distances between the peaks
    
    def islegal (start,end):
        if end >= start:
            return True

    def greatestlegaldistancefromlowest(anarray):
        startval = min(anarray)
        startpoint = anarray.index(startval)
        arrayRight = anarray[startpoint:]
        arrayLeft = anarray[:startpoint+1]
        arrayLeft.reverse()

        
        pass



print(Solution.greatestlegaldistancefromlowest([2,7,6,5,4,3]))