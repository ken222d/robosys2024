#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Kenta ishizeki<a.w.g.d0201@icloud.com>
# SPDX-License-Identifier: BSD-3-Clause

import random

def pachinko_game():
    print("🎰 パチンコゲームへようこそ！ 🎰")
    print("エンターキーを押してスタートしてください（終了するには'q'を入力）。")
    points = 0

    while True:
        user_input = input("▶ スタート: ")
        if user_input.lower() == 'q':
            print(f"ゲーム終了！最終スコア: {points}点")
            break

        print("🎱 ボールが弾かれています...")
        result = random.choices(
            ["ハズレ", "リーチ", "大当たり！", "フィーバー！"],
            weights=[70, 20, 8, 2],  # 出現確率
            k=1
        )[0]

        if result == "ハズレ":
            print("😢 残念！ハズレです！")
        elif result == "リーチ":
            print("😮 リーチ！あと少しで大当たり…！")
        elif result == "大当たり！":
            points += 100
            print("🎉 大当たり！100点獲得！")
        elif result == "フィーバー！":
            points += 500
            print("🔥 フィーバー！500点獲得！")

        print(f"現在のスコア: {points}点")
        print("-" * 30)

# ゲーム開始
pachinko_game()

