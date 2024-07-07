import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('census.csv')
    
    # 1. How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    
    # 2. What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()
    
    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100
    
    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = (higher_education['salary'] == '>50K').mean() * 100
    
    # 5. What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = (lower_education['salary'] == '>50K').mean() * 100
    
    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()
    
    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100
    
    # 8. What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).max() * 100
    
    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]
    
    # Print the results if print_data is True
    if print_data:
        print("1. Number of people of each race:")
        print(race_count)
        print("\n2. Average age of men:", round(average_age_men, 1))
        print("\n3. Percentage of people with a Bachelor's degree:", round(percentage_bachelors, 1))
        print("\n4. Percentage of people with advanced education earning >50K:", round(higher_education_rich, 1))
        print("\n5. Percentage of people without advanced education earning >50K:", round(lower_education_rich, 1))
        print("\n6. Minimum number of hours worked per week:", min_work_hours)
        print("\n7. Percentage of people who work the minimum number of hours and earn >50K:", round(rich_percentage, 1))
        print("\n8. Country with the highest percentage of people earning >50K:", highest_earning_country)
        print("   Percentage:", round(highest_earning_country_percentage, 1))
        print("\n9. Most popular occupation for those who earn >50K in India:", top_IN_occupation)
    
    # Return dictionary of results
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

# Call the function to calculate and print the results
calculate_demographic_data()
