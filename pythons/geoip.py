#/usr/bin/env python
#import sys 

import geoip2.database
#import maxminddb

class GeoIP():
	def get_iso_code(self,ip_address):
		try:
			reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
			response = reader.city(ip_address)
			iso_code = response.country.iso_code
			return iso_code
		except Exception, e:
			print e
			return False


if __name__ == '__main__':
	geoip = GeoIP()
	while True:
		try:
			your_ip_address = raw_input('Input ip address: ')
			break
		except (KeyboardInterrupt, EOFError, ValueError):
			print '\ninvalid input... try again'

	try:
		your_country_code = geoip.get_iso_code(your_ip_address)
		if  your_country_code:
			print 'Country code of \'%s\' is \'%s\'.'%(your_ip_address, your_country_code)
		else:
			print 'Failed to get country code.'
	except Exception, e:
		print e
	finally:
		print 'Script closed.'