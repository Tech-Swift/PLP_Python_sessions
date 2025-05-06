import pandas as pd
## Ensure not to name the files by using the panda or numpy name

jsMummies = {
    "Name":["Everline", "Annie", "Martha", "Lydia", "Lucy", "Mabel", "Lillian", "Ethel", "Edith", "Clara"],
    "Age": [30, 25, 35, 28, 22, 40, 33, 29, 31, 27],
    "Height" : [5.4, 5.6, 5.5, 5.7, 5.8, 5.9, 6.0, 5.3, 5.2, 5.1],
    "Weight" : [130, 140, 150, 160, 170, 180, 190, 200, 210, 220],
    "Occupation" : ["Teacher", "Nurse", "Engineer", "Doctor", "Artist", "Scientist", "Writer", "Musician", "Chef", "Athlete"]
}

df = pd.DataFrame(jsMummies)
print(df)
# print(jsMummies.df.head(3))
# print(jsMummies.df.tail(3))