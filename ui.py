from tkinter import *
from tkinter import filedialog
import qrcode
import qrcode.image.svg
import tempfile
import zipfile

class Win:
    def __init__(self):
        self.links = {}
        self.svg_files = []
        self.window = Tk()
        self.openBtn = Button(text='Open File', command=self.open_file)
        self.saveBtn = Button(text='Save Codes', command=self.save_qr)
        self.openBtn.pack()
        self.saveBtn.pack()

    def start(self):
        self.window.mainloop()

    def open_file(self):
        path = filedialog.askopenfilename()
        file = open(path, 'r')
        file_lines = file.read().split('\n')

        for i in file_lines:
            line_data = i.split('\t')
            if len(line_data) > 1:
                if not self.links.get(line_data[1], False):
                    self.links[line_data[1]] = []
                self.links[line_data[1]].append(line_data[0])
            else:
                if not self.links.get('Phygit', False):
                    self.links['Phygit'] = []
                self.links['Phygit'].append(line_data[0])
        print(self.links)

    def save_qr(self):

        for i in self.links:
            for j, z in enumerate(self.links[i]):
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    image_factory=qrcode.image.svg.SvgPathImage,
                    box_size=20,
                    border=2,
                )

                qr.add_data(z)
                qr.make(fit=True)
                img = qr.make_image(fill_color='black', back_color='white', embeded_image_path='./')
                filename = i.replace(' ', '-').lower() + '-' + str(j + 1) + '.svg'
                file = open(filename, 'w')
                file.write(img.to_string(encoding='unicode'))
                file.flush()
                file.close()



