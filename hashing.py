# hashtable- python has dictionary as an emplementation 

def get_hash(key):
    h = 0 
    for char in key:
        h += ord(char)
    return h % 10

# print(ord('a'))
# print(get_hash('march 28'))

class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self,key):
        h = 0 
        for char in key:
            h += ord(char)
        return h % self.Max
    # def add(self,key,val):
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            

        # return self.arr[h_index]
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]



# t.add('march 16',130)
# t.add('march 6',10)
# print(t.get('march 6'))
# print(t.arr)
# print(t.get_hash('march 28'))
t = HashTable()
t['june 3'] = 12
t['april 12'] = 90
t['jan 26'] = 72
t['feb 14'] = 54
t['march 5'] = 89
t['march 6'] = 120
t['march 17'] = 459

del t['feb 14']
print(t['june 3'])
print(t['march 17'])
print(t.arr)
