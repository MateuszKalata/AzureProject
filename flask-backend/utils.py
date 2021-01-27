import os
import pandas as pd
from sentence_transformers import SentenceTransformer
from sentence_transformers import util
import pickle
import time
import json

from flask import jsonify

WIKI_PICKLE_FILE_PATH = 'data/wikipedia2.pickle'
CORPUS_EMBEDDINGS_PICKLE_FILE_PATH = 'data/corpus_embeddings_for_cds_czywiesz_bi_encoder_600k.pickle'
MODEL_PATH = 'data/cds-czywiesz-bi-encoder--content-drive-MyDrive-models-cds-bi-encoder-cds-bi-encoder-paraphrase-xlm-r-multilingual-v1-2021-01-24_20-05-32-2021-01-24_22-00-53/'

class Utils:

	def __init__(self):
		self.wiki_pickle_file_path = WIKI_PICKLE_FILE_PATH
		self.loadWiki(self.wiki_pickle_file_path)

		print("load bi_encoder...")
		self.bi_encoder = SentenceTransformer(MODEL_PATH) # 'paraphrase-xlm-r-multilingual-v1'
		print("load corpus_embeddings_for_bi_encoder..")
		self.corpus_embeddings_for_bi_encoder = pickle.load( open( CORPUS_EMBEDDINGS_PICKLE_FILE_PATH, 'rb' ))

	def divide_into_par(self, text, threshold=10):
		splits = text.split('\n')
		pars = []
		par = ''
		for split in splits:
			words = split.split(' ')
			if len(words) > 0 and len(words) < threshold:
				if len(par) > 0:
					pars.append(par)
					par = ''
			elif len(words) > threshold:
				par += split
		if len(pars) > 0:
			return pars
		return [text]

	def loadWiki(self, file_path: str):
		wiki = pickle.load( open(file_path, 'rb' ))
		wiki = pd.DataFrame(data=wiki, columns=['id', 'url', 'title', 'text'])
		wiki['paragraph'] = wiki['text'].apply(self.divide_into_par)
		wiki.reset_index(drop=True, inplace=True)
		wiki = wiki.explode('paragraph')
		wiki.reset_index(drop=True, inplace=True)
		wiki = wiki.sort_values(by='title')
		wiki.reset_index(drop=True, inplace=True)
		self.wiki = wiki

	def search(self, question: str):
		bi_encoder = self.bi_encoder
		corpus = self.wiki
		corpus_embd = self.corpus_embeddings_for_bi_encoder
		query = question

		#Encode the query using the bi-encoder and find potentially relevant passages
		start_time = time.time()
		question_embedding = bi_encoder.encode(query, convert_to_tensor=True)
		hits = util.semantic_search(question_embedding, corpus_embd, top_k=10)
		hits = hits[0]  # Get the hits for the first query
		end_time = time.time()

		#Output of top-5 hits
		print("Input question:", query)
		print("Results (after {:.3f} seconds):".format(end_time - start_time))
		elements = []
		for hit in hits[0:10]:
			index = hit['corpus_id']
			article = corpus.iloc[index]	
			# print('\nTitle:', article['title'])
			# print('Paragraph:', article['paragraph'])
			# print('Url:', article['url'])
			# print('Index:', index)
			elem = {
				"title" : article['title'],
				"paragraph" : article['paragraph'],
				"url" : article['url'],
				"index" : int(index)
			}
			elements.append(elem)
		# print("\n\n========\n")
		return elements
