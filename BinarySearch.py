class BinarySearch(list):
    result_array = []
    length = 0
    step = 0

    def __init__(self, a, b):

        #create a list of length a. Consecutive elements should have step(difference) b
        self.step = b

        #self.result_array = range(1, a+1, b)
        self.result_array = [i for i in range(1, a+1, b)]

        self.length = len(self.result_array)

        #return result_array

    def search(self, item):
        #item_index = self.result_array.index(item)
        first_element = 0
        last_element = (self.length - 1) - self.step
        found = False
        count = 0

        while first_element <= last_element and not found:
            mid_element = (first_element + last_element)//2
            count += 1
            #print 'Loop Number:' + str(count)
            if self.result_array[mid_element] == item:
                found = True
            else:
                if item < self.result_array[mid_element]:
                    last_element = mid_element - 1
                else:
                    first_element = mid_element + 1
        #return item_index
        #return self.result_array
        return {'count':count, 'index':self.result_array.index(item)}

b = BinarySearch(40, 1)
b_result_array = b.result_array

b_first_element = b_result_array[0]
b_last_element = b_result_array[18]

search_element = b.search(16)
print search_element

print b_result_array
print 'First Element: ' + str(b_first_element)
#print b_result_array.index(19)
print b_last_element
print len(b_result_array)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]