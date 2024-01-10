from geopy.geocoders import Nominatim
import csv
import pandas as pd
import secrets
 
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

id = secrets.token_hex(4)

if first_name[-1] == 'a':
    gender = "F"
elif first_name[-1] == 'i':
    gender = "F"
elif first_name[-1] == 'o':
    gender =  "M"
else:
    gender = "M"

fields = ['ID', 'First Name', 'Last Name', 'Gender', 'Age']
rows = [[id, first_name.capitalize(), last_name.capitalize(), gender, age]]

with open("user_data.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

with open("geolocation.txt", "w") as file: 
    file.write(address)
file.close()

loc = Nominatim(user_agent="GetLoc")

with open("geolocation.txt") as file: 
    data = file.readlines()
getLoc = loc.geocode(data)
file.close()

fields = ['ID', 'Address', 'Latitude', 'Longitude']
rows = [[id, str(getLoc.address), str(getLoc.latitude), str(getLoc.longitude)]]

with open("location_data.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
file.close()

df1 = pd.read_csv('user_data.csv')
df2 = pd.read_csv('location_data.csv')

df = pd.merge(df1,df2, how = 'outer', on='ID')

df.to_csv('adverts_data.csv', mode='a', header=False)

adverts_data = pd.read_csv('adverts_data.csv')
updated_row = df.loc[0,:]
print(updated_row.to_string())
print(adverts_data)