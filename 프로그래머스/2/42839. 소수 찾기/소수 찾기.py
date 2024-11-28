from itertools import permutations

def solution(numbers):
    numbers = [*map(str,numbers)]
    answer = 0
    visit = [False] * len(numbers)
    
    
    nums = set()
    for i in range(1,len(numbers)+1):
        for num in permutations(numbers,i):
            if num[0] != '0':
                nums.add(int(''.join(num)))
    nums = list(nums)
    def isPrime(x):
        if x == 1: return False
        for i in range(2,int(x**0.5)+1):
            if x % i == 0: return False
        return True
    ans = 0
    for n in nums:
        if isPrime(n): ans += 1
        
    
    return ans