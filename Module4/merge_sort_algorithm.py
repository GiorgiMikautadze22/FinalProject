def sort_merge(arr):
    if len(arr) <= 1:
        return arr

    middle_index = len(arr) // 2
    left = sort_merge(arr[:middle_index])
    right = sort_merge(arr[middle_index:])

    return merge(left,right)

def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


nums = [8, 3, 5, 3, 4, 7, 6, 2, 1]
sorted_arr = sort_merge(nums)
print("Sorter Array: ",sorted_arr)