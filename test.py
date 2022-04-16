def minJump(arr,n):
 
    # unoptimized and non usable code for all testcases
    i=0
    count=0
    while(i<n):
        jump=arr[i]
        i+=jump
        if(i>=n-1):
            count+=1
            return count
        else:
            count+=1
    return -1



def minJump1(arr,n):
    pass

           

print(minJump1([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9],11))
