"""
整形されたデータの集計を行う
"""

# ライブラリのインポート
import collections
import self_exception
from decimal import Decimal, ROUND_HALF_UP

# 定数を定義
COLUMN_PLAYWRIGHT = 0       # 整形したlistのカラム番号(脚本家)
COLUMN_STORY_NUMBER = 1     # 整形したlistのカラム番号(担当話数)
COLUMN_REP_RATIO = 1        # 分析したlistのカラム番号(担当話数の割合)

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

def calculating_playwright_ratio(list_playwright):
    """
    脚本家毎の担当話数の割合を出す

    Args:
        list_playwright (list): 各話毎の脚本家一覧
    Returns:
        list: 脚本家毎の担当話数の割合([脚本家, 担当話数の割合])
    Raises:
        Exception: 引数のフォーマットに誤りがある場合に発生
    """
    try:
        # トータル話数を取得する
        total_story_number = len(list_playwright)
        # 脚本家毎の担当話数を取得する
        list_temp = counting_playwright(list_playwright)

        list = []
        for row in list_temp:
            # (担当話数 / トータル話数) * 100で割合を算出する
            ratio = (row[COLUMN_STORY_NUMBER] / total_story_number) * 100
            # 結果を四捨五入する
            ratio = Decimal(ratio).quantize(Decimal('0.01'), ROUND_HALF_UP)
            # リストに格納する
            list.append([row[COLUMN_PLAYWRIGHT], ratio])

        return list
    except Exception as e:
        # 呼び出し元に例外をthrow
        raise

def calculating_main_ratio(list_playwright, main_playwright):
    """
    メイン脚本の担当話数の割合を出す

    Args:
        list_playwright (list): 各話毎の脚本家一覧
        main_playwright: メイン脚本家名
    Returns:
        float: メイン脚本の割合
    Raises:
        Exception: 引数のフォーマットに誤りがある場合に発生
        InvalidInput: 引数のメイン脚本家名が、各話毎の脚本家一覧に存在しない場合に発生
    """
    try:
        # 脚本家毎の担当話数の割合を取得する
        list = calculating_playwright_ratio(list_playwright)

        ret_ratio = 0
        for row in list:
            # 引数で受け取ったメイン脚本家名と一致する場合、戻り値に割合を格納
            if row[COLUMN_PLAYWRIGHT] == main_playwright:
                ret_ratio = row[COLUMN_REP_RATIO]

        # 引数が0のままの場合、入力値エラーとする
        if ret_ratio == 0:
            raise self_exception.InvalidInput
        else:
            # 呼び出し元に結果を返却
            return ret_ratio
    except Exception as e:
        # 呼び出し元に例外をthrow
        raise
