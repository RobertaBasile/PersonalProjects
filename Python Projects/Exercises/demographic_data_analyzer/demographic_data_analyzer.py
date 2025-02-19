"""
Dataset Description: Adult Data (Census Income)

This dataset, extracted from the 1994 Census database, contains demographic information
and income data for individuals. The primary objective of the dataset is to predict
whether a person earns more than $50,000 a year based on various demographic factors.

Columns:
1. age: Age of the individual.
2. workclass: The employment status and sector.
3. fnlwgt: Final weight, representing the number of people the census believes the entry represents.
4. education: Highest level of education achieved.
5. education-num: Number of years of education.
6. marital-status: Marital status of the individual.
7. occupation: Occupation of the individual.
8. relationship: Family relationship status.
9. race: Race of the individual.
10. sex: Gender of the individual.
11. capital-gain: Income from investment sources, apart from wages/salary.
12. capital-loss: Losses from investment sources.
13. hours-per-week: Number of hours worked per week.
14. native-country: Country of origin.
15. salary: Income level of the individual, categorized as '>50K' or '<=50K'.

Sources:
- Kohavi, R. (1996). Census Income [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5GP7S.

Usage:
This dataset is commonly used for tasks involving:
- Classification
- Demographic analysis
- Income prediction

Example:
import pandas as pd

# Load the dataset
df = pd.read_csv('adult.data.csv', header=None, names=[
    'age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 
    'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
    'hours-per-week', 'native-country', 'salary'])

# Display the first few rows of the dataframe
print(df.head())
"""
import pandas as pd

def calculate_demographic_data(print_data=True):
    # Carica il dataset
    df = pd.read_csv('adult.data.csv', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 
        'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
        'hours-per-week', 'native-country', 'salary'])

    # Quante persone di ogni etnia sono rappresentate in questo dataset?
    race_count = df['race'].value_counts()

    # Qual è l'età media degli uomini?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Qual è la percentuale di persone che hanno un diploma di laurea?
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    # Qual è la percentuale di persone con istruzione avanzata (Laurea, Master o Dottorato) che guadagnano più di 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1)

    # Qual è la percentuale di persone senza istruzione avanzata che guadagnano più di 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)

    # Qual è il numero minimo di ore che una persona lavora alla settimana?
    min_work_hours = df['hours-per-week'].min()

    # Qual è la percentuale di persone che lavorano il numero minimo di ore alla settimana e guadagnano più di 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # Quale paese ha la percentuale più alta di persone che guadagnano >50K e qual è quella percentuale?
    country_rich_percentage = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100)
    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # Identifica l'occupazione più popolare per quelli che guadagnano >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
