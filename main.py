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
    result = operation_excel.formatting_excel(operation_excel.loading_excel(path))
    # 脚本家毎の担当話数を表示する
    print(analysis.counting_playwright(result))
except Exception as e:
    # エラーを表示する
    print(e)
