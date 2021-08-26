import mynavi
import common

# main処理
def main(loop_count=1, search_keyword="高収入"):

    mynavi.create_log('スクレイピングを開始します。')


    for i in range(loop_count):
        result = common.multiThread(i+1, search_keyword)
        result.start()
    
    mynavi.create_log('処理を終了します。')

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main(3, "リモート")