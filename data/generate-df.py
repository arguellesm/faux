from cgitb import text
import pandas as pd
import json
import os


def get_text(path):
	"""
	Extracts text.
	"""

	with open(path) as f:
		file = json.load(f)

	return file['text']


def get_authors(path):
	"""
	Extract author(s) if there are any.
	"""

	with open(path) as f:
		file = json.load(f)
		
	if 'authors' in file.keys():
		authors = file['authors']

	return authors


def generate_df():
	"""
	Generates .csv dataframe.
	"""

	# json fields
	headlines = []
	ratings = []
	texts = []
	sources = []
	original_titles	= []
	links = []
	authors = []

	# get articles
	with open('dataset/reviews/HealthRelease.json') as f:
		release = json.load(f)

	with open('dataset/reviews/HealthStory.json') as f:
		history = json.load(f)

	# get release articles information
	for i in release:
		path = 'dataset/content/HealthRelease/' + i['news_id'] + '.json'

		if not os.path.exists(path):
			continue

		texts.append(get_text(path))
		authors.append(get_authors(path))
		headlines.append(i['title'])
		sources.append(i['news_source'])
		original_titles.append(i['original_title'])
		links.append(i['link'])
		ratings.append(i['rating'])


	# get history articles information
	for i in history:
		path = 'dataset/content/HealthStory/' + i['news_id'] + '.json'

		if not os.path.exists(path):
			continue

		texts.append(get_text(path))
		authors.append(get_authors(path))
		headlines.append(i['title'])
		sources.append(i['news_source'])
		original_titles.append(i['original_title'])
		links.append(i['link'])
		ratings.append(i['rating'])


	# create pandas dataframe
	df = pd.DataFrame({
		'headline' 		: headlines,
		'author'  		: authors,
		'source' 		: sources,
		'original title': original_titles,
		'link' 			: links,
		'text' 			: texts,
		'rating' 		: ratings
		})

	# export to csv
	df.to_csv('dataset.csv')



if __name__ == "__main__":
	generate_df()
