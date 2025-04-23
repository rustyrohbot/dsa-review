def bucket_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    min_val = min(arr)
    
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    
    for num in arr:
        index = int((num - min_val) / (max_val - min_val) * (bucket_count - 1))
        buckets[index].append(num)

    
    for i in range(bucket_count):
        buckets[i].sort()

    
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr