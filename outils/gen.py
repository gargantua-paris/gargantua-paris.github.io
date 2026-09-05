# -*- coding: utf-8 -*-
import json, html
S='/Users/hamouda/Desktop/project amira parcour/SITE_GARGANTUA/'
M=json.load(open(S+'images/manifest.json'))
oe={}
for o in M['oeuvres']: oe.setdefault(o['artist'],[]).append(o)
po=M['portraits']

PIECE_AFFICHE={'agnes-dubois':3,'faust-cardinali':1,'thierry-vendome':0,'amira-sliman':0}

ARTISTES=[
 dict(k='agnes-dubois', nom='Agnès Dubois', n='01',
   credit_portrait='Portrait : galerie bettina flament',
   credit_oeuvres='Photos : Agnès Dubois',
   bio=["Diplômée de l’AFEDAP en 2000",
        "Après un parcours en Sciences Humaines et dans l’édition, j’ai choisi de me consacrer au bijou contemporain, me formant à l’AFEDAP Paris à la fin des années 1990. Créatrice indépendante depuis 2001, j’envisage le bijou comme un champ plastique à part entière, un médium à travers lequel j’interroge la relation entre le corps et le monde qui l’environne, entre le geste créatif et l’acte de porter.",
        "Je conçois le bijou comme un marqueur identitaire, un vecteur de communication capable de signifier autant que de parer. Mes créations, souvent minimalistes, agissent comme révélateurs du corps dans sa présence sensible et se muent en sculptures habitées, en éléments de narration silencieuse.",
        "L’équilibre, la sensorialité, la notion de plaisir, la cohérence entre espace corporel et extra-corporel nourrissent ma recherche formelle. J’explore l’art du lien : celui entre l’objet et le mouvement, le geste et l’émotion, entre l’artiste (moi-même) et la personne qui s’approprie l’objet.",
        "Mon travail est régulièrement présenté dans des galeries dédiées au bijou contemporain, à Paris et en région, et je participe depuis plus de vingt ans à des événements liés aux métiers d’art. J’ai pris part au festival Parcours Bijoux, notamment en 2020 et 2023, en tant que porteuse de projets collectifs."]),
 dict(k='faust-cardinali', nom='Faust Cardinali', n='02',
   credit_portrait='',
   credit_oeuvres='Photos : Alessandro Schinco',
   note='Représenté en France par la Galerie Minimasterpiece.',
   bio=["Né à Paris en 1961. Artiste pluridisciplinaire, je me forme en tant que sculpteur, peintre et orfèvre.",
        "Mon travail allie dessin et écriture dans une réflexion artistique qui explore la « plastification poétique » de la société, matérialisant un temps à la fois archéologique et « futurible ».",
        "Mes œuvres incarnent simultanément la mémoire du passé, la présence du présent et une vision du futur, dans une seule et même expression plastique et conceptuelle.",
        "J’utilise des matériaux hétérogènes : polychlorure de vinyle, polyester, métaux précieux. Ces éléments, en apparence éloignés, se fondent pour dépasser les frontières entre peinture, sculpture et orfèvrerie : des disciplines autonomes mais profondément complémentaires.",
        "Mes créations traduisent la liquidité du monde contemporain, marquée par les blessures historiques, psychologiques et géologiques, révélant de nouvelles formes de « polycorps » : une conception de l’art non pas in situ, mais in tempore.",
        "Mes œuvres figurent dans d’importantes collections en Europe et en Asie."]),
 dict(k='thierry-vendome', nom='Thierry Vendome', n='03',
   credit_portrait='Portrait : The French Jewelry Post, « Dans la famille Vendome, Thierry le fils »',
   credit_oeuvres='Photos : @olivierfoulonstudio',
   bio=["<span class=\"up\">MES BIJOUX SONT DES ACTES POÉTIQUES</span>",
        "Je ne cherche pas tant à représenter le visible qu’à exprimer des émotions qui me sont inspirées par ma vision du monde. C’est pourquoi je suis fasciné par les matières « vivantes » chargées d’un passé qu’il me plaît de transformer. Fragments d’éclats d’obus, clous rouillés, fils de fer barbelé, minéraux…",
        "Je les dévie de leur trajectoire. Je les fais entrer dans une nouvelle histoire. La trace visible et irréversible de leur passé sur leur surface devient mon matériau de création. Je les choisis toujours pour une dimension physique, sensorielle et émotionnelle inédite. Un grain, une forme, une couleur.",
        "Ces matières empreintes de leur propre histoire m’inspirent de nouveaux dialogues possibles entre présent et passé, entre mémoire et futur, entre formes brutes et matières délicates. Je cherche à provoquer une expérience immédiate et humaine renvoyant chacun à sa part sensible. À son propre ressenti du vécu.",
        "En portant mes bijoux, chacun devient sujet de l’expérience."]),
 dict(k='amira-sliman', nom='Amira Sliman', n='04',
   credit_portrait='',
   credit_oeuvres='',
   bio=["Diplômée en Design Industriel de l’École des Beaux-Arts de Tunis et de l’AFEDAP (1997). En 2003, je fonde ma galerie de bijoux contemporains à Paris, que je dirige depuis.",
        "Mon approche du bijou s’apparente à celle d’un architecte : je conçois mes pièces comme des « architectures à porter », aux lignes fluides, épurées et intemporelles.",
        "Ma recherche artistique repose sur l’équilibre, entre les formes, les matières, les couleurs, et sur une quête de complémentarité.",
        "La nature constitue ma principale source d’inspiration : structures végétales, ossatures, textures organiques nourrissent mon imaginaire. Je privilégie les matériaux naturels : pierres que je taille, bois, plumes….",
        "Le bijou n’est pas un simple ornement ; il représente un lien du corps au monde, un objet porteur de sens. Ce lien est lui aussi une quête : celle de la reconnaissance de la place de l’individu dans un groupe.",
        "Depuis quelques années, mes pièces uniques sont donc construites comme des chapitres de vie, ils racontent mon propre rapport au monde."]),
]

PROJET=["Gargantua, au-delà du personnage truculent imaginé par Rabelais, incarne une figure hautement symbolique ancrée dans l’inconscient collectif français, qui dépasse son seul statut littéraire.",
 "Dans l’œuvre de Rabelais, il illustre l’abondance, voire l’excès, la satire du pouvoir et la liberté intellectuelle en réaction aux dogmes.",
 "Métaphore de la curiosité humaine, du désir et de la joie, autrement dit, de l’élan vital incarné, Gargantua s’inscrit dans une dimension intemporelle et universelle, tel un archétype culturel qui véhicule des valeurs hautement humanistes, porteuses d’un idéal de tolérance et de progrès.",
 "À l’heure où notre monde traverse des mutations profondes, chacun de nous se voit confronté à la nécessité de faire des choix, de se repositionner. Cela soulève des questions essentielles : qu’est-ce qui nous définit en tant qu’êtres humains ?",
 "Quatre artistes bijoutiers d’expressions et d’horizons différents, invitent le public à découvrir une exposition célébrant nos penchants gargantuesques et nos excès sous toutes leurs formes, à les examiner pour en extraire ce qui nous définit comme les porteurs de cet héritage humaniste, à les envisager comme une véritable ode à la vie."]

def esc(s): return s

def navlab(nom):
    pre,_,last=nom.rpartition(' ')
    return '<span class="fn">%s </span>%s'%(pre,last)
nav=''.join('<a href="#%s">%s</a>'%(a['k'],navlab(a['nom'])) for a in ARTISTES)

secs=[]
for i,a in enumerate(ARTISTES):
    p=po[a['k']]
    o=oe[a['k']][PIECE_AFFICHE[a['k']]]
    bio=''.join('<p>%s</p>'%b for b in a['bio'])
    pcred='<figcaption><p class="credit">%s</p></figcaption>'%a['credit_portrait'] if a['credit_portrait'] else ''
    note='<p class="credit" style="margin-top:16px">%s</p>'%a['note'] if a.get('note') else ''
    ocred='<p class="credit">%s</p>'%a['credit_oeuvres'] if a['credit_oeuvres'] else ''
    sens='' if i%2==0 else ' piece--inv'
    secs.append('''
<section class="artiste" id="%s">
 <div class="artiste__h"><h2>%s</h2><span>%s / 04</span></div>
 <div class="piece%s">
  <figure class="piece__im" role="button" tabindex="0" aria-label="Voir %s en grand"
          data-full="%s" data-bg="%s" data-titre="%s" data-mat="%s" data-cred="%s" data-nom="%s">
   <img src="%s" width="%d" height="%d" alt="%s, %s" loading="lazy">
   <figcaption>
    <h3>%s</h3>
    <p>%s</p>
    %s
    <span class="zoom">Voir en grand <i>&#8599;</i></span>
   </figcaption>
  </figure>
  <div class="piece__t">
   <figure class="pf"><img src="%s" width="%d" height="%d" alt="Portrait de %s" loading="lazy">%s</figure>
   <div class="prose">%s%s</div>
  </div>
 </div>
</section>'''%(a['k'],esc(a['nom']),a['n'],sens,
    esc(o['titre']),o['file'],o['bg'],esc(o['titre']),esc(o['matiere']),a['credit_oeuvres'],esc(a['nom']),
    o['file'],o['w'],o['h'],esc(o['titre']),esc(a['nom']),
    esc(o['titre']),esc(o['matiere']),ocred,
    p['file'],p['w'],p['h'],esc(a['nom']),pcred,bio,note))

doc='''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Gargantua · Parcours Bijoux 2026</title>
<meta name="description" content="Gargantua. Une proposition pour le Parcours Bijoux 2026, projet initié par Amira Sliman. Agnès Dubois, Faust Cardinali, Thierry Vendome, Amira Sliman. Galerie Psyché Paris, 5 au 17 octobre 2026.">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="icon" type="image/png" sizes="512x512" href="favicon-512.png">
<link rel="apple-touch-icon" href="favicon-180.png">
<link rel="stylesheet" href="style.css">
</head>
<body>

<header class="bar">
 <a class="bar__b" href="#top">Gargantua</a>
 <nav class="bar__n">%s</nav>
</header>

<main>

<section class="hero" id="top">
 <h1>Gargantua.</h1>
 <div class="hero__sub">
  <em>Projet initié par Amira Sliman</em>
 </div>

 <p class="invit">Vous êtes invités.</p>

 <div class="meta">
  <div><span class="lbl">Dates</span><p>05 au 17 octobre 2026</p></div>
  <div><span class="lbl">Lieu</span>
   <p><a class="carte" href="https://www.google.com/maps/search/?api=1&amp;query=Galerie+Psych%%C3%%A9%%2C+18+rue+du+Pont+Louis+Philippe%%2C+75004+Paris"
         target="_blank" rel="noopener">Galerie Psyché Paris<br>18 rue du Pont Louis Philippe<br>75004 Paris<span class="carte__k">Voir sur la carte <i>&#8599;</i></span></a></p></div>
  <div><span class="lbl">Vernissage</span><p>08 octobre à 18h</p></div>
  <div><span class="lbl">Rencontre autour de Gargantua</span><p>08 octobre à 14h<br>Espace L’Échappée Belle</p></div>
 </div>
</section>

<section>
 <div class="split">
  <div><span class="lbl">Parcours Bijoux</span></div>
  <div class="prose">
   <p>Gargantua fait partie de Parcours Bijoux, le rendez-vous parisien du bijou
   contemporain porté par l’association d’un bijou à l’autre depuis 2011.</p>
   <p>Pour sa cinquième édition, du 1<sup>er</sup> au 31 octobre 2026, Parcours Bijoux
   réunit 33 expositions et plus de 200 artistes dans toute la ville : galeries, musées,
   écoles, centres culturels et ateliers d’artistes, d’une rive à l’autre. S’y ajoutent
   un colloque international, des performances et des rencontres.</p>
   <p><a class="lien" href="https://www.parcoursbijoux.com" target="_blank" rel="noopener">parcoursbijoux.com <i>&#8599;</i></a></p>
  </div>
 </div>
 <div class="rule"></div>
</section>

<section class="affiche">
 <figure>
  <img src="images/affiche/affiche_gargantua.jpg" width="1080" height="1350" alt="Affiche Gargantua, Parcours Bijoux Paris 2026">
  <figcaption><span class="lbl">Parcours Bijoux Paris 2026</span><span class="lbl">Affiche de Gargantua</span></figcaption>
 </figure>
</section>

<section>
 <div class="split">
  <div><span class="lbl">Le projet</span></div>
  <div class="prose">%s</div>
 </div>
 <div class="rule"></div>
</section>

%s

</main>

<div class="vue" id="vue" hidden>
 <button class="vue__x" aria-label="Fermer">&#215;</button>
 <img id="vueIm" alt="">
 <div class="vue__c"><h3 id="vueT"></h3><p id="vueM"></p><p class="credit" id="vueC"></p></div>
</div>

<footer>
 <div class="foot">
  <div><span class="lbl">Exposition</span><p>Gargantua<br>05 au 17 octobre 2026<br>Galerie Psyché Paris</p></div>
  <div><span class="lbl">Organisé par</span><p>d’un bijou à l’autre<br>
   <span class="foot__x">Association créée en 2011, elle porte et organise Parcours Bijoux.</span></p></div>
<div class="foot__ig">
   <span class="lbl">Instagram</span>
   <div class="igs">
    <a class="ig" href="https://www.instagram.com/agnes.dubois.bijoux/" target="_blank" rel="noopener">
     <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.4" y="2.4" width="19.2" height="19.2" rx="5.4"/><circle cx="12" cy="12" r="4.6"/><circle class="d" cx="17.6" cy="6.4" r="1.15"/></svg>
     <span class="ig__n">Agnès Dubois</span><span class="ig__h">@agnes.dubois.bijoux</span></a>
    <a class="ig" href="https://www.instagram.com/faustcardinali/" target="_blank" rel="noopener">
     <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.4" y="2.4" width="19.2" height="19.2" rx="5.4"/><circle cx="12" cy="12" r="4.6"/><circle class="d" cx="17.6" cy="6.4" r="1.15"/></svg>
     <span class="ig__n">Faust Cardinali</span><span class="ig__h">@faustcardinali</span></a>
    <a class="ig" href="https://www.instagram.com/thierry_vendome/" target="_blank" rel="noopener">
     <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.4" y="2.4" width="19.2" height="19.2" rx="5.4"/><circle cx="12" cy="12" r="4.6"/><circle class="d" cx="17.6" cy="6.4" r="1.15"/></svg>
     <span class="ig__n">Thierry Vendome</span><span class="ig__h">@thierry_vendome</span></a>
    <a class="ig" href="https://www.instagram.com/amiraslimanjewellery/" target="_blank" rel="noopener">
     <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.4" y="2.4" width="19.2" height="19.2" rx="5.4"/><circle cx="12" cy="12" r="4.6"/><circle class="d" cx="17.6" cy="6.4" r="1.15"/></svg>
     <span class="ig__n">Amira Sliman</span><span class="ig__h">@amiraslimanjewellery</span></a>
   </div>
  </div>
 </div>
</footer>

<script>
/* visionneuse plein ecran */
const vue=document.getElementById('vue'),vueIm=document.getElementById('vueIm');
let lastFocus=null;
function ouvrir(f){
  lastFocus=f;
  vueIm.src=f.dataset.full; vueIm.alt=f.dataset.titre+', '+f.dataset.nom;
  vue.style.background=f.dataset.bg;
  document.getElementById('vueT').textContent=f.dataset.titre;
  document.getElementById('vueM').textContent=f.dataset.mat;
  document.getElementById('vueC').textContent=f.dataset.cred||'';
  vue.hidden=false; document.body.style.overflow='hidden';
  vue.querySelector('.vue__x').focus();
}
function fermer(){ vue.hidden=true; vueIm.removeAttribute('src'); document.body.style.overflow='';
  if(lastFocus) lastFocus.focus(); }
document.querySelectorAll('.piece__im').forEach(f=>{
  f.addEventListener('click',e=>{ if(!e.target.closest('.credit')) ouvrir(f); });
  f.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){e.preventDefault();ouvrir(f);} });
});
vue.addEventListener('click',fermer);
addEventListener('keydown',e=>{ if(e.key==='Escape'&&!vue.hidden) fermer(); });

const links=[...document.querySelectorAll('.bar__n a')];
const secs=links.map(a=>document.querySelector(a.getAttribute('href')));
const io=new IntersectionObserver(es=>{
  es.forEach(e=>{
    const i=secs.indexOf(e.target);
    if(i<0)return;
    if(e.isIntersecting){links.forEach(l=>l.classList.remove('on'));links[i].classList.add('on');}
  });
},{rootMargin:'-45%% 0px -50%% 0px',threshold:0});
secs.forEach(s=>s&&io.observe(s));
</script>

</body>
</html>
'''%(nav,''.join('<p>%s</p>'%p for p in PROJET),''.join(secs))

open(S+'index.html','w').write(doc)
print('index.html',len(doc),'octets')

# --- page solo Suzanne (structure, textes à remplir) ---
solo='''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Suzanne Somogyi</title>
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="icon" type="image/png" sizes="512x512" href="favicon-512.png">
<link rel="apple-touch-icon" href="favicon-180.png">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="bar">
 <a class="bar__b" href="index.html">Gargantua</a>
 <nav class="bar__n"><a href="index.html">Retour</a></nav>
</header>
<main>
<section class="hero" id="top">
 <h1>Suzanne&nbsp;Somogyi.</h1>
 <div class="hero__sub"><span class="ph">Exposition solo, sous-titre à venir.</span></div>
 <div class="meta">
  <div><span class="lbl">Dates</span><p class="ph">à venir</p></div>
  <div><span class="lbl">Lieu</span><p class="ph">à venir</p></div>
  <div><span class="lbl">Vernissage</span><p class="ph">à venir</p></div>
 </div>
</section>
<section>
 <div class="split">
  <div><span class="lbl">Le projet</span></div>
  <div class="prose"><p class="ph">Texte de présentation à venir.</p></div>
 </div>
 <div class="rule"></div>
</section>
<section>
 <div class="split">
  <div><span class="lbl">Bio</span></div>
  <div class="prose"><p class="ph">Bio à venir.</p></div>
 </div>
 <a class="retour" href="index.html">Retour à Gargantua</a>
</section>
</main>
<footer><div class="foot"><div><span class="lbl">Galerie</span><p>Amira Sliman</p></div></div></footer>
</body>
</html>
'''
open(S+'suzanne-somogyi.html','w').write(solo)
print('suzanne-somogyi.html ok')
