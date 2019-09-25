n, m = list(map(int, input().strip().split(' ')))
mima = [0]*n
lr_list = []
for i in range(1, m+1):
    l, r = list(map(int, input().strip().split(' ')))
    lr_list.append([l,r])
    
# 开始
already_set = set()
while len(lr_list)>0:
    l, r = lr_list.pop()
    index_set = set(range(l,r+1)) - already_set
    for j in index_set:
        mima[j] = m
    already_set |= index_set
    m -= 1

# 计算这个数111
res = 0
for k in range(n):
    res += k*mima[k]
print(res%100000009)