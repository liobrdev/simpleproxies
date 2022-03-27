from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from typing import Collection, Optional


def requests_retry_session(
    retries: int = 4, backoff_factor: float = 0.1,
    status_forcelist: Optional[Collection[int]] = (500, 502, 504),
    session: Optional[Session] = None,
) -> Session:
    retry = Retry(
        total=retries, connect=retries, read=retries,
        backoff_factor=backoff_factor, status_forcelist=status_forcelist,)
    adapter = HTTPAdapter(max_retries=retry)
    session = session or Session()
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session
