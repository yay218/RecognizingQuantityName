import numpy as numpy
import pandas as pd

with open('none.txt', 'r') as reader:
	content = [x.strip().split(';') for x in reader.readlines()]
	previous_dataset_id = ''
	previous_csv_id = ''
	previous_column_name = ''
	for index, single_content in enumerate(content):
		if index > 0:
			if (content[index - 1][0] == single_content[0]):# and (content[index - 1][2] == single_content[2]):
				continue	
			else:
				print(single_content[0] + ';' + single_content[1] + ';' + single_content[2])
		# xnt_column_name = single_content[2]

