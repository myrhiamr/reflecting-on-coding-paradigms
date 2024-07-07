"""
function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
"""

def flatten_and_sort(array):
    # Helper function to flatten the list
    def flatten(lst):
        return [item for sublist in lst for item in sublist]
    
    # Helper function to sort the list
    def sort(lst):
        return sorted(lst)
    
    # pure function to flatten and sort the array
    def process_array(arr):
        return sort(flatten(arr))
    
    return process_array(array)


array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
result = flatten_and_sort(array)
print(result)


"Object Oriented Prompt"

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
#Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"

#Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"


pod1 = Podracer(400, "perfect", 15000)
pod2 = AnakinsPod(450, "repaired", 20000)
pod3 = SebulbasPod(380, "trashed", 18000)

print(pod1.max_speed, pod1.condition, pod1.price)
pod1.repair()
print(pod1.condition)

print(pod2.max_speed)
pod2.boost()
print(pod2.max_speed)

print(pod3.condition)
pod3.flame_jet(pod1)
print(pod1.condition)
