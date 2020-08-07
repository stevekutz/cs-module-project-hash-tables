class HashTableEntry:
     """
     Linked List hash table key/value pair
     # could use Double LL but deleting/inserting from middle is rare with hash tables and managing prev, next overhead usually overkill
     """
     def __init__(self, key, value):
          # self.key = key
          # self.value = value
          # self.next = None
          self.key = key   # Day 1, index
          self.value = value # Day 1, element value
          self.next = None # Day 2, pointer to next node in LL

     # def __str__(self):
     #      print(f' at key {self.key} >> value is: {self.value}')

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
     """
     A hash table that with `capacity` buckets
     that accepts string keys

     Implement this.
     """
 
     def __init__(self, capacity):
          #self.capacity = MIN_CAPACITY  # Day 1, size here is same a number of slots, until we deal with collisions
          #self.slots = [ None for item in range(self.capacity)]
          # Day 2
          self.capacity = capacity
          self.slots = [None] * capacity  # this hold LL (e.g. HashTableEntry)
          self.items_stored = 0           # inc/dec for items added/deleted

     def get_num_slots(self):
          """
          Return the length of the list you're using to hold the hash
          table data. (Not the number of items stored in the hash table,
          but the number of slots in the main list.)

          One of the tests relies on this.

          Implement this.
          """
          # Your code here
          return len(self.slots)

     def get_load_factor(self):
          """
          Return the load factor for this hash table.
               load Factor = (# of items stored) / (total # of slots)
               Good practice is to resize when load factor > 0.7
               CANNOT COPY OLD ITEMS into resized hashtable, new size means modulus is different, hence new hashes & new indices
               'Amortized' complexity is O(1)
          Implement this.
          """
          # Your code here
          return self.slots

     def fnv1(self, key):
          """
          FNV-1 Hash, 64-bit

          Implement this, and/or DJB2.
          """

          # Your code here


     def djb2(self, key):
          """
          DJB2 hash, 32-bit

          Implement this, and/or FNV-1.
          """
          # Your code here
               #salt = 5381
          hash_val = 5381     

          for ch in key:
               hash_val = ((hash_val << 5) + hash_val) + ord(ch)
               # hash_val = (hash_val * 33) + ord(ch)     

          # print(f' \n dbj2 with key {key} gives hash_val >> {hash_val} ')
          # return hash_val & 0xFFFFFFFF
          return hash_val   

     def hash_index(self, key):
          """
          Take an arbitrary key and return a valid integer index
          between within the storage capacity of the hash table.
          """
          #return self.fnv1(key) % self.capacity
          # print(f' \t %%%  key {key} gives djb2 hash of {self.djb2(key)}')
          return self.djb2(key) % self.capacity

     def put(self, key, value):
          """
          Store the value with the given key.

          Hash collisions should be handled with Linked List Chaining.
          # we make an array of linked list nodes
          Implement this.
          """
          # Your code here
          # Day 1
          # hashed_index = self.hash_index(key)

          # if self.slots[hashed_index] != None:
          #      print(f' \n\t Collision at key {key} with hashed_index {hashed_index} & overwrite of {self.slots[hashed_index]}')

          # self.slots[hashed_index] = value
          # print(f' put: using key {key } >> index {hashed_index} >>> value is    \"{self.slots[hashed_index]}\"')

          # Day 2  - add to tail method
          hashed_index = self.hash_index(key)

          self.items_stored += 1

          # test if slot empty
          if self.slots[hashed_index] != None:
               print(f' \n\t Collision at key {key} with hashed_index {hashed_index} & overwrite of {self.slots[hashed_index].value}')
                              
               # create new node
               new_tail = HashTableEntry(key, value)   
               current =  self.slots[hashed_index]    

               # find tail  
               while current.next != None:
                    # check if key exists already
                    print(f' Current key is {current.key}')
                    if current.key == key:
                         current.value = value
                         return None
                    current = current.next
               # append to tail
               current.next = new_tail  
                    
                   
          else:  
               print(f' \n\t Create HashItem at key {key} with hashed_index {hashed_index} value: {value}')    
               self.slots[hashed_index] = HashTableEntry(key, value)


     def delete(self, key):
          """
          Remove the value stored with the given key.

          Print a warning if the key is not found.

          Implement this.
          """
          # Your code here
          # if key in range(self.capacity):
          #      self.slots[key] = None
          # else:
          #      print(f' Cannot delete key that does not exist ')     

          hashed_index = self.hash_index(key)
          print(f' delete:  key {key}, hashed_index{hashed_index}')
          self.slots[hashed_index] = None

     def get(self, key):
          """
          Retrieve the value stored with the given key.

          Returns None if the key is not found.

          Implement this.
          """
          # Your code here

          # if key not in range(self.capacity):
          #      print("KEY OUT OF range")  
          #      return None  
          # Day 1 
          # hashed_index = self.hash_index(key)
          # value = self.slots[hashed_index]

          # print(f' get: key {key} value at index {hashed_index} is {value}')

          # return self.slots[hashed_index]


          # Day 2
          # Find hashed index and iterate until key located, return val OR None if not found
          hashed_index = self.hash_index(key)

          if self.slots[hashed_index] == None:
               return None
          else:
              current = self.slots[hashed_index] 

              while current.next != None:      
                    if current.key == key:
                             return current.value
                    else:
                         current = current.next

     def resize(self, new_capacity):
          """
          Changes the capacity of the hash table and
          rehashes all key/value pairs.
               ?? Resize down when load factor <= 0.7
          Implement this.
          """
          # Your code here



if __name__ == "__main__":
     ht = HashTable(1)

     print(f' # slots func: {ht.get_num_slots()}')
     print(ht.slots)
     # print("****** OVERLOADING TABLE ******")

     ht.put("line_1", "'Twas brillig, and the slithy toves")
     ht.put("line_2", "Did gyre and gimble in the wabe:")
     ht.put("line_3", "All mimsy were the borogoves,")
     ht.put("line_4", "And the mome raths outgrabe.")
     ht.put("line_5", '"Beware the Jabberwock, my son!')
     ht.put("line_6", "The jaws that bite, the claws that catch!")
     ht.put("line_7", "Beware the Jubjub bird, and shun")
     ht.put("line_8", 'The frumious Bandersnatch!"')
     ht.put("line_9", "He took his vorpal sword in hand;")
     ht.put("line_10", "Long time the manxome foe he sought--")
     ht.put("line_11", "So rested he by the Tumtum tree")
     ht.put("line_12", "And stood awhile in thought.")


     # # print out our HT
     # for ind in range(8):
     #      slot_num = ht.slots[ind]
     #      print(f' slot_num: {ind} key: {slot_num.key} value: {slot_num.value}' )

     print(f" total items stored {ht.items_stored}")
     print(f" \t **** GET test")

     print(ht.get("line_1"))
     print(ht.get("line_3"))
   
     ht.put("line_1", " You been rewritten ")
     ht.put("line_3", "AGAIN, this was rewritten,")
     ht.put("line_12", " GOT  a rewrite ")

     print("")

     print(ht.get("line_1"))
     print(ht.get("line_3"))
     print(ht.get("line_12"))

     print(f" \t **** DELETE test ")
     # ht.delete("line_1")
     # ht.get("line_1")

     # print(f' $$$$$    Show entire table $$$$$$$$ \n')
     # print(f' all slots {ht.slots}')
     # print(ht.slots)
     # # Test storing beyond capacity
     # for i in range(1, 13):
     #      print(ht.get(f"line_{i}"))

     # # Test resizing
     # old_capacity = ht.get_num_slots()
     # ht.resize(ht.capacity * 2)
     # new_capacity = ht.get_num_slots()

     # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

     # # Test if data intact after resizing
     # for i in range(1, 13):
     #      print(ht.get(f"line_{i}"))

     # print("")

## First pass
# print(f' ht capacity  is >> {ht.capacity} ')
# print(ht.slots)
# print(ht.get(1))
# print(ht.get(100))

# print(ht.put(2, "Apple"))
# print(ht.put(3, "Orange"))
# print(ht.slots)

# print(ht.put(200, "Apple"))
# print(ht.slots)

# print(ht.delete(2))
# print(ht.slots)

# print(ht.delete(100))

# print(ht.hash_index("Value"))
# print("")
# print(ht.hash_index("line_1"))
# print(ht.hash_index("LLLine_1"))

# print(f'{177622 % 8}')
# print(f'{5381 << 5}')