"""
メインプログラム
"""

# モジュールのインポート
import operation_excel

try:
    # ファイルパスを取得する
    path = input("読み込むファイルのパスを入力：")
    # Excelファイルを読み込んで、整形結果を出力する
    result = operation_excel.formatting_excel(operation_excel.loading_excel(path))
    print(result)
except Exception as e:
    # エラーを表示する
    print(e)
