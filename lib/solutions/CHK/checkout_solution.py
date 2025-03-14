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
    
    # For F (offer)
    offer_3f = count_f // 3
    remainder_f = count_f % 3

    #Each 3 pack of F costs 20
    cost_f = offer_3f * 2 * 10
    cost_f += remainder_f * 10

    total += cost_f

    # For H
    offer_10h = count_h // 10
    leftover_h10 = count_h % 10
    cost_h = offer_10h * 80

    offer_5h = leftover_h10 // 5
    remainder_h = leftover_h10 % 5
    cost_h += offer_5h * 45
    cost_h += remainder_h * 10
    total += cost_h

    # For K 
    offer_2k = count_k // 2
    remainder_k = count_k % 2
    cost_k = offer_2k * 120 + remainder_k * 70
    total += cost_k

    # For P
    offer_5p = count_p // 5 
    remainder_p = count_p % 5
    cost_p = offer_5p * 200 + remainder_p * 50 
    total += cost_p

    # For Q
    offer_3q = count_q // 3
    remainder_q = count_q % 3
    cost_q = offer_3q * 80 + remainder_q * 30
    total += cost_q

    # For U
    offer_4u = count_u // 4
    leftover_u = count_u % 4
    cost_u = offer_4u * (3 * 40) + leftover_u * 40
    total += cost_u


    # For V
    offer_3v = count_v // 3
    remainder_v = count_v % 3
    cost_v = offer_3v * 130
    
    if remainder_v == 2:
        cost_v += 90
    elif remainder_v == 1:
        cost_v += 50

    total += cost_v

    # Handeling group discount
    group_prices = []

    group_prices.extend([21] * count_z)
    group_prices.extend([20] * count_s)
    group_prices.extend([20] * count_t)
    group_prices.extend([20] * count_y)
    group_prices.extend([17] * count_x)
    
    group_prices.sort(reverse=True)

    sets_of_3 = len(group_prices) // 3
    leftover_group = len(group_prices) % 3

    cost_group = sets_of_3 * 45

    if leftover_group > 0:
        for i in range(leftover_group):
            cost_group += group_prices[-(i+1)]
    
    total += cost_group

    # For C
    total_c = count_c * 20
    total += total_c

    #For D
    total_d = count_d * 15
    total += total_d

    #For E (40 each)
    total_e = count_e * 40
    total += total_e

    # For G
    total_g = count_g * 20
    total += total_g

    # For I
    total_i = count_i * 35
    total += total_i

    # For J
    total_j = count_j * 60
    total += total_j

    # For L
    total_l = count_l * 90
    total += total_l

    # For M
    total_m = count_m * 15
    total += total_m

    # For N
    total_n = count_n * 40
    total += total_n

    # For O
    total_o = count_o * 10
    total += total_o

    # For R
    total_r = count_r * 50
    total += total_r

    # # For S
    # total_s = count_s * 30
    # total += total_s

    # # For T
    # total_t = count_t * 20
    # total += total_t

    # For W
    total_w = count_w * 20
    total += total_w

    # # For X
    # total_x = count_x * 90
    # total += total_x

    # # For Y
    # total_y = count_y * 10
    # total += total_y

    # # For Z
    # total_z = count_z * 50
    # total += total_z

    return total

