# Đọc file txt (UTF-8)
with open("CARD_Desc_E.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Mã hóa sang UTF-16LE rồi lưu lại file bin
with open("CARD_Desc_E.bin", "wb") as f:
    f.write(text.encode("utf-16le"))
