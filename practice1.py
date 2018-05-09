from datetime import datetime
from math import *

now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
print ("The date is %02d-%02d-%04d" % (current_day,current_month,current_year))

def hotel_cost(days):
  nights = days - 1
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city,days,spending_money):
    sum = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    return sum

