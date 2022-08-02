from secrets import choice
from faker import Faker
from faker import *
from faker.providers import BaseProvider
import csv
import datetime
from random import *
from random import choice

fake = Faker()


class MyProvider(BaseProvider):
    __provider__ = "types"
    __provider__ = "description"
    __provider__ = "location_description"

    def types(self):
        types = [
            "ASSAULT",
            "BATTERY",
            "BURGLARY",
            "CRIMINAL DAMAGE",
            "MOTOR VEHICLE THEFT",
            "NARCOTICS",
            "OFFENSE INVOLVING CHILDREN",
            "OTHER OFFENSE",
        ]
        return choice(types)

    def description(self):
        description = ["SIMPLE", "AGGREVATED", "RECKLESS CONDUCT", "UNLAWFUL"]
        return choice(description)

    def location_description(self):
        location_description = [
            "RESIDENCE",
            "OFFICE",
            "STREET",
            "PARKING LOT",
            "STORE",
            "PARKING",
        ]
        return choice(location_description)


fake.add_provider(MyProvider)

now = datetime.datetime.now()
now_date_time = now.strftime("%d/%m/%Y %H:%M:%S %p")


def datagenerate(records, headers):

    with open("Crimes_2001_to_Present.csv", "a") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        # Only while creating a new file, we open in 'wt' mode and write header
        # writer.writeheader()
        for i in range(records):
            location_lat = str(fake.latitude())
            location_lon = str(fake.longitude())
            location_co = "(" + location_lat + ", " + location_lon + ")"

            writer.writerow(
                {
                    "ID": i,
                    "Case_Number": fake.bothify(text="H?######", letters="PQRST"),
                    "Date": fake.date_time_this_year().strftime("%x %X")
                    + " "
                    + fake.am_pm(),
                    "Block": fake.street_address(),
                    "IUCR": fake.pyint(),
                    "Primary_Type": fake.types(),
                    "Description": fake.description(),
                    "Location_Description": fake.location_description(),
                    "Arrest": fake.boolean(chance_of_getting_true=25),
                    "Domestic": fake.boolean(chance_of_getting_true=25),
                    "Beat": fake.pyint(),
                    "District": fake.pyint(1, 25),
                    "Ward": fake.pyint(1, 50),
                    "Community_Area": fake.pyint(1, 75),
                    "FBI_Code": fake.pyint(1, 30),
                    "XCoordinate": fake.pyint(1000001, 9999999),
                    "YCoordinate": fake.pyint(1000001, 9999999),
                    "Year": fake.date_between_dates(
                        datetime.date(2000, 1, 1), datetime.date(2022, 1, 1)
                    ).year,
                    "Updated_On": now_date_time,
                    "Latitude": location_lat,
                    "Longitude": location_lat,
                    "Location": location_co,
                }
            )


records = 100000
headers = [
    "ID",
    "Case_Number",
    "Date",
    "Block",
    "IUCR",
    "Primary_Type",
    "Description",
    "Location_Description",
    "Arrest",
    "Domestic",
    "Beat",
    "District",
    "Ward",
    "Community_Area",
    "FBI_Code",
    "XCoordinate",
    "YCoordinate",
    "Year",
    "Updated_On",
    "Latitude",
    "Longitude",
    "Location",
]
datagenerate(records, headers)
print("CSV generation complete!")
