import requests
import json

# توکن ربات بله (جایگزین کن)
BOT_TOKEN = "2071296181:C1ouATv8fb7OjzcR5y8aqlwtEnxlkPrMFCtNzqGz"

# لیست شناسه‌های کاربران
user_ids = [
    14837678, 16731210, 22324372, 49282306, 98586051,
    160855369, 163711382, 245382349, 278276479, 288644072,
    319311841, 320366232, 338088424, 352254762, 360977394,
    401141175, 556435059, 613370762, 657257668, 661277673,
    664306808, 690678264, 742940608, 839565474, 884283806,
    1021023729, 1059424559, 1099962144, 1151388082, 1177842404,
    1215073085, 1276115100, 1346877390, 1358102534, 1413663550,
    1419208550, 1461093641, 1498701998, 1504517814, 1563366543,
    1578464393, 1614542423, 1617936784, 1636054993, 1636512043,
    1643353202, 1699419914, 1705262589, 1717122983, 1750020609,
    1811594152, 1867756189, 1873714943, 2076796435, 2089656296,
    2121802962, 2135023769, 2143480267
]

# متن پیام
message_text = """دنبال هوش مصنوعی رایگان و بدون محدودیت هستی 🥳\nاگه دنبال ابزار های پرکاربرد و کارآمد هستید🥳\nاگه دنبال یک بازوی همه کاره هستی \nبازوی صرات مخصوص خودت همین الان استارت کن🌷 
# دکمه‌های شیشه‌ای
keyboard = {
    "inline_keyboard": [
        [{"text": "بازوی صراط", "url": "https://ble.ir/seratbot"}]
    ]
}

# آدرس API بله
API_URL = f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendMessage"

# ارسال پیام به تمام کاربران
for user_id in user_ids:
    payload = {
        "chat_id": user_id,
        "text": message_text,
        "reply_markup": keyboard
    }
    
    response = requests.post(API_URL, json=payload)
    
    if response.status_code == 200:
        print(f"پیام با موفقیت به {user_id} ارسال شد.")
    else:
        print(f"خطا در ارسال پیام به {user_id}: {response.text}")
