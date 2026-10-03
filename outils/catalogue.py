# -*- coding: utf-8 -*-
# catalogue.html : le catalogue PDF tel quel, en page web. Ordinateur : les pages A4 de presentation.pdf.
# Telephone : la mise en page de presentation_telephone.pdf. Le HTML et le CSS viennent de pdf.py, rien n'est redessine ici.
import os, re, subprocess, sys
from PIL import Image
O=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(O)+'/'
subprocess.run([sys.executable,O+'/pdf.py'],check=True,capture_output=True)            # ecrit le HTML des pages A4
h=open(os.environ.get('TMPDIR','/tmp')+'/gargantua_pdf.html').read().replace('file://'+S,'')
tel=re.search(r"if TEL: css\+='''(.*?)'''",open(O+'/pdf.py').read(),re.S).group(1)   # le CSS du PDF telephone
os.makedirs(S+'images/catalogue',exist_ok=True)
def web(m):   # chaque image du PDF, a la taille du web, dans images/catalogue
    src=m.group(1)
    if not src.startswith('images/') or src.startswith('images/portraits') or src.startswith('images/affiche'): return m.group(0)
    n='images/catalogue/'+os.path.splitext(os.path.basename(src))[0]+('.png' if src.endswith('.png') else '.jpg')
    im=Image.open(S+src); im.thumbnail((2000,2000),Image.LANCZOS)
    im.save(S+n) if n.endswith('.png') else im.convert('RGB').save(S+n,quality=88,optimize=True,progressive=True)
    return 'src="%s"'%n
h=re.sub(r'src="([^"]+)"',web,h)
HEAD='''<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Gargantua · Catalogue</title>
<meta name="description" content="Catalogue de l'exposition Gargantua, Parcours Bijoux Paris 2026.">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png"><link rel="icon" type="image/png" sizes="512x512" href="favicon-512.png"><link rel="apple-touch-icon" href="favicon-180.png">
<style>
.dl{display:block;text-align:center;font-size:8pt;letter-spacing:.16em;text-transform:uppercase;color:#757575;text-decoration:none;padding:6mm 0 10mm}
@media screen and (min-width:701px){body{background:#d9d9d9}.p{margin:8mm auto;background:#fff;box-shadow:0 1px 6px rgba(0,0,0,.2)}}
@media screen and (max-width:700px){
%s
body{padding:24px 20px}
.p{min-height:0;margin:0 0 12mm;padding:0 0 12mm;border-bottom:1px solid #e3e3e3}
.p:first-child{min-height:86vh;display:flex;flex-direction:column}
.affiche{height:auto}.affiche img{width:100%%}
.oe .im,.oe .im.haut{height:auto;margin:0}.oe .ph{width:100%%}.oe img{width:100%%;max-height:none}
}
</style></head>'''%tel
JS='''<a class="dl" href="catalogue.pdf">Télécharger le catalogue en PDF</a>
<script>
/* ordinateur : les pages A4 tiennent dans la largeur ; telephone : l'image prend la largeur de l'ecran, sans l'agrandissement ni le decalage choisis pour l'A4 */
const ph=[...document.querySelectorAll('.ph')],A4=ph.map(d=>d.querySelector('img').style.transform);
function cale(){const t=innerWidth<=700,z=t?1:Math.min(1,(innerWidth-40)/(210*96/25.4));
 document.querySelectorAll('.p').forEach(p=>p.style.zoom=z);
 ph.forEach((d,i)=>d.querySelector('img').style.transform=t?'none':A4[i])}
cale();addEventListener('resize',cale);
</script></body>'''
h=h.replace('</head>',HEAD,1).replace('</body>',JS,1)
open(S+'catalogue.html','w').write(h); print('catalogue.html',len(h),'octets,',h.count('class="p"'),'pages')
