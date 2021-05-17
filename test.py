import utils
from datetime import datetime, timedelta

# today = datetime.today()
# print((today - timedelta(days=2)).day)
today = utils._date()
print(today+1)