class ArrayList():
    elements = []
    size = 0

    def __init__(self, initElements = []):
        self.elements = initElements
        self.size = len(initElements)
    
    # returns a string representation of array; used by print()
    def __str__(self):
        return str(self.elements)
    
    # equals method:
    # checks for equality between ArrayList objects
    def __eq__(self, other_array):
        if isinstance(other_array, ArrayList) and other_array.length() == self.size:
            for i in range(self.size):
                if (self.get(i) != other_array.get(i)):
                    return False
                return True
        else:
            return False
    
    # size of array
    def length(self):
        return self.size
    
    # private helper method to check if an index is valid or out-of-bounds
    def __is_valid_index(self, index):
        if index < self.size and index >= 0:
            return True
        else:
            return False
        
    # get element at specified index
    def get(self, index):
        if self.__is_valid_index(index):
            return self.elements[index]
        else:
            raise Exception("Exception: Index out-of-bounds.")
    
    # adds an element to the back of the array
    def add(self, element):
        self.elements.append(element)
        self.size += 1
        
    # sets element at specified index
    def set(self, element, index):
        if self.__is_valid_index(index):
            self.elements[index] = element
        else:
            raise Exception("Exception: Index out-of-bounds.")
        
    # searching methods
    
    # linear search algorithm:
    # iterates through each list element to find a match
    # runs in O(n) time.
    # if element exists in array, returns the index
    # of the first occurrence, otherwise returns -1
    def __linear_search(self, element):
        found_index = -1
        for i in range(self.size):
            if element == self.get(i):
                found_index = i
                break
                
        return found_index
    
    def search(self, element, method = "linear"):
        if method == "linear":
            return self.__linear_search(element)
        else:
            return self.__linear_search(element)
    
    # sorting methods
    
    # Selection Sort:
    # Partitions off the beginning of the array as the sorted segment,
    # then iteratively finds the next smallest element and swaps it with the
    # end of the sorted segment.
    # Runs in O(n^2) time; note that selection sort will always scan the whole array
    # with each pass throught he loop REGARDLESS of whether the array is already sorted or not
    def selection_sort(self, trace = False):
        ending_index = 0 # end of the sorted segment
        
        while ending_index < self.size:
            current_min = self.get(ending_index)
            current_min_index = ending_index
            temp = self.get(ending_index)
            for i in range(ending_index, self.size):
                if self.get(i) < current_min:
                    current_min = self.get(i)
                    current_min_index = i
                
                if trace:
                    print(self.elements)
            
            self.set(temp, current_min_index)
            self.set(current_min, ending_index)
                
            ending_index += 1
    
    # Insertion Sort:
    # Partitions off the beginning of the array as the sorted segment,
    # then reads next element and inserts into the sorted segment in correct order
    # runs in O(n) time; note that insertion sort won't need to scan through the whole
    # array if the array is already sorted. This makes insertion sort faster than selection sort
    # on average (best case scenario is O(n) when the array is already sorted)
    def insertion_sort(self, trace = False):
        ending_index = 0 # end of the sorted segment
        
        while ending_index < self.size - 1:
            temp = self.get(ending_index + 1)
            
            # scan through sorted segment in reverse order, 
            # this helps improve runtime if the array is already sorted
            for i in reversed(range(ending_index + 1)):
                current_element_to_compare = self.get(i)
                if temp < current_element_to_compare:
                    self.set(current_element_to_compare, i+1)
                    self.set(temp, i)
                else:
                    break
                
                if trace:
                    print(self.elements)
            
                
            ending_index += 1
    
    # Merge Sort:
    # Divide-and-conquer method that recursively splits the array into 2 smaller arrays
    # and sorts the smaller arrays. The two sorted halves are then "zipped" together 
    # to merge back into one big sorted array.
    # Merge sort is usually implemented via recursion; the recursion bottoms-out at 
    # singleton arrays (this is the base-case).
    # Merge sort runs in O(n log n) time, making it the fastest sorting algorithm on the
    # worst case scenario.
    def merge_sort(self, trace = False):
        
        # the easy version of merge sort creates 2x new ArrayList objects at each
        # recursively call. This is memory inefficient because the new objects 
        # are just copies of the larger objects; we are using memory to store
        # redundant information.
        
        # A more clever version of merge sort uses indices to keep track where smaller arrays.
        # Since the sub-arrays are just contiguous slices of the larger array, we can represent
        # each sub-array as a pair of indices (i, j) which correspond to the start and end of the sub-array
        # relatively to how it sits inside the bigger array.
        
        start_index = 0
        end_index = self.size - 1
        temp_array = [None] * self.size # create a temporary array that will house the final sorted list
        
        self.__merge_sort_helper(temp_array, start_index, end_index, trace)
    
    # private helper method that does Merge Sort, but uses a pair (start_index, end_index)
    # to represent each subarray, thereby saving memory
    def __merge_sort_helper(self, temp_array, start_index, end_index, trace):
        
        # implicit base-case: start_index == end_index, in which case we have reached a singleton array
        if (start_index < end_index):
            # if not in base-case (not singleton) then make recursive calls
            mid_index = (end_index + start_index)//2 # int division to find middle-index
            self.__merge_sort_helper(temp_array, start_index, mid_index, trace)
            self.__merge_sort_helper(temp_array, mid_index + 1, end_index, trace)
            
            if (self.elements[mid_index] > self.elements[mid_index+1]):
                self.__merge(temp_array, start_index, mid_index, end_index, trace)
            # self.__merge(temp_array, start_index, mid_index, end_index,trace)
        
    
    def __merge(self, temp_array, start_index, mid_index, end_index, trace):
        
        left_start_index = start_index
        left_end_index = mid_index
        right_start_index = mid_index + 1
        right_end_index = end_index
        
        index = left_start_index
        
        # zip the two halves together into a sorted larger array
        # this is done by "ping-pong"-ing back and forth between the arrays
        # and inserting elements in ascending order
        while ( (left_start_index <= left_end_index) and (right_start_index <= right_end_index) ):
            if (self.get(left_start_index) < self.get(right_start_index)):
                temp_array[index] = self.get(left_start_index)
                left_start_index += 1
            else:
                temp_array[index] = self.get(right_start_index)
                right_start_index += 1
            
            index += 1
            
            if trace:
                print(temp_array)
        
        # The loop exits when one of the halves has run out of elements
        # but it's possible the other half still has elements remaining to be sorted
        while (left_start_index <= left_end_index):
            temp_array[index] = self.get(left_start_index)
            left_start_index += 1
            index += 1
            
            if trace:
                print(temp_array)
            
        while (right_start_index <= right_end_index):
            temp_array[index] = self.get(right_start_index)
            right_start_index += 1
            index += 1
            
            if trace:
                print(temp_array)
        
        # finally, copy the elements from the sorted array back into the original array
        for i in range(start_index, end_index+1):
            self.set(temp_array[i], i)
        
                        