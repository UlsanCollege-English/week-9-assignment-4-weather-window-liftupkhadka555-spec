import heapq

def sliding_window_max(nums, k):
    if not nums or k <= 0:
        return []
    if k > len(nums):
        return [max(nums)]

    result = []
    heap = []  # max-heap via (-value, index)

    for i, num in enumerate(nums):
        heapq.heappush(heap, (-num, i))
        # remove items outside the window
        while heap and heap[0][1] <= i - k:
            heapq.heappop(heap)
        if i >= k - 1:
            result.append(-heap[0][0])

    return result
