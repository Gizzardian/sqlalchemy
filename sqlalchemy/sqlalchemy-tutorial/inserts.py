# imports
from datetime import date
from actor import Actor
from base import Session, engine, Base 
from contact_details import ContactDetails
from movie import Movie
from stuntman import Stuntman

# generate database schema
Base.metadata.create_all(engine)

# create a new session
session = Session()

# create movies
bourne_identity = Movie("The Bourne Identity", date(2002, 10, 11))
furious_7 = Movie("Furious 7", date(2015, 4, 2))
pain_and_gain = Movie("Pain & Gain", date(2013, 8, 23))

# create actors
matt_damon = Actor("Matt Damon", date(1970, 10, 8))
dwayne_johnson = Actor("Dwayne Johnson", date(1972, 5, 2))
mark_wahlberg = Actor("Mark Wahlberg", date(1971, 6, 5))

# add actors to movies
bourne_identity.actors = [matt_damon]
furious_7.actors = [dwayne_johnson]
pain_and_gain.actors = [mark_wahlberg]

# add contact details to actors
matt_contact = ContactDetails("415 555 2543", "Burbank, CA", matt_damon)
dwayne_contact = ContactDetails("234 23 2343", "Glendale, CA", dwayne_johnson)
dwayne_contact_2 = ContactDetails("231 12 1212", "West Hollywood, CA", dwayne_johnson)
mark_contact = ContactDetails("234 23 2545", "Glendale, CA", mark_wahlberg)

# create stuntmen
matt_stuntman = Stuntman("John Doe", True, matt_damon)
dwayne_stuntman = Stuntman("John Roe", True, dwayne_johnson)
mark_stuntman = Stuntman("Richard Doe", True, mark_wahlberg)

# persist data
session.add(bourne_identity)
session.add(furious_7)
session.add(pain_and_gain)

session.add(matt_contact)
session.add(dwayne_contact)
session.add(dwayne_contact_2)
session.add(mark_contact)

session.add(matt_stuntman)
session.add(dwayne_stuntman)
session.add(mark_stuntman)

# commit and close session

session.commit()
session.close()