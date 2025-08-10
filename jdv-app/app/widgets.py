from kivy_garden.zbarcam import ZBarCam
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout
from plyer import camera
import os,time
_dialog=None

def alert(title,text):
    global _dialog
    if _dialog: _dialog.dismiss()
    _dialog=MDDialog(title=title,text=text,buttons=[MDFlatButton(text='Fechar',on_release=lambda x:_dialog.dismiss())])
    _dialog.open()
class ScannerLayout(BoxLayout):
    def __init__(self,on_code,**kw):
        super().__init__(orientation='vertical',**kw); self.cam=ZBarCam(); self.add_widget(self.cam); self.on_code=on_code; self.cam.bind(symbols=self._got)
    def _got(self,instance,symbols):
        if symbols:
            code=symbols[0].data.decode('utf-8'); self.on_code(code)
async def open_scanner(kind,on_code):
    global _dialog
    layout=ScannerLayout(on_code=lambda code: (_dialog.dismiss(), on_code(code)))
    _dialog=MDDialog(title=f'Scanner {kind}', type='custom', content_cls=layout); _dialog.open()

def take_photo(prefix='jdv'):
    ts=int(time.time()); fname=f'{prefix}_{ts}.jpg'
    outdir=os.path.join(os.getcwd(),'photos'); os.makedirs(outdir,exist_ok=True)
    path=os.path.join(outdir,fname)
    try:
        camera.take_picture(filename=path,on_complete=lambda *a,**kw: None); return path
    except Exception as e:
        alert('Câmera',f'Falha ao capturar foto: {e}'); return None