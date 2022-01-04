def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)

# Other Solution
# def solution(absolutes, signs):
#     return sum([absolutes if signs else -absolutes for absolutes, signs in zip(absolutes, signs)])