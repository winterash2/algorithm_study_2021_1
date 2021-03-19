N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
answer = 0
answer += nums[0] * (M % (K+1))
answer += nums[0] * K * (M // (K+1))
answer += nums[1] * (M // (K+1))

print(answer)