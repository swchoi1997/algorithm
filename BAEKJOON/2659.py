def clock_number(nums):
    num1 = 1000* nums[0] + 100 * nums[1] + 10 * nums[2] + nums[3]
    num2 = 1000* nums[1] + 100 * nums[2] + 10 * nums[3] + nums[0]
    num3 = 1000* nums[2] + 100 * nums[3] + 10 * nums[0] + nums[1]
    num4 = 1000* nums[3] + 100 * nums[0] + 10 * nums[1] + nums[2]

    return min(num1,num2,num3,num4)

numbers = list(map(int,input().split()))

initClockNumber = clock_number(numbers)


cnt = 1
for i in range(1111, 10000):
    if initClockNumber == i:
        print(cnt)
        break

    if str(i)[3] == 0 or str(i)[2] == 0 or str(i)[1] == 0:
        continue
    x = [int(a) for a in str(i)]

    tmpClockNumber = clock_number(x)

    if tmpClockNumber != i:
        continue    
    cnt += 1
