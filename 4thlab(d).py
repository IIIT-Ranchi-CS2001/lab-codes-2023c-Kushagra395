#  Generate two sets – first for all singers and second for all dancers of the class
# using set comprehension. Perform set operations to generate the following sets
# a. of all artists of the class
# b. allrounders of the class
# c. dancers but not singers
# d. singers but not dancers
# e. dancers but not singers cum singers but not dancers

singers = set(input("Enter singers: ").split())
dancers = set(input("Enter dancers: ").split())

print("All artists:", singers | dancers)
print("Allrounders:", singers & dancers)
print("Dancers but not singers:", dancers - singers)
print("Singers but not dancers:", singers - dancers)
print("Symmetric difference:", dancers ^ singers)
