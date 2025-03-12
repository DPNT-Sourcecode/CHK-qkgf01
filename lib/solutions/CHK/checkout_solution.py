# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # This is for validating the input
    if not isinstance(skus, str):
        return -1

    items = {'A','B','C','D','E','F','G','H',
             'I','J','K','L','M','N','O','P','Q','R',
             'S','T','U','V','W','X','Y','Z'}

    for ch in skus:
        if ch not in items:
            return -1
        
    # Count occurrences of each SKU
    count_a = skus.count('A')
    count_b = skus.count('B')
    count_c = skus.count('C')
    count_d = skus.count('D')
    count_e = skus.count('E')
    count_f = skus.count('F')

    # Calculating total using special offers

    total = 0

    # For A
    offer_5a = count_a // 5
    remainder_5a = count_a % 5
    total_a = offer_5a * 200

    offer_3a = remainder_5a // 3
    remainder_a = remainder_5a % 3
    total_a += offer_3a * 130
    total_a += remainder_a * 50

    total += total_a

    #For E
    offer_e = count_e // 2
    free_b = min(offer_e, count_b)
    count_b -= free_b

    # For B
    offer_b = count_b // 2
    remainder_b = count_b % 2
    total_b = offer_b * 45 + remainder_b * 30
    total += total_b
   

    # For C
    total_c = count_c * 20
    total += total_c

    #For D
    total_d = count_d * 15
    total += total_d

    #For E (40 each)
    total_e = count_e * 40
    total += total_e
    
    # For F (offer)
    offer_3f = count_f // 3
    remainder_f = count_f % 3

    #Each 3 pack of F costs 20
    cost_f = offer_3f * 2 * 10
    cost_f += remainder_f * 10

    total += cost_f

    return total


