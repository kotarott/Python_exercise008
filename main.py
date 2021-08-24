import mynavi_scr
import time

# main処理
def main(loop_count=1, search_keyword="高収入"):

    mynavi_scr.create_log('スクレイピングを開始します。')

    # result1 = mynavi_scr.multiThread(1, search_keyword)
    # result1.start()
    # time.sleep(2)
    result2 = mynavi_scr.multiThread(2, search_keyword)
    result2.start()

    # for i in range(loop_count):
    #     result = mynavi_scr.multiThread(i+1, search_keyword)
    #     result.start()
    
    mynavi_scr.create_log('処理を終了します。')

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main(1, "リモート")