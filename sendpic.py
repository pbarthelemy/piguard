import sys
import argparse
import requests
import HartlandPiconfig as cfg


parser = argparse.ArgumentParser(description='sendpic parameters')
parser.add_argument('-t', '--text',  action='store' ,required=True ,
                    help='text of the message')
parser.add_argument('-u', '--url',  action='store' ,nargs='?' ,
                    help='URL of the image')

args = parser.parse_args()


rq = cfg.synoconst
rq.update(cfg.synotoken)

if args.url is None :
	payload = '{"text": "' + args.text + '"}'
else :
	payload = '{"text": "' + args.text + '", "file_url":"'+ args.url + '"}'

print(payload)
rq['payload'] = payload

r = requests.get(cfg.synoURL, params=rq)

if r.status_code == 200  :
	exit(0)
else :
	print(r.url,file=sys.stderr)
	print(r.status_code,file=sys.stderr)
	print(r.text,file=sys.stderr)
	print(r.json,file=sys.stderr)
	exit(1)
