def bucket_sort(arr):
    if not arr:
        return []

    # Separate infinities
    neg_infs = [x for x in arr if x == float('-inf')]
    pos_infs = [x for x in arr if x == float('inf')]
    normals = [x for x in arr if x != float('-inf') and x != float('inf')]

    if not normals:
        return neg_infs + pos_infs

    max_val = max(normals)
    min_val = min(normals)

    if max_val == min_val:
        return neg_infs + normals + pos_infs

    bucket_count = len(normals)
    buckets = [[] for _ in range(bucket_count)]

    for num in normals:
        index = int((num - min_val) / (max_val - min_val) * (bucket_count - 1))
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return neg_infs + sorted_arr + pos_infs
