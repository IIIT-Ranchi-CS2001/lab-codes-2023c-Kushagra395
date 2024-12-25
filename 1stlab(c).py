#write a python code to find equivalent impdance when two impedence z1,z2 are connect connectd in parallel
def calculate_parallel_impedance(z1, z2):
     
        
    z1 = complex(z1)
    z2 = complex(z2)
    

    z_eq = (z1 * z2) / (z1 + z2)
    return z_eq



print("Calculate Equivalent Impedance for Two Impedances in Parallel")

    
z1 = input("Enter the first impedance (e.g., 5+3j): ")
z2 = input("Enter the second impedance (e.g., 4-2j): ")


result = calculate_parallel_impedance(z1, z2)


print(f"The equivalent impedance is: {result}")

 
