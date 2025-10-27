import json

with open("json_files/text.json", "r", encoding="utf-8") as f:
    texts = json.load(f)

WELCOME_TEXT = texts["welcome"]
MENU_TEXT = texts["commands"]
ADMIN_ID = texts["admin_id"]