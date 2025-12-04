import os

count = 0

# If the number of digits is prime, then input is invalid iff all of its digits are the same.
# Otherwise, number of digits can be divided by a prime number.
# Thus, 
#   - if number of digits % 2 == 0, then we should check for repeating patterns like XYXY...
#   - similarly, if num of digits % 3 == 0, we should check for XYZXYZ... etc
# Observation: max number of digits = 10
#   - checking division with primes > 5 is unecessary, becasue there are no numbers x, y ∈ ℕ such that x > 5 and x ∙ y < 10
#   - checking division with 5 is also uncessary, because there are no numbers x, y ∈ ℕ such that x = 5, y ≠ 2 and x ∙ y < 10.Patterns of 5 repeating digits XYZUVXYZUV can be detected during division with 2.
divs = [2, 3]

def repeating(number):
    if number == len(number) * number[0] and len(number) != 1 :
        return True
    
    for d in divs:
        if len(number) % d == 0 and len(number) // d != 1:
            t = set([number[i:i+d] for i in range(0, len(number), d)])
            if len(t) == 1:
                return True
            q = len(number) // d
            t = set([number[i:i+q] for i in range(0, len(number), q)])
            if len(t) == 1:
                return True
            
    return False


with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        ranges = line.strip().split(",")
        for r in ranges:
            bounds = r.split("-")
            for number in range(int(bounds[0]), int(bounds[1])+1):
                if repeating(str(number)):
                    # print(number)
                    count += number

print(count)