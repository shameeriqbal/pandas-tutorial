
# coding: utf-8

# We will create a function to find if a given number is even or odd.
# ### Create a function called even_or_odd

# In[1]:

def even_or_odd(num):
    """
    Prints if the given number is even or odd
    
    Arguments:
    num: number to check 
    """
    
    # use the modulus to see if the division has any reminder
    if num % 2 == 0:
        # if the reminder is 0, then the number is even
        print num, " is even!"
    else:
        # if the reminder is not 0, then its odd
        print num, " is odd!"
    
    return


# ### Call the function with an even number

# In[2]:

even_or_odd(20)


# ### Call the function with an odd number

# In[3]:

even_or_odd(17)

