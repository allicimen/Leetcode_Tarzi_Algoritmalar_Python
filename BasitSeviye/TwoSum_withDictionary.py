def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []

nums = [2, 15, 11, 7,]
target = 9

print(two_sum(nums, target))

#ierasyon durumlarını yazalim teker teker 
# i = 0 , num = 2 , compelement = 7 ,  seen { '2' : 0 }
# i = 1 , num = 7 , compelement = 2 , if bloğuna girdi   0 , 1 ekrana verdi
#returna girmediğini farz edip döngüyü  devam ettirelim
# i = 2 , num = 11 , compelement = -2 ,  seen { '11' : 1}
# i = 3 , num = 15 , compelement = -6 ,  seen { '15' : 2}
