import qrcode
import qrcode.image.svg


def make_svg(prefix, urls):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        image_factory=qrcode.image.svg.SvgPathImage,
        box_size=20,
        border=2,
    )

    for i, j in enumerate(urls):
        qr.add_data(j)
        qr.make(fit=True, size_ratio=1)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(prefix + str(i) + '.svg')
