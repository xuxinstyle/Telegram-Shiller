import pandas
excel_data = pandas.read_excel('./config/Recipients data.xlsx', sheet_name='Recipients')


f = open("./config/Message.txt", 'r', encoding='UTF-8') # 返回一个文件对象
Message = f.readlines() # 调用文件的 readline()方法
f.close()

def fetch_text():
    self = excel_data['Message'][0] # Message Here
    return self
# 小迷妹
def fetch_text1():
    return str(Message[1])

# 翻身
def fetch_text2():
    self = excel_data['Message'][2] # Message Here
    return self

def period_time():
    return int(Message[2])

def telegram_path():
    return str(Message[0])

def group0():
    channel_list = excel_data['Username'].tolist()#groups for account number 0

    return channel_list


def group1():
    channel_list = excel_data['Username'].tolist()#groups for account number 1

    return channel_list


def group2():
    channel_list = excel_data['Username'].tolist()#groups for account number 2

    return channel_list




def group3():
    channel_list = excel_data['Username'].tolist()#groups for account number 2

    return channel_list
#
#
# def group4():
#     channel_list = [] #groups for account number 4
#
#     return channel_list

