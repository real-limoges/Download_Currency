'''


'''
# Standard Modules
import Quandl
import pandas

# User Made Modules
import global_vars

# Global Variables
curr_series = ['FRED/DEXCAUS', 'FRED/DEXUSEU', 'FRED/DEXUSUK', 
			   'FRED/DEXJPUS']

reverse_series = ['FRED/DEXCAUS', 'FRED/DEJPUS']

API_KEY = global_vars.API_KEY
outfile = global_vars.outfile

def main():

	try:
		df = Quandl.get(curr_series)
		print df
		df.to_csv(outfile, index = True)
	except:
		raise Exception

if __name__ == '__main__':
	main()