import os
import time
import pickle
import pandas as pd
from bs4 import BeautifulSoup
from multiprocessing import Process
from multiprocessing import Manager
from multiprocessing import cpu_count

### Configuration ###

inpath = 'plwiki3'
outfile = 'wikipedia.pickle'
threads = cpu_count()

### End #############

def listfiles( path:str ) -> list:
	files = []
	for f in os.listdir( path ):
		if f[-4:] == '.txt':
			files.append( os.path.abspath( path + '/' + f ))
		else:
			files += listfiles( path + '/' + f )
	return files

def read( id, files, start, end, values ) -> None:
	tab = []

	for path in files[start:end]:
		with open( path, 'r', encoding='utf-8' ) as f:
			article = f.read()
			soup = BeautifulSoup( article, 'lxml' )
			id = soup.find( 'doc' )[ 'id' ]
			url = soup.find( 'doc' )[ 'url' ]
			title = soup.find( 'doc' )[ 'title' ]
			text = soup.find( 'doc' ).text
			pos = text.find('\n\n')
			tab.append( [id, url, title, text[pos+2:]] )

	values[id] = tab
	return


if __name__ == '__main__':
	files = listfiles( inpath )
	files.sort()

	scope = len( files ) // threads
	rest = len( files ) % threads

	manager = Manager()
	values = manager.dict()

	procs = []
	for n in range( threads ):
		start = n * scope
		end = start + scope
		if n == threads - 1:
			end += rest

		th = Process(
			target=read,
			args=( n, files, start, end, values )
		)
		procs.append( th )
		th.start()
	
	start = time.time()
	for proc in procs:
		proc.join()
	stop = time.time()
	print( 'time: {0:02f}s'.format( stop - start ) )

	data = []
	for val in values.values():
		data += val
	
	df = pd.DataFrame( data=data, columns=['id', 'url', 'title', 'text'] )
	
	pickle.dump( df, open( outfile, 'wb' ))