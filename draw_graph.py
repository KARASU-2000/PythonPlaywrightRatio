"""
グラフの描画を行う
"""

# ライブラリのインポート
import matplotlib.pyplot as plt

# 定数を定義
COLUMN_ELEMENT_NAME = 0     # 引数で受け取ったリストの、要素の名前
COLUMN_ELEMENT_RATIO = 1    # 引数で受け取ったリストの、要素の割合
TITLE_BOTTOM_PADDING = 20   # グラフのタイトル下のパディング

def drawing_pie_chart(pie_chart_element, title):
    """
    受け取った引数をもとに、円グラフを描画する(割合は小数点第一位まで表示、描画は上の頂点からスタートする)

    Args:
        pie_chart_element (list): 脚本家毎の担当話数の割合([脚本家, 担当話数の割合])
        title (string): 円グラフに表示するタイトル
    Returns:
        なし
    Raises:
        Exception: 引数のフォーマットに誤りがある場合に発生
    """

    try:
        # 日本語が文字化けしないように、フォントを指定する
        plt.rcParams["font.family"] = "IPAGothic"

        # 要素の割合を昇順でソートする
        pie_chart_element.sort(reverse=False, key=lambda list: list[COLUMN_ELEMENT_RATIO])
        # 円グラフのタイトルを設定する
        plt.title(title, pad=TITLE_BOTTOM_PADDING)
        # 円グラフを描画する(割合は小数点第一位まで表示、描画は上の頂点からスタートする)
        plt.pie([col[COLUMN_ELEMENT_RATIO] for col in pie_chart_element], labels=[
                col[COLUMN_ELEMENT_NAME] for col in pie_chart_element], autopct="%.1f %%", startangle=90)
        # 円グラフを表示する
        plt.show()
    except Exception as e:
        # 呼び出し元に例外をthrow
        raise
