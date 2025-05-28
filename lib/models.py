from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    """Company model representing a company that gives freebies."""

    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship("Freebie", back_populates="company")
    devs = association_proxy("freebies", "dev")

    def give_freebie(self, dev, item_name: str, value: int) -> 'Freebie':
        """Create a new freebie given to a dev."""
        return Freebie(item_name=item_name, value=value, company=self, dev=dev)

    @classmethod
    def oldest_company(cls, session):
        """Return the oldest company based on founding year."""
        return session.query(cls).order_by(cls.founding_year).first()

    def __repr__(self):
        return f'<Company {self.name}>'


class Dev(Base):
    """Dev model representing developers who receive freebies."""

    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    freebies = relationship("Freebie", back_populates="dev")
    companies = association_proxy('freebies', 'company')

    def received_one(self, item_name: str) -> bool:
        """Return True if the dev has received a freebie with the given item_name."""
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, other_dev: 'Dev', freebie: 'Freebie') -> bool:
        """
        Transfer a freebie to another dev.
        Returns True if successful, False if freebie not owned.
        """
        if freebie in self.freebies:
            freebie.dev = other_dev
            return True
        return False

    def __repr__(self):
        return f'<Dev {self.name}>'


class Freebie(Base):
    """Freebie model representing items given from companies to devs."""

    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    company = relationship("Company", back_populates="freebies")
    dev = relationship("Dev", back_populates="freebies")

    def print_details(self):
        """Print details about this freebie."""
        print(f"Freebie: {self.item_name}, Value: {self.value}, Given by: {self.company.name}, Received by: {self.dev.name}")

    def __repr__(self):
        return f'<Freebie {self.item_name}>'
