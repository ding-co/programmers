import math
def solution(n, m):
    answer = []
    gcd = math.gcd(n, m)
    lcm = (n * m) // gcd
    answer.extend([gcd, lcm])
    return answer