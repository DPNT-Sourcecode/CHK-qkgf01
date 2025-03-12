# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # This is for validating the input
    if not isinstance(skus, str):
        return -1

    items = {'A','B','C','D'}

    for ch in skus:
        if ch not in items:
            return -1
        
    # Count occurrences of each SKU
    count_a = skus.count('A')
    count_b = skus.count('B')
    count_c = skus.count('C')
    count_d = skus.count('D')

    # Calculating total using special offers

    total = 0

    # For A
    


