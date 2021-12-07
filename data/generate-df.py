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


def get_author(path):
	"""
	Extract author(s) if there are any.
	"""

	with open(path) as f:
		file = json.load(f)

	if 'author' in file.keys():
		author = file['author']

	if 'authors' in file.keys():
		author = file['authors']

	return author


def generate_df():
	"""
	Generates .csv dataframe.
	"""

	# json fields
	headline 	= []
	rating 		= []
	text 		= []
	source 		= []
	o_title		= []
	link 		= []
	author  	= []

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

		text.append(get_text(path))
		author.append(get_author(path))
		headline.append(i['title'])
		source.append(i['news_source'])
		o_title.append(i['original_title'])
		link.append(i['link'])
		rating.append(i['rating'])


	# get history articles information
	for i in history:
		path = 'dataset/content/HealthStory/' + i['news_id'] + '.json'

		if not os.path.exists(path):
			continue

		text.append(get_text(path))
		author.append(get_author(path))
		headline.append(i['title'])
		source.append(i['news_source'])
		o_title.append(i['original_title'])
		link.append(i['link'])
		rating.append(i['rating'])


	# create pandas dataframe
	df = pd.DataFrame({
		'headline' 		: headline,
		'author'  		: author,
		'source' 		: source,
		'original title': o_title,
		'link' 			: link,
		'text' 			: text,
		'rating' 		: rating
		})

	# export to csv
	df.to_csv('dataset.csv')



if __name__ == "__main__":
	generate_df()
