#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
session = Session(bind=engine)

# Clear existing data (optional, but useful during development)
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()
session.commit()

# Create Companies
company1 = Company(name="TechCorp", founding_year=1999)
company2 = Company(name="InnoSoft", founding_year=2005)

# Create Devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

session.add_all([company1, company2, dev1, dev2])
session.commit()

# Create Freebies
freebie1 = Freebie(item_name="Cool Sticker", value=10, company_id=company1.id, dev_id=dev1.id)
freebie2 = Freebie(item_name="T-Shirt", value=20, company_id=company2.id, dev_id=dev2.id)

session.add_all([freebie1, freebie2])
session.commit()

print("Seed data added successfully.")
