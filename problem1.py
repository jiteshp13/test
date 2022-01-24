def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

def main():
    nums = [int(x) for x in input().split()]
    target = int(input())
    print(twoSum(nums, target))

if __name__ == '__main__':
    main()
