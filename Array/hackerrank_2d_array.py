#Problem link : https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def solve(arr):
    max_sum=-63
    for i in range(4):
        for j in range(4):
            sum =arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if sum > max_sum:
                max_sum=sum
    return max_sum

if __name__=='__main__':
    array=[]
    for i in range(6):
        inp =[int(element) for element in  input().split(' ')]
        array.append(inp)
    print(solve(array))
