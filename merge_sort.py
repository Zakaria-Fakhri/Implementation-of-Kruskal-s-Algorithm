
def merge_sort(edges_list):
    """
    This function implements the Merge Sort algorithm with a time complexity of
    O(n log n). It is a recursive sorting technique that divides an input list
    into smaller sublists and then merges those sublists in a sorted manner.

    This function is specifically designed to sort a list of edges,
    where each edge is represented as a tuple containing relevant data,
    including weights.
    """
    l = len(edges_list)
    # If the list is empty or contains only one element, it is already sorted.
    if l <= 1:
        return

    mid = l // 2  # Calculate the midpoint of the list
    left_half = []  
    right_half = []

    # Fill the left half with elements from the original list
    for i in range(mid):
        left_half.append(edges_list[i])

    # Fill the right half with the remaining elements from the original list
    for i in range(mid, l):
        right_half.append(edges_list[i])

    # Recursively sort the left and right halves
    merge_sort(left_half)
    merge_sort(right_half)

    j = 0  # Index for right_half
    k = 0  # Index for merged result
    i = 0  # Index for left_half

    # Merge the sorted halves back into edges_list
    while i < len(left_half) and j < len(right_half):
        if left_half[i][2] < right_half[j][2]:  # Compare weights (the weight is located at index 2 of the tuple in edges_list)
            edges_list[k] = left_half[i]  # Add the smaller element to the merged list
            i += 1
        else:
            edges_list[k] = right_half[j]  # Add the smaller element to the merged list
            j += 1
        k += 1

    # Add any remaining elements from the left half
    while i < len(left_half):
        edges_list[k] = left_half[i]
        i += 1
        k += 1

    # Add any remaining elements from the right half
    while j < len(right_half):
        edges_list[k] = right_half[j]
        j += 1
        k += 1



        # Recursively sort the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        j = 0  # Index for right_half
        k = 0  # Index for merged result
        i = 0  # Index for left_half

        # Merge the sorted halves back into edges_list
        while i < len(left_half) and j < len(right_half):
            if left_half[i][2] < right_half[j][2]:  # Compare weights (the weight is located at index 2 of the tuple in edges_list)
                edges_list[k] = left_half[i]  # Add the smaller element to the merged list
                i += 1
            else:
                edges_list[k] = right_half[j]  # Add the smaller element to the merged list
                j += 1
            k += 1

        # Add any remaining elements from the left half
        while i < len(left_half):
            edges_list[k] = left_half[i]
            i += 1
            k += 1

        # Add any remaining elements from the right half
        while j < len(right_half):
            edges_list[k] = right_half[j]
            j += 1
            k += 1
