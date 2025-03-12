# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # This is for validating the input
    if not isinstance(skus, str):
        return -1

    items = {'A','B','C','D','E'}

    for ch in skus:
        if ch not in items:
            return -1
        
    # Count occurrences of each SKU
    count_a = skus.count('A')
    count_b = skus.count('B')
    count_c = skus.count('C')
    count_d = skus.count('D')
    count_e = skus.count('E')

    # Calculating total using special offers

    total = 0

    # For A
    offer_a = count_a // 3
    remainder_a = count_a % 3
    total += offer_a * 130 + remainder_a * 50

    offer_5a = count_a // 5
    remainder_5a = count_a % 5
    total_a = offer_5a * 200

    # For B
    offer_b = count_b // 2
    remainder_b = count_b % 2
    total += offer_b * 45 + remainder_b * 30

    # For C
    total += count_c * 20

    # For D
    total += count_d * 15

    #For E
    offer_e = count_e // 2
    free_b = min(offer_e, count_b)
    count_b -= free_b

    total += count_e * 40

    return total

