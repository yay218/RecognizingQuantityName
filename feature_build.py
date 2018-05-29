import numpy as np 
import glob
import pandas as pd
import csv


file_root = '/data'

def feature(quantity_name):
	if quantity_name == 'length':
		txt_file = 'quantity_length.txt'
		csv_file = 'features_length.csv'
		append_number = '1'
	elif quantity_name == 'time':
		txt_file = 'quantity_time.txt'
		csv_file = 'features_time.csv'
		append_number = '2'
	elif quantity_name == 'percent':
		txt_file = 'quantity_percent.txt'
		csv_file = 'features_percent.csv'
		append_number = '3'
	elif quantity_name == 'currency':
		txt_file = 'quantity_currency.txt'
		csv_file = 'features_currency.csv'
		append_number = '4'
	elif quantity_name == 'weight':
		txt_file = 'quantity_weight.txt'
		csv_file = 'features_weight.csv'
		append_number = '5'
	elif quantity_name == 'none':
		txt_file = 'quantity_none.txt'
		csv_file = 'features_none.csv'
		append_number = '0'


	with open(txt_file, 'r') as reader:
		content = [x.strip().split(';') for x in reader.readlines()]
		csv_path_list = ['/'.join([file_root] + x[:2]+['data.csv']) for x in content]
		column_names_list = [x[2:] for x in content]

		index = 0
		for csv_path, column_names in zip(csv_path_list, column_names_list):
			index = index + 1
			print(index)
			for single_column in column_names:
				try:
					df = pd.read_csv(csv_path, header=0, low_memory = True)
					content = df[single_column].values.tolist()
					content_list = [x for x in content if str(x) != 'nan']
					

					##################################################################
					# Features:
					# 	Column Content:
					# 	1. Maximum value
			  		# 	2. Minimum value
			  		# 	3. Average value
			  		# 	4. Range value (maximum - minimum)
			  		# 	5. Length of the maximum value (when expressed as a string)
			  		# 	
			  		# 	Column Name:
			  		# 	1. Number of words
			  		# 	2. Number of characters
			  		# 	3. Presence of quantity-specific terms
					##################################################################
					
					maximum_value = max(content_list)
					minimum_value = min(content_list)
					average_value = reduce(lambda x, y: x + y, content_list) / len(content_list)
					range_value = maximum_value - minimum_value
					length_max_value = len(str(maximum_value))


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

					new_row.append(append_number)
					print("ok")

					with open(r'features_length.csv', 'a') as f:
						writer = csv.writer(f)
						writer.writerow(new_row)

				except Exception as e:
					pass


if __name__ == "__main__":
	feature('length')
	feature('time')
	feature('percent')
	feature('currency')
	feature('weight')
	feature('none')
	


