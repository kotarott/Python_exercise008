# Python_exercise008
並列処理  
マイナビ転職のページから、求人タイトル、求人対象者、初年度年収を取得する。  
ページごとに並列処理が行われ、ページごとにCSVファイルが生成される。  
  

## インストール
pip install selenium  
pip install pandas  
pip install ChromeDriverManager  
pip install threading  
  

## main.py
main(loop_cunt=取得したいページ数, search_keyword=検索キーワード)  
⇒マルチスレッドでページごとにデータを取得する。  
  