# ライブラリ
import scratchattach as scratch3
import os
import json
from dotenv import load_dotenv

load_dotenv()
data: dict = {}

project_id: str = "891115344"

# ログインや接続
session = scratch3.login(os.environ["user"], os.environ["pass"])
conn = session.connect_cloud(project_id)
events = scratch3.CloudEvents(project_id)


# クラウド変数が変更されたときの処理
@events.event
def on_set(event) -> None:
    if event.var == "POST":
        print(f"User: {event.user}, Value: {event.value}")
        value: str = event.value
        user: str = event.user
        post_id: str = value[5:]

        print(value[0], value[1:5], post_id)
        if value[0] == "1":
            if value[1:5] == "0000":
                if not user in data:
                    data[user] = {"dark": False, "page": 1}
                    with open("./dat.json", "w") as f:
                        f.write(json.dumps(data, indent=4))

                conn.set_var(
                    "GET",
                    f"{int(data[user]['dark'])}{str(data[user]['page']).zfill(2)}{post_id}",
                )
    else:
        return


# JSON読み込み
data_file = open("./dat.json", "r")
data = json.loads(data_file.read())
data_file.close()

# 処理開始
print("================================================================")
print("Server is started!")
print("================================================================")
events.start()
