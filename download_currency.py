'''
By : Real Limoges

This script uses Quandl's free FRED library to download currency
data for major currencies to USD. In cases where the data is only
available in USD to FX, it is inverted.

'''
# Standard Modules

try:
	import Quandl
	import pandas
	import pickle
	import sys
except:
	from setuptools.command import easy_install
	for req in REQUIREMENTS:
		easy_install.main( [req] )

# User Made Modules
import global_vars


def main():
	curr_series = ['FRED/DEXCAUS', 'FRED/DEXUSEU', 'FRED/DEXUSUK', 
				   'FRED/DEXJPUS']
	
	reverse_series = ['FRED/DEXCAUS', 'FRED/DEJPUS']


	try:
		df = Quandl.get(curr_series, authtoken = global_vars.API_KEY)
		reverse_series = [ x.replace('/', '.') for x in reverse_series ]
		reverse_series = [ x + ' - Value' for x in reverse_series ]
		
		try:
			df.to_csv(global_vars.outfile, index = True)
		except:
			pickle.dump(df, global_vars.emergency_dump)
	except:
		print "Unexpected error:", sys.exc_info()

if __name__ == '__main__':
	main()