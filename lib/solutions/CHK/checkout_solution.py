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
    count_g = skus.count('G')
    count_h = skus.count('H')
    count_i = skus.count('I')
    count_j = skus.count('J')
    count_k = skus.count('K')
    count_l = skus.count('L')
    count_m = skus.count('M')
    count_n = skus.count('N')
    count_o = skus.count('O')
    count_p = skus.count('P')
    count_q = skus.count('Q')
    count_r = skus.count('R')
    count_s = skus.count('S')
    count_t = skus.count('T')
    count_u = skus.count('U')
    count_v = skus.count('V')
    count_w = skus.count('W')
    count_x = skus.count('X')
    count_y = skus.count('Y')
    count_z = skus.count('Z')


#----------------- Section of Free product offers -----------------

    # For 2E = 1B Free
    offer_e = count_e // 2
    free_b = min(offer_e, count_b)
    count_b -= free_b

    # For 3N = 1M Free
    offer_n = count_n //3
    free_m = min(offer_n, count_m)
    count_m -= free_m

    # For 3R = 1Q Free
    offer_r = count_r // 3
    free_q = min(offer_r, count_q)
    count_q -= free_q
# ----------------- End of secction -----------------------------


#------------------ Calculating total using special offers ---------------------

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

    # For G
    total_g = count_g * 20
    total += total_g

    # For H
    offer_10h = count_h // 10
    leftover_h10 = count_h % 10
    cost_h = offer_10h * 80

    offer_5h = leftover_h10 // 5
    remainder_h = leftover_h10 % 5
    cost_h += offer_5h * 45
    cost_h += remainder_h * 10
    total += cost_h

    # For I
    total_i = count_i * 35
    total += total_i

    # For J
    total_j = count_j * 60
    total += total_j

    # For K 
    offer_2k = count_k // 2
    remainder_k = count_k % 2
    cost_k = offer_2k * 150 + remainder_k * 80
    total += cost_k

    # For L
    total_l = count_l * 90
    total += total_l

    # For M
    total_m = count_m * 15
    total += total_m


    # For N
    total_n = count_n * 40
    total += total_n



    return total


