# ライブラリ
import scratchattach as scratch3
import os

project_id = "プロジェクトのID"

# ログインや接続
session = scratch3.login(os.environ["user"], os.environ["pass"])
conn = session.connect_cloud(project_id)
events = scratch3.CloudEvents(project_id)


# クラウド変数が変更されたときの処理
@events.event
def on_set(event):
    pass


# 処理開始
events.start()
