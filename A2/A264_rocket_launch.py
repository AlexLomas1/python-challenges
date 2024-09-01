import math

class Planet:
    def __init__(self,planet_name,mass,radius):
        """Initialise the Planet instance."""
        self.planet_name = planet_name
        self.mass = mass
        self.radius = radius * 1000 # Converting from kilometres to metres.
    def calc_escape_velocity(self):
        """Calculate the escape velocity of the planet in km/s."""
        G = 6.67430 * 10**-11 # Universal gravitational constant.
        escape_velocity = math.sqrt((2 * G * self.mass) / self.radius)
        # Converts escape velocity from m/s to km/s.
        escape_velocity = escape_velocity / 1000
        # Rounding escape velocity to 2 decimal places.
        return round(escape_velocity,3)
    def display_escape_velocity(self):
        """Print the escape velocity of the planet."""
        escape_velocity = self.calc_escape_velocity()
        print(f"{self.planet_name}'s escape velocity is approximately {escape_velocity} km/s")
    
planet_name = input("Enter planet name: ")
mass = float(input("Enter planet's mass in kilograms: "))
radius = float(input("Enter planet's radius in kilometres: "))
user_planet = Planet(planet_name,mass,radius)
user_planet.display_escape_velocity()