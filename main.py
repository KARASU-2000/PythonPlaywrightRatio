"""
メインプログラム
"""

# モジュールのインポート
import operation_excel
import analysis

try:
    # ファイルパスを取得する
    path = input("読み込むファイルのパスを入力：")
    # Excelファイルを読み込んで整形する
    excel = operation_excel.formatting_excel(operation_excel.loading_excel(path))

    # 脚本家一覧を表示する
    list = analysis.calculating_playwright_ratio(excel)
    print("脚本家一覧")
    for row in list:
        print("　" + row[analysis.COLUMN_PLAYWRIGHT])

    # メイン脚本家の割合を表示する
    playwright = input("メイン脚本家名を入力：")
    print(str(analysis.calculating_main_ratio(excel, playwright)) + "%")
except Exception as e:
    # エラーを表示する
    print(e)
