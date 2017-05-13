#!/usr/bin/python3

import os
import json

def split_into_pages(items, max_item_per_page):
	pages = []
	page = []
	nb_items = 1
	for item in items:
		if nb_items % max_item_per_page == 0:
			nb_items = 0
			pages.append(page)
			page = []
		page.append(item)
		nb_items += 1
	return pages

def export_jsondata_to_file(name, data):
	str = json.dumps(data, indent=4)
	file = open('results/' + name, 'w')
	file.write(str)
	file.close()

print('Step 1: Get Content')
contents = []
for filename in os.listdir('.'):
	if filename.endswith('.json'):
		file = open(filename, 'r')
		contents.append(file.read())

print('Step 2: Convert to JSON data')
datas = []
for content in contents:
	datas.append(json.loads(content))

print('Step 3: Split by word class')
verbs = []
nouns = []
na_adjectives = []
i_adjectives = []
for pages in datas:
	for word in pages:
		if word['class'] == 'i-adjective':
			i_adjectives.append(word)
		elif word['class'] == 'na-adjective':
			na_adjectives.append(word)
		elif word['class'] == 'noun':
			nouns.append(word)
		elif word['class'] == 'verb':
			verbs.append(word)

print('Step 4: Split into pages')

verbpages = split_into_pages(verbs, 10)
nounpages = split_into_pages(nouns, 10)
na_adjpages = split_into_pages(na_adjectives, 10)
i_adjpages =  split_into_pages(i_adjectives, 10)

print('Step 5: Export JSON data')
export_jsondata_to_file('verbs.json', verbpages)
export_jsondata_to_file('nouns.json', nounpages)
export_jsondata_to_file('na_adjectives.json', na_adjpages)
export_jsondata_to_file('i_adjectives,json', i_adjpages)
