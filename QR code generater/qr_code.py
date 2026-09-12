import qrcode as qr

from PIL import Image

qr = qr.QRCode(version=1,
                    error_correction=qr.constants.ERROR_CORRECT_H,
                    box_size=10,
                    border=4)

qr.add_data("https://youtu.be/xPQn1_WtnMU?si=AEw3Jytt_iUYBbBc")
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="pink")
img.save("hanuman.png")