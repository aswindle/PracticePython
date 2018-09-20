def fib(n):
    nums = [1,1]
    if(n<=2):
        return 1
    else:
        for i in range (2, n):
            nums.append(nums[-1]+nums[-2])
    print(nums)
    return nums[-1]
            
fibnum = int(input("Which Fibonacci number do you want? "))
print(fib(fibnum))