# Getting user input
city_flight = input("Enter the city you will be flying to (New York, Paris, Tokyo): ")
num_nights = int(input("Enter the number of nights you will be staying at the hotel: "))
rental_days = int(input("Enter the number of days you will be hiring a car: "))


def hotel_cost(num_nights):
    price_per_night = 100  # Assuming the price per night is $100
    return num_nights * price_per_night

def plane_cost(city_flight):
    if city_flight == "New York":
        return 500  # Flight cost to New York is $500
    elif city_flight == "Paris":
        return 800  # Flight cost to Paris is $800
    elif city_flight == "Tokyo":
        return 1000  # Flight cost to Tokyo is $1000
    else:
        return 0

def car_rental(rental_days):
    daily_rental_price = 50  # Assuming the daily rental price is $50
    return rental_days * daily_rental_price

def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

 
# Calculating costs
hotel_total = hotel_cost(num_nights)
plane_total = plane_cost(city_flight)
car_total = car_rental(rental_days)
holiday_total = holiday_cost(hotel_total, plane_total, car_total)

# Printing holiday details
print("Holiday Details:")
print(f"City of Flight: {city_flight}")
print(f"Hotel Cost: ${hotel_total}")
print(f"Flight Cost: ${plane_total}")
print(f"Car Rental Cost: ${car_total}")
print(f"Total Holiday Cost: ${holiday_total}")