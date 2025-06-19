class Toyota():
    #class attributes -> because they are common to the class Toyota
    logo = "Toyota"
    service_Center = "toyota_Center" # All toyota can be serviced at this center
    def __init__(self, model, trim, year, center):
        #instance attributes -> because they are unique to each toyota
        self.model = model
        self.trim = trim
        self.year = year
        self.center = center # it can serve a specific trim
        
#creating instances
fav1 = Toyota("Fortuner", "SUV", 2023)
fav2 = Toyota("Crown", "Sedan", 2020)
fav3 = Toyota("Fielder", "Hatchback", 2019)

print(fav1.model, fav2.trim, fav3.year)