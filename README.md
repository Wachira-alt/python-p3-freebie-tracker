# Freebie Tracker

A simple Python project using SQLAlchemy ORM to model companies giving freebies to developers.  
This project demonstrates model relationships, association proxies, business logic, migrations, and seeding.

## Project Structure

migrations/
├─ alembic.ini
├─ debug.py
├─ freebies.db
├─ models.py
├─ seed.py
.canvas
.gitignore
CONTRIBUTING.md
LICENSE.md
Pipfile
Pipfile.lock
README.md

## Setup Instructions

### 1. Clone the repository


git clone <your-repo-url>
cd <your-repo-folder>

### 2. Create a virtual environment and install dependencies

pipenv install
pipenv shell

or using venv and pip

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3. Run Alembic migrations to create the database and tables

alembic upgrade head

### 4. Seed the database with sample data

python lib/seed.py

## Running the Application

You can test and interact with your models using the `debug.py` script:python migrations/debug.py


---

### Step 5: Models Overview

## Models Overview

### Company

- Attributes: `id`, `name`, `founding_year`
- Relationships:
  - `.freebies` — freebies given by this company
  - `.devs` — developers who have received freebies (via association proxy)
- Methods:
  - `give_freebie(dev, item_name, value)` — create and assign a new freebie to a dev
  - `oldest_company(session)` — find the oldest company by founding year

### Dev

- Attributes: `id`, `name`
- Relationships:
  - `.freebies` — freebies received by this dev
  - `.companies` — companies that gave freebies (via association proxy)
- Methods:
  - `received_one(item_name)` — check if dev has received a specific freebie
  - `give_away(other_dev, freebie)` — transfer ownership of a freebie to another dev

### Freebie

- Attributes: `id`, `item_name`, `value`, `company_id`, `dev_id`
- Relationships:
  - `.company` — company giving the freebie
  - `.dev` — dev receiving the freebie
- Methods:
  - `print_details()` — print info about the freebie and involved entities

## Testing Your Work

Run the `debug.py` script to verify:

- Model relationships (`dev.freebies`, `company.freebies`)
- Business logic (`give_freebie`, `give_away`, etc.)
- Data integrity and association proxies (`dev.companies`, `company.devs`)


## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.




