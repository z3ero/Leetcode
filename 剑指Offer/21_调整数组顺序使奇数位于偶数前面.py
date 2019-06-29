class Solution:
    # 思路1: 冒泡排序的思路，前偶后奇交换，O(n**2)
    # 思路2: 插入排序的思路
    #       使用两个指针，a 指针指向下一个奇数要插入的位置，b指针用来遍历数组
    #       每次找到一个奇数，则将[a,b] 统一向后移动一位，复杂度也是 O(n**2)
    def reOrderArray_2(self, array):
        p1 = 0
        p2 = 0
        length = len(array)
        # 找到第一个偶数(即奇数要插入的位置)
        while p1<length and array[p1] & 1:
            p1 += 1
        p2 = p1
        while p2<length:
            # 找到第一个奇数
            while p2<length and not array[p2] & 1:
                p2 += 1
            if p2 < length:   # 插入第一个奇数，并将[p1:p2]元素后移
                tmp = array[p2]
                array[p1+1:p2+1] = array[p1:p2]
                array[p1] = tmp
                p1 += 1    
        return array

    # 思路3: 使用额外空间
    # 时间复杂度 O(n)，空间复杂度O(n)
    def reOrderArray_3(self, array):
        eve_arr = filter(lambda x: not x & 1, array) #偶数
        odd_arr = filter(lambda x: x & 1, array) #奇数
        return odd_arr + eve_arr

sol = Solution()
print(sol.reOrderArray_2([1,2,3,4,5,6,7,8]))
