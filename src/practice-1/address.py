student = {
  'name': 'Oleksandr',
  'last_name': 'Morozov',
  'country': 'Ukraine',
  'zip_code': '00100',
  'city': 'Kyiv',
  'street': 'Maidan Nezalezhnosti Str.2',
};

def log_location_details(user):
    print(f"{user['name']} {user['last_name']}\n"
          f"{user['country']}\n"
          f"{user['zip_code']}\n"
          f"{user['city']}\n"
          f"{user['street']}"
        )

log_location_details(student)