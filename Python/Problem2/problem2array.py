import time

start = time.perf_counter_ns()

nums = [0, 1]
while nums[-1] <= 4000000:
    nums.append(nums[-1] + nums[-2])
nums = nums[:-1]
summ = sum([i if not i % 2 else 0 for i in nums])
# summ = 0
# for i in nums:
#     if not i % 2:
#         summ += i

end = time.perf_counter_ns()
print("Time elapsed:", end - start, "ns")

print("Result =", summ)
