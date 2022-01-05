'''
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7 
P = 2, difference = |4 − 9| = 5 
P = 3, difference = |6 − 7| = 1 
P = 4, difference = |10 − 3| = 7 
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
'''

def solution(A):

    def finddiff(anArray,anSplit):
        firsthalf = anArray[:anSplit]
        secondhalf = anArray[anSplit:]
        if len(firsthalf) == 0 or len(secondhalf) == 0:
            return 10000000000000000000
        else:
            difference = abs(sum(secondhalf)-sum(firsthalf))
            #print('E'+str(secondhalf) + ' - E'+str(firsthalf) +  '='+str(difference))
            return difference


    splitpoint = int(len(A)/2)
    if len(A) <= 2:
       diff = finddiff(A,1)
    else:
        
        backdiff    = finddiff(A,splitpoint-1)
        diff        = finddiff(A,splitpoint)
        frontdiff   = finddiff(A,splitpoint+1)

        testpoint = splitpoint
        if frontdiff < diff:
            # move splitpoint up as long as the difference decreases
            while diff < olddiff:
                olddiff = diff
                testpoint +=1
                newdiff = finddiff(A,testpoint)
                if newdiff < diff:
                    diff = newdiff
                    splitpoint = testpoint
        else:
            olddiff = diff+1
            while diff < olddiff:
                olddiff = diff
                testpoint -=1
                newdiff = finddiff(A,testpoint)
                if newdiff < diff:
                    diff = newdiff
                    splitpoint = testpoint

    return diff


print(solution([3,1,2,4,3]))
print(solution([-1000,1000]))
print(solution([1000,1000]))
print(solution([1000,-1000]))
print(solution([1,1,3]))
print(solution([-10, -20, -30, -40, 100]))
print(solution([-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1,-1,0,1]))







