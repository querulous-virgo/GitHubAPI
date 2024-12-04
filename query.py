import pandas as pd

# Load the data from users.csv
users_df = pd.read_csv('users.csv')

## Question 1 - nicknochnack,brendangregg,cornflourblue,0vm,davecheney
# Sort by 'followers' in descending order and select the top 5 users
top_5_users = users_df.sort_values(by='followers', ascending=False).head(5)
# Get their logins as a comma-separated string
top_5_logins = ','.join(top_5_users['login'])
#print(f" First question answer is: {top_5_logins} \n")

## Question 2 - dylanegan,cjheath,freshtonic,dhowden,mikel

# Convert 'created_at' to datetime format to ensure correct sorting
users_df['created_at'] = pd.to_datetime(users_df['created_at'])
# Sort by 'created_at' in ascending order and select the top 5 users
earliest_users = users_df.sort_values(by='created_at', ascending=True).head(5)
# Get their logins as a comma-separated string
earliest_logins = ', '.join(earliest_users['login'])
#print(f" Second question answer is: {earliest_logins} \n")


## Question 3 - mit,other,apache-2.0
import pandas as pd
# Load the data from repositories.csv
repos_df = pd.read_csv('repositories.csv')
# Filter out rows with missing licenses
repos_df = repos_df[repos_df['license_name'].notna()]
# Get the 3 most common licenses
top_3_licenses = repos_df['license_name'].value_counts().head(3).index
# Convert the top licenses to a comma-separated string
top_3_licenses_str = ','.join(top_3_licenses)
#print("Answer for third question is: ")
#print(top_3_licenses_str)

## Question 4 ATLASSIAN

# Filter out rows with missing or empty company values
users_df = users_df[users_df['company'].notna() & (users_df['company'] != '')]
# Find the most common company
most_common_company = users_df['company'].value_counts().idxmax()
#print(most_common_company)

## Question 5 - JavaScript
# Filter out rows with missing or empty language values
repos_df = repos_df[repos_df['language'].notna() & (repos_df['language'] != '')]

# Find the most common programming language
most_popular_language = repos_df['language'].value_counts().idxmax()
#print(most_popular_language)

## Question 6 - TypeScript
import pandas as pd
from datetime import datetime

# Read the data
users_df = pd.read_csv('users.csv')
repos_df = pd.read_csv('repositories.csv')

# Convert created_at to datetime
users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# Filter users who joined after 2020
recent_users = users_df[users_df['created_at'] > '2020-01-01']['login'].unique()

# Filter repositories belonging to these users
recent_repos = repos_df[repos_df['login'].isin(recent_users)]

# Count languages, excluding None/empty values
language_counts = recent_repos['language'].value_counts().dropna()

#print("\nTop 5 languages for users who joined after 2020:")
#print(language_counts.head())
#print(f"\nSecond most popular language: {language_counts.index[1]}")

# Additional analysis for verification
#print(f"\nTotal users who joined after 2020: {len(recent_users)}")
#print(f"Total repositories analyzed: {len(recent_repos)}")

## Question 7 - Mermaid  
import pandas as pd

# Load repositories data
repos_df = pd.read_csv('repositories.csv')

# Filter out repositories with missing or empty language values
repos_df = repos_df[repos_df['language'].notna() & (repos_df['language'] != '')]

# Calculate the average number of stars per language
avg_stars_per_language = repos_df.groupby('language')['stargazers_count'].mean()

# Find the language with the highest average stars
top_language = avg_stars_per_language.idxmax()
highest_avg_stars = avg_stars_per_language.max()

#print(f"The language with the highest average stars per repository is {top_language} with an average of {highest_avg_stars:.2f} stars.")

## Question 8 - brendangregg,cornflourblue,Canva,nicknochnack,0vm
import pandas as pd

# Load the data from users.csv
users_df = pd.read_csv('users.csv')

# Calculate leader_strength
users_df['leader_strength'] = users_df['followers'] / (1 + users_df['following'])

# Sort by leader_strength in descending order and select the top 5 users
top_5_leader_strength = users_df.sort_values(by='leader_strength', ascending=False).head(5)

# Get their logins as a comma-separated string
top_5_logins = ','.join(top_5_leader_strength['login'])
#print(top_5_logins)

## Question 9 - 0.035
# Calculate the correlation between followers and public_repos
users_df = pd.read_csv('users.csv')
correlation = users_df['followers'].corr(users_df['public_repos'])
print(f"The correlation between the number of followers and the number of public repositories is: {correlation:.3f}")

## Question 10 - 0.067
import pandas as pd
from scipy.stats import linregress

# Load the data from users.csv
users_df = pd.read_csv('users.csv')

# Define the independent variable (X) and dependent variable (y)
X = users_df['public_repos']
y = users_df['followers']
# Calculate the slope and intercept
slope, intercept, r_value, p_value, std_err = linregress(X, y)

# print(f"Slope: {slope:.3f}")
# print("Intercept:", intercept)

## Question 11
df = pd.read_csv('repositories.csv')
df[['has_wiki', 'has_projects']] = df[['has_wiki', 'has_projects']].astype(int)
# Find the correlation between the two columns
correlation = df['has_projects'].corr(df['has_wiki'])
print("11th Correlation:", correlation)

## Question 12
import pandas as pd
import numpy as np

# Read users data
users_df = pd.read_csv('users.csv')

# Calculate average following for hireable users (True)
hireable_avg = users_df[users_df['hireable'] == True]['following'].mean()

# Calculate average following for the rest (False or null/NaN)
non_hireable_avg = users_df[users_df['hireable'] != True]['following'].mean()

# Calculate the difference rounded to 3 decimal places
difference = hireable_avg - non_hireable_avg

print(f"12th answer is {difference:.3f}")

## Question 13 - -9.971
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# # Read users data
# users_df = pd.read_csv('users.csv')

# # Filter users with bios and calculate word counts
# users_with_bios = users_df[users_df['bio'].notna() & (users_df['bio'] != '')]
# users_with_bios['word_count'] = users_with_bios['bio'].str.split().str.len()

# # Prepare data for regression
# X = users_with_bios['word_count'].values.reshape(-1, 1)
# y = users_with_bios['followers'].values

# # Fit regression model
# model = LinearRegression()
# model.fit(X, y)

# # Get slope rounded to 3 decimal places
# slope = round(model.coef_[0], 3)

#print(f"{slope}")


## Question 14 - timgates42,pinkforest,johndpope,mvandermeulen,mikeyhodl
import pandas as pd

# Load the data from repositories.csv
repos_df = pd.read_csv('repositories.csv')

# Convert 'created_at' to datetime format
repos_df['created_at'] = pd.to_datetime(repos_df['created_at'])

# Extract the day of the week (0=Monday, 6=Sunday)
repos_df['day_of_week'] = repos_df['created_at'].dt.dayofweek

# Filter for weekends (Saturday=5, Sunday=6)
weekend_repos = repos_df[repos_df['day_of_week'].isin([5, 6])]

# Count the number of repositories created by each user
user_repo_counts = weekend_repos['login'].value_counts().head(5)

# Get the top 5 users
top_users = user_repo_counts.index.tolist()

# Print the top 5 users' logins in order, comma-separated
#print(','.join(top_users))


## Question 15
import pandas as pd
import numpy as np

# Read users data
users_df = pd.read_csv('users.csv')

# For hireable users (True)
hireable_users = users_df[users_df['hireable'] == True]
hireable_fraction = (hireable_users['email'].notna() & (hireable_users['email'] != '')).mean()

# For the rest (False or null/NaN)
non_hireable_users = users_df[users_df['hireable'] != True]
non_hireable_fraction = (non_hireable_users['email'].notna() & (non_hireable_users['email'] != '')).mean()

# Calculate difference rounded to 3 decimal places
difference = round(hireable_fraction - non_hireable_fraction, 3)

print(f"15th : {difference}")

## Question 16 - Wu,Zhang
import pandas as pd

# Load the data from users.csv
users_df = pd.read_csv('users.csv')

# Extract surnames
# Ignore missing names, trim whitespace, and split by whitespace
users_df['surname'] = users_df['name'].dropna().apply(lambda x: x.strip().split()[-1])

# Count occurrences of each surname
surname_counts = users_df['surname'].value_counts()

# Get the most common surname(s)
most_common_count = surname_counts.max()
most_common_surnames = surname_counts[surname_counts == most_common_count].index.tolist()

# Sort the surnames alphabetically
most_common_surnames.sort()

# Output results
#print(f"Most common surname(s): {', '.join(most_common_surnames)}")
#print(f"Number of users with the most common surname: {most_common_count}")
