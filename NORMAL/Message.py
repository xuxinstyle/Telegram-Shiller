import pandas
excel_data = pandas.read_excel('../Recipients data.xlsx', sheet_name='Recipients')

def fetch_text():
    self = excel_data['Message'][0] # Message Here
    return self



def group0():
    channel_list = excel_data['Username'].tolist()#groups for account number 0

    return channel_list


def group1():
    channel_list = excel_data['Username'].tolist()#groups for account number 1

    return channel_list


def group2():
    channel_list = excel_data['Username'].tolist()#groups for account number 2

    return channel_list

# 小迷妹
def fetch_text1():
    self = excel_data['Message'][1] # Message Here
    return self
# def group3():
#     channel_list = ] #groups for account number 3
#
#     return channel_list
#
#
# def group4():
#     channel_list = [] #groups for account number 4
#
#     return channel_list

