from Regle import*
from Renommage import *
from ListeRegle import*
from tkinter  import *
import tkinter  as tk
from tkinter.messagebox import *



'''
Mon interface de renommage (Annexe 1)
'''
fenetre =Tk()

#titre
label= Label(fenetre,text='Renommer en lots')
label.pack()

# frame Logo dans frame rep1
FrameLogo = Frame(fenetre, bg="white", relief=GROOVE)
FrameLogo.pack(side=RIGHT, padx=0, pady=0)


#logo
photo = PhotoImage(file="ma_photo.png")
canvas = Canvas(FrameLogo,bg="white",width=100, height=120)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

fenetre['bg']='white'

FrameSup=Frame(fenetre,  bg="white",relief=GROOVE)
FrameSup.pack(side=TOP, padx=0, pady=0)

# frame repertoire 1
FrameRep1 = Frame(FrameSup,  bg="white",relief=GROOVE)
FrameRep1.pack(side=LEFT, padx=0, pady=0)

# frame repertoire 2
FrameRep2 = Frame(FrameRep1, bg="white", relief=GROOVE)
FrameRep2.pack(side=LEFT, padx=0, pady=0)

# frame Ammorce
FrameAmorce = Frame(FrameRep1, bg="white", relief=GROOVE)
FrameAmorce.pack(side=LEFT, padx=0, pady=0)




#liste ammorce
liste= Listbox(FrameRep2,bg="white",width=7,height=5)
liste.insert(1,"Aucune")
liste.insert(2,"Lettre")
liste.insert(3,"Chiffre")
liste.selection_set(0)



# Ajout de labels Nom du repertoire
Label(FrameRep1, text="Nom du répertoire").pack(side=TOP,padx=10, pady=10)

Label(FrameLogo,bg="white").pack(padx=0, pady=0)
#repertoires
repertoire = Entry(FrameRep1, textvariable=str, width=80)
repertoire.pack(side=TOP)
# Ajout de labels Ammorce
Label(FrameRep2, text="Ammorce").pack(padx=0, pady=0)
Label(FrameLogo,bg="white").pack(padx=0, pady=0)




#Mes champs



# prefixe
Label(FrameRep1, text="Prefixe:").pack(side=LEFT)
prefixe = Entry(FrameRep1, textvariable=str, width=10)
prefixe.pack(side=LEFT)

#Nom du fichier
Label(FrameRep1, text="Nom du fichier:").pack(side=LEFT,padx=0, pady=0)
global value
value = StringVar()
bouton1 = Radiobutton(FrameRep1, text="Nom original", variable=value, value=1)
bouton2 = Radiobutton(FrameRep1,text="Nom personnalisé" , variable=value, value=2)
bouton1.select()
nomP = Entry(FrameRep1, textvariable=str, width=20)
bouton1.pack(side=LEFT)
bouton2.pack(side=LEFT)
nomP.pack(side=LEFT)

# postfixe
Label(FrameRep1, text="Postfixe:").pack(side=LEFT)
postfixe = Entry(FrameRep1, textvariable=str, width=10)
postfixe.pack(side=LEFT)

# Extension
Label(FrameRep1, text="Extension concernée:").pack(side=LEFT)
extension = Entry(FrameRep1, textvariable=str, width=20)
extension.pack(side=LEFT)



# A partir de
aPartirDe = Entry(FrameRep2, textvariable=str, width=5)
liste.pack()
# Ajout du labels A partir de
Label(FrameRep2, text="A partir de").pack(padx=0, pady=0)
aPartirDe.pack()


def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'Tant pis...')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")


#fonction qui récupére la saisie et qui renomme les fichiers concernés
def RenomeLesFichier():
    rep=repertoire.get()
    try:
     a=liste.get(liste.curselection())
    except:
        showerror("Erreur", "Vous devez choisir une ammorce dans la liste")
    pre=prefixe.get()
    nom=value.get()
    post=postfixe.get()
    ext=extension.get()
    ap=aPartirDe.get()
    list=ext.split(",")

    if(pre == ''):
        pre='aucun'
    if(post == ''):
        post='aucun'
    if(nom=='1'):
        nom=True
    elif(nom == '2'):
        nom=nomP.get()
    if(a=='Lettre' and ap==''):
        ap='A'
    elif(a=='Chiffre' and ap==''):
        ap='0'

    r1 = Regle(a, ap,pre, nom, post, list)
    a1 = Renommage(rep, r1)
    a1.renommer()
    showinfo('Succès', 'Renommé avec succès!')




#Bouton renommer
Button(FrameRep1, text ='Renommer',command=RenomeLesFichier).pack(side=BOTTOM, padx=0, pady=0)

'''
Alerte d'information qui se déclenche lorsqu'on clique sur '?'  présent dans le menu horizontale 
'''

def alert():
    showinfo("Information", "Ce logiciel à été développé par DIAGANA Bayahya dans le cadre d'un projet python proposé par Mme SANS")

'''
Interface 'Lister' présent dans le menu horizontale lorsqu'on clique sur 'Regle'
'''

def interfaceLister():
    fenetre2=Tk()
    fenetre2['bg'] = 'white'
    FrameSup = Frame(fenetre2, bg="white", relief=GROOVE)
    FrameSup.pack(side=TOP, padx=0, pady=0)
    # frame repertoire 1
    FrameRep1 = Frame(FrameSup, bg="white", relief=GROOVE)
    FrameRep1.pack(side=LEFT, padx=0, pady=0)
    # frame repertoire 2
    FrameRep2 = Frame(FrameRep1, bg="white", relief=GROOVE)
    FrameRep2.pack(side=LEFT, padx=0, pady=0)
    # frame Ammorce
    FrameAmorce = Frame(FrameRep1, bg="white", relief=GROOVE)
    FrameAmorce.pack(side=LEFT, padx=0, pady=0)

    r1=Regle('','','','','',[])
    l1=ListeRegle(r1)
    fichier= l1.charger('RENAME.ini')
    listeDesRegles=fichier.split('\n\n')
    limite=len(listeDesRegles)
    lbox = Listbox(fenetre2, bg="white", width=15, height=15)
    del listeDesRegles[limite-1]
    for i in range(len(listeDesRegles)):
        lesRegles=listeDesRegles[i].split(' ')
        print(lesRegles)
        lbox.insert(i+1, lesRegles[0])

    lbox.select_set(0)
    lbox.pack()
    def affiche():
        lbox.pack_forget()
        selection=lbox.curselection()
        index=int(selection[0])
        nomRegle=lbox.get(selection)
        uneRegle=listeDesRegles[index].split(' ',6)
        nom=uneRegle[0]
        ammorce=uneRegle[1]
        apartirDe=uneRegle[2]
        pref=uneRegle[3]
        nomF=uneRegle[4]
        post=uneRegle[5]
        uneRegle[6]=uneRegle[6].replace("'","")
        listExt=list(uneRegle[6])
        if '[' or ']'in listExt:
            listExt.remove('[')
            listExt.remove(']')
        positionAmmorce=0
        if ammorce =='Aucune':
            positionAmmorce=0
        elif ammorce == 'Lettre':
            positionAmmorce=1
        else:
            positionAmmorce=2
        # liste ammorce
        liste = Listbox(FrameRep2, bg="white", width=7, height=5)
        liste.insert(1, "Aucune")
        liste.insert(2, "Lettre")
        liste.insert(3, "Chiffre")
        liste.select_set(positionAmmorce)

        # Ajout de labels Nom du repertoire
        Label(FrameRep1, text="Nom du répertoire").pack(side=TOP, padx=10, pady=10)
        Label(FrameLogo, bg="white").pack(padx=0, pady=0)
        # repertoires
        repertoire = Entry(FrameRep1, textvariable=str, width=80)
        repertoire.pack(side=TOP)
        # Ajout de labels Ammorce
        Label(FrameRep2, text="Ammorce").pack(padx=0, pady=0)
        Label(FrameLogo, bg="white").pack(padx=0, pady=0)
        liste.pack()
        # prefixe
        Label(FrameRep1, text="Prefixe:").pack(side=LEFT)
        prefixe = Entry(FrameRep1, textvariable=str, width=10)
        if(pref!='aucun'):
            prefixe.insert(0,pref)

        prefixe.pack(side=LEFT)
        def nomO():
            value.set(1)
        def nomP():
            value.set(2)
        # Nom du fichier
        Label(FrameRep1, text="Nom du fichier:").pack(side=LEFT, padx=0, pady=0)
        bouton1 = Radiobutton(FrameRep1, text="Nom original", variable=value, value=1, command=nomO)
        bouton2 = Radiobutton(FrameRep1, text="Nom personnalisé", variable=value, value=2, command=nomP)
        nomP = Entry(FrameRep1, textvariable=str, width=20)
        if(nomF == 'True' ):
            bouton1.select()
        else:
            bouton2.select()
            nomP.insert(0,nomF)

        bouton1.pack(side=LEFT)
        bouton2.pack(side=LEFT)
        nomP.pack(side=LEFT)

        # postfixe
        Label(FrameRep1, text="Postfixe:").pack(side=LEFT)
        postfixe = Entry(FrameRep1, textvariable=str, width=10)
        if(post !='aucun'):
            postfixe.insert(0,post)
        postfixe.pack(side=LEFT)

        # Extension
        Label(FrameRep1, text="Extension concernée:").pack(side=LEFT)
        extension = Entry(FrameRep1, textvariable=str, width=20)
        ex=''
        listedesEx=[]
        for i in range(len(listExt)):
            ex=ex+listExt[i]

        extension.insert(0,ex)
        extension.pack(side=LEFT)



        # A partir de
        aPartirDe = Entry(FrameRep2, textvariable=str, width=5)
        aPartirDe.insert(0,apartirDe)
        liste.pack()
        # Ajout du labels A partir de
        Label(FrameRep2, text="A partir de").pack(padx=0, pady=0)
        aPartirDe.pack()
        ok.pack_forget()
        def renommer():
            nom=value.get()
            ap=aPartirDe.get()
            try:
                a = liste.get(liste.curselection())
            except:
                showerror("Erreur", "Vous devez choisir une ammorce dans la liste")
            if (nom == '1'):
                nom = True
            elif (nom == '2'):
                nom = nomP.get()
            if (a == 'Lettre' and ap == ''):
                ap = 'A'
            elif (a == 'Chiffre' and ap == ''):
                ap = '0'
            listeExtensions = extension.get().split(',')
            r1 = Regle(ammorce, ap, pref, nom, post,listeExtensions )
            a1 = Renommage(repertoire.get(), r1)
            a1.renommer()
            showinfo('Succès', 'Renommé avec succès!')
        renom = Button(fenetre2, text='renommer', command=renommer)
        renom.pack()

    ok= Button(fenetre2, text='Ok', command=affiche)
    ok.pack()






'''
Interface 'Creer' présent dans le menu horizontale lorsqu'on clique sur 'Regle'
'''

def interfaceCreer():
    fenetre3=Tk()
    # titre
    label = Label(fenetre3, text='Créer une règle')
    label.pack()

    # frame Logo dans frame rep1
    FrameLogo = Frame(fenetre3, bg="white", relief=GROOVE)
    FrameLogo.pack(side=RIGHT, padx=0, pady=0)

    fenetre3['bg'] = 'white'

    FrameSup = Frame(fenetre3, bg="white", relief=GROOVE)
    FrameSup.pack(side=TOP, padx=0, pady=0)

    # frame repertoire 1
    FrameRep1 = Frame(FrameSup, bg="white", relief=GROOVE)
    FrameRep1.pack(side=LEFT, padx=0, pady=0)

    # frame repertoire 2
    FrameRep2 = Frame(FrameRep1, bg="white", relief=GROOVE)
    FrameRep2.pack(side=LEFT, padx=0, pady=0)

    # frame Ammorce
    FrameAmorce = Frame(FrameRep1, bg="white", relief=GROOVE)
    FrameAmorce.pack(side=LEFT, padx=0, pady=0)

    # liste ammorce
    lbox = Listbox(FrameRep2, bg="white", width=7, height=5)
    lbox.insert(1, "Aucune")
    lbox.insert(2, "Lettre")
    lbox.insert(3, "Chiffre")
    lbox.select_set(0)

    # Ajout de labels Nom du repertoire
    Label(FrameRep1, text="Nom de la règle").pack(side=TOP, padx=10, pady=10)

    Label(FrameLogo, bg="white").pack(padx=0, pady=0)
    # repertoires
    repertoire = Entry(FrameRep1, textvariable=str, width=80)
    repertoire.pack(side=TOP)
    # Ajout de labels Ammorce
    Label(FrameRep2, text="Ammorce").pack(padx=0, pady=0)
    Label(FrameLogo, bg="white").pack(padx=0, pady=0)



    # Mes champs

    # prefixe
    Label(FrameRep1, text="Prefixe:").pack(side=LEFT)
    prefixe = Entry(FrameRep1, textvariable=str, width=10)
    prefixe.pack(side=LEFT)
    def nomO():
        value.set(1)
    def nomP():
        value.set(2)
    # Nom du fichier
    Label(FrameRep1, text="Nom du fichier:").pack(side=LEFT, padx=0, pady=0)
    bouton1 = Radiobutton(FrameRep1, text="Nom original", variable=value, value=1,command=nomO)
    bouton2 = Radiobutton(FrameRep1, text="Nom personnalisé", variable=value,value=2,command=nomP)
    bouton1.select()
    bouton1.pack(side=LEFT)
    bouton2.pack(side=LEFT)
    nomP = Entry(FrameRep1, textvariable=str, width=20)
    nomP.pack(side=LEFT)
    # postfixe
    Label(FrameRep1, text="Postfixe:").pack(side=LEFT)
    postfixe = Entry(FrameRep1, textvariable=str, width=10)
    postfixe.pack(side=LEFT)

    # Extension
    Label(FrameRep1, text="Extension concernée:").pack(side=LEFT)
    extension = Entry(FrameRep1, textvariable=str, width=20)
    extension.pack(side=LEFT)

    # A partir de
    aPartirDe = Entry(FrameRep2, textvariable=str, width=5)
    lbox.pack()
    # Ajout du labels A partir de
    Label(FrameRep2, text="A partir de").pack(padx=0, pady=0)
    aPartirDe.pack()
    def creer():
        nomRegle = repertoire.get()
        try:
            a = lbox.get(lbox.curselection())
        except:
            showerror("Erreur", "Vous devez choisir une ammorce dans la liste")
        pre = prefixe.get()
        nomF = value.get()
        post = postfixe.get()
        ext = extension.get()
        ap = aPartirDe.get()
        liste = ext.split(",")



        if (pre == ''):
            pre = 'aucun'
        if (post == ''):
            post = 'aucun'
        if (nomF == '1'):
            nomF = True
        elif (nomF == '2'):
            nomF = nomP.get()
        if (a == 'Lettre' and ap == ''):
            ap = 'A'
        elif (a == 'Chiffre' and ap == ''):
            ap = '0'
        r1 = Regle(a, ap, pre, nomF, post, liste)
        l1 = ListeRegle(r1)
        l1.sauvegarder('RENAME.ini',nomRegle)
        showinfo('Succès', 'Créé avec succès!')
    # Bouton Creer une liste
    Button(FrameRep1, text='Creer', command=creer).pack(side=BOTTOM, padx=0, pady=0)
    fenetre3.mainloop()


'''
Menu horizontale
'''

menubar = Menu(fenetre)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Lister",command=interfaceLister)
menu1.add_command(label="Créer",command=interfaceCreer)
menubar.add_cascade(label="Regles", menu=menu1)
menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Information", command=alert)
menubar.add_cascade(label="?", menu=menu2)
fenetre.config(menu=menubar)
fenetre.mainloop()


