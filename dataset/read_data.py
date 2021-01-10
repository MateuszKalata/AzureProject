import pickle
import pandas as pd

df = pickle.load( open( 'wikipedia.pickle', 'rb' ))

print( df.describe() )