def top_n (items, n):
    """Return the top n items in an array inndescending order.
    Args:
        items (array): list or arrays like objects
        n (int): Number of items to return

    Return:
        array: top n items, in descending order.
    
    Example:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
    """
    for i in range(n): #keeps sorting until we have a top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]: #if it's bigger than the next item
                items[j], items[j+1] = items[j+1], items[j]  #swap both

    top_n = items[-n:]

    return top_n[::-1]