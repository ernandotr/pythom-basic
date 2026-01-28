def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6]
    print("Original array:", sample_array)
    sorted_array = insertion_sort(sample_array)
    print("Sorted array:", sorted_array)
    