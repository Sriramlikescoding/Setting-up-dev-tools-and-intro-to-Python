TripLength = int(input("How many days will your trip be? \n" ))

#Calculating for car
CarWorth = int(input("\nEnter the daily price of the rental car: \n"))
CarCost = TripLength*CarWorth

#Calculating for hotel
HotelWorth = int(input("\n Enter the daily price of the hotel:\n"))
HotelCost = TripLength*HotelWorth

#Calculating for plane
PlaneCost1 = int(input("\n How much will the plane ride there cost? \n"))
PlaneCost2 = int(input("\n How much will the plane ride back cost? \n"))

#Calculating total cost
print("Your trip's base cost will be:", CarCost+HotelCost+PlaneCost1+PlaneCost2)