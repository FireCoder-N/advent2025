import os
import bisect

class SortedMap:
    def __init__(self):
        self.keys = [] #min of each range
        self.values = [] #max of each range

    def find(self, key):
        # O(logn)
        idx = bisect.bisect_left(self.keys, key)
        if idx < len(self.keys) and self.keys[idx] == key:
            return True, idx
        return False, idx

    def insert(self, key, value):
        # O(logn)
        exists, idx = self.find(key)
        if exists:
            return idx  # key already exists
        self.keys.insert(idx, key)
        self.values.insert(idx, value)
        return idx
    
    def insertat(self, idx, key, value):
        # O(1)
        self.keys.insert(idx, key)
        self.values.insert(idx, value)

    def cleanup(self):
        # cleanup overlapping ranges
        # if the maximum of the (n)th range falls within the (n+1)th range, dissolve n range by setting (n+1)'s minimum to the minimum of the two
        # similarly we shall dissolve (n)th range if its minimum falls within the (n-1)th range.
        while True: 
            for i in range(1, len(self.keys)):
                if self.keys[i-1] <= self.keys[i] <= self.values[i-1]:
                    self.values[i-1] = max(self.values[i], self.values[i-1])
                    self.keys.pop(i)
                    self.values.pop(i)
                    break
            else:
                break

        while True:
            for i in range(0, len(self.keys)-1):
                if self.keys[i+1] <= self.values[i] <= self.values[i+1]:
                    self.keys[i+1] = min(self.keys[i], self.keys[i+1])
                    self.keys.pop(i)
                    self.values.pop(i)
                    break
            else:
                break



fresh = SortedMap()
toggleOp = True # True for fresh ranges, false for ingredient ID
total = 0 

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        if line == "\n":
            toggleOp = False
            fresh.cleanup()               

        elif toggleOp:
            r = [int(x) for x in line.strip().split("-")]
            state, idx = fresh.find(r[0])

            if state:
                fresh.values[idx] = max(r[1], fresh.values[idx])
            else:
                fresh.insertat(idx, r[0], r[1])        
                
        else:
            for i in range(len(fresh.keys)):
                if fresh.keys[i] <= int(line.strip()) <= fresh.values[i]:
                    total += 1
                    break

print(total)

