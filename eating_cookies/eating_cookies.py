'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n): # Runtime is O(c^n)
#     # If value is negative, return 0
#     if n < 0:
#         return 0
#     # if value is 0, that means there's one way of eating the cookies (TBC)
#     elif n == 0:
#         return 1
#     else:
#         return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
    

# the cache allows us to save our work
# cache is a dictionary where keys is the n, value is the answer
def eating_cookies(n, cache): # runtime O(n)
    # If value is negative, return 0
    if n < 0:
        return 0
    # if value is 0, that means there's one way of eating the cookies (TBC)
    elif n == 0:
        return 1
    # check if answer is in our cache
    elif cache[n] > 0:
        return cache[n]
    # otherwise, cache doesnt't contain answer, so we wil use recursive logic
    #. and save it in our cache
    else:
        cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)
        
    return cache[n]
    
    


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 100
    cache = {i: 0 for i in range(num_cookies+1)}
    
    print(f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to each {num_cookies} cookies")
