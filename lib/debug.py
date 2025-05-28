#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
session = Session(bind=engine)

def test_relationships():
    # print("=== All Companies and their Freebies ===")
    # companies = session.query(Company).all()
    # for company in companies:
    #     print(f'{company.name} founded in {company.founding_year}')
    #     for freebie in company.freebies:
    #         print(f'  Freebie: {freebie.item_name}, Value: {freebie.value}')
    #     print()

    # print("=== All Devs and their Freebies ===")
    # devs = session.query(Dev).all()
    # for dev in devs:
    #     print(f'Dev: {dev.name}')
    #     for freebie in dev.freebies:
    #         print(f'  Freebie: {freebie.item_name} from {freebie.company.name}')
    #     print()

    # print("=== Test Freebie print_details() method ===")
    # freebies = session.query(Freebie).all()
    # for freebie in freebies:
    #     freebie.print_details()

    # dev = session.query(Dev).first()
    # print(dev)
    # print(dev.companies)  # Should show all companies that gave freebies to this dev

    # company = session.query(Company).first()
    # print(company)
    # print(company.devs)   # Should show all devs who got freebies from this company
    # Setup DB and session


    # Fetch sample data
    company1 = session.query(Company).filter_by(name="TechCorp").first()
    company2 = session.query(Company).filter_by(name="InnoSoft").first()

    dev1 = session.query(Dev).filter_by(name="Alice").first()
    dev2 = session.query(Dev).filter_by(name="Bob").first()

    freebie1 = session.query(Freebie).filter_by(item_name="Cool Sticker").first()
    freebie2 = session.query(Freebie).filter_by(item_name="T-Shirt").first()

    # TEST relationships
    print("Dev1 Freebies:", dev1.freebies)
    print("Company2 Freebies:", company2.freebies)
    freebie1.print_details()

    # # TEST Company.give_freebie()
    # new_freebie = company1.give_freebie(dev2, "Laptop Sticker", 30)
    # session.add(new_freebie)
    # session.commit()
    # print(f"New Freebie: {new_freebie}")
    # new_freebie.print_details()

    # #  TEST Dev.received_one()
    # print("Did Bob receive a T-Shirt?", dev2.received_one("T-Shirt"))   # True
    # print("Did Alice receive a Laptop Sticker?", dev1.received_one("Laptop Sticker"))  # False

    # #  TEST Dev.give_away()
    # print("Before giving away:", dev1.freebies)
    # success = dev1.give_away(dev2, freebie1)
    # session.commit()
    # print("Give away successful?", success)
    # print("After giving away:")
    # print("Alice:", dev1.freebies)
    # print("Bob:", dev2.freebies)

    # #  TEST Company.oldest_company()
    # oldest = Company.oldest_company(session)
    # print("Oldest Company:", oldest)


if __name__ == "__main__":
    test_relationships()
