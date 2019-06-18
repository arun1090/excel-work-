import xlsxwriter
#def file_read(fname):
  #  with open(fname) as f:
    #Content_list is the list that contains the read lines.     
	#	data = f.readline()
    #    # Some sample data for the table.



data = [
    ['Apples', 10000, 5000, 8000, 6000],
    ['Pears', 2000, 3000, 4000, 5000],
    ['Bananas', 6000, 6000, 6500, 6000],
    ['Oranges', 500, 300, 200, 700],

	]
workbook = xlsxwriter.Workbook('test1.xlsx')
worksheet = workbook.add_worksheet()
currency_format = workbook.add_format({'num_format': '$#,##0'})

caption = 'Table with column formats.'

# Set the columns widths.
worksheet.set_column('B:G', 12)
# Write the caption.
worksheet.write('B1', caption)
# Options to use in the table.
options = {'data': data,
		   'total_row': 1,
		   'columns': [{'header': 'Product', 'total_string': 'Totals'},
					   {'header': 'Quarter 1',
						'total_function': 'sum',
						'format': currency_format,
						},
					   {'header': 'Quarter 2',
						'total_function': 'sum',
						'format': currency_format,
						},
					   {'header': 'Quarter 3',
						'total_function': 'sum',
						'format': currency_format,
						},
					   {'header': 'Quarter 4',
						'total_function': 'sum',
						'format': currency_format,
						},
					   {'header': 'Year',
						'formula': '=SUM(Table1[@[Quarter 1]:[Quarter 4]])',
						'total_function': 'sum',
						'format': currency_format,
						},
					   ]}
# Add a table to the worksheet.
worksheet.add_table('B3:G8', options)
workbook.close()

#file_read('test.txt')