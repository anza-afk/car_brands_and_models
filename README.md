# JSON with cars brands and models

### car_brands_and_models.json
**JSON**, which contains all car brands and list of car models for each brand at the time of upload.

### car_brands_and_models_fixture.json
Django fixture with all car brands and models.    

**JSON**, which contains all car brands and car models at the time of upload.    
Each brand has a **pk**, and each model, in addition to the **pk**, has a **pk** of the corresponding brand.    
It can be loaded into your Django project with the command 
```
python manage.py loaddata <path_to_file>
```
#### **NB!** Before use You should replace 'assets' in JSON with your app name.

### car_fixture_to_json.py
Script that make classic JSON from Django fixture.
