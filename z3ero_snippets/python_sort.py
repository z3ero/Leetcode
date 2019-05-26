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
    pass

if __name__=="__main__":
    sort_func_map = {
        'bubble sort:\t': bubble_sort,
        'selection sort:\t': selection_sort,
        'insertion sort\t': insertion_sort,
        'shell sort\t': shell_sort    
    }
    for key in sort_func_map:
        nums = [8,10,2,9,35,23,4,6,7,2,3,4,17]
        print(key, sort_func_map[key](nums))
