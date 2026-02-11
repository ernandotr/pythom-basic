def timSort(arr):
    minRun = 32
    n = len(arr)
    for i in range(0, n, minRun):
        arr[i:i + minRun] = sorted(arr[i:i + minRun])
    size = minRun
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = []
            left_index, right_index = start, midpoint + 1
            while left_index <= midpoint and right_index <= end:
                if arr[left_index] < arr[right_index]:
                    merged_array.append(arr[left_index])
                    left_index += 1
                else:
                    merged_array.append(arr[right_index])
                    right_index += 1
            while left_index <= midpoint:
                merged_array.append(arr[left_index])
                left_index += 1
            while right_index <= end:
                merged_array.append(arr[right_index])
                right_index += 1
            arr[start:start + len(merged_array)] = merged_array
        size *= 2

# Example usage
if __name__ == "__main__":
    arr = [5, 21, 7, 23, 19, 10, 3, 15]
    timSort(arr)
    print("Sorted array:", arr)
    