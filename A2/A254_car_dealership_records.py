class CarRecord:
    def __init__(self, _vehicle_id, _registration, _date_of_registration,
                 _engine_size, _purchase_price):
        """Initialise the CarRecord object."""
        self.vehicle_id = _vehicle_id
        self.registration = _registration
        self.date_of_registration = _date_of_registration
        self.engine_size = _engine_size
        self.purchase_price = _purchase_price

# Creates empty dictionary to store the objects of CarRecord.
records = {}
# Repeats to allow for any amount of objects to be created.
while True:
    record_name = input("Enter record name: ")
    if record_name.lower() == "exit":
        break
    vehicle_id = input("Enter vehicle ID: ")
    registration = input("Enter registration: ")
    date_of_registration = input("Enter date of registration: ")
    engine_size = input("Enter engine size: ")
    purchase_price = input("Enter purchase price: ")
    # Creates CarRecord object and stores in records, with record_name
    # as the key.
    records[record_name] = CarRecord(vehicle_id, registration, date_of_registration,
                                     engine_size, purchase_price)