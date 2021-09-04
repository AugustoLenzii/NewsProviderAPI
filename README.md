# Instructions and documentation
## Documentation -> [Here](https://app.swaggerhub.com/apis-docs/augustolenzi/NewsProviderAPI/1.0.0) 
## Running for development
### 1- Clone this repository
```
git clone https://github.com/AugustoLenzii/NewsProviderAPI.git
```
### 2- Cd into _NewsProviderAPI_ and install the requirements
```
cd NewsProviderAPI
pip install -r requirements.txt
```
### 3- Start the container
```
docker-compose -f docker-compose.yml up -d
```
### 4- Migrate the models
```
python manage.py migrate
```
### 5- Run the server
```
python manage.py runserver
```
### 6- Open any REST app to send requests to it
```
http://localhost:8000/api/
```
## Running for Production
### 1- Clone this repository
```
git clone https://github.com/AugustoLenzii/NewsProviderAPI.git
```
### 2- Cd into _NewsProviderAPI_ and install the requirements
```
cd NewsProviderAPI
pip install -r requirements.txt
```
### 3- Turn Debug off and change the DATABASE settings so the HOST look like this
```
DEBUG = False
```
```
'HOST': 'db'
```
### 4- Start the container
```
docker-compose -f docker-compose.prod.yml up -d
```
### 5- Migrate the models
```
docker container exec newsproviderapi_web_1 python /core/manage.py migrate
```
### 6- Open any REST app to send requests to it
```
http://<server address>:8000/api/
```
