def solution(s):
    answer = []
    s_list = s.split(' ')
    for item in s_list:
        result = ''
        for i in range(len(item)):
            if i % 2 == 0:
                result += item[i].upper()
            else:
                result += item[i].lower()
        answer.append(result)
    return ' '.join(answer)