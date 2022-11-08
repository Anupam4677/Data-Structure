# hashtable- python has dictionary as an emplementation 

def get_hash(key):
    h = 0 
    for char in key:
        h += ord(char)
    return h % 100

# print(ord('a'))
# print(get_hash('march 28'))

class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]

    def get_hash(self,key):
        h = 0 
        for char in key:
            h += ord(char)
        return h % self.Max
    # def add(self,key,val):
    def __setitem__(self,key,val):
        # convert the key into a hash value 
        h = get_hash(key)
        # Now the hash valueis the new key 
        self.arr[h] = val
    def __getitem__(self,key):
        h_index = self.get_hash(key)
        return self.arr[h_index]
    def __delitem__(self,key):
        h = get_hash(key)
        self.arr[h] = None


t = HashTable()
# t.add('march 16',130)
# t.add('march 6',10)
# print(t.get('march 6'))
# print(t.arr)
# print(t.get_hash('march 28'))

t['june 3'] = 12
t['april 12'] = 90
t['jan 26'] = 72
t['feb 14'] = 54
t['march 5'] = 89

del t['feb 14']
print(t['june 3'])
print(t['feb 14'])
print(t.arr)
