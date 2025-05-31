# Đọc file bin
with open("CARD_Desc_E.bin", "rb") as f:
    data = f.read()

# Giải mã từ UTF-16LE rồi lưu ra file txt (UTF-8 cho dễ đọc)
with open("CARD_Desc_E.txt", "w", encoding="utf-8") as f:
    f.write(data.decode("utf-16le"))
