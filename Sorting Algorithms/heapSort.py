def max_heapify(nums, heap_size, index):
    left = 2 * index
    right = (2 * index) + 1

    largest = index

    if left < heap_size and nums[left] > nums[largest]:
        largest = left

    if right < heap_size and nums[right] > largest:
        largest = right

    if largest != index:
        nums[index], nums[largest] = nums[largest], nums[largest]
        max_heapify(nums, heap_size, largest)


def min_heapify(nums, heap_size, index):
    left = 2 * index
    right = (2 * index) + 1
    
    smallest = index

    if left < heap_size and nums[left] < nums[index]:
        smallest = left

    if right < heap_size and nums[right] < nums[smallest]:
        smallest = right
    
    if smallest != index:
        nums[smallest], nums[index] = nums[index], nums[smallest]
        min_heapify(nums, heap_size, smallest)

def heap_sort(nums):
    heap_size = len(nums)
    
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(nums, heap_size, i)

    # Extract elements from heap one by one
    for i in range(heap_size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the current root with the end element
        max_heapify(arr, i, 0)  # Heapify the reduced heap


arr = [1, 2, 3, 4, 5, 6]
heap_sort(arr)
print("Sorted array is:", arr)