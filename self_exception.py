"""
自作の例外クラス
"""

class InvalidInput(Exception):
    """
    無効な入力値を受け取った時に発生させる例外
    """
    def __init__(self):
        pass

    def __str__(self):
        return "無効な入力値です"
