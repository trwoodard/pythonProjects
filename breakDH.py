# A proof of concept for how the Diffie-Hellman Key Exchange Protocol can be broken if a small numbers are chosen for the prime, generator, and secret integers. 


# This takes in the secret integer values, a and b, and will calulate public values using the formula g^s mod p.
def check_public(a, A, b, B):
    check_a = (g ** a) % p
    check_b = (g ** b) % p
    if check_a == A and check_b == B:
        return True


# The main component of the script, which iterates through a range of values to guess the secret integers, a and b.
# In order to guess these values, the script must check that the formula A^b mod p = B^a mod p. 
# If the following is true, then the script checks if the values for a and b also create the correct public values.
def find_secrets():
    for i in range(1, 100):
        a = i
        formula_a = (B ** a) % p
        for i in range(1, 100):
            b = i
            formula_b = (A ** b) % p
            if formula_a == formula_b:
                if check_public(a, A, b, B):
                    return a, b


# Check whether the shared secret keys are equal.                
def calc_shared_secret(a, A, b, B):
    K1 = (B**a) % p
    K2 = (A**b) % p
    if K1 == K2:
        return K1, K2


# Print out a solution statement with all the values.     
def solution_statement(a, b, K1, K2):
    print(f"""
    Here is the solution:
    p = {p}
    g = {g}
    a = {a}
    b = {b}
    A = {A}
    B = {B}
    
    Here's the proof:
    A = (g**a) mod p should be {A}
    A = ({g}**{a}) mod {p} = {A}
    B = (g**b) mod p should be {B}
    B = ({g}**{b}) mod {p} = {B}
    
    To check the numbers, we check whether:
    ((B**a) mod p) == ((A**b) mod p) 
    (({B}**{a}) mod {p}) = {K1} == (({A} ** {b}) mod {p}) = {K2}
    
    So the shared secret is: {K1}          
    """)


# Main portion of the script, using the previously-defined functions.    
def break_dh():
    a, b = find_secrets()
    K1, K2 = calc_shared_secret(a, A, b, B)
    if calc_shared_secret(a, A, b, B):
        solution_statement(a, b, K1, K2)


if __name__ == '__main__':
    break_dh()
