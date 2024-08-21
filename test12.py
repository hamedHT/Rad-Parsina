#solution:Basketball team


def bubble_sort(my_array):
    n = len(my_array)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                swapped = True
        if not swapped:
            break


# array = [7, 3, 9, 12, 11]
# bubble_sort(array)
# print(array)

#############################################################33

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

	# Check base case
	if high >= low:

		mid = (high + low) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1

# Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 10

# # Function call
# result = binary_search(arr, 0, len(arr)-1, x)

# if result != -1:
# 	print("Element is present at index", str(result))
# else:
# 	print("Element is not present in array")

####################################################################

player = []
hieght = []
result = []

def basketball_team():
  n = int(input('enter number of members: '))
  player_name = input('enter name of players: ')
  player =player_name.split(',')
  player_hieght = input('enter hieght of players: ')
  hieght = player_hieght.split('|')
  player_select = input('enter name of player selected: ')

  if len(player) == n:
    
    index = player.index(player_select)
    hieght_selected = int(hieght[index])

    for i in hieght:
         result.append(int(i))
    
    bubble_sort(result)
    result_index = binary_search(result,0,len(result)-1,hieght_selected)
    answer = (len(result) - 1) - result_index + 1
    return answer

#print(basketball_team())  

###########################################################################

def yekan():
      base = int(input("enter base number: "))
      exponent = int(input('enter exponent number: '))
      number = pow(base,exponent)
      Yekan = number % 10
      return Yekan

print(yekan())