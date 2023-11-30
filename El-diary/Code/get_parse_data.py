import requests
from json import loads
from datetime import datetime
from constants import abs_path as a_p
from get_valid_session_id import get_valid_session_id

PATH = a_p(r'data\session_id.txt')
try:
    with open(PATH) as f:
        SESSION_ID = f.read()
except IOError:
    open(PATH, 'w').close()
    SESSION_ID = ''

def get_journal():
    global SESSION_ID, PATH
    cookies = {
        'NodeID': 'node1',
        'csrftoken': 'wgmFSFHiPDittFj0jATUtUUGUncT4sxaweOE0W9kS2mt63dnupngz5R1AtEOq0B8',
        '_ym_uid': '1694519613705193957',
        '_ym_d': '1694519613',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
        'sessionid': SESSION_ID,
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Referer': 'https://sh-open.ris61edu.ru/personal-area/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^116^\\^, ^\\^Not)A;Brand^\\^;v=^\\^24^\\^, ^\\^Google',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '^\\^Windows^\\^',
    }

    params = (
        ('date', datetime.now().strftime('%Y-%m-%d')),
    )

    response = requests.get('https://sh-open.ris61edu.ru/api/MarkService/GetSummaryMarks', headers=headers, params=params, cookies=cookies)
    result = str(response.content)

    if 'fault' in result:
        value = get_valid_session_id()
        if value == 'error':
            return 'error'
        if value == False:
            return False
        SESSION_ID = value if value else get_journal()
        with open(PATH, 'w') as f:
            f.write(SESSION_ID)
        result = get_journal()
    return result

def get_ordered_dict(journal):
    return [{elem['discipline'].encode('ascii').decode('unicode_escape'):
                [{mark_data['date']: mark_data['mark']}
                    for mark_data in elem['marks']]}
                        for elem in journal['discipline_marks']]


def get_list_of_disciplines_and_marks():
    value = get_journal()
    if value == 'error':
        return value
    return get_ordered_dict(loads(value[2:-1])) if value else False