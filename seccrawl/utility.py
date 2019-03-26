from datetime import datetime

DATE_STD_FORMAT = '%Y-%m-%d'

def format_date(date_string, origin_format, new_format = DATE_STD_FORMAT):
    '''Converts date in the string to a
        format common to all the spiders

        Arguments:
            data_string {string} -- scraped string
            containing the date

        Returns:
            {string} -- the formatted string if 
            successful, the old string otherwise
        '''

    try:
        date = datetime.strptime(date_string, origin_format)
    except ValueError:
        return date_string
    return date.strftime(new_format)
    
