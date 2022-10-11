
import pandas
excel_data = pandas.read_excel('../Recipients data.xlsx', sheet_name='Recipients')

def fetch_text():
    self = excel_data['Message'][0]  # Your Message here
    return self


def fetch_list():
    channel_list = excel_data['Username'].tolist() #Channel list here
    return channel_list

