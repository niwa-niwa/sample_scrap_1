import requests
from cachecontrol import CacheControl
from cachecontrol.caches import FileCache


session = requests.Session()

# using cachecontrol not to crawl a page that is not updated
cached_session = CacheControl(session, cache=FileCache('.webcache'))

response = cached_session.get('https://docs.python.org/3/')

print(f'from_cache: {response.from_cache}')
print(f'status_cache: {response.status_code}')
if False == response.from_cache:
    print(response.text)
