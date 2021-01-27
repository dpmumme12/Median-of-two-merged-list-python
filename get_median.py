def get_median(list1 , list2):
    nums_list = list1 + list2

    #Uses bubble sort to sort the list
    for x in range(len(nums_list) - 1, 0, -1):
        for y in range(0, x):
            
            if nums_list[y] > nums_list[y + 1]:
                temp = nums_list[y+1]
                nums_list[y+1] = nums_list[y]
                nums_list[y] = temp

    x = len(nums_list)
    if (x % 2) == 0:
        x = (x // 2) - 1
        y = x + 1
        x = (nums_list[x] + nums_list[y]) / 2
        return x
    else:
        x = (x // 2)
        x = nums_list[x]
        return x
  
lst1 = [int(x) for x in input("Numbers in first list (put spaces between numbers): ").split()]
lst2 = [int(x) for x in input("Numbers in second list (put spaces between numbers): ").split()]

print(f'Median: {get_median(lst1, lst2)}')






