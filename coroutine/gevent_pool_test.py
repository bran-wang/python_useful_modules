import requests
import gevent

from gevent import monkey, pool
monkey.patch_all()

p = pool.Pool(10)
jobs = []
urls = [
  'http://www.baidu.com',
  'http://github.com'
]

def get_links(url):
  r = requests.get(url)
  if r.status_code == 200:
    print url, "ok"

for url in urls:
  jobs.append(p.spawn(get_links, url))

gevent.joinall(jobs)
