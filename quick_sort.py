def quickSort(arr):
    """Sorts an array using the quicksort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new sorted list.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quickSort(left) + middle + quickSort(right)
# Example usage
if __name__ == "__main__":
    sample_array = [34, 7, 23, 32, 5, 62]
    print("Original array:", sample_array)
    sorted_array = quickSort(sample_array)
    print("Sorted array:", sorted_array)