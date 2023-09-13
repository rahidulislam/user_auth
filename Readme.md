### virutal Environment Create
python3 -m venv venv

### Activate Virtual Environment
source venv/bin/activate

### package installation
pip install -r requirements.txt

### Makemigrations and Migrate
python manage.py makemigrations
python manage.py migrate

### SuperUser Create
python manage.py createsuperuser

### Run Server
python manage.py runserver