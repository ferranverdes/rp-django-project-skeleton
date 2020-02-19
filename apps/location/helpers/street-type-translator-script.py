#!/usr/bin/python

import json
from googletrans import Translator

with open('./input_file.json') as json_file:
	translator = Translator()
	input_data = json.load(json_file)
	output_data = []

	for input_object in input_data:
		name = input_object['fields']['name']
		name = name.lower().capitalize()

		translated_object = translator.translate(
			name,
			src='en',
			dest='ca',
		)

		translated_name = translated_object.text.lower().capitalize()

		record = {}
		record['model'] = "location.StreetTypeTranslation"
		record['pk'] = int(input_object['pk'])
		record['fields'] = {}
		record['fields']['base_street_type'] = input_object['pk']
		record['fields']['translated_to'] = 2
		record['fields']['name'] = translated_name
		record['fields']['abbreviation'] = input_object['fields']['abbreviation']

		output_data.append(record)

with open('output.json', 'w') as outfile:
	json.dump(output_data, outfile)
