def get_ground(weight):
    if weight > 10:
        cost_per_lb = 4.75
    elif weight > 6:
        cost_per_lb = 4.00
    elif weight > 2:
        cost_per_lb = 3.00
    else:
        cost_per_lb = 1.50
    ground_cost = weight * cost_per_lb + 20
    return ground_cost


premium_ground_cost = 125


def get_drone(weight):
    if weight > 10:
        cost_per_lb = 14.25
    elif weight > 6:
        cost_per_lb = 12.00
    elif weight > 2:
        cost_per_lb = 9.00
    else:
        cost_per_lb = 4.50
    drone_cost = weight * cost_per_lb
    return drone_cost


def print_get_cheapest(weight):
    weight = float(input("Enter item weight:"))
    ground = get_ground(weight)
    drone = get_drone(weight)
    premium = premium_ground_cost
    if ground < drone and ground < premium:
        method = "Standard Ground"
        cost = ground
    elif drone < ground and drone < premium:
        method = "Drone"
        cost = drone
    else:
        method = "Premium Ground"
        cost = premium
    print(f'''The cheapest method is {method}
at a cost of ${cost:.2f}''')


print_get_cheapest(41.5)