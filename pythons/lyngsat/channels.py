__author__ = 'www'
import threading

from lyngsat import Lyngsat
from lyngsat import MyLogging
from lyngsat import config_logging

if __name__ == '__main__':
	logger = config_logging(0)
	lyngsat = Lyngsat()

	urls_sats =  lyngsat.lookup_sat_urls('13.0E')
	for urls_sat in urls_sats:
		(result, chn_name) = lyngsat.lookup_chn_in_sat(urls_sat, 10758, 17022)
		if result:break
	logger.info('chn name:' + chn_name)

	exit()