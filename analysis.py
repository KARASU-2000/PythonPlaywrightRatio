"""
整形されたデータの集計を行う
"""

# ライブラリのインポート
import collections

def counting_playwright(list_playwright):
    """
    脚本家毎の担当話数をカウントする

    Args:
        list_playwright (list): 各話毎の脚本家一覧
    Returns:
        list: 脚本家毎の担当話数([脚本家, 担当話数])
    Raises:
        Exception: 引数のフォーマットに誤りがある場合に発生
    """

    try:
        # 重複した要素を削除する
        distinct_list = set(list_playwright)

        list = []
        for row in distinct_list:
            # 要素ごとの出現回数をカウントして、リストに格納する
            list.append([row, list_playwright.count(row)])

        return list
    except Exception as e:
        # 呼び出し元に例外をthrow
        raise
