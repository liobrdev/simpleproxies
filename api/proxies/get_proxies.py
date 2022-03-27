from bs4 import BeautifulSoup, Tag

from proxies.requests import requests_retry_session
from proxies.user_agents import get_user_agent


def get_proxies() -> list[str]:
    headers = { 'User-Agent': get_user_agent() }
    response = requests_retry_session().get(
        url='https://free-proxy-list.net/', headers=headers, timeout=5,)
    html_response = response.text
    soup = BeautifulSoup(html_response, 'html.parser')
    proxies_table: Tag = soup.find_all(
        'table', class_='table table-striped table-bordered',
    )[0]

    proxies: list[str] = []
    row: Tag

    for row in proxies_table.tbody.find_all('tr'):
        data = row.find_all('td')

        if data[4].string == 'elite proxy' and data[6].string == 'yes':
            proxies.append(':'.join([data[0].string, data[1].string]))

    return proxies
