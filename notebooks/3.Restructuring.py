
# coding: utf-8

# ### Making our Program DRY
# 
# DRY stands for Don't repeat yourselves
# 
# One should not repeat the same functionality or copy the same code again. So, we use functions just like the one we did in the previous exercise.
# 
# However, the way we structured the program does not work well in the context of import.
# 
# ### Define a new function

# In[2]:

def print_n_stars(n):
    """
    Prints n no. of stars
    
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


# 

# In[ ]:



