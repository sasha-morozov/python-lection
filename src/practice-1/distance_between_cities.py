import math

x1, y1 = 39.9075, 116.39723  # Пекін
x2, y2 = 50.45466, 30.5238  # Київ 

x1_rad, y1_rad = math.radians(x1), math.radians(y1)
x2_rad, y2_rad  = math.radians(x2), math.radians(y2)

distance = 6371.032 * math.acos(math.sin(x1_rad) * math.sin(x2_rad) + 
                                  math.cos(x1_rad) * math.cos(x2_rad) * 
                                  math.cos(y1_rad - y2_rad))

print(f"Distance between Kyiv and Bejing: {distance:>10.3f} км")
