"""
Excelファイルの読み込み、読み込んだExcelファイルの整形を行う
"""

# ライブラリのインポート
import pandas
import re

# 定数を定義
READ_SHEET_INDEX = 0                  # Excelファイルの、読み込むシート番号
KEYWORD_PLAYWRIGHT = "脚本"           # Excelファイルで、脚本家の名前が記載されたカラム名
PATTERN_VALID = "^\d+"                # Excelファイルの、有効な行のパターン
TARGET_COLUMN_DEFAULT_VALUE = -1      # Excelファイルで、取得対象とするカラムのデフォルト値
COLUMN_SEQ = 0                        # Excelファイルの、連番カラム

def loading_excel(path):
    """
    Excelファイルを読み込む

    Args:
        path (string): 読み込むExcelファイルのパス
    Returns:
        object: 読み込んだExcelファイルのデータ(二次元)
        string: 読み込んだExcelファイルのシート名
    Raises:
        OSError: ファイル読み込み失敗時に発生
    """
    try:
        # Excelファイルを読み込み
        # シート名を取得する
        input_file = pandas.ExcelFile(path)
        # 定数で定義したシートを読み込む
        read_sheet_name = input_file.sheet_names[READ_SHEET_INDEX]
        load_data = pandas.read_excel(path, sheet_name=read_sheet_name)
        return load_data, read_sheet_name
    except Exception as e:
        # 呼び出し元に例外をthrow
        raise OSError("ファイル読み込み失敗")


def formatting_excel(load):
    """
    Excelファイルを整形する

    Args:
        load (object): 整形対象のExcelファイル
    Returns:
        list: 整形したExcelデータ(一次元)
    Raises:
        Exception: Excelファイルのフォーマットに誤りがある場合に発生
    """
    try:
        # 脚本家の名前が記載されたカラムを検索する
        target_column = TARGET_COLUMN_DEFAULT_VALUE
        for i, header in enumerate(load.columns):
            # ヘッダーに脚本家の列が存在する場合は、列番号を取得する
            if header == KEYWORD_PLAYWRIGHT:
                target_column = i
                break

        # 脚本家の列が存在しなかった場合はエラーとしてプログラム終了する
        if target_column == TARGET_COLUMN_DEFAULT_VALUE:
            # ファイルのフォーマットに誤りあり
            raise Exception("読み込みファイルのフォーマットに誤りがります")

        list = []
        for row in load.values:
            if re.match(PATTERN_VALID, str(row[COLUMN_SEQ])) != None:
                # セル結合の影響でnanとなっているデータを変換する
                if pandas.isna(row[target_column]):
                    # nanの場合は、前回値を取得する
                    parameter = list[-1]
                else:
                    # nanではない場合は、読み取ったデータを取得する
                    parameter = row[target_column]
                # リストにデータを格納
                list.append(parameter)

        return list
    except Exception as e:
        # 呼び出し元に例外をthrow
        raise
