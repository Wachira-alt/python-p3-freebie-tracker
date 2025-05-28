#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
session = Session(bind=engine)

def test_relationships():
    print("=== All Companies and their Freebies ===")
    companies = session.query(Company).all()
    for company in companies:
        print(f'{company.name} founded in {company.founding_year}')
        for freebie in company.freebies:
            print(f'  Freebie: {freebie.item_name}, Value: {freebie.value}')
        print()

    print("=== All Devs and their Freebies ===")
    devs = session.query(Dev).all()
    for dev in devs:
        print(f'Dev: {dev.name}')
        for freebie in dev.freebies:
            print(f'  Freebie: {freebie.item_name} from {freebie.company.name}')
        print()

    print("=== Test Freebie print_details() method ===")
    freebies = session.query(Freebie).all()
    for freebie in freebies:
        freebie.print_details()

if __name__ == "__main__":
    test_relationships()
