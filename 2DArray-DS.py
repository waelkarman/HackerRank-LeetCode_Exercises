
def hourglassSum(arr):
    # Write your code here
    
    max_sum=arr[0][0]+arr[0][1]+arr[0][2]+arr[1][1]+arr[2][0]+arr[2][1]+arr[2][2]
    print(max_sum)
    for i in range(4):
        for j in range(4):
            sum_h = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if sum_h > max_sum :
                max_sum = sum_h

    return max_sum


