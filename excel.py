import xlsxwriter
import settings

class excel():
    def printXLSX():

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(str(settings.contentDir)+"/"+str(settings.testName)+"/"+str(settings.testName)+".xlsx")
        worksheet = workbook.add_worksheet()

        # Start from the first cell. Rows and columns are zero indexed.
        row = 1
        col = 0

        worksheet.write(0, col,     "Workers")
        worksheet.write(0, col + 1, "mean")
        worksheet.write(0, col + 2, "std")
        worksheet.write(0, col + 3, "median")
        worksheet.write(0, col + 4, "min")
        worksheet.write(0, col + 5, "max")

        # Iterate over the data and write it out row by row.
        for key in settings.concurrency:
            print(key)
            worksheet.write(row, col,    key)
            worksheet.write(row, col + 1, settings.resultDict[str(key)]["avg"])
            worksheet.write(row, col + 2, settings.resultDict[str(key)]["std"])
            worksheet.write(row, col + 3, settings.resultDict[str(key)]["median"])
            worksheet.write(row, col + 4, settings.resultDict[str(key)]["min"])
            worksheet.write(row, col + 5, settings.resultDict[str(key)]["max"])
            row += 1

        # Write a total using a formula.
        # worksheet.write(row, 0, 'Total')
        # worksheet.write(row, 1, '=SUM(B2:B'+str(row-1)+')')
        # worksheet.write(row, 2, '=SUM(C2:C'+str(row-1)+')')
        # worksheet.write(row, 3, '=SUM(D2:D'+str(row-1)+')')
        # worksheet.write(row, 4, '=SUM(E2:E'+str(row-1)+')')
        workbook.close()
