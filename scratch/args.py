import argparse
import requests
import HartlandPiconfig as cfg


parser = argparse.ArgumentParser(description='sendpic parameters')
parser.add_argument('-t', '--text',  action='store' , nargs=1,required=True ,
                    help='text of the message')
parser.add_argument('-u', '--url',  action='store' , nargs=1,required=True ,
                    help='URL of the image')

args = parser.parse_args()
print(args.text)
print(args.url)

rq = cfg.synoconst
rq.update(cfg.synotoken)

payload = '{"text": "' + args.text + '": "'+args.url+'"}'
print(payload)

rq['payload'] = '{"text": "' + args.text + '": "'+args.url+'"}'

r = requests.get(cfg.synoURL, params=rq)

print(r.url)
print(r.status_code)
print(r.text)
print(r.json)
