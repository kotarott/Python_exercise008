import threading
import mynavi


class multiThread(threading.Thread):
    def __init__(self, page, keyword):
        threading.Thread.__init__(self)
        self.keyword = keyword
        self.page = page

    def run(self):
        result = mynavi.get_data(self.page, self.keyword)
        mynavi.create_csv(result, "data_page"+str(self.page)+".csv")
        print("finish!")

