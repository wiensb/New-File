class Temperatures:
    def __init__ (city, name):
        city.name = name
        city.temp = []
    
    def enterTemp(city):
        for i in range(3):
            t = float(input("Enter the Tempuratures of %s on day %d: "%(city.name,i+1)))
            city.temp.append(t)
            
    def displayTemp(city):
        print(city.name, " recorded the following temperatures", city.temp)
    
    def calcAverageTemp(city):
        sumtemps = sum(city.temp)
        average = sumtemps/len(city.temp)
        print("The average temperature for %s across these days was:"%str(city.name)," %.1f" % float(str(average)))

city1 = Temperatures("Toronto")
city1.enterTemp()

city2 = Temperatures("Vancouver")
city2.enterTemp()

city3 = Temperatures("Ottawa")
city3.enterTemp()

city1.displayTemp()
city2.displayTemp()
city3.displayTemp()
 
city1.calcAverageTemp()
city2.calcAverageTemp()
city3.calcAverageTemp()

input("ENTER")


