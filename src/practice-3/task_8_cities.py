
cities = {
    'Paris': {
        'country': 'France',
        'population': 2148000,
        'fact': 'Known as the City of Light.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Has the busiest train station in the world.'
    },
    'Cairo': {
        'country': 'Egypt',
        'population': 9900000,
        'fact': 'Home to the ancient pyramids.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city}")
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")
