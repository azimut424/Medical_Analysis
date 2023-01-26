import glob
import itertools


def getpalu() :
    palu = [
                  "fatigue",
                  "chair de poule",
                  "fievre",
                  "frissons",
                 " maux de tete",
                 " douleurs musculaires",
                  "vomissements",
                  "diarrhees",
                  "toux",
                  "anemie"]
    return palu
def gettyphoide():
    typhoide = [

                  "ballonnements",
                  "vomissements",
                  "constipation",
                  "diarrhee",
                  "nausees",
                  "fatigue",
                  "fievre",
                  "perte d appetit",
                  "faiblesse musculaire",
                  "perte de poids",
                  "eruption cutanee",
                  "migraine"
           ]
    return typhoide
def getmeningite():
    meningite = ["fievre",
                  "raideur au cou",
                  "mal de tete",
                  "vomissements",
                  "somnolence",
                  "convulsions",
                  "taches rouges" ,
                 "bleues sur la peau",
                  "constipation"]
    return meningite
def gethepatite():
    hepatite = ["fatigue",
                  "un confort physique",
                  "perte d appetit",
                  "jaunisse",
                  "maux de ventre du cote droit",
                  "demangeaisons",
                  "urines foncees",
                  "nausees"

           ]
    return hepatite
def getgrippe():
    grippe = ["fatigue",
                  "rougeur",
                  "chair de poule",
                  "courbatures",
                  "deshydratation",
                  "fievre",
                  "perde d appetit",
                  "transpiration",
                  "nez qui coule",
                  "eternuements",
                  "mal de gorge",
                  "maux de tete",
                  "nausee",
           ]
    return grippe
def getebola():
    ebola = [     "fievre",
                  "maux de tete",
                  "fatigue",
                  "douleurs",
                  "faiblesse musculaire",
                  "mal de gorge",
                  "eruption cutanee",
                  "nausees",
                  "vomissements",
                  "diarrhee",
                  "hemorragie",
                  "saigement"]
    return ebola
def getdrepanocytose():
    drepanocytose = []
    diabete = ["augmentation de la production d urine",
                  "soif excessive",
                  "perte de poids",
                  "faim accrue",
                  "fatigue",
                  "problemes de peau",
                  "cicatrisation lente des plaies",
                  "infections a levures",
                  "picotements" ,
                  "engourdissements dans les pieds et ou les orteils"]
    return drepanocytose
def getcovid():

    covid=['mal de gorge',
           'ecoulement nasal',
           'eternuement',
           'apparition ou aggravation de la toux',
           'essouflement',
           'difficulte respiratoire' ,
           'temperature mal de gorge',
           'ecoulement nasal',
           'eternuement',
           'apparition ou aggravation de la toux',
           'essouflement ou difficulte respiratoire',
           'temperature egale ou superieur à 38 degre',
           'sansation de fievre',
           'frissons',
           'fatigue',
           'faiblesse',
           'douleurs musculaires ou courbatures',
           'perte de l odorat ou du gout',
           'mal de tete',
           'douleurs addominales',
           'diarrhee',
           'vomissements',
           'malaises intenes']
    return covid
def getavc():

    avc = ["faiblesse d un cote du corps",
           "un engourdissement ou un fourmillement au niveau du visage dans les bras et dans les jambes",
           "une difficulte a parler ou a comprendre ce que disent les autres",
           "des troubles de la vue, comme une vision double" , "l incapacite de voir, surtout d un oeil",
           "des etourdissements", "la perte d equilibre surtout si vous presentez egalement d autres signes"]
    return avc
def getcholera():
    cholera = ["crampes musculaires",
                  "faiblesse",
                  "miction reduite ou absente",
                  "une peau des doigts ridee",
                  "pouls filant",
                  "les yeux renfonces dans les orbites"
               ]
    return cholera
def getchlamydia():
    chlamydia = ["saignements vaginaux après les relations sexuelles et entre les menstruations",
                 "écoulements anormaux par le pénis ou l'anus",
                 "picotements ou sensation de brûlure en urinant",
                 "douleurs aux testicules ou dans la région de l'anus"]
    return chlamydia
def getcancer():
    cancer = [    "Perte de poids inexpliquée",
                    "Fatigue",
                   " Sueurs nocturnes",
                    "Perte d'appétit",
                    "Douleur nouvelle et prolongée",
                   " Problèmes de vue ou d'audition",
                    "Nausées ou vomissements récurrents",
                    "Sang dans l'urine",
                    "Sang dans les selles (visible ou détectable par des examens de laboratoire)",
                   "Récente modification du transit intestinal (constipation ou diarrhée)",
                   "Saignements vaginaux anormaux, en particulier après la ménopause",
                   "Fièvre récurrente",
                   "Toux chronique",
                   "Changements de taille",
                   " changements dans une ulcération cutanée qui ne guérit pas"
                   "Excroissance ou marque sur la peau qui grossit ou change d’aspect",
                   "Lésion qui ne cicatrise pas",
                   "Ganglions lymphatiques hypertrophiés",
                  ]
    return cancer
def getvih():

    vih = [    "de la fièvre",
                "une fatigue",
                "des frissons",
                "un mal de gorge",
                "des maux de tête",
                "des douleurs articulaires",
               " des douleurs musculaires",
                "l'enflure de glandes (ganglions lymphatiques)"
            ]
    return vih



val1 = getebola()
val2 = getavc()
val3 = gettyphoide()
val4 = getchlamydia()
val5 = getgrippe ()
val6 = getvih()
val7 = getcancer()
val8 = getdrepanocytose()
val9 = getcholera()
val10 = gethepatite()
val11 = getmeningite()
values_list = getcovid()
liste2 = []
def analyse():
    s=0
    disco = {"ebola":val1,"avc":val2,"typhoide":val3,"chlamydia":val4,
             "grippe":val5,"vih":val6,"cancer":val7,
             "drepanocytose":val8,"cholera":val9,
             "hepatite":val10,"meningite":val11,"covid":values_list}
    liste3 = [val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,values_list]

    t=0
    o=int(input("Nombre de symptomes: "))

    while t<o:
        a = str(input("entrer maladie: "))
        for k,v in disco.items():


                for j in v:

                    if a in j:
                        print("Trouve dans ",k)

                        r=[len(v) for v in disco.values()]
                        for i in range(len(r)):
                            y=r[i]-1
                            r[i] = y
                        print(r)
                        print(r)
                        print(k)
                        sym = j

                        print([sym])


        t+=1



analyse()
