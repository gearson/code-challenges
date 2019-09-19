#%%
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('days/01-03-datetimes/code', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

#%%

with open(logfile) as f:
    loglines = f.readlines()


#%% for you to code:
loglines[:2]
#%%
def convert_to_datetime(line):
    time = line.split()[1]
    time_format = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(time, time_format)
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
#%%
def time_between_shutdowns(loglines):
    shutdown_events = [convert_to_datetime(line) for line in loglines if SHUTDOWN_EVENT in line]
    shutdown_delta = shutdown_events[1] - shutdown_events[0]
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    return shutdown_delta

#%%
time_between_shutdowns(loglines)
