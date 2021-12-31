def solution(array, commands):
    results = []
    for command in commands:    
        sorted_arr = sorted(array[command[0] - 1 : command[1]])
        results.append(sorted_arr[command[2] - 1])
    return results
        