from random import randint, shuffle


def binary_search(arr, val):
    if len(arr) == 0: # If list is empty
        raise Exception('List is empty')
    elif val == arr[0]: # If searching for first element
        return 0
    elif val == arr[-1]: # If searching for last element
        return len(arr) - 1
    else:
        mid = len(arr) // 2
        low = 0
        high = len(arr) - 1
        while arr[mid] != val and low <= high:
            if arr[mid] < val:
                low = mid + 1 # Search in right side of a list
            elif arr[mid] > val:
                high = mid - 1 # Search in left side of a list
            mid = (low + high) // 2

        if low > high: # If element is not found
            raise Exception("Value does not exist in the list")
        else:
            return mid # Return index of searched element
    

def insertion_sort(arr):
    if len(arr) == 0: # If list is empty
        raise Exception('List is empty')
    else:
        for i in range(1, len(arr)):
            key = arr[i]
            for j in range(i - 1, -1, -1): 
                if arr[j] > key: 
                    arr[j + 1], arr[j] = arr[j], key # Swap elements
                else:
                    break # Other elements under key are sorted



def bogo_sort(arr):
    if len(arr) == 0: # If list is empty
        raise Exception('List is empty')
    else:
        while not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)): # If list isn't sorted
            shuffle(arr) # Shuffle all elements


def counting_sort(string):
    if len(string) == 0: # If list is empty
        raise Exception('String is empty')
    else:
        string = string.lower() # All letters are lowercase
        max_char = max(string)
        lst = []
        for _ in range(0, ord(max_char) - 96): # ord makes, for example, a = 97, so we substract 96. Each lowercase letter is in the range 97-122
            lst.append(0)

        unsupported_characters = (' ', ',', '.', '!', '?', ':', ';', '@', '#', '%', '^', '&', '*', '(' , ')', '[', ']', '{', '}')
        for letter in string:
            if letter not in unsupported_characters:
                lst[ord(letter) - 96 - 1] += 1 # Increase letter count

        sorted_letters = []
        for i in range(0, len(lst)):
            if lst[i] != 0:
                for _ in range(0, lst[i]):
                    sorted_letters.append(chr(i + 96 + 1))
        
        return "".join(sorted_letters)


def quick_sort(arr, start, end):
    if len(arr) == 0: # If list is empty
        raise Exception('List is empty')
    elif start >= end: # If subarray is empty or has only 1 element
        return

    def partition(arr, start, end): # Splitting an array
        pivot = arr[end]
        low = start
        high = end - 1 # Because pivot at the end
        while True:
            while low <= high and arr[high] >= pivot: # Searching for element which isn't at right place
                high -= 1
            
            while low <= high and arr[low] <= pivot: # Searching for element which isn't at right place
                low += 1

            if low <= high:
                arr[low], arr[high] = arr[high], arr[low] # Switch this 2 elements so now they are at right place
            else:
                break
        arr[end], arr[low] = arr[low], arr[end] # Switch pivot and first element which is greater than pivot
        return low # Index of pivot element

    partition_index = partition(arr, start, end) # Get pivot index after splitting
    quick_sort(arr, start, partition_index - 1) # Sort left subarray
    quick_sort(arr, partition_index + 1, end) # Sort right subarray
