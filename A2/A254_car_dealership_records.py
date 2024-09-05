class CarRecord:
    def __init__(self, _vehicle_id, _registration, _date_of_registration, _engine_size, _purchase_price):
        """Initialise the CarRecord object."""
        self.vehicle_id = _vehicle_id
        self.registration = _registration
        self.date_of_registration = _date_of_registration
        self.engine_size = _engine_size
        self.purchase_price = _purchase_price

# Creates empty list to store the objects of CarRecord.
records = []
# Repeats to allow for any amount of objects to be created.
while True:
    record_name = input("Enter record name: ")
    vehicle_id = input("Enter vehicle ID: ")
    registration = input("Enter registration: ")
    date_of_registration = input("Enter date of registration: ")
    engine_size = input("Enter engine size: ")
    purchase_price = input("Enter purchase price: ")
    # Creates CarRecord object with the name record_name
    globals()[record_name] = CarRecord(vehicle_id, registration, date_of_registration, engine_size, purchase_price)
    # Adds current CarRecord object to the list records.
    records.append(globals()[record_name])
