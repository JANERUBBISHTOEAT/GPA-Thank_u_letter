from PIL import Image, ImageDraw, ImageFont 
import qrcode
import cv2
from os.path import dirname, join

# Constants
POS_DIREC = "in.png"
FILE_TYPE = ".png"
QRC_DIREC = ".\\qr\\"

def paste_all(post_path, qr_path, out_path, font_path, my_name):
    try:
        print("Loading: " + post_path)
        oriImg = Image.open(post_path)
        # addImg(oriImg)
        print("Loading: " + qr_path)
        qrcImg = Image.open(qr_path)
        qrcImg = qrcImg.resize((350, 350), Image.ANTIALIAS)
        oriImg.paste(qrcImg,(2730,1730))

        draw = ImageDraw.Draw(oriImg)
        print("Loading: " + font_path)
        _font = ImageFont.truetype(font_path,200)

        w, h = _font.getsize(my_name)
        width, height = oriImg.size
        draw.text(((width-w)/2, 1080),  my_name, fill = (51, 166, 138), font = _font)
        # oriImg.show()
        oriImg.save(out_path)

        # oriImg.show()
    except IOError:
        print("can't open the file,check the path again\n")
        newImg = Image.new('RGBA',(320,240),'blue')
        newImg.save(out_path)


def makea_qr(code, name):
    out_path = QRC_DIREC + name + FILE_TYPE
    out_path = join(dirname(__file__), out_path)
    qr = qrcode.QRCode(
        version = None, # Make it as tiny as possible
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=50, # HD 
        border = 3
    )
    try:
        print("Making QRcode for {} with value :{}".format(name,code))
        qr.add_data(code)
        qr.make(fit = True)
        # newImg = qr.make_image()
        newImg = qr.make_image(fill_color = (51, 166, 134),
                            back_color = 'white')
        newImg.save(out_path)
        # newImg.show()


    except:
        print("can't create qr code,check priv\n")
        newImg = Image.new('RGBA',(320,240),'blue')
        newImg.save(out_path)

# for single use
if __name__ == '__main__':
    tmp_code = "这一年辛苦啦！！！超级感谢你的付出~祝未来万事顺意！！"
    tmp_name = "Yuchen Ni"
    makea_qr(tmp_code, tmp_name)
    qr_path  = join(dirname(__file__), QRC_DIREC + tmp_name + FILE_TYPE)
    out_path = join(dirname(__file__) + '\\' + tmp_name + FILE_TYPE)
    post_path= join(dirname(__file__), POS_DIREC)
    font_path= join(dirname(__file__),".\\Fonts\\Montserrat-Bold-3.ttf")
    paste_all(post_path, qr_path, out_path, font_path, tmp_name)