def selection_sort(arr):
  # iterate through all of the elements in
  # our passed in arr
  #
  # position will represent the location of the
  # first unsorted element in our array going forward
  for position in range(len(arr)):
    # set our min_item to 0
    min_item = position
    # iterate through the rest of our array
    for i in range(position+1, len(arr)):
      # if an element in the rest of our array
      # is smaller than the current min_item
      if arr[i] < arr[min_item]:
        # set that to our new min_item
        min_item = i

    # swap the minimum item to the first unsorted element in
    # our array.
    arr[position], arr[min_item] = arr[min_item], arr[position]

  # return our sorted array
  return arr

my_array = [5, 3, 9, 2, 1, 6]
print(selection_sort(my_array))