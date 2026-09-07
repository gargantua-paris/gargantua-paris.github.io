from PIL import Image
import numpy as np, scipy.ndimage as nd, json, os, unicodedata, re

S='/Users/hamouda/Desktop/project amira parcour/SITE_GARGANTUA/'
D='/Users/hamouda/Desktop/'; F=D+'FAUST CARDINALI/'; W='/Users/hamouda/Downloads/'

OEUVRES = [
 ('thierry-vendome','LE PASSAGE','Corolle de rouille, saphir rose (3,66 ct), saphirs roses, or jaune plissé.',D+'JPEG image.jpeg'),
 ('faust-cardinali','LE BAPTÊME DE PANTAGRUEL','Pendentif. Gargantua 2026.',F+'FAUST CARDINALI_ LE BAPTÊME DE PANTAGRUEL_-3.jpg'),
 ('faust-cardinali','AMBIGUA NASCENTIA','Pendentif-collier. Gargantua 2026.',F+'FAUST CARDINALI_ AMBIGUA NASCENTIA -1.jpg'),
 ('faust-cardinali','GARGANTUA','Bague. Fonte d’aluminium, creuset en argent, polyester.',F+'FAUST CARDINALI_ GARGANTUA_BAGUE.jpg'),
 ('faust-cardinali','BAT-STARTER II','Bracelet, outil et dispositif de performance.',F+'GARGANTUA_ FAUST CARDINALI_BAT-STARTER II (GARGANTUA)_6.jpg'),
 ('faust-cardinali','MARTA','Sculpture-pinceau accompagnant Bat-Starter II.',F+'GARGANTUA_ FAUST CARDINALI_MARTA_7.jpg'),
 ('amira-sliman','MOURIR POUR VIVRE','Broche. Os, or jaune, argent.',W+'Gargantua Broche Amira Sliman.jpg'),
 ('amira-sliman','AINSI VINT-IL AU MONDE','Boucles. Argent, aluminium, galalithe.',W+'Gargantua Boucles Amira Sliman.png'),
 ('amira-sliman','YOUNG COUPLES','Bague. Ébène, argent, quartz à rutiles.',W+'Gargantua Young Couples Amira Sliman.jpg'),
 ('amira-sliman','THÉLÈME','Collier. Ébène, or jaune, argent.',W+'Gargantua Collier Amira Sliman.png'),
 ('agnes-dubois','CORNUCOPIA','Bracelet et boucles d’oreilles. Argent et perles d’eau douce. 2026.',D+'Gargantua Agnes Dubois Cornucopia (1).JPG'),
 ('agnes-dubois','CORNUCOPIA','Bracelet. Argent. 2026.',D+'Agnes Dubois Cornucopia Bracelet.JPG'),
 ('agnes-dubois','SILÈNES','Collier. Laiton patiné et corne. 2026.',D+'Agnes Dubois Silenes Collier (1).JPG'),
 ('agnes-dubois','SILÈNES','Collier. Laiton patiné et corne. 2026.',D+'Agnes Dubois Silenes Collier (2).JPG'),
]

SANS_RECADRAGE = {'faust-cardinali'}      # image entiere, telle quelle

def slug(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode()
    return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')

def bgcolor(a):
    h,w,_=a.shape; b=max(6,min(h,w)//60)
    ring=np.concatenate([a[:b].reshape(-1,3),a[-b:].reshape(-1,3),a[:,:b].reshape(-1,3),a[:,-b:].reshape(-1,3)])
    return np.median(ring,0)

def piece_box(a,bg):
    g=a.mean(2); sat=a.max(2)-a.min(2)
    m=(g<bg.mean()-9)|(sat>45)
    m=nd.binary_opening(m,np.ones((3,3)))
    m=nd.binary_closing(m,np.ones((9,9)))
    lab,n=nd.label(m)
    if n==0: return None
    sz=nd.sum(m,lab,range(1,n+1)); keep=np.where(sz>sz.max()*0.02)[0]+1
    mm=np.isin(lab,keep)
    ys,xs=np.where(mm)
    return ys.min(),ys.max(),xs.min(),xs.max()

man=[]
counts={}
for artist,title,mat,src in OEUVRES:
    full=Image.open(src).convert('RGB')
    small=full.copy(); small.thumbnail((1600,1600), Image.LANCZOS)
    k=full.width/small.width                      # facteur de retour vers la pleine def
    a=np.array(small).astype(int)
    box=None if artist in SANS_RECADRAGE else piece_box(a,bgcolor(a))
    im=full
    if box:
        y0,y1,x0,x1=box
        mh=int((y1-y0)*0.09)+12; mw=int((x1-x0)*0.09)+12
        y0=max(0,y0-mh); y1=min(a.shape[0],y1+mh); x0=max(0,x0-mw); x1=min(a.shape[1],x1+mw)
        im=full.crop((int(x0*k),int(y0*k),int(round(x1*k)),int(round(y1*k))))
    im.thumbnail((2400,2400), Image.LANCZOS)
    bg=bgcolor(np.array(im).astype(int))          # fond mesure APRES recadrage
    counts[artist]=counts.get(artist,0)+1
    name='%s_%02d_%s.jpg'%(artist,counts[artist],slug(title))
    im.save(S+'images/oeuvres/'+name,'JPEG',quality=90,optimize=True,progressive=True)
    man.append(dict(artist=artist,titre=title,matiere=mat,src=src.replace('/Users/hamouda/','~/'),
                    file='images/oeuvres/'+name,w=im.width,h=im.height,
                    bg='#%02x%02x%02x'%tuple(np.round(bg).astype(int))))
    print('%-16s %-26s %4dx%-4d bg %s' % (artist,title[:26],im.width,im.height,man[-1]['bg']))

# portraits
POR=[('thierry-vendome',D+'Crédit photo Olivier Foulon.jpg'),('faust-cardinali',D+'download.jpg'),
     ('amira-sliman',D+'DXC.jpg'),('agnes-dubois',D+'agnes-dubois-bijoux.webp')]
port={}
for k,p in POR:
    im=Image.open(p).convert('RGB'); im.thumbnail((1100,1100),Image.LANCZOS)
    n='images/portraits/%s.jpg'%k
    im.save(S+n,'JPEG',quality=90,optimize=True,progressive=True)
    port[k]=dict(file=n,w=im.width,h=im.height)
    print('portrait %-16s %dx%d'%(k,im.width,im.height))
json.dump(dict(oeuvres=man,portraits=port),open(S+'images/manifest.json','w'),ensure_ascii=False,indent=1)
