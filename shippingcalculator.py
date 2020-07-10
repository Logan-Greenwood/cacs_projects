def ground_shipping(weight):
    if weight > 10:
        cost = weight * 4.75 + 20.00
    elif weight > 6:
        cost = weight * 4.00 + 20.00
    elif weight > 2:
        cost = weight * 3.00 + 20.00
    else:
        cost = weight * 1.50 + 20.00
    return cost


#print(ground_shipping(8.4))


premium_ground_shipping = 125.00


def drone_shipping(weight):
    if weight > 10:
        cost = weight * 14.25
    elif weight > 6:
        cost = weight * 12.00
    elif weight > 2:
        cost = weight * 9.00
    else:
        cost = weight * 4.50
    return cost

#print(drone_shipping(1.5))


def cheapest_shipping(weight):
    gs_cost = ground_shipping(weight)
    ds_cost = drone_shipping(weight)
    pgs_cost = premium_ground_shipping
    if gs_cost < ds_cost and gs_cost < pgs_cost:
        method = "Standard ground shipping"
        cost = gs_cost
    elif ds_cost < gs_cost and ds_cost < pgs_cost:
        method = "Drone shipping"
        cost = ds_cost
    else:
        method = "Premium ground shipping"
        cost = pgs_cost

    print(f'''{method} is the cheapest 
method of shipping with a cost of ${cost:.2f}.''')

cheapest_shipping(41.5)
