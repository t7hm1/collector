import re
import sys
import string
from termcolor import colored,cprint
sys.dont_write_byte_code=True

class Parser:
	def __init__(self,result,domain,counter):
		self.result 	= result
		self.domain 	= domain
		self.counter    = counter
		self.users  	= []

	def genericClean(self):
		self.result = re.sub('<b>','',self.result)
		self.result = re.sub('</b>','',self.result)
		self.result = re.sub('<em>','',self.result)
		self.result = re.sub('</em>','',self.result)
		self.result = re.sub('<wbr>','',self.result)
		self.result = re.sub('</wbr>','',self.result)
		self.result = re.sub('<strong>','',self.result)
		self.result = re.sub('</strong>','',self.result)
		self.result = re.sub('%2f',' ',self.result)
		self.result = re.sub('%3a',' ',self.result)
		for e in ('>','<',':',';','/','\\','&','%3A','%3D','%3C'):
			self.result = string.replace(self.result,e,' ')

	def __Twitter_parser(self):
		try:
			twitter_reg = re.compile('(@[a-zA-Z0-9._ -]*)')
			parse_it    = twitter_reg.findall(self.result)
			count 		= self.counter._count_it(parse_it)
			users		= self.counter._return_list()

			for u in users:
				y = string.replace(u, ' | LinkedIn', '')
				y = string.replace(y, ' profiles ', '')
				y = string.replace(y, 'LinkedIn', '')
				y = string.replace(y, '"', '')
				y = string.replace(y, '>', '')
				if y != " ":
					self.users.append(y)
			return self.users

		except KeyboardInterrupt:
			sys.exit(cprint('[-] Canceled by user','red'))

	def __Linkedin_parser(self):
		try:
			linkedin_reg = re.compile('">[a-zA-Z0-9._ -]* \| LinkedIn')
			parse_it 	 = linkedin_reg.findall(self.result)
			count 		 = self.counter._count_it(parse_it)
			users 		 = self.counter._return_list()
			
			for u in users:
				y = string.replace(u, '| LinkedIn', '')
				y = string.replace(y, ' profiles ', '')
				y = string.replace(y, 'LinkedIn', '')
				y = string.replace(y, '"', '')
				y = string.replace(y, '>', '')
				if y != " ":
					self.users.append(y)
			return self.users

		except KeyboardInterrupt:
			sys.exit(cprint('[-] Canceled by user','red'))

	def __Gplus_parser(self):
		try:
			self.result = re.sub('</b>', '', self.result)
			self.result = re.sub('<b>', '', self.result)

			gplus_reg   = re.compile('>[a-zA-Z0-9._ ]* - Google\+')
			parse_it    = gplus_reg.findall(self.result)
			count 		= self.counter._count_it(parse_it)
			users		= self.counter._return_list()

			for u in users:
				y = string.replace(u, ' | LinkedIn','')
				y = string.replace(y, ' profiles ','')
				y = string.replace(y, 'LinkedIn','')
				y = string.replace(y, '"','')
				y = string.replace(y, '>', '')
				if y != " ":
					self.users.append(y)
			return self.users
		except KeyboardInterrupt:
			sys.exit(cprint('[-] Canceled by user','red'))

