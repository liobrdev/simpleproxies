from random import choices


USER_AGENT_DICTS = [
    {"percent":"14.6%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36","system":"Chrome 99.0 Win10"},
    {"percent":"7.9%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36","system":"Chrome 98.0 Win10"},
    {"percent":"6.0%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36","system":"Chrome 99.0 macOS"},
    {"percent":"5.8%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0","system":"Firefox 97.0 Win10"},
    {"percent":"5.2%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0","system":"Firefox 98.0 Win10"},
    {"percent":"4.5%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36","system":"Chrome 99.0 Win10"},
    {"percent":"3.7%","useragent":"Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0","system":"Firefox 91.0 Win10"},
    {"percent":"3.4%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36","system":"Chrome 98.0 macOS"},
    {"percent":"2.6%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15","system":"Safari 15.3 macOS"},
    {"percent":"1.9%","useragent":"Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0","system":"Firefox 98.0 Linux"},
    {"percent":"1.7%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0","system":"Firefox 97.0 macOS"},
    {"percent":"1.7%","useragent":"Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0","system":"Firefox 97.0 Linux"},
    {"percent":"1.7%","useragent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36","system":"Chrome 99.0 Linux"},
    {"percent":"1.3%","useragent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0","system":"Firefox 97.0 Linux"},
    {"percent":"1.1%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36","system":"Chrome 99.0 macOS"},
    {"percent":"1.1%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0","system":"Firefox 98.0 macOS"},
    {"percent":"1.1%","useragent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0","system":"Firefox 91.0 Linux"},
    {"percent":"1.1%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39","system":"Edge 99.0 Win10"},
    {"percent":"1.1%","useragent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0","system":"Firefox 98.0 Linux"},
    {"percent":"1.0%","useragent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36","system":"Chrome 98.0 Linux"},
    {"percent":"0.8%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36","system":"Chrome 98.0 macOS"},
    {"percent":"0.8%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.31","system":"Opera Generic Win10"},
    {"percent":"0.7%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62","system":"Edge 98.0 Win10"},
    {"percent":"0.6%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15","system":"Safari 15.2 macOS"},
    {"percent":"0.5%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36","system":"Edge 99.0 Win10"},
    {"percent":"0.5%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36","system":"Chrome 99.0 Win10"},
    {"percent":"0.5%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0","system":"Firefox 91.0 Win10"},
    {"percent":"0.5%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36","system":"Chrome 97.0 Win10"},
    {"percent":"0.5%","useragent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36","system":"Chrome 98.0 Win7"},
    {"percent":"0.5%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15","system":"Safari 15.1 macOS"},
    {"percent":"0.5%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15","system":"Safari 15.4 macOS"},
    {"percent":"0.5%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0","system":"Firefox 96.0 Win10"},
    {"percent":"0.5%","useragent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36","system":"Chrome 99.0 Win7"},
    {"percent":"0.4%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30","system":"Edge 99.0 Win10"},
    {"percent":"0.4%","useragent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36","system":"Chrome 99.0 Linux"},
    {"percent":"0.4%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36","system":"Chrome 98.0 macOS"},
    {"percent":"0.4%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36","system":"Chrome 97.0 Win10"},
    {"percent":"0.4%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46","system":"Edge 99.0 Win10"},
    {"percent":"0.3%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15","system":"Safari 14.1 macOS"},
    {"percent":"0.3%","useragent":"Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0","system":"Firefox 96.0 Linux"},
    {"percent":"0.3%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.70","system":"Opera 83 Win10"},
    {"percent":"0.3%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/84.0.4316.21","system":"Opera Generic Win10"},
    {"percent":"0.3%","useragent":"Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0","system":"Firefox 95.0 Linux"},
    {"percent":"0.3%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36","system":"Chrome 97.0 macOS"},
    {"percent":"0.3%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36","system":"Chrome 96.0 Win10"},
    {"percent":"0.3%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0","system":"Firefox 95.0 Win10"},
    {"percent":"0.3%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0","system":"Firefox 99.0 Win10"},
    {"percent":"0.3%","useragent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36","system":"Chrome 99.0 Win7"},
    {"percent":"0.3%","useragent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36","system":"Chrome 98.0 Linux"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0","system":"Firefox 98.0 Win7"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36","system":"Chrome 96.0 Win10"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15","system":"Safari 15.0 macOS"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.4.837 Yowser/2.5 Safari/537.36","system":"Yandex Browser Generic Win10"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0","system":"Firefox 97.0 Win7"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0","system":"Firefox 98.0 Linux"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36","system":"Chrome 99.0 macOS"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36","system":"Chrome 96.0 macOS"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36","system":"Chrome 97.0 macOS"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.121 Safari/537.36","system":"Chrome 98.0 Win10"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36","system":"Chrome 99.0 Win8.1"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0","system":"Firefox 97.0 Win8.1"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36","system":"Chrome 97.0 Linux"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0","system":"Firefox 97.0 Linux"},
    {"percent":"0.2%","useragent":"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0","system":"Firefox 97.0 Linux"},
]


def calculate_cumulative_weights(weights: list[float]) -> list[float]:
    cumulative_weights: list[float] = []

    for index, weight in enumerate(weights):
        try:
            cumulative_weights.append(weight + cumulative_weights[index - 1])
        except IndexError:
            cumulative_weights.append(weight)
    
    return cumulative_weights


USER_AGENT_DICTS.reverse()

user_agents = [a['useragent'] for a in USER_AGENT_DICTS]

ua_relative_weights = [float(a['percent'][:-1]) for a in USER_AGENT_DICTS]

ua_cumulative_weights = calculate_cumulative_weights(ua_relative_weights)

def get_user_agent() -> str:
    return choices(user_agents, cum_weights=ua_cumulative_weights)[0]


__all__ = [
    'user_agents', 'ua_relative_weights', 'ua_cumulative_weights',
    'get_user_agent',
]
