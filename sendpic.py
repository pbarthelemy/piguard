import requests
import HartlandPiconfig as cfg

rq = cfg.synoconst
rq.update(cfg.synotoken)
rq['payload'] = '{"text": "my first webhook via rest","file_url": "http://192.168.0.118:8000/a.jpg"}'

r = requests.get(cfg.synoURL, params=rq)

print(r.url)
print(r.status_code)
print(r.text)
print(r.json)
