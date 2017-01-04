import Quandl
import pandas as pd

api_key=open('quandlapikey.txt','r').read()

df=Quandl.get('FMAC/HPI_AK',authtoekn=api_key)

print df.head()