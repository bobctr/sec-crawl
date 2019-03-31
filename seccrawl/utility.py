from datetime import datetime
from scrapy.http import Request, TextResponse
import os

DATE_STD_FORMAT = '%Y-%m-%d'

def format_date(date_string, origin_format, new_format = DATE_STD_FORMAT):
    '''Converts date in the string to a
        format common to all the spiders

        Arguments:
            data_string {string} -- string
                containing the date

        Raises:
            ValueError: if the string is not a date

        Returns:
            {string} -- the formatted string if 
                successful, the old string otherwise
        '''
    try:
        date = datetime.strptime(date_string, origin_format)
    except ValueError:
        return date_string
    return date.strftime(new_format)
    

def fake_response(file_name=None):
    """[for testing]
    Create a Scrapy fake HTTP response from a HTML file
    """
    url = 'http://localhost'

    request = Request(url=url)
    if file_name:
        if not file_name[0] == '/':
            responses_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(responses_dir, file_name)
        else:
            file_path = file_name
        file_content = open(file_path, 'r').read()
    else:
        file_content = ''

    response = TextResponse(url=url, request=request, 
        body=file_content,encoding='utf-8')
    return response