from bs4 import BeautifulSoup, Tag
from flask_restful import Resource
from httpx import get

from utils import cache, get_user_agent


class ProxiesAPI(Resource):
    @cache.cached()
    def get(self) -> list[str]:
        headers = { 'User-Agent': get_user_agent() }
        response = get('https://free-proxy-list.net/', headers=headers)

        html_response = response.text
        soup = BeautifulSoup(html_response, 'html.parser')

        table_class = 'table table-striped table-bordered'
        proxies_table: Tag = soup.find_all('table', class_=table_class)[0]

        proxies: list[str] = []
        row: Tag

        for row in proxies_table.tbody.find_all('tr'):
            data = row.find_all('td')

            if data[4].string == 'elite proxy' and data[6].string == 'yes':
                proxies.append(':'.join([data[0].string, data[1].string]))

        return proxies
