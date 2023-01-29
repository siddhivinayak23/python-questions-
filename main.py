'''Write a python program to read the age of a candiadte and detrermine whether it is eligible for casting his/her own vote'''

vote_age = int(input("Enter your age: "))

if vote_age > 18:
  print(
    f"Congratulastion! You are age {vote_age} eligible for casting your vote")
else:
  print(f"Sorry, You are age {vote_age} less for casting vote..")