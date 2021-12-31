def solution(answers):
    pattern_1 = "12345"
    pattern_2 = "21232425"
    pattern_3 = "3311224455"
    
    score_list = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == int(pattern_1[i % len(pattern_1)]):
            score_list[0] += 1
        if answers[i] == int(pattern_2[i % len(pattern_2)]):
            score_list[1] += 1
        if answers[i] == int(pattern_3[i % len(pattern_3)]):
            score_list[2] += 1
    return [i + 1 for i in range(len(score_list)) if max(score_list) == score_list[i]]

# Other Solution
