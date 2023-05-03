
class account_config:
    def __init__(self):
        self.m_tg_config = tg_config()



class tg_config():

    def __init__(self):
        self.channel_list = []
        self.config_list = {}
        self.max_index = 0
        self.reload()
        self.channelslist()


    def reload(self):
        f = open("./config/config.txt", 'r', encoding='UTF-8')  # 返回一个文件对象
        strlist = f.readlines()
        index = 0
        for str in strlist:
            cofigs_str = str.split(";")
            self.config_list[index] = cofigs_str  # 调用文件的 readline()方法
            index = index + 1

        self.max_index = index
        f.close()

    def period_time(self, id):
        return int(self.config_list[id][2])

    def telegram_path(self, id):
        return str(self.config_list[id][0])

    def advertising_message(self, id):
        return str(self.config_list[id][1])

    def get_owner(self, id):
        return str(self.config_list[id][3])

    def get_t_id(self, id):
        return str(self.config_list[id][4])

    def get_t_hash(self, id):
        return str(self.config_list[id][5])

    def channelslist(self):
        f = open("./config/channel.txt", 'r', encoding='UTF-8')  # 返回一个文件对象
        self.channel_list = f.readlines()  # 调用文件的 readline()方法
        f.close()
        return self.channel_list


