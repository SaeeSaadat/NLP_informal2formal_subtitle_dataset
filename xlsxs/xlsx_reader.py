import openpyxl


def read_from_xlsx(file_name: str):
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active

    values = []
    for row in sheet.iter_rows():
        values.append(row[0].value)

    return values

