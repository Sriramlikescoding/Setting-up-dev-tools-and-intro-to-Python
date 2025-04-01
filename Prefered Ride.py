PreferedRide = input("Do you prefer to ride Bikes or Cars? (Enter answer like this Bikes / Cars): ")


if PreferedRide == 'Bikes':
    subclass = input("Do you prefer motorcycles or pedal bikes? (Enter like this: Motorcycles / Pedal Bikes)")
    if subclass == 'Motorcycles':
        print("Some brands of motorcycles include Mitsubishi, Yamaha, and BMW")
    else:
        print("Some brands of Pedal Bikes include BMX, Trek, and Giant")

else:
   subclass = input("Do you prefer sports cars or family cars? (Enter like this: Sports Cars / Family Cars)")
   if subclass == 'Sports Cars':
       print("Some brands of Sports Cars include Bugatti, Ferrari, Lamborghini")
   elif subclass == 'Family Cars':
       print("Some brands of family cars include Toyota, Honda, and Lexus")