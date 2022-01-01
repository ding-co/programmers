def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] not in result:
                result.append(numbers[i] + numbers[j])
    result.sort()
    return result

# Other Solution
# def solution(numbers):
#     result = set([])
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             result.add(numbers[i] + numbers[j])
#     return sorted(list(result))