import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].nunique()

    # What is the average age of men?
    average_age_men =df[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    tem_bachelors = df[df['education'] == 'Bachelors']
    ganha_apartir_50k = tem_bachelors[tem_bachelors['salary'] == '>50K']
    percentage_bachelors = (len(ganha_apartir_50k)/ len(tem_bachelors) ) *100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    went_university = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    went_university_rich =went_university[went_university['salary']== '>50K']
    # What percentage of people without advanced education make more than 50K?
    not_went_university = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    not_went_university_rich = not_went_university[not_went_university['salary'] == '>50K']
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = (len(went_university_rich)/len(went_university)) * 100
    lower_education_rich = (len(not_went_university_rich)/len(not_went_university))*100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    min_hours_rich = num_min_workers[num_min_workers['salary']== '>50K']
    rich_percentage = (len(min_hours_rich)/ len(num_min_workers)) * 100

    # What country has the highest percentage of people that earn >50K?
    # Calcular a porcentagem de pessoas que ganham >50K por país
    porcentagens = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    highest_earning_country = porcentagens.idxmax()
    highest_earning_country_percentage = porcentagens.max()


    # Identify the most popular occupation for those who earn >50K in India.
    indian_people = df[df['native-country']== 'India']
    top_IN_occupation = indian_people['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
