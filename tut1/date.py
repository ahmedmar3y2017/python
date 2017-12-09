from __future__ import print_function
from datetime import date
from datetime import time
from datetime import datetime



def main():
    today=date.today()
    print("Today is : ", today)

    print(today.day , "    **    " , today.month , "    *    " , today.year)
    print(today.weekday())
    TimeNow=datetime.now()
    print(TimeNow)



if __name__=="__main__":
    main()


