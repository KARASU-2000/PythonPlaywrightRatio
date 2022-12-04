"""
メインプログラム
"""

# モジュールのインポート
import operation_excel
import analysis
import draw_graph

try:
    # ファイルパスを取得する
    path = input("読み込むファイルのパスを入力：")
    # Excelファイルを読み込んで整形する
    load_data, read_sheet_name = operation_excel.loading_excel(path)
    format_data = operation_excel.formatting_excel(load_data)
    # 脚本家の割合を円グラフで表示する
    draw_graph.drawing_pie_chart(analysis.calculating_playwright_ratio(format_data), read_sheet_name)
except Exception as e:
    # エラーを表示する
    print(e)
