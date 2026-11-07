# Hasta onay linki önizleme görseli (1200x630) — deploy.sh çağırır
import sys,glob
from PIL import Image,ImageDraw,ImageFont
def font(b,sz):
    for p in glob.glob('/usr/share/fonts/**/DejaVuSans%s.ttf'%('-Bold' if b else ''),recursive=True)+glob.glob('/usr/share/fonts/**/LiberationSans-%s.ttf'%('Bold' if b else 'Regular'),recursive=True):
        return ImageFont.truetype(p,sz)
    return ImageFont.load_default(sz)
W,H=1200,630;im=Image.new('RGB',(W,H));d=ImageDraw.Draw(im)
for y in range(H):
    t=y/H;d.line([(0,y),(W,y)],fill=(int(11+4*t),int(91+31*t),int(96+19*t)))
d.ellipse([820,-200,1400,380],fill=(20,110,108));d.ellipse([-150,420,350,900],fill=(16,100,100))
f1=font(1,64);f2=font(0,34);f3=font(1,29);C=(15,122,115)
x0,y0=90,110;d.rounded_rectangle([x0,y0,x0+150,y0+150],28,fill=(255,255,255))
d.rounded_rectangle([x0+28,y0+38,x0+122,y0+122],10,outline=C,width=8);d.line([x0+28,y0+66,x0+122,y0+66],fill=C,width=8)
d.line([x0+52,y0+26,x0+52,y0+48],fill=C,width=8);d.line([x0+98,y0+26,x0+98,y0+48],fill=C,width=8)
d.line([x0+52,y0+96,x0+68,y0+110,x0+100,y0+80],fill=C,width=9,joint='curve')
d.text((280,118),'Randevunuzu',font=f1,fill='white');d.text((280,192),'yanıtlayın',font=f1,fill='white')
for i,(t,fg) in enumerate([('✓ Geleceğim',C),('Başka bir gün',(30,60,60)),('Gelemeyeceğim',(170,50,40))]):
    x=90+i*350;d.rounded_rectangle([x,340,x+320,436],48,fill='white');tw=d.textlength(t,font=f3);d.text((x+160-tw/2,370),t,font=f3,fill=fg)
d.text((90,500),'Tek dokunuş · giriş gerekmez',font=f2,fill=(220,240,238))
im.save(sys.argv[1] if len(sys.argv)>1 else 'onay.jpg',quality=72,optimize=True,progressive=True)
