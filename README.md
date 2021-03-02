# django_rest_api

**Yêu cầu**  
Có cài đặt pipenv

**Các bước**  
1. Dùng pipenv tạo virtual env và cài các package cần thiết, rồi activate env đó
> <code>pipenv install</code>
> <code>pipenv install -r requirements.txt</code> 
> <code>pipenv sync</code>  
> <code>pipenv shell</code>  
2. Migration và Migrate Database
> <code>python manage.py makemigrations</code>  
> <code>python manage.py migrate</code>  
3. Runserver
> <code>python manage.py runserver</code>  
