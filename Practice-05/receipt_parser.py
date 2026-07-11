import re
import json


with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()


prices = re.findall(r"\n([\d\s]+,\d{2})\nСтоимость", text)

prices = [price.replace(" ", "").replace(",", ".") for price in prices]


products = re.findall(r"\d+\.\n(.+)", text)


total = re.search(r"ИТОГО:\s*\n([\d\s]+,\d{2})", text)

if total:
    total_amount = total.group(1).replace(" ", "").replace(",", ".")
else:
    total_amount = "0"


date_time = re.search(r"Время:\s*(.+)", text)

if date_time:
    receipt_time = date_time.group(1)
else:
    receipt_time = ""


payment = re.search(r"(Банковская карта:)", text)

if payment:
    payment_method = payment.group(1)
else:
    payment_method = ""


receipt = {
    "products": products,
    "prices": prices,
    "total": total_amount,
    "date_time": receipt_time,
    "payment": payment_method
}


print(json.dumps(receipt, indent=4, ensure_ascii=False))