import argparse

parser = argparse.ArgumentParser(description='sendpic parameters')
parser.add_argument('-t', '--text',  action='store' , nargs=1,required=True ,
                    help='text of the message')
parser.add_argument('-u', '--url',  action='store' , nargs=1,required=True ,
                    help='URL of the image')

args = parser.parse_args()
print args.text
print args.url
