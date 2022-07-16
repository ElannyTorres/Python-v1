def search_by_year():
  year_info = int(input('Enter the year of interest: '))

  with open('life-expectancy.csv') as life_expectancy:
    total_years = 0
    count = 0

    lowest_age = 99999999999999
    highest_age = 0.000000001
    lowest_country = ''
    highest_country = ''
    lowest_year = 99999999999999
    highest_year = 0.000000001
  
    next(life_expectancy)
  
    for line in life_expectancy:
      line = line.strip()
      parts = line.split(',')
      countries = parts[0]
      abbreviations = parts[1]
      years = int(parts[2])
      ages_data = float(parts[3])
      if year_info == years:
        total_years += ages_data
        count += 1
        if ages_data < lowest_age:
          lowest_age = ages_data
          lowest_country = countries
          lowest_year = years
        if ages_data > highest_age:
          highest_age = ages_data
          highest_country = countries
          highest_year = years
  
  print('\n=========================================================================')
  print(f'For the year {year_info}:')
  print(f'The average life expectancy across all countries was {total_years/count:.2f}')
  print(f'The max life expectancy was in {highest_country} with {highest_age}')
  print(f'The min life expectancy was in {lowest_country} with {lowest_age}')
  print('=========================================================================')

def search_by_country():
  country_info = input('Enter the country of interest: ')

  with open('life-expectancy.csv') as life_expectancy:
    total_years = 0
    count = 0

    lowest_age = 99999999999999
    highest_age = 0.000000001
    lowest_country = ''
    highest_country = ''
    lowest_year = 99999999999999
    highest_year = 0.000000001
  
    next(life_expectancy)
  
    for line in life_expectancy:
      line = line.strip()
      parts = line.split(',')
      countries = parts[0]
      abbreviations = parts[1]
      years = int(parts[2])
      ages_data = float(parts[3])
      if country_info.capitalize() == countries:
        total_years += ages_data
        count += 1
        if ages_data < lowest_age:
          lowest_age = ages_data
          lowest_country = countries
          lowest_year = years
        if ages_data > highest_age:
          highest_age = ages_data
          highest_country = countries
          highest_year = years

  print('\n=========================================================================')
  print(f'For the country {country_info.capitalize()}:')
  print(f'The average life expectancy across all countries was {total_years/count:.2f}')
  print(f'The max life expectancy was in {highest_country} with {highest_age}')
  print(f'The min life expectancy was in {lowest_country} with {lowest_age}')
  print('=========================================================================')

print('\nWelcome to "Life Expectancy from 1959 to 2019"')

print('\n=========================================================================')
print('Some general info:')

with open('life-expectancy.csv') as life_expectancy:

  lowest_age = 99999999999999
  highest_age = 0.000000001
  lowest_country = ''
  highest_country = ''
  lowest_year = 99999999999999
  highest_year = 0.000000001

  next(life_expectancy)

  for line in life_expectancy:
    line = line.strip()
    parts = line.split(",")
    countries = parts[0]
    abbreviations = parts[1]
    years = int(parts[2])
    ages_data = float(parts[3])
    if ages_data < lowest_age:
      lowest_age = ages_data
      lowest_country = countries
      lowest_year = years
    if ages_data > highest_age:
      highest_age = ages_data
      highest_country = countries
      highest_year = years

print(f'The overall max life expectancy is: {highest_age} from {highest_country} in {highest_year}')
print(f'The overall min life expectancy is: {lowest_age} from {lowest_country} in {lowest_year}')

print('=========================================================================')

more_info = input('\nDo you want to know more (yes/no)? ')

while more_info.lower() == 'yes':
  
  print('Excellent!')
  search_by = input('Do you wanna search info by year o country? ')
  if search_by.lower() == 'year':
    
    search_by_year()

    more_info = input('\nDo you want to know more (yes/no)? ')

  elif search_by.lower() == 'country':
    
    search_by_country()

    more_info = input('\nDo you want to know more (yes/no)? ')

print('Thanks for the visit!')