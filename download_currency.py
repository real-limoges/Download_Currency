'''


'''
# Standard Modules
import Quandl
import pandas

# Global Variables
curr_series = ['FRED/DEXCAUS', 'FRED/DEXUSEU', 'FRED/DEXUSUK', 
			   'FRED/DEXJPUS']

reverse_series = ['FRED/DEXCAUS', 'FRED/DEJPUS']

outfile = 'currency_data.csv'

def main():

	try:
		df = Quandl.get(curr_series)
		print df
		df.to_csv(outfile, index = True)
	except:
		raise Exception

if __name__ == '__main__':
	main()