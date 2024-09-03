from sqlalchemy import (
    create_engine, Table, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

#create a class-basedd model for the "Programmer" table
# class Programmer(base):
#     __tablename__ = "Programmer"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     gender = Column(String)
#     nationality = Column(String)
#     famous_for = Column(String)

#create a class-based model for the "Your Favourite Places" table
class FavouritePlaces(base):
     __tablename__ = "FavouritePlaces"
     id = Column(Integer, primary_key=True)
     country_name = Column(String)
     capital_city = Column(String)
     population = Column(String)
     famous_tourist_site = Column(String)

# Instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
#opens an actual session by calling the Session() subclass defined above
session = Session()

#creating the database using declarative_base subclass
base.metadata.create_all(db)


#creating records on the Your Favourite Places table
egypt = FavouritePlaces(
     country_name ="Egypt",
     capital_city ="Cairo",
     population="109 Million",
     famous_tourist_site="Pyramids of Giza"
)
brazil = FavouritePlaces(
     country_name ="Brazil",
     capital_city ="Rio de Janeiro",
     population="217 Million",
     famous_tourist_site=" UNESCO World Heritage site"
)

united_arab_emirates = FavouritePlaces(
     country_name ="UAE",
     capital_city ="Dubai",
     population="10 Million",
     famous_tourist_site="Burj Khalifa"
)
uganda = FavouritePlaces(
     country_name ="Uganda",
     capital_city ="Kampala",
     population="42 Million",
     famous_tourist_site="Kampala Museum"
)

zimbabwe = FavouritePlaces(
     country_name ="Zimbabwe",
     capital_city ="Harare",
     population="16 Million",
     famous_tourist_site="Victoria Falls"
)

guatemala = FavouritePlaces(
     country_name ="Guatemala",
     capital_city ="Guatemala City",
     population="20 Million",
     famous_tourist_site="Tika"
)

singapore = FavouritePlaces(
     country_name ="Singapore",
     capital_city ="Singapore",
     population="6 Million",
     famous_tourist_site="Marina Bay Sands"
)


#add each instance of our favourite places to our session
#session.add(egypt)
#session.add(brazil)
#session.add(united_arab_emirates)
#session.add(uganda)
#session.add(zimbabwe)
#session.add(guatemala)
#session.add(singapore)

# commit our session to the database
#session.commit()

# updating a single favourite place record
#favourite_place = session.query(FavouritePlaces).filter_by(id=9).first()
#favourite_place.famous_tourist_site = "Infinity Pool"

# commit our session to the database
#session.commit()

# updating multiple records to favourite places to capitalise every CAPITAL CITYcolumn
capital_cities = session.query(FavouritePlaces).all()

# loop over each capital city in the list and apply conditional logic to update the capital city column accordingly
#for capital in capital_cities:
    #Access the capital cities column
    #capital_city_names = capital.capital_city

    # convert the site name to uppercase
    #capital_city_name_upper = capital_city_names.upper()

    # Apply conditional logic based on the uppercase site name
    # if capital_city_name_upper.startswith("CAIRO"):
    #     capital.capital_city = "CAIRO"
    # elif capital_city_name_upper.startswith("RIO DE JANEIRO"):
    #     capital.capital_city = "RIO DE JANEIRO"
    # elif capital_city_name_upper.startswith("DUBAI"):
    #     capital.capital_city = "DUBAI"
    # elif capital_city_name_upper.startswith("KAMPALA"):
    #     capital.capital_city = "KAMPALA"
    # elif capital_city_name_upper.startswith("HARARE"):
    #     capital.capital_city = "HARARE"
    # elif capital_city_name_upper.startswith("GUATEMALA CITY"):
    #     capital.capital_city = "GUATEMALA CITY"
    # elif capital_city_name_upper.startswith("SINGAPORE"):
    #     capital.capital_city = "SINGAPORE"
    # else:
    #     print(f"Capital City: {capital_city_name_upper} - is not specifically categorized.")

    # session.commit()

# deleting a single record from the favourite place database
countryName = input("Enter a country: ")
capital_city_name = input("Enter the country's capital city: ")
country_spec = session.query(FavouritePlaces).filter_by(country_name=countryName, capital_city=capital_city_name).first()
# defensive programming
if country_spec is not None:
     print("Country Found: ", country_spec.country_name + " " + country_spec.capital_city)
     confirmation = input("Are you sureyou want to delete this country record? (y/n) ")
     if confirmation.lower() == "y":
         session.delete(country_spec)
         session.commit()
         print("country deleted successfully")
     else:
         print("Country not deleted")
else:
     print("Country not found")


# create a session to find all the favourite places
favourite_places = session.query(FavouritePlaces)
for favourite_place in favourite_places:
    print(
        favourite_place.id,
        favourite_place.country_name,
        favourite_place.capital_city,
        favourite_place.population,
        favourite_place.famous_tourist_site,
        sep=" | "
    )

#creating records on our Programmer table
# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="F",
#     nationality="British",
#     famous_for="First Programmer"
# )

# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="M",
#     nationality="British",
#     famous_for="Modern Computing"
# )

# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="F",
#     nationality="American",
#     famous_for="COBOL Language"
# )

# margaret_hamilton = Programmer(
#     first_name="Margaret",
#     last_name="Hamilton",
#     gender="F",
#     nationality="American",
#     famous_for="Aollo 11"
# )

# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="M",
#     nationality="American",
#     famous_for="Microsoft"
# )

# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="M",
#     nationality="British",
#     famous_for="World Wide Web"
# )
# terence_zengeya = Programmer(
#     first_name="Terence",
#     last_name="Zengeya",
#     gender="M",
#     nationality="Zimbabwean",
#     famous_for="Full Stack Development"
# )

#add each instance of our progrmmers to our session
#session.add(ada_lovelace)
#session.add(alan_turing)
#session.add(grace_hopper)
#session.add(margaret_hamilton)
#session.add(bill_gates)
#session.add(tim_berners_lee)
#session.add(terence_zengeya)

# commit our session to the database
#session.commit()

# updating a single record
#programmer = session.query(Programmer).filter_by(id=13).first()
#programmer.famous_for = "World President"

# commit our session to the database
#session.commit()

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sureyou want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer deleted successfully")
#     else:
#         print("Programmer not deleted")
# else:
#     print("Programmer not found")

#query the database to find all programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )