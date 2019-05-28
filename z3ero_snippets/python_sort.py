# Several common sorting algorithms: ascending
# 1. Bubble Sort
def bubble_sort(nums):
    nums_len = len(nums)
    for i in range(0, nums_len):
        for j in range(0, nums_len-i-1):
            if nums[j+1] < nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums 
# 2. Selection Sort
def selection_sort(nums):
    nums_len = len(nums)
    for i in range(0, nums_len):
        min_index = i
        for j in range(i+1, nums_len):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
# 3. Insertion Sort
def insertion_sort(nums):
    nums_len = len(nums)
    for i in range(1, nums_len):
        value = nums[i]
        insert_index = i-1
        while insert_index >= 0 and nums[insert_index] > value:
            nums[insert_index + 1] = nums[insert_index]
            insert_index -= 1
        nums[insert_index+1] = value
    return nums
# 4. Insert Sort
def shell_sort(nums):
    nums_len = len(nums)
    gap = nums_len // 2
    while gap > 0:
        for i in range(gap, nums_len):
            value = nums[i]
            insert_index = i-gap
            while insert_index >= 0 and nums[insert_index] > value:
                nums[insert_index + gap] = nums[insert_index]
                insert_index -= gap
            nums[insert_index + gap] = value
        gap = gap // 2
    return  nums
# 5. Merge Sort
def merge_sort(nums):
    def sort(arr, l, r):
        if r-l<=1:
            return
        mid = (l+r)//2
        sort(arr, l, mid)
        sort(arr, mid, r)
        merge(arr, l, mid, r)
    def merge(arr, l, mid, r):
        tmp_arr = [0]*(r-l)
        p1, p2 = l, mid
        # compare two arr, select smaller one to fill temporary array
        index = 0
        while p1 < mid and p2 < r:
            if arr[p1]<=arr[p2]:
                tmp_arr[index]=arr[p1]
                p1+=1
            else:
                tmp_arr[index]=arr[p2]
                p2+=1
            index+=1
        while p1 < mid:
            tmp_arr[index] = arr[p1]
            p1+=1; index+=1
        while p2 < r:
            tmp_arr[index] = arr[p2]
            p2+=1; index+=1
        # copy tmp_arr to arr
        arr[l:r] = tmp_arr
    sort(nums, 0, len(nums))
    return nums
# 6. Quick Sort
def qucik_sort(nums):
    def q_sort(arr, l, r):
        if l>=r: return
        pos = partition(arr, l, r)
        q_sort(arr, l, pos-1)
        q_sort(arr, pos+1, r)
    def partition(arr, l, r):
        pos = l; l+=1
        while l<=r:
            while l<=r and arr[r]>=arr[pos]: # find the first num on the right less than value
                r-=1
            if l<=r:
                arr[pos], arr[r] = arr[r], arr[pos]
                pos = r 
                r-=1
            while l<=r and arr[l] <= arr[pos]: # find the first num on the left more than value
                l+=1
            if l<=r:
                arr[pos], arr[l] = arr[l], arr[pos]
                pos = l
                l+=1
        return pos
    q_sort(nums, 0, len(nums)-1)
    return nums
# 7. Heap Sort
def heap_sort(nums):
    def build_max_heap(nums):
        # 从最后一个非叶子节点开始向上构造最大堆
        nums_len = len(nums)
        for i in range(nums_len//2, -1, -1):
            adjust_heap(nums, i)
    def adjust_heap(nums, i):
        max_index = i
        # 如果有左子树
        if i*2<nums_len and nums[i*2] > nums[max_index]:
            max_index = i*2
        # 如果有右子树
        if i*2+1<nums_len and nums[i*2+1] > nums[max_index]:
            max_index = i*2 + 1
        # 如果父节点不是最大值，则将父节点和最大值交换，并且递归调整与父节点交换的位置
        if max_index != i:
            nums[max_index], nums[i] = nums[i], nums[max_index]
            adjust_heap(nums, max_index)
    nums_len = len(nums)
    if nums_len < 1:
        return nums
    # 1， 构建一个最大堆
    build_max_heap(nums)
    # 2.  循环将堆首位(最大值)与末位交换，然后重新调整最大堆
    while nums_len > 0:
        nums[0], nums[nums_len-1] = nums[nums_len-1], nums[0]
        nums_len -= 1
        adjust_heap(nums, 0)
    return nums
# 8. Count Sort
def count_sort(nums):
    # 不是基于比较的，而是基于数组下标的，只适用于 整数数组，且极差较小的数组
    max_value, min_value = max(nums), min(nums)
    count_arr = [0]*(max_value-min_value+1)
    # 第一次遍历，填充数组
    for each in nums:
        count_arr[each-min_value]+=1
    # 频率数组—>元素开始的索引, 保持稳定排序
    for i in range(0, len(count_arr)-1):
        count_arr[i+1] += count_arr[i]
    # 从后向前遍历，保持稳定排序
    new_nums = [None]*len(nums)
    for each in nums:
        new_nums[count_arr[each-min_value]-1] = each
        count_arr[each-min_value] -= 1
    return new_nums
# 9. bucket sort
def bucket_sort(nums):
    max_value, min_value = max(nums), min(nums)
    # 设置桶的数量，以及桶的跨度
    bucket_num = 10
    span = (max_value - min_value)//10 + 1
    bucket_list = [[] for i in range(10)]
    # 遍历数组，将数据放入桶中
    for each in nums:
        bucket_list[(each - min_value)//span].append(each)
    # 将每个桶排序
    for bucket in bucket_list:
        bucket.sort()
    # 给每个桶排序后，合并所有的桶
    return [ i for bucket in bucket_list for i in bucket]
    

if __name__=="__main__":
    sort_func_map = {
        'bubble sort:\t': bubble_sort,
        'selection sort:\t': selection_sort,
        'insertion sort\t': insertion_sort,
        'shell sort\t': shell_sort,
        'merge sort\t': merge_sort,
        'quick sort\t': qucik_sort,
        'heap sort\t': heap_sort,
        'count sort\t': count_sort,
        'bucket sort\t': bucket_sort
    }
    for key in sort_func_map:
        nums = [8,10,2,9,35,23,4,6,7,2,3,4,17]
        print(key, sort_func_map[key](nums))
