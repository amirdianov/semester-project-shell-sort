def shell_sort(data: list[int]) -> list[int]:
    gap = len(data) // 2
    while gap > 0:
        for i in range(gap, len(data)):
            j = i
            delta = j - gap
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - gap
        gap //= 2
    return data



