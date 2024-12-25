#If the given string S1= “Maha Bharat”, generate the following strings by manipulating S1.
s0 ="Maha Bharat"
s1 = s0.upper().replace('M' ,'m').replace('B','b')
print(s1)
s2 = s0.split()[1]
print(s2)
for i in range(0,3):
    print(s2,end="") 
    
print("\nMera " + s2)
print (f"\nMera {s2} Mahan")