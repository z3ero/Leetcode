'''
n, m, k = list(map(int, input().strip().split()))
# 思路: a+b 的取值范围 0 ~ m+n, a取值[0,n+1], b取值[0, m+1]
min_count = m+n
for a in range(0, n+1):
    for b in range(0, m+1):
        if (n-a) * (m-b) <= k:
            if min_count > a+b:
                min_count = a+b
print(min_count)
'''
T = int(input().strip())
for i in range(T):
    n = int(input().strip())
    ai_list = []
    bi_list = []
    for j in range(n):
        ai, bi = list(map(int, input().strip().split(' ')))
        ai_list.append(ai)
        bi_list.append(bi)
    # 从前往后遍历
    print("Yes")