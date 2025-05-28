#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Company, Dev, Freebie

# Create engine and session
engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
session = Session(bind=engine)

# Clear existing data (in proper order due to FK constraints)
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()
session.commit()

# ----------------------------
# 1. Create Companies
# ----------------------------
techcorp = Company(name="TechCorp", founding_year=1999)
innosoft = Company(name="InnoSoft", founding_year=2005)

# ----------------------------
# 2. Create Devs
# ----------------------------
alice = Dev(name="Alice")
bob = Dev(name="Bob")

# ----------------------------
# 3. Create Freebies via Object Relationships
# ----------------------------
freebie1 = Freebie(item_name="Cool Sticker", value=10, company=techcorp, dev=alice)
freebie2 = Freebie(item_name="T-Shirt", value=20, company=innosoft, dev=bob)
freebie3 = Freebie(item_name="Keychain", value=5, company=techcorp, dev=bob)  # extra for better tests

# ----------------------------
# 4. Add All and Commit
# ----------------------------
session.add_all([techcorp, innosoft, alice, bob, freebie1, freebie2, freebie3])
session.commit()

print("✅ Seed data added successfully.")

