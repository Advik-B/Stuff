import datetime as dt

global __black_listed_days
global __months

__black_listed_days = [
    'SAT',
    'SUN'
    ]

__months = {
    1:'JAN',
    2:'FEB',
    3:'MAR',
    4:'APR',
    5:'MAY',
    6:'JUN',
    7:'JUL',
    8:'AUG',
    9:'SEP',
    10:'OCT',
    11:'NOV',
    12:'DEC',
    }

def __create_download_link(date:int, month:str , year:int) -> str:
    return f'https://archives.nseindia.com/content/historical/EQUITIES/{year}/{month.upper()}/cm{date}{month.upper()}{year}bhav.csv.zip'

def create_link(date:int , month:int , year:int , console_output:bool=False) -> str:
    """returns a link for you to download from nseindia.com:\n\t
    IT WILL NOT DOWNLOAD IT!"""
    try:
        if (dt.date(year,month,date).strftime('%a')).upper() in __black_listed_days:
            day= (dt.date(year,month,date).strftime('%A'))
            raise Exception(f'error: The date given refers to a week-end ( {date}-{month}-{year} is a {day} )')
        else:

            month = __months[month]
            if console_output:
                print('(Possible) Download Link',__create_download_link(date=date, month = month , year = year), end='\n\n')
            return __create_download_link(date=date, month = month , year = year)
    except (ValueError, IndexError):
        print(f'error: {month} is not a valid month number')