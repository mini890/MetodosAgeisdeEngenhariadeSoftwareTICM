from openpyxl import load_workbook

wb = load_workbook(filename='2_XLS_producao_de_residuos_municipios_LIPOR.xlsx', read_only=True)

ws = wb['Folha1']

for row in ws.rows:
    for cell in row:
        print(cell.value)
        print(cell.value, type(cell.value))
