global choice 
def add(num_1 , num_2 , num_3) :

    return num_1 + num_2 + num_3

def sub (num_1 , num_2 , num_3) :
    
    return num_1 - num_2 - num_3

def mutiply (num_1 , num_2 , num_3) :
    
    return num_1 * num_2 * num_3 

def division (num_1 , num_2) :
    
    choice = input (f"Do you want to divide {num_1} by {num_2} (Yes / No)?? ")
    
    if choice.lower() == "yes":
    
        return num_1 / num_2
    
    else :
        return num_2 / num_1 
    
