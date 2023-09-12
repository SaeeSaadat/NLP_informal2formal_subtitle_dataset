import openpyxl


def read_from_xlsx(file_name: str, just_first_col: bool = False):
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active

    values = []
    for row in sheet.iter_rows():
        if just_first_col:
            values.append(row[0].value)
        else:
            values.append(tuple(r.value for r in row))

    return values

