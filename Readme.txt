LITTLE LEMON RESTAURANT - DJANGO REST API

Project:
Little Lemon Restaurant Backend API

Technologies:
- Django 5.2
- Django REST Framework
- MySQL
- Djoser
- JWT Authentication
- Insomnia
- Git and GitHub

API ENDPOINTS

1. User Registration
POST
http://127.0.0.1:8000/auth/users/

2. JWT Token
POST
http://127.0.0.1:8000/auth/jwt/create/

3. User Details
GET
http://127.0.0.1:8000/auth/users/me/

4. Categories
GET / POST
http://127.0.0.1:8000/api/categories/

5. Menu
GET / POST
http://127.0.0.1:8000/api/menu/

6. Bookings
GET / POST
http://127.0.0.1:8000/api/bookings/

7. Admin
http://127.0.0.1:8000/admin/

TEST USER

Username: customer1
Password: Customer@123

To test protected endpoints, first obtain an access token from:
http://127.0.0.1:8000/auth/jwt/create/

Use the access token as a Bearer Token in Insomnia.

RUNNING THE PROJECT

1. Install dependencies using Pipenv.
2. Configure the MySQL database in settings.py.
3. Run:
python manage.py migrate
4. Run:
python manage.py runserver

UNIT TESTS

Run:
python manage.py test