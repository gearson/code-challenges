#%% 
from datetime import date, timedelta

start_100days = date(2019, 8, 20)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    end_date = start_100days + timedelta(days = 100)
    return end_date.strftime('%Y-%m-%d')
    # """Return a string of yyyy-mm-dd"""
    


def get_days_between_pb_start_first_joint_pycon():
   days_between = pycon_date - pybites_founded
   return days_between.days
   

#%%
print(get_days_between_pb_start_first_joint_pycon())

#%%
