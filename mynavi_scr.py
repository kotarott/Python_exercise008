import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd
import datetime
from webdriver_manager.chrome import ChromeDriverManager
import threading


class multiThread(threading.Thread):
    def __init__(self, page, keyword):
        threading.Thread.__init__(self)
        self.keyword = keyword
        self.page = page

    def run(self):
        result = get_date_per_page(self.page, self.keyword)
        create_csv(result, "data_page"+str(self.page)+".csv")
        print("finish!")


# Chromeを起動する関数
def set_driver(driver_path, headless_flg):

    if "chrome" in driver_path:
        options = ChromeOptions()
    else:
        options = Options()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    if "chrome" in driver_path:
        return Chrome(ChromeDriverManager().install(), options=options)
    else:
        return Firefox(executable_path=os.getcwd() + "/" + driver_path,options=options)


def get_date_per_page(page, search_keyword):

    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)

    time.sleep(5)
    create_log('ドライバを起動しました。')

    # 空のDataFrame作成
    driver.get("https://tenshoku.mynavi.jp/list/kw" + search_keyword + "/pg" + str(page))
    time.sleep(3)

    try:
        while driver.find_element_by_class_name("karte-close") != "":
            driver.execute_script('document.querySelector(".karte-close").click()')
    except:
        pass

    df = pd.DataFrame()

    # ページ終了まで繰り返し取得
    # 検索結果の一番上の会社名を取得

    
    # 2ページ以降上手く取得できない。

    name_list = driver.find_elements_by_class_name("cassetteRecruit__name")
    applicant_list =driver.find_elements_by_xpath("/html/body/div[1]/div[3]/form/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td")
    income_list = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/form/div/div/div/div[2]/div[1]/table/tbody/tr[5]/td")

    create_log(f'{page+1}ページ内のデータを取得しています。')
    
    # 1ページ分繰り返し
    for count, (name, applicant, income) in enumerate(zip(name_list, applicant_list, income_list)):
        # print(name.text, applicant.text, income.text)
        # DataFrameに対して辞書形式でデータを追加する
        create_log(f'{count}件目のデータを取得しています。')
        df = df.append(
            {"会社名": name.text, 
            "対象": applicant.text,
            "初年度年収": income.text}, 
            ignore_index=True)
    return #df


# 会社名のみを取得する関数
def split_items(items, symbol):
    item_list = {}

    for item in items:
        first_second = item.split(symbol)

        if (len(first_second) >= 2):
            item_list[first_second[0]] = first_second[1]
        else:
            item_list[first_second[0]] = ""

    return item_list


# CSV作成関数
def create_csv(data, file_name="company_list.csv"):
    data.to_csv(file_name)
    # num = 0
    # while num == 0:
    #     if os.path.exists(file_name):
    #         print(f"ファイル名{file_name}は存在します。")
    #         num = 0
    #         file_name = input("ファイル名を入力してください >>>")
    #         file_name += ".csv"
    #     else:
    #         data.to_csv(file_name)
    #         create_log(f'ファイル名:{file_name} を作成しました。')
    #         return print("ファイルを作成しました。")


# ログ作成関数
def create_log(comment):
    path = "log.csv"
    now = datetime.datetime.now()
    time_stamp = now.strftime("%Y/%m/%d %H:%M:%S")
    logs = ','.join([time_stamp, comment])

    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(logs)
    else:
        with open(path, 'a', encoding='utf-8') as f:
            f.write('\n' + logs)
