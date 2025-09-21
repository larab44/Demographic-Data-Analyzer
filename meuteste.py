import pandas as pd
# Read data from file
df = pd.read_csv('adult.data.csv')
df.describe()
 # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = df['race'].nunique()

# What is the average age of men?
average_age_men = df['age'].mean()
print(race_count)
print(average_age_men)
print(df["education"].value_counts())
print(lower_education = df[df['education'] != 'Bachelors'& df['education'] != 'Masters' & df['education'] != 'Doctorate' ]['salary'] == '>50k'.percent()
)