import qrcode 

def generate_qr(
    address,
    amount
):
    data = f"{address}:{amount}"

    img = qrcode.make(data)

    filename = f"qr_{address[-5:]}.png"

    img.save(filename)

    return filename