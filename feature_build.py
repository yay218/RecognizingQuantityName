import numpy as np 
import glob
import pandas as pd
import csv
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

file_root = '/net/dusk/pool0/data1/wume/zhc415/exp/data_engine/automatic-eureka/data'

with open('length_type_unit.txt', 'r') as reader:
	content = [x.strip().split(';') for x in reader.readlines()]

	# # id = content[:,0]
	# for row in content:
	# 	length = len(content)

	# print(content.shape)
	# csv_path_list = []
	# column_names = []
	# for x in content:
	# 	column_amount = len(x)
	# 	csv_path = '/'.join([file_root] + x[1:3] + ['data.csv'])
	# 	column_names = x[3:column_amount + 1]
	# 	df = pd.read_csv(csv_path, header = 0)
	# 	for name in column_names:
	# 		content = df[name].tolist()
	# 		print(content)

	csv_path_list = ['/'.join([file_root] + x[:2]+['data.csv']) for x in content]
	column_names_list = [x[2:] for x in content]
	corpus = []
	index = 0
	for csv_path, column_names in zip(csv_path_list, column_names_list):
		index = index + 1
		print(index)
		for single_column in column_names:
			try:
				df = pd.read_csv(csv_path, header=0, low_memory = True)
				content = df[single_column].values.tolist()
				content_list = [x for x in content if str(x) != 'nan']
				

				#######################################
				# Features:
				# 	column content:
				# 	1. maximum value in the column
		  		# 	2. minimum value in the column
		  		# 	3. average value in the column
		  		# 	4. range value in the column
		  		# 	5. length of the maximum value in the column
		  		# 	6. ????????? int or decimal (0 or 1)
		  		# 	7. 
		  		# 	column name:
		  		# 	1. number of characters
		  		# 	2. number of words
		  		# 	3. rule-based features
				#######################################
				
				maximum_value = max(content_list)
				minimum_value = min(content_list)
				average_value = reduce(lambda x, y: x + y, content_list) / len(content_list)
				range_value = maximum_value - minimum_value
				length_max_value = len(str(maximum_value))
				# document = ''
				# for i in content_list:
				# 	document = document + ' ' + str(i)
				# corpus.append(document)


				number_char = len(single_column)
				number_word = len(single_column.split())

				length_type = 0
				time_type = 0
				percent_type = 0
				currency_type = 0
				weight_type = 0
				length = ['meter', '(m)', 'in_m', 'mile', '(mi)', 'in_mi', 'inch', '(in)', 'in_in', 'feet', '(ft)', 'in_ft', 'length', 'height', 'width']
				time = ['second', '(s)', 'in_s', '(sec)', 'in_sec', 'minute', '(min)', 'in_min', 'hour', '(hr)', 'in_hr', 'hrs', 'in_hrs', 'duration', 'time']
				percent = ['percent', '%', 'percentage', 'accuracy']
				currency = ['dollar', '$', 'usd', 'euro', 'EUR', 'pound', 'GBP', 'amount', 'cost']
				weight = ['weight', 'gram', 'kilogram', '(g)', 'in_g', '(kg)', 'in_kg', 'pound', '(lb)', 'in_lb', 'ounce', '(oz)', 'in_oz', 'tons', '(t)', 'in_t']
				for unit_length in length:
					if unit_length in single_column.lower():
						length_type = 1
				for unit_time in time:
					if unit_time in single_column.lower():
						time_type = 1
				for unit_percent in percent:
					if unit_percent in single_column.lower():
						percent_type = 1
				for unit_currency in currency:
					if unit_currency in single_column.lower():
						currency_type = 1
				for unit_weight in weight:
					if unit_weight in single_column.lower():
						weight_type = 1


				new_row = []
				new_row.append(csv_path.strip().split('/')[11])
				new_row.append(csv_path.strip().split('/')[12])
				new_row.append(single_column)

				new_row.append(maximum_value)
				new_row.append(minimum_value)
				new_row.append(average_value)
				new_row.append(range_value)
				new_row.append(length_max_value)

				new_row.append(number_char)
				new_row.append(number_word)
				new_row.append(length_type)
				new_row.append(time_type)
				new_row.append(percent_type)
				new_row.append(currency_type)
				new_row.append(weight_type)

				new_row.append('1')
				print("ok")

				with open(r'features_length.csv', 'a') as f:
					writer = csv.writer(f)
					writer.writerow(new_row)

			except Exception as e:
				pass

with open('time_type_unit.txt', 'r') as reader:
	content = [x.strip().split(';') for x in reader.readlines()]

	# # id = content[:,0]
	# for row in content:
	# 	length = len(content)

	# print(content.shape)
	# csv_path_list = []
	# column_names = []
	# for x in content:
	# 	column_amount = len(x)
	# 	csv_path = '/'.join([file_root] + x[1:3] + ['data.csv'])
	# 	column_names = x[3:column_amount + 1]
	# 	df = pd.read_csv(csv_path, header = 0)
	# 	for name in column_names:
	# 		content = df[name].tolist()
	# 		print(content)

	csv_path_list = ['/'.join([file_root] + x[:2]+['data.csv']) for x in content]
	column_names_list = [x[2:] for x in content]
	corpus = []
	index = 0
	for csv_path, column_names in zip(csv_path_list, column_names_list):
		index = index + 1
		print(index)
		for single_column in column_names:
			try:
				df = pd.read_csv(csv_path, header=0, low_memory = True)
				content = df[single_column].values.tolist()
				content_list = [x for x in content if str(x) != 'nan']
				

				#######################################
				# Features:
				# 	column content:
				# 	1. maximum value in the column
		  		# 	2. minimum value in the column
		  		# 	3. average value in the column
		  		# 	4. range value in the column
		  		# 	5. length of the maximum value in the column
		  		# 	6. ????????? int or decimal (0 or 1)
		  		# 	7. 
		  		# 	column name:
		  		# 	1. number of characters
		  		# 	2. number of words
		  		# 	3. rule-based features
				#######################################
				
				maximum_value = max(content_list)
				minimum_value = min(content_list)
				average_value = reduce(lambda x, y: x + y, content_list) / len(content_list)
				range_value = maximum_value - minimum_value
				length_max_value = len(str(maximum_value))
				# document = ''
				# for i in content_list:
				# 	document = document + ' ' + str(i)
				# corpus.append(document)


				number_char = len(single_column)
				number_word = len(single_column.split())

				length_type = 0
				time_type = 0
				percent_type = 0
				currency_type = 0
				weight_type = 0
				length = ['meter', '(m)', 'in_m', 'mile', '(mi)', 'in_mi', 'inch', '(in)', 'in_in', 'feet', '(ft)', 'in_ft', 'length', 'height', 'width']
				time = ['second', '(s)', 'in_s', '(sec)', 'in_sec', 'minute', '(min)', 'in_min', 'hour', '(hr)', 'in_hr', 'hrs', 'in_hrs', 'duration', 'time']
				percent = ['percent', '%', 'percentage', 'accuracy']
				currency = ['dollar', '$', 'usd', 'euro', 'EUR', 'pound', 'GBP', 'amount', 'cost']
				weight = ['weight', 'gram', 'kilogram', '(g)', 'in_g', '(kg)', 'in_kg', 'pound', '(lb)', 'in_lb', 'ounce', '(oz)', 'in_oz', 'tons', '(t)', 'in_t']
				for unit_length in length:
					if unit_length in single_column.lower():
						length_type = 1
				for unit_time in time:
					if unit_time in single_column.lower():
						time_type = 1
				for unit_percent in percent:
					if unit_percent in single_column.lower():
						percent_type = 1
				for unit_currency in currency:
					if unit_currency in single_column.lower():
						currency_type = 1
				for unit_weight in weight:
					if unit_weight in single_column.lower():
						weight_type = 1


				new_row = []
				new_row.append(csv_path.strip().split('/')[11])
				new_row.append(csv_path.strip().split('/')[12])
				new_row.append(single_column)

				new_row.append(maximum_value)
				new_row.append(minimum_value)
				new_row.append(average_value)
				new_row.append(range_value)
				new_row.append(length_max_value)

				new_row.append(number_char)
				new_row.append(number_word)
				new_row.append(length_type)
				new_row.append(time_type)
				new_row.append(percent_type)
				new_row.append(currency_type)
				new_row.append(weight_type)

				new_row.append('2')
				print("ok")

				with open(r'features_time.csv', 'a') as f:
					writer = csv.writer(f)
					writer.writerow(new_row)

			except Exception as e:
				pass



with open('percent_type_unit.txt', 'r') as reader:
	content = [x.strip().split(';') for x in reader.readlines()]

	# # id = content[:,0]
	# for row in content:
	# 	length = len(content)

	# print(content.shape)
	# csv_path_list = []
	# column_names = []
	# for x in content:
	# 	column_amount = len(x)
	# 	csv_path = '/'.join([file_root] + x[1:3] + ['data.csv'])
	# 	column_names = x[3:column_amount + 1]
	# 	df = pd.read_csv(csv_path, header = 0)
	# 	for name in column_names:
	# 		content = df[name].tolist()
	# 		print(content)

	csv_path_list = ['/'.join([file_root] + x[:2]+['data.csv']) for x in content]
	column_names_list = [x[2:] for x in content]
	corpus = []
	index = 0
	for csv_path, column_names in zip(csv_path_list, column_names_list):
		index = index + 1
		print(index)
		for single_column in column_names:
			try:
				df = pd.read_csv(csv_path, header=0, low_memory = True)
				content = df[single_column].values.tolist()
				content_list = [x for x in content if str(x) != 'nan']
				

				#######################################
				# Features:
				# 	column content:
				# 	1. maximum value in the column
		  		# 	2. minimum value in the column
		  		# 	3. average value in the column
		  		# 	4. range value in the column
		  		# 	5. length of the maximum value in the column
		  		# 	6. ????????? int or decimal (0 or 1)
		  		# 	7. 
		  		# 	column name:
		  		# 	1. number of characters
		  		# 	2. number of words
		  		# 	3. rule-based features
				#######################################
				
				maximum_value = max(content_list)
				minimum_value = min(content_list)
				average_value = reduce(lambda x, y: x + y, content_list) / len(content_list)
				range_value = maximum_value - minimum_value
				length_max_value = len(str(maximum_value))
				# document = ''
				# for i in content_list:
				# 	document = document + ' ' + str(i)
				# corpus.append(document)


				number_char = len(single_column)
				number_word = len(single_column.split())

				length_type = 0
				time_type = 0
				percent_type = 0
				currency_type = 0
				weight_type = 0
				length = ['meter', '(m)', 'in_m', 'mile', '(mi)', 'in_mi', 'inch', '(in)', 'in_in', 'feet', '(ft)', 'in_ft', 'length', 'height', 'width']
				time = ['second', '(s)', 'in_s', '(sec)', 'in_sec', 'minute', '(min)', 'in_min', 'hour', '(hr)', 'in_hr', 'hrs', 'in_hrs', 'duration', 'time']
				percent = ['percent', '%', 'percentage', 'accuracy']
				currency = ['dollar', '$', 'usd', 'euro', 'EUR', 'pound', 'GBP', 'amount', 'cost']
				weight = ['weight', 'gram', 'kilogram', '(g)', 'in_g', '(kg)', 'in_kg', 'pound', '(lb)', 'in_lb', 'ounce', '(oz)', 'in_oz', 'tons', '(t)', 'in_t']
				for unit_length in length:
					if unit_length in single_column.lower():
						length_type = 1
				for unit_time in time:
					if unit_time in single_column.lower():
						time_type = 1
				for unit_percent in percent:
					if unit_percent in single_column.lower():
						percent_type = 1
				for unit_currency in currency:
					if unit_currency in single_column.lower():
						currency_type = 1
				for unit_weight in weight:
					if unit_weight in single_column.lower():
						weight_type = 1


				new_row = []
				new_row.append(csv_path.strip().split('/')[11])
				new_row.append(csv_path.strip().split('/')[12])
				new_row.append(single_column)

				new_row.append(maximum_value)
				new_row.append(minimum_value)
				new_row.append(average_value)
				new_row.append(range_value)
				new_row.append(length_max_value)

				new_row.append(number_char)
				new_row.append(number_word)
				new_row.append(length_type)
				new_row.append(time_type)
				new_row.append(percent_type)
				new_row.append(currency_type)
				new_row.append(weight_type)

				new_row.append('3')
				print("ok")

				with open(r'features_percent.csv', 'a') as f:
					writer = csv.writer(f)
					writer.writerow(new_row)

			except Exception as e:
				pass

with open('currency_type_unit.txt', 'r') as reader:
	content = [x.strip().split(';') for x in reader.readlines()]

	# # id = content[:,0]
	# for row in content:
	# 	length = len(content)

	# print(content.shape)
	# csv_path_list = []
	# column_names = []
	# for x in content:
	# 	column_amount = len(x)
	# 	csv_path = '/'.join([file_root] + x[1:3] + ['data.csv'])
	# 	column_names = x[3:column_amount + 1]
	# 	df = pd.read_csv(csv_path, header = 0)
	# 	for name in column_names:
	# 		content = df[name].tolist()
	# 		print(content)

	csv_path_list = ['/'.join([file_root] + x[:2]+['data.csv']) for x in content]
	column_names_list = [x[2:] for x in content]
	corpus = []
	index = 0
	for csv_path, column_names in zip(csv_path_list, column_names_list):
		index = index + 1
		print(index)
		for single_column in column_names:
			try:
				df = pd.read_csv(csv_path, header=0, low_memory = True)
				content = df[single_column].values.tolist()
				content_list = [x for x in content if str(x) != 'nan']
				

				#######################################
				# Features:
				# 	column content:
				# 	1. maximum value in the column
		  		# 	2. minimum value in the column
		  		# 	3. average value in the column
		  		# 	4. range value in the column
		  		# 	5. length of the maximum value in the column
		  		# 	6. ????????? int or decimal (0 or 1)
		  		# 	7. 
		  		# 	column name:
		  		# 	1. number of characters
		  		# 	2. number of words
		  		# 	3. rule-based features
				#######################################
				
				maximum_value = max(content_list)
				minimum_value = min(content_list)
				average_value = reduce(lambda x, y: x + y, content_list) / len(content_list)
				range_value = maximum_value - minimum_value
				length_max_value = len(str(maximum_value))
				# document = ''
				# for i in content_list:
				# 	document = document + ' ' + str(i)
				# corpus.append(document)


				number_char = len(single_column)
				number_word = len(single_column.split())

				length_type = 0
				time_type = 0
				percent_type = 0
				currency_type = 0
				weight_type = 0
				length = ['meter', '(m)', 'in_m', 'mile', '(mi)', 'in_mi', 'inch', '(in)', 'in_in', 'feet', '(ft)', 'in_ft', 'length', 'height', 'width']
				time = ['second', '(s)', 'in_s', '(sec)', 'in_sec', 'minute', '(min)', 'in_min', 'hour', '(hr)', 'in_hr', 'hrs', 'in_hrs', 'duration', 'time']
				percent = ['percent', '%', 'percentage', 'accuracy']
				currency = ['dollar', '$', 'usd', 'euro', 'EUR', 'pound', 'GBP', 'amount', 'cost']
				weight = ['weight', 'gram', 'kilogram', '(g)', 'in_g', '(kg)', 'in_kg', 'pound', '(lb)', 'in_lb', 'ounce', '(oz)', 'in_oz', 'tons', '(t)', 'in_t']
				for unit_length in length:
					if unit_length in single_column.lower():
						length_type = 1
				for unit_time in time:
					if unit_time in single_column.lower():
						time_type = 1
				for unit_percent in percent:
					if unit_percent in single_column.lower():
						percent_type = 1
				for unit_currency in currency:
					if unit_currency in single_column.lower():
						currency_type = 1
				for unit_weight in weight:
					if unit_weight in single_column.lower():
						weight_type = 1


				new_row = []
				new_row.append(csv_path.strip().split('/')[11])
				new_row.append(csv_path.strip().split('/')[12])
				new_row.append(single_column)

				new_row.append(maximum_value)
				new_row.append(minimum_value)
				new_row.append(average_value)
				new_row.append(range_value)
				new_row.append(length_max_value)

				new_row.append(number_char)
				new_row.append(number_word)
				new_row.append(length_type)
				new_row.append(time_type)
				new_row.append(percent_type)
				new_row.append(currency_type)
				new_row.append(weight_type)

				new_row.append('4')
				print("ok")

				with open(r'features_currency.csv', 'a') as f:
					writer = csv.writer(f)
					writer.writerow(new_row)

			except Exception as e:
				pass


with open('weight_type_unit.txt', 'r') as reader:
	content = [x.strip().split(';') for x in reader.readlines()]

	# # id = content[:,0]
	# for row in content:
	# 	length = len(content)

	# print(content.shape)
	# csv_path_list = []
	# column_names = []
	# for x in content:
	# 	column_amount = len(x)
	# 	csv_path = '/'.join([file_root] + x[1:3] + ['data.csv'])
	# 	column_names = x[3:column_amount + 1]
	# 	df = pd.read_csv(csv_path, header = 0)
	# 	for name in column_names:
	# 		content = df[name].tolist()
	# 		print(content)

	csv_path_list = ['/'.join([file_root] + x[:2]+['data.csv']) for x in content]
	column_names_list = [x[2:] for x in content]
	corpus = []
	index = 0
	for csv_path, column_names in zip(csv_path_list, column_names_list):
		index = index + 1
		print(index)
		for single_column in column_names:
			try:
				df = pd.read_csv(csv_path, header=0, low_memory = True)
				content = df[single_column].values.tolist()
				content_list = [x for x in content if str(x) != 'nan']
				

				#######################################
				# Features:
				# 	column content:
				# 	1. maximum value in the column
		  		# 	2. minimum value in the column
		  		# 	3. average value in the column
		  		# 	4. range value in the column
		  		# 	5. length of the maximum value in the column
		  		# 	6. ????????? int or decimal (0 or 1)
		  		# 	7. 
		  		# 	column name:
		  		# 	1. number of characters
		  		# 	2. number of words
		  		# 	3. rule-based features
				#######################################
				
				maximum_value = max(content_list)
				minimum_value = min(content_list)
				average_value = reduce(lambda x, y: x + y, content_list) / len(content_list)
				range_value = maximum_value - minimum_value
				length_max_value = len(str(maximum_value))
				# document = ''
				# for i in content_list:
				# 	document = document + ' ' + str(i)
				# corpus.append(document)


				number_char = len(single_column)
				number_word = len(single_column.split())

				length_type = 0
				time_type = 0
				percent_type = 0
				currency_type = 0
				weight_type = 0
				length = ['meter', '(m)', 'in_m', 'mile', '(mi)', 'in_mi', 'inch', '(in)', 'in_in', 'feet', '(ft)', 'in_ft', 'length', 'height', 'width']
				time = ['second', '(s)', 'in_s', '(sec)', 'in_sec', 'minute', '(min)', 'in_min', 'hour', '(hr)', 'in_hr', 'hrs', 'in_hrs', 'duration', 'time']
				percent = ['percent', '%', 'percentage', 'accuracy']
				currency = ['dollar', '$', 'usd', 'euro', 'EUR', 'pound', 'GBP', 'amount', 'cost']
				weight = ['weight', 'gram', 'kilogram', '(g)', 'in_g', '(kg)', 'in_kg', 'pound', '(lb)', 'in_lb', 'ounce', '(oz)', 'in_oz', 'tons', '(t)', 'in_t']
				for unit_length in length:
					if unit_length in single_column.lower():
						length_type = 1
				for unit_time in time:
					if unit_time in single_column.lower():
						time_type = 1
				for unit_percent in percent:
					if unit_percent in single_column.lower():
						percent_type = 1
				for unit_currency in currency:
					if unit_currency in single_column.lower():
						currency_type = 1
				for unit_weight in weight:
					if unit_weight in single_column.lower():
						weight_type = 1


				new_row = []
				new_row.append(csv_path.strip().split('/')[11])
				new_row.append(csv_path.strip().split('/')[12])
				new_row.append(single_column)

				new_row.append(maximum_value)
				new_row.append(minimum_value)
				new_row.append(average_value)
				new_row.append(range_value)
				new_row.append(length_max_value)

				new_row.append(number_char)
				new_row.append(number_word)
				new_row.append(length_type)
				new_row.append(time_type)
				new_row.append(percent_type)
				new_row.append(currency_type)
				new_row.append(weight_type)

				new_row.append('5')
				print("ok")

				with open(r'features_weight.csv', 'a') as f:
					writer = csv.writer(f)
					writer.writerow(new_row)

			except Exception as e:
				pass

with open('none_type_unit.txt', 'r') as reader:
	content = [x.strip().split(';') for x in reader.readlines()]

	# # id = content[:,0]
	# for row in content:
	# 	length = len(content)

	# print(content.shape)
	# csv_path_list = []
	# column_names = []
	# for x in content:
	# 	column_amount = len(x)
	# 	csv_path = '/'.join([file_root] + x[1:3] + ['data.csv'])
	# 	column_names = x[3:column_amount + 1]
	# 	df = pd.read_csv(csv_path, header = 0)
	# 	for name in column_names:
	# 		content = df[name].tolist()
	# 		print(content)

	csv_path_list = ['/'.join([file_root] + x[:2]+['data.csv']) for x in content]
	column_names_list = [x[2:] for x in content]
	corpus = []
	index = 0
	for csv_path, column_names in zip(csv_path_list, column_names_list):
		index = index + 1
		print(index)
		for single_column in column_names:
			try:
				df = pd.read_csv(csv_path, header=0, low_memory = True)
				content = df[single_column].values.tolist()
				content_list = [x for x in content if str(x) != 'nan']
				

				#######################################
				# Features:
				# 	column content:
				# 	1. maximum value in the column
		  		# 	2. minimum value in the column
		  		# 	3. average value in the column
		  		# 	4. range value in the column
		  		# 	5. length of the maximum value in the column
		  		# 	6. ????????? int or decimal (0 or 1)
		  		# 	7. 
		  		# 	column name:
		  		# 	1. number of characters
		  		# 	2. number of words
		  		# 	3. rule-based features
				#######################################
				
				maximum_value = max(content_list)
				minimum_value = min(content_list)
				average_value = reduce(lambda x, y: x + y, content_list) / len(content_list)
				range_value = maximum_value - minimum_value
				length_max_value = len(str(maximum_value))
				# document = ''
				# for i in content_list:
				# 	document = document + ' ' + str(i)
				# corpus.append(document)


				number_char = len(single_column)
				number_word = len(single_column.split())

				length_type = 0
				time_type = 0
				percent_type = 0
				currency_type = 0
				weight_type = 0
				length = ['meter', '(m)', 'in_m', 'mile', '(mi)', 'in_mi', 'inch', '(in)', 'in_in', 'feet', '(ft)', 'in_ft', 'length', 'height', 'width']
				time = ['second', '(s)', 'in_s', '(sec)', 'in_sec', 'minute', '(min)', 'in_min', 'hour', '(hr)', 'in_hr', 'hrs', 'in_hrs', 'duration', 'time']
				percent = ['percent', '%', 'percentage', 'accuracy']
				currency = ['dollar', '$', 'usd', 'euro', 'EUR', 'pound', 'GBP', 'amount', 'cost']
				weight = ['weight', 'gram', 'kilogram', '(g)', 'in_g', '(kg)', 'in_kg', 'pound', '(lb)', 'in_lb', 'ounce', '(oz)', 'in_oz', 'tons', '(t)', 'in_t']
				for unit_length in length:
					if unit_length in single_column.lower():
						length_type = 1
				for unit_time in time:
					if unit_time in single_column.lower():
						time_type = 1
				for unit_percent in percent:
					if unit_percent in single_column.lower():
						percent_type = 1
				for unit_currency in currency:
					if unit_currency in single_column.lower():
						currency_type = 1
				for unit_weight in weight:
					if unit_weight in single_column.lower():
						weight_type = 1


				new_row = []
				new_row.append(csv_path.strip().split('/')[11])
				new_row.append(csv_path.strip().split('/')[12])
				new_row.append(single_column)

				new_row.append(maximum_value)
				new_row.append(minimum_value)
				new_row.append(average_value)
				new_row.append(range_value)
				new_row.append(length_max_value)

				new_row.append(number_char)
				new_row.append(number_word)
				new_row.append(length_type)
				new_row.append(time_type)
				new_row.append(percent_type)
				new_row.append(currency_type)
				new_row.append(weight_type)

				new_row.append('0')
				print("ok")

				with open(r'features_none.csv', 'a') as f:
					writer = csv.writer(f)
					writer.writerow(new_row)

			except Exception as e:
				pass

	# count_vect = CountVectorizer()
	# X_train_counts = count_vect.fit_transform(corpus)
	# tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
	# X_train_tf = tf_transformer.transform(X_train_counts)

	# with open('returns.csv', 'wb') as output:
	# 	writer = csv.writer(output)
	# 	for val in X_train_tf.todense():
	# 		writer.writerow([val])
			





