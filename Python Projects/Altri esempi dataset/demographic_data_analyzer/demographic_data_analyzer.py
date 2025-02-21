""" Demographic Data Analyzer
You will be working on this project with our Gitpod starter code.

We are still developing the interactive instructional part of the Python curriculum. For now, here are some videos on the freeCodeCamp.org YouTube channel that will teach you everything you need to know to complete this project:

Python for Everybody Video Course (14 hours)

How to Analyze Data with Python Pandas (10 hours)

In this challenge you must analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database. Here is a sample of what the data looks like:

|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |
You must use Pandas to answer the following questions:

How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
What is the average age of men?
What is the percentage of people who have a Bachelor's degree?
What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
What percentage of people without advanced education make more than 50K?
What is the minimum number of hours a person works per week?
What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
What country has the highest percentage of people that earn >50K and what is that percentage?
Identify the most popular occupation for those who earn >50K in India.
Use the starter code in the file demographic_data_analyzer.py. Update the code so all variables set to None are set to the appropriate calculation or code. Round all decimals to the nearest tenth.

Development
Write your code in demographic_data_analyzer.py. For development, you can use main.py to test your code.

Testing
The unit tests for this project are in test_module.py. We imported the tests from test_module.py to main.py for your convenience.

Submitting
Copy your project's URL and submit it to freeCodeCamp.

Dataset Source
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.

"""
import pandas as pd
def load_data():
    column_names = [
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
    ]
    df = pd.read_csv('adult.data.csv', header=None, names=column_names, skipinitialspace=True)
    
    return df

def race_count(df):
    return df['race'].value_counts()

def average_age_men(df):
    return round(df[df['sex'] == 'Male']['age'].mean(), 1)

def percentage_bachelors(df):
    return round((df['education'] == 'Bachelors').mean() * 100, 1)

def percentage_advanced_edu_high_earners(df):
    advanced_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    return round((df[advanced_edu]['salary'] == '>50K').mean() * 100, 1)

def percentage_non_advanced_edu_high_earners(df):
    non_advanced_edu = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    return round((df[non_advanced_edu]['salary'] == '>50K').mean() * 100, 1)

def min_work_hours(df):
    return df['hours-per-week'].min()

def percentage_high_earners_min_hours(df):
    min_hours = min_work_hours(df)
    min_hours_workers = df[df['hours-per-week'] == min_hours]
    return round((min_hours_workers['salary'] == '>50K').mean() * 100, 1)

def highest_earning_country(df):
    # Compute the total number of people per country
    total_by_country = df.groupby('native-country').size()
    # Compute the number of high earners per country
    high_earners_by_country = df[df['salary'] == '>50K'].groupby('native-country').size()
    # Calculate percentage of high earners by country
    percentage = (high_earners_by_country / total_by_country * 100).round(1)
    highest_country = percentage.idxmax()
    highest_percentage = percentage.max()
    return highest_country, highest_percentage

def most_popular_high_earner_occupation_india(df):
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    return india_high_earners['occupation'].mode()[0]

if __name__ == "__main__":
    df = load_data()
    
    print("Number of people of each race:")
    print(race_count(df))
    
    print("Average age of men:", average_age_men(df))
    
    print("Percentage with Bachelors degrees:", percentage_bachelors(df))
    
    print("Percentage with advanced education earning >50K:", percentage_advanced_edu_high_earners(df))
    
    print("Percentage without advanced education earning >50K:", percentage_non_advanced_edu_high_earners(df))
    
    print("Minimum work hours:", min_work_hours(df))
    
    print("Percentage of high earners working minimum hours:", percentage_high_earners_min_hours(df))
    
    highest_country, highest_percentage = highest_earning_country(df)
    print(f"Country with highest percentage of high earners: {highest_country} ({highest_percentage}%)")
    
    print("Most popular occupation for high earners in India:", most_popular_high_earner_occupation_india(df))
