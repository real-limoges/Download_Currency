By: Real Limoges

-------------

Description:

This script uses Quandl's free databases of FRED data to download
the currencies required for PCRI. Downloads the currencies and then
transforms them into FX to USD (or how many USD it takes to buy 1 FX)

For instance:
On 9/8/15, it takes approximately 0.002 USD to buy one JPY.
On 9/8/15, it takes approximately 1.15 USD to buy one EUR.

Requirements:

Quandl should be installed in the python path. If not, the script will
use easy_install to install it onto the user's path.