from datetime import datetime


class LruElement:
    def __init__(self, value: int, key: int):
        self.Value = value
        self.Next = None
        self.Back = None
        self.Key = key
    

class LRUCache:
    
    def __init__(self, capacity: int):
        self.Capacity = capacity
        self.Tracker = dict()
        self.element_list = None
        self.last_element = None
    
    def get(self, key: int) -> int:
        if key in self.Tracker:
            return self.update_to_last_recently_used(self.Tracker[key]).Value
        return -1
    
    def update_to_last_recently_used(self, element):
        if element != self.element_list:
            # it is not the first already:
            prev = element.Back
            if prev:
                prev.Next = element.Next
                if prev.Next:
                    prev.Next.Back = prev
                else:
                    self.last_element = prev
            # points to none to be the first.
            element.Back = None
            element.Next = self.element_list
            self.element_list.Back = element
            # place it at top of the list
            self.element_list = element
        return element

    def put(self, key: int, value: int) -> None:
        if key in self.Tracker:
            result = self.Tracker[key]
            # update to last recently used
            self.update_to_last_recently_used(result)
            # then return:
            result.Value = value
        else:
            # creates new value
            new_val = LruElement(value, key)
            # set it at first value
            new_val.Next = self.element_list
            if self.element_list:
                self.element_list.Back = new_val
            else:
                self.last_element = new_val
                
            # place it at top of the list
            self.element_list = new_val
            self.Tracker[key] = new_val
            
            # set at capacity again by removing last element
            if len(self.Tracker) > self.Capacity:
                del self.Tracker[self.last_element.Key]
                self.last_element = self.last_element.Back
                self.last_element.Next = None
                
        
