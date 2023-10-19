# cars_brands_and_models
Django fixture with all car brands and models.    
    
**JSON**, which contains all models and brands of cars at the time of upload.    
Each brand has a **pk**, and each model, in addition to the **pk**, has a **pk** of the corresponding brand.    
It can be loaded into your Django project with the command 
```
python manage.py loaddata <filename>
```
Before use You should replace 'assets' in JSON with your app name.
