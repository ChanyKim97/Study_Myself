import pandas as pd

name = ['Taylor Swift', 'Aaron Sorkin', 'Harry Potter', 'Ji-Sung Park']
birthday = ['December 13, 1989', 'June 9, 1961', 'July 31, 1980', 'February 25, 1981']
occupation = ['Singer-songwriter','Screenwriter','Wizard','Footballer']

dic = {
    'name': pd.Series(name),
    'birthday': pd.Series(birthday),
    'occupation': pd.Series(occupation)
}
df = pd.DataFrame(dic)

print(df)