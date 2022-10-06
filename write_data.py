import xlsxwriter
from parser_site import get_array_item


def writer(parametr):
	book = xlsxwriter.Workbook(r'C:\Users\Admin\Desktop\projects\parser\data.xlsx')
	page = book.add_worksheet('товар')

	row = 0
	column = 0

	page.set_column('A:A', 20)
	page.set_column('B:B', 50)
	page.set_column('C:C', 20)
	page.set_column('D:D', 50)


	for item in parametr():
		page.write(row, column, item[0])
		page.write(row, column+1, item[1])
		page.write(row, column+2, item[2])
		page.write(row, column+3, item[3])
		row += 1

	book.close()

writer(get_array_item)
