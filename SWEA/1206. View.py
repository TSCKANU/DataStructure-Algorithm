#T = int(input())

def process(test_case):
    n = int(input())
    building = list(map(int, input().split()))
    result = 0
    for i in range(2, n-1):
        if building[i] > max([building[i - 2], building[i - 1], building[i + 1], building[i + 2]]):
            result += (building[i] - max([building[i - 2], building[i - 1], building[i + 1], building[i + 2]])
    
    print("#{} {}".format(test_case, result))


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    process(test_case)
