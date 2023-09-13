### 1. virutal Environment Create
python3 -m venv venv

### 2. Activate Virtual Environment
source venv/bin/activate

### 3. package installation
pip install -r requirements.txt

### 4. Makemigrations and Migrate
python manage.py makemigrations
python manage.py migrate

### 5. SuperUser Create
python manage.py createsuperuser

### Run Server
python manage.py runserver