# Question 1

def power(a, b):
    if a < 1 or b < 1:
        return -1

    else:
        return abs(a * power(a, b-1))


a = 3
b = 3

print(power(a, b))


# Question 2

def binary_search(numbers, num, start, end):

    # checking the base case
    if end >= start:
        middle = (end + start) // 2  # defining the middle of the list

        # if the element is in the middle
        if numbers[middle] == num:
            return middle

        # if the element is smaller than the middle, it can only be in the left part
        elif numbers[middle] > num:
            return binary_search(numbers, num, start, middle - 1)  # now the end is the middle - 1

        # else the element can only be in the right part, therefore the start is the middle + 1
        else:
            return binary_search(numbers, num, middle + 1, end)

    else:  # the element is nowhere to be found
        return - 1


numbers = [1, 2, 7, 9, 44, 90]
num = 2

result = binary_search(numbers, num, 0, len(numbers)-1)
print(result)


# Question 3, 4, 5, 6, 7

class HashTable:
    def __init__(self):
        self.max = 8
        self.arr = [[] for x in range(self.max)]

    def __my_hash(self, element):
        if type(element) is str:
            key = 0
            for char in element:
                key += ord(char)
            return key % self.max
        elif type(element) is int:
            return element % self.max

    def insert(self, element):
        key = self.__my_hash(element)
        self.arr[key].append(element)

    def get_element(self, element):
        key = self.__my_hash(element)
        if len(self.arr[key]) == 0:
            return False
        else:
            try:
                return self.arr[key].remove(element)
            except:
                return False

    def get_size(self):
        length = 0
        for key in range(self.max):
            if len(self.arr[key]) == 0:
                length += 1
            else:
                length += len(self.arr[key])

        return length


t = HashTable()
t.insert("Giacomo")
t.insert("Jack")
t.insert("Test")
t.insert(22)
t.insert(8)
t.insert("Algorithm")
print(t.get_element(9))
print(t.get_size())

print(t.arr)
