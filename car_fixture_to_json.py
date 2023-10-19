import json

with open('cars_brands_models_fixture.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    car_brands = []
    for item in data:
        if item['model'] == 'assets.carbrand':
            current_brand = item['fields']['name']
            current_brand_pk = item['pk']
            car_brands.append({
                'pk': current_brand_pk,
                'brand': current_brand,
                'models': []})
        elif item['model'] == 'assets.carmodel':
            for brand in car_brands:
                if item['fields']['brand'] == brand['pk']:
                    brand['models'].append(item['fields']['name'])

    for item in car_brands:
        item.pop('pk')

    with open(
        'cars_brands_and_models.json', 'w', encoding='utf-8'
    ) as dump_file:
        json.dump(car_brands, dump_file, indent=2)
