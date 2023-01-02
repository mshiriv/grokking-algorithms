def binary_search(list: list, item: int)-> None or int:
  low = 0
  high = len(list) - 1
  while low <= high:
    mid = (low + high)//2
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None

my_list_1 = [1,2,3,4,5,6,7,8]
my_list_2 = [2,3,4,6,7,8,100]

print(binary_search(my_list_1, 6))
print(binary_search(my_list_2, -1))
