# -*- coding: utf-8 -*-
# catalogue.html : le catalogue en page web (telephone et ordinateur), memes textes, memes pieces et memes images que presentation.pdf.
import os, sys, json
sys.argv.append('--pres')            # gen n'ecrit pas index.html
sys.path.insert(0, os.path.dirname(__file__))
import gen
from gen import ARTISTES, PROJET, po, FOCAL, typo, S, HEAD, BODY, SCRIPT, JSONLD, nav, fil, noms, FL, PORTRAIT_HD
from pieces import PIECES, TEXTE_GENERAL
from PIL import Image
import numpy as np

os.makedirs(S+'images/catalogue',exist_ok=True)
def image(a,i,o):   # l'image telle que le PDF la montre (fond blanchi / recadree), a la taille du web
    b=os.path.basename(o['img']); src=next(p for p in (S+'images/crop/'+b if a['k']=='thierry-vendome' else '',S+'images/crop/blanc_'+b,S+o['img']) if p and os.path.exists(p))
    im=Image.open(src).convert('RGB'); plein=im.copy(); plein.thumbnail((2400,2400),Image.LANCZOS); im.thumbnail((1400,1400),Image.LANCZOS)
    n='images/catalogue/%s_%02d'%(a['k'],i+1); plein.save(S+n+'.jpg',quality=88,optimize=True,progressive=True); im.save(S+n+'_m.jpg',quality=85,optimize=True,progressive=True)
    bg='#%02x%02x%02x'%tuple(int(v) for v in np.median(np.asarray(im)[:8,:8].reshape(-1,3),0))
    return n+'_m.jpg',n+'.jpg',im.width,im.height,bg

secs=[]
for a in ARTISTES:
    p=po[a['k']]; liste=PIECES[a['k']]
    bio=''.join('<p>%s</p>'%b for b in a['bio'])
    pcred='<figcaption><p class="credit">%s</p></figcaption>'%a['credit_portrait'] if a['credit_portrait'] else ''
    note='<p class="credit" style="margin-top:16px">%s</p>'%a['note'] if a.get('note') else ''
    srcset='%s %dw'%(p['file'],p['w'])
    if a['k'] in PORTRAIT_HD: srcset+=', %s %dw'%PORTRAIT_HD[a['k']]
    gen_t=''
    if a['k'] in TEXTE_GENERAL:
        t,ps=TEXTE_GENERAL[a['k']]
        gen_t='<div class="split"><div><span class="lbl">%s</span></div><div class="prose">%s</div></div>'%(t,''.join('<p>%s</p>'%x for x in ps))
    oe=[]
    for i,o in enumerate(liste):
        m,plein,w,h,bg=image(a,i,o)
        mat='%s. %s'%(o['type'],o['mat'])
        oe.append('''
 <div class="oeuvre">
  <figure class="piece__im" role="button" tabindex="0" aria-label="Voir {t} en grand"
          data-full="{plein}" data-bg="{bg}" data-titre="{t}" data-mat="{mat}" data-cred="{cred}" data-nom="{nom}">
   <img src="{m}" width="{w}" height="{h}" alt="{t}, {nom}" loading="lazy" decoding="async">
  </figure>
  <div class="oeuvre__t"><span class="lbl">Pièce {i:02d} / {n:02d}</span><h3>{t}</h3><p class="mat">{mat}</p>
   <div class="prose">{desc}</div>{ocred}</div>
 </div>'''.format(t=o['titre'],plein=plein,bg=bg,mat=mat,cred=a['credit_oeuvres'],nom=a['nom'],m=m,w=w,h=h,i=i+1,n=len(liste),
            desc=''.join('<p>%s</p>'%x for x in o['desc']),ocred='<p class="credit">%s</p>'%a['credit_oeuvres'] if a['credit_oeuvres'] else ''))
    secs.append('''
<section class="artiste" id="{k}">
 <div class="artiste__h"><h2>{nom}</h2><span>{n} / 04</span></div>
 <div class="split cr">
  <div><figure class="pf"><img src="{pfile}" srcset="{srcset}" style="--fp:{fp}" sizes="(max-width:620px) calc(100vw - 40px), 230px" width="{pw}" height="{ph}" alt="Portrait de {nom}" loading="lazy" decoding="async">{pcred}</figure></div>
  <div class="prose">{bio}{note}</div>
 </div>{gen_t}{oe}
</section>'''.format(k=a['k'],nom=a['nom'],n=a['n'],pfile=p['file'],srcset=srcset,fp=FOCAL[a['k']],pw=p['w'],ph=p['h'],pcred=pcred,bio=bio,note=note,gen_t=gen_t,oe=''.join(oe)))

CSS='''<style>
.oeuvre{display:grid;grid-template-columns:minmax(0,1fr);gap:22px;margin-top:clamp(56px,9vh,120px);padding-top:clamp(28px,4vh,48px);border-top:1px solid var(--line)}
.oeuvre .piece__im{align-items:center}.oeuvre .piece__im img{max-height:72vh}
.oeuvre__t h3{font-weight:700;font-size:clamp(14px,1.1vw,16px);letter-spacing:.03em;text-transform:uppercase;margin-top:10px}
.oeuvre__t .mat{margin-top:4px;color:var(--soft);font-size:clamp(13px,1vw,15px)}
.oeuvre__t .prose{margin-top:18px}.oeuvre__t .credit{margin-top:14px}
.pdf{display:inline-block;margin-top:clamp(26px,4vh,52px)}
@media(min-width:900px){.oeuvre{grid-template-columns:minmax(0,6fr) minmax(0,5fr);gap:clamp(32px,5vw,96px);align-items:center}}
</style>
</head>'''
MAIN='''
<main>

<section class="hero pres" id="top">
 <img class="logo" src="favicon-512.png" width="512" height="512" alt="G." decoding="async">
 <p class="hero__k lbl">Parcours Bijoux Paris 2026 · Catalogue</p>
 <h1>Gargantua.</h1>
 <div class="hero__sub">
  <em>Projet initié par Amira Sliman</em>
 </div>
 <p class="noms">{noms}</p>
 <a class="k pdf" href="catalogue.pdf">Télécharger le catalogue en PDF {fl}</a>

 <div class="meta">
  <div><span class="lbl">Dates</span><p>05 au 17 octobre 2026</p></div>
  <div><span class="lbl">Lieu</span><p>Galerie Psyché Paris<br>18 rue du Pont Louis Philippe<br>75004 Paris</p></div>
  <div><span class="lbl">Vernissage</span><p>08 octobre à 18h</p></div>
  <div><span class="lbl">Rencontre autour de Gargantua</span><p>08 octobre à 14h<br>Le Peloton Studio, 13 rue du Pont Louis-Philippe<br>Présentée par Bruno Laubin</p></div>
 </div>
</section>

<section>
 <div class="split">
  <div><span class="lbl">Le projet</span></div>
  <div class="prose">{projet}</div>
 </div>
 <div class="rule"></div>
</section>

{secs}

</main>
'''
head=HEAD.replace('<title>Gargantua · Parcours Bijoux 2026</title>','<title>Gargantua · Catalogue</title>')\
 .replace('content="https://gargantua-paris.github.io/"','content="https://gargantua-paris.github.io/catalogue.html"')\
 .replace('content="Gargantua · Parcours Bijoux Paris 2026"','content="Gargantua · Catalogue"').replace('</head>',CSS)
pied=BODY[BODY.index('<div class="vue"'):]
doc=head.replace('{jsonld}',JSONLD).replace('{nav}',nav).replace('{fil}',fil) \
 + typo(MAIN.replace('{noms}',noms).replace('{projet}',''.join('<p>%s</p>'%p for p in PROJET)).replace('{secs}',''.join(secs)).replace('{fl}',FL)+pied.replace('{fl}',FL)) + SCRIPT
open(S+'catalogue.html','w').write(doc)
print('catalogue.html',len(doc),'octets,',sum(len(v) for v in PIECES.values()),'pieces')
