# Several common sorting algorithms: ascending
# 1. Bubble Sort
def bubble_sort(nums):
    nums_len = len(nums)
    for i in range(0, nums_len):
        sign = True
        for j in range(0, nums_len-i-1):
            if nums[j+1] < nums[j]:
                sign = False
                nums[j], nums[j+1] = nums[j+1], nums[j]
        if sign:
            break
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
# 4. Insert Sort (希尔排序是升级版的插入排序)
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
def merge_sort(nums, l, r):  # 初始的 l=0; r= len(arr)-1
    def merge(arr, l, mid, r):
        tmp_arr = [0]*(r-l+1)
        p1, p2 = l, mid+1
        # compare two arr, select smaller one to fill temporary array
        index = 0
        while p1 <= mid and p2 <= r:
            if arr[p1]<=arr[p2]:
                tmp_arr[index]=arr[p1]; p1+=1
            else:
                tmp_arr[index]=arr[p2]; p2+=1
            index += 1
        if p1<=mid:
            tmp_arr[index:]=arr[p1:mid+1]
        elif p2<=mid:
            tmp_arr[index:]=arr[p2:r+1]
        # 转移到原数组上
        arr[l:r+1] = tmp_arr   

    if l >= r:
        return
    mid = (l+r)//2
    merge_sort(nums, l, mid)
    merge_sort(nums, mid+1, r)
    merge(nums, l, mid, r)
    return nums

# 6. Quick Sort
def qucik_sort(nums):
    def q_sort(arr, low, high):
        if low < high:
            pos = partition(arr, low, high)
            q_sort(arr, low, pos-1)
            q_sort(arr, pos+1, high)
    def partition(arr, low, high):
        key = arr[low]
        while low < high:
            while low < high and arr[high] >= key:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] <= key:
                low += 1
            arr[high] = arr[low]
        arr[low] = key
        return low
    q_sort(nums, 0, len(nums)-1)
    return nums

# 7. Heap Sort： 以小顶堆为例
def heap_sort(arr):   # 注意：堆排序的数组下标是以 1 开头的
    def adjust_heap(arr, i, length): # 对某一个节点，调整以它为顶点的树
        key = arr[i]
        # 从该节点开始 沿着 关键字 较小的孩子方向向下进行
        while i*2 <= length:
            child_index = i*2
            if child_index < length and arr[child_index] > arr[child_index+1]:  # 如果有两个孩子，且右孩子较小, 和右孩子比较即可
                child_index += 1
            if key > arr[child_index]  # 根节点比孩子大，要把孩子调整上去
                arr[i] = arr[child_index]
                i = child_index    # 下一步比较 key 和 （child_index 的孩子节点）
            else:   # 根节点符合小顶条件，子节点本就符合小顶条件，不用调整了
                break
        arr[i] = key   # 将 key 放在最后调整出来的位置

    length = len(arr)
    # 构建最小堆
    for i in range(length//2, -1, 1):  # 从后往前 对每个元素 自顶向下的 调整堆
        adjust_heap(arr, i, length)

    # 输出最小堆的排序序列
    for i in range(length, -1, 1):
        # 堆顶记录和最后一个元素互换
        arr[1], arr[i] = arr[i], arr[1]
        # 重新调整 1 ~ i-1 为小顶堆
        adjust_heap(arr, 1, i-1)

    # 最终数组按照从后往前的顺序，为从小到大的顺序
    return arr.reverse()

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
