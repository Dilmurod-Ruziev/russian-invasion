import pandas as pd
# Importing csv and excel materials
xls = pd.ExcelFile('Datasets/Countries.xlsx')
countries_and_coalitions = pd.DataFrame(pd.read_excel(xls, "Countries and Coalitions"))
comtrade = pd.DataFrame(pd.read_csv("Datasets/comtrade.csv"))
# Formatting of float numbers
pd.options.display.float_format = '{:.2f}'.format

# IMPORT shares
world_import = comtrade[(comtrade['Trade Flow'] == 'Import') & (comtrade['Partner'] == 'World')].reset_index().set_index('Reporter')
russian_import = comtrade[(comtrade['Trade Flow'] == 'Import') & (comtrade['Partner'] == 'Russian Federation')].reset_index().set_index('Reporter')
ukrainian_import = comtrade[(comtrade['Trade Flow'] == 'Import') & (comtrade['Partner'] == 'Ukraine')].reset_index().set_index('Reporter')
# EXPORT shares
world_export = comtrade[(comtrade['Trade Flow'] == 'Export') & (comtrade['Partner'] == 'World')].reset_index().set_index('Reporter')
russian_export = comtrade[(comtrade['Trade Flow'] == 'Export') & (comtrade['Partner'] == 'Russian Federation')].reset_index().set_index('Reporter')
ukrainian_export = comtrade[(comtrade['Trade Flow'] == 'Export') & (comtrade['Partner'] == 'Ukraine')].reset_index().set_index('Reporter')

# New trade DataFrame and sorting
trade = pd.DataFrame({
    'Reporter': russian_import['Trade Value (US$)'].div(world_import['Trade Value (US$)']).mul(100).index,
    'Import Rus %': round(russian_import['Trade Value (US$)'].div(world_import['Trade Value (US$)']).mul(100).fillna(0), 2),
    'Export Rus %': round(russian_export['Trade Value (US$)'].div(world_export['Trade Value (US$)']).mul(100).fillna(0), 2),
    'Import Ukr %': round(ukrainian_import['Trade Value (US$)'].div(world_import['Trade Value (US$)']).mul(100).fillna(0), 2),
    'Export Ukr %': round(ukrainian_export['Trade Value (US$)'].div(world_export['Trade Value (US$)']).mul(100).fillna(0), 2)
})

# Cleaned version of countries and their political coalitions
countries = countries_and_coalitions[['Countries', 'Status', 'In Nato ', 'In Shanghai Cooperation Organisation', 'In CSTO']]







