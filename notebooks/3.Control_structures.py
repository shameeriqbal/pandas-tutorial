
# coding: utf-8

# This exercise will show case two things:
#     1. Control structures
#     2. How to structure your program correctly
#    
# ### Control structures
# Similar to other languages Python support various control structures such as:
#     1. If...else
#     2. For
#     3. While
#     4. Break, continue
#     5. But, no swtich
# ### Making our Program DRY
# 
# DRY stands for Don't repeat yourselves
# 
# One should not repeat the same functionality or copy the same code again. So, we use functions just like the one we did in the previous exercise.
# 
# However, the way we structured the program does not work well in the context of import.
# 
# ### Define a new function

# In[1]:

def print_n_stars(n):
    """
    Prints n no. of stars
    
    Arguments:
    n: number of stars to print
    """
    for i in range(n):
        print "*", # having a ',' tells print not to insert a new line after print

    print '' # inserts a new line after the loop
    return


# ### Changing how function is called
# Instead of immedialtely calling the function, we wrap the function call with an if condition:
# ~~~~
# if __name__ == '__main__':
# ~~~~
# Which is check if the script is run alone.

# In[2]:

if __name__ == '__main__':
    m = 5
    i = 0
    while True:
        if i < m:
            i = i +1
            print_n_stars(i)
        else:
            break


# However, this function call will not imported when imported in other scripts.
