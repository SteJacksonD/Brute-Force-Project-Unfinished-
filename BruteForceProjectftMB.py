wimport sys
import hashlib
from itertools import permutations

  # Function to find permutations of a given string
def allPermutations(str, chars):
    # Get all permutations of string 'ABC'
    permList = permutations(str, chars)
    return list(permList)
    '''
    # print all permutations
    for perm in list(permList):
    print (''.join(perm))
    '''  
#Main goal convert the hash back to the actual password

  # take user input of hash
hash = input("Enter hash: ")  # MD5 hash
#Takes user input of Passwword
bank = "abcdefghijklmnopqrstuvwxyz1234567890"
counter = 0
test_counter = 0
running = True
while running:
  print("Number of characters: " + str(counter))
  counter += 1
  print("Number of characters: " + str(counter))
  perms = allPermutations(bank, counter)
  for test_value in perms:
    test_string = ''.join(element for element in test_value)
    test_hash = hashlib.md5(str(test_string).encode('utf-8')).hexdigest()
    
    test_counter += 1
    if test_counter % 10000 == 0:
          print(str(test_counter) + " permutations calculated")
    
    if test_hash == hash:
      string = str(test_string)
      running = False
      break
  
print(hash + " is \"" + string + "\" in string from")