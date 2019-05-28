from math import sqrt 
# 质数判断  
def is_prime(n):  
    for i in range(2, int(sqrt(n))+1):  
        if n % i == 0:  
            return False  
    return True  

# 求最大指数因子
def max_prime_factor(num):
    index = 2  
    maxPrime = None
    while index <= num:
        if num % index == 0 and is_prime(index):  
            num /= index 
            maxPrime = index
        index += 1
    return maxPrime

if __name__=="__main__":
    num = 460897024
    print(max_prime_factor(num))