from flask_caching import Cache

from random import choices

from user_agents import USER_AGENT_DICTS


cache = Cache()


USER_AGENT_DICTS.reverse()
user_agents = [a['useragent'] for a in USER_AGENT_DICTS]
ua_relative_weights = [float(a['percent'][:-1]) for a in USER_AGENT_DICTS]


def calculate_cumulative_weights(weights: list[float]) -> list[float]:
    cumulative_weights: list[float] = []

    for index, weight in enumerate(weights):
        try:
            cumulative_weights.append(weight + cumulative_weights[index - 1])
        except IndexError:
            cumulative_weights.append(weight)
    
    return cumulative_weights


ua_cumulative_weights = calculate_cumulative_weights(ua_relative_weights)


def get_user_agent(
    user_agents: list[str] = user_agents,
    cum_weights: list[float] = ua_cumulative_weights,
) -> str:
    return choices(user_agents, cum_weights=cum_weights)[0]


def ip_address_regex():
    ip_field = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

    return (
        r'^' + ip_field + r'\.' + ip_field + r'\.' + ip_field + r'\.' +
        ip_field + r':[\d]{2,5}$')
