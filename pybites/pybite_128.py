#%%
from datetime import datetime

THIS_YEAR = 2018

#%%
def years_ago(date):
    date_input = datetime.strptime(date, '%d %b, %Y')
    return THIS_YEAR - date_input.year
    """Receives a date string of 'DD MMM, YYYY', for example: 8 Aug, 2015
       Convert this date str to a datetime object (use strptime).
       Then extract the year from the obtained datetime object and subtract
       it from the THIS_YEAR constant above, returning the int difference.
       So in this example you would get: 2018 - 2015 = 3"""
#%%     
print(years_ago('8 Aug, 2015'))

def convert_eu_to_us_date(date):
    eu_date = datetime.strptime(date, '%d/%m/%Y')
    us_date = eu_date.strftime('%m/%d/%Y')
    return us_date

print(convert_eu_to_us_date('17/01/1990'))
#%%
