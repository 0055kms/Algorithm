def solution(arr1, arr2):
    answer = [[]]
    # arr1 : 행3 열2  arr2 : 행2 열2  new : 행2 열2
    """
    1 4   3 3 3        
    3 2   3 3 4
    4 1 
    
    x행 y열의 값 = arr1[x][c] 값들 넣고 arr2[c][y] 값들 넣고 더함
    """
    x_len = len(arr1)
    y_len = len(arr2[0])
    common = len(arr2) # == len(arr[0])
    new = [[0] * y_len for _ in range(x_len)]
    for x in range(x_len):
        for y in range(y_len):
            val = 0
            for c in range(common):
                val += (arr1[x][c] * arr2[c][y])
            new[x][y] = val
    return new