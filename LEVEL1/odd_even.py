# odd_even.py
# 프로그래머스 LEVEL 1 - 짝수와 홀수

def solution(n):
    return "Odd" if n % 2 else "Even"

# --- 아래는 다른 방식들 ---

def solution_bit(n):
    # 비트 방식: n & 1 이 1이면 홀수
    return "Odd" if (n & 1) else "Even"

def solution_divisible(n):
    # 나머지 비교 대신 나눠떨어짐 판별
    return "Even" if n % 2 == 0 else "Odd"

if __name__ == "__main__":
    for v in [0, 1, 2, 3, 4, 11, 100]:
        print(v, solution(v), solution_bit(v), solution_divisible(v))
