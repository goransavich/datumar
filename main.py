from datetime import datetime
from dateutil import relativedelta
date_1 = datetime(2002, 12, 1)
date_2 = datetime(2021, 12, 1)
# Get the interval between two dates
diff = relativedelta.relativedelta(date_2, date_1)
print('Complete Difference between two dates: ')
print(diff.years , ' years, ', diff.months, ' months and ', diff.days, ' days')
