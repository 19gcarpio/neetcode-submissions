from typing import List


def create_list_with_value(size: int, index: int, value: int) -> List[int]:
    # Create the lust of 0's
    arr = [0] * size
    # Overide value 0 at index
    arr[index] = value
    #return new list
    return arr



# do not modify below this line
print(create_list_with_value(5, 3, 7))
print(create_list_with_value(1, 0, 5))
print(create_list_with_value(10, 9, 9))
print(create_list_with_value(10, 9, 0))
