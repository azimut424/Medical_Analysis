import datetime
import random

import wikipedia
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Custumer, Message, Malaria, Avc, Palu, Prediction, GetMalaria
from .testM import getcovid, getebola, getavc, gettyphoide


# Create your views here.
def SingUp(request):
    if request.method == 'POST':

        nom = request.POST.get('nom')
        print(nom)
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        age = request.POST.get('age')
        mdp = request.POST.get('mdp')
        sexe = request.POST.get('sexe')
        phone = request.POST.get('PhoneNumbers')
        try:

            std = User.objects.create_user(username=nom, last_name=prenom, email=email, password=mdp)

            Custumer.objects.create(user=std, age=age, sexe=sexe, PhoneNumbers=phone)

            return redirect("SingIn")
        except:

            mess = "user existe deja!!"
            return render(request, "SingUp.html", {'mess': mess})

    return render(request, 'SingUp.html')


def SingIn(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        mdp = request.POST.get('password')
        user = authenticate(username=nom, password=mdp)
        if user is not None:
            login(request, user)

            return redirect('acceuil')
        else:

            return redirect("SingUp")
    return render(request, 'SingIn.html')


@login_required
def acceuil(request):
    global symptomes
    p = Malaria.objects.all()
    # context = {'p':p,'t':t}
    recup = request.POST.getlist('countries[]')
    val1 = getebola()
    val2 = getavc()
    val3 = gettyphoide()
    values_list = getcovid()
    liste = [values_list, val1, val2, val3]
    for t in range(len(liste)):
        print(len(liste[t]))
    x = ""
    k = 0

    u = 0

    cov = []
    ebol = []
    av = []
    typ = []
    maxi = 0
    message = ""
    countries = ""
    wikipedia.set_lang("fr")
    if request.method == 'POST':
        countries = request.POST.getlist('countries[]')
        print("les valeurs", countries)
        for i in range(len(countries)):
            if countries[i] in values_list and countries[i] in val1 and countries[i] in val2 and countries[i] in val3:
                cov.append(countries[i])
                ebol.append(countries[i])
                av.append(countries[i])
                typ.append(countries[i])
            if countries[i] in values_list and countries[i] in val1 and countries[i] in val2:
                cov.append(countries[i])
                ebol.append(countries[i])
                av.append(countries[i])
            if countries[i] in values_list and countries[i] in val1:
                cov.append(countries[i])
                ebol.append(countries[i])
            if countries[i] in values_list and (
                    countries[i] not in val1 and countries[i] not in val2 and countries[i] not in val3):
                cov.append(countries[i])
            if countries[i] in val1 and (
                    countries[i] not in values_list and countries[i] not in val2 and countries[i] not in val3):
                ebol.append(countries[i])
            if countries[i] in val2 and (
                    countries[i] not in values_list and countries[i] not in val1 and countries[i] not in val3):
                av.append(countries[i])
            if countries[i] in val3 and (
                    countries[i] not in values_list and countries[i] not in val1 and countries[i] not in val2):
                typ.append(countries[i])
            if countries[i] in values_list and countries[i] in val1 and (
                    countries[i] not in val2 and countries[i] not in val3):
                cov.append(countries[i])
                ebol.append(countries[i])
            if countries[i] in values_list and countries[i] in val2 and (
                    countries[i] not in val1 and countries[i] not in val3):
                cov.append(countries[i])
                av.append(countries[i])
            if countries[i] in values_list and countries[i] in val3 and (
                    countries[i] not in val1 and countries[i] not in val2):
                cov.append(countries[i])
                av.append(countries[i])
            if countries[i] in val1 and countries[i] in val3 and (
                    countries[i] not in val2 and countries[i] not in values_list):
                ebol.append(countries[i])
                typ.append(countries[i])
            if countries[i] in values_list and countries[i] in val1 and countries[i] in val2 and countries[
                i] not in val3:
                cov.append(countries[i])
                ebol.append(countries[i])
                av.append(countries[i])
            if countries[i] in values_list and countries[i] in val1 and countries[i] in val3 and countries[
                i] not in val2:
                cov.append(countries[i])
                ebol.append(countries[i])
                typ.append(countries[i])
            if countries[i] in values_list and countries[i] in val2 and countries[i] in val3 and countries[
                i] not in val1:
                cov.append(countries[i])
                av.append(countries[i])
                typ.append(countries[i])
            if countries[i] in val1 and countries[i] in val2 and countries[i] in val3 and countries[
                i] not in values_list:
                ebol.append(countries[i])
                av.append(countries[i])
                typ.append(countries[i])
            if countries[i] not in val1 and countries[i] not in val2 and countries[i] not in val3 and countries[
                i] not in values_list:
                message = "Maladie inrouvable"
            print("cov", cov)
            print('ebol', ebol)
            print('av', av)
            print('typ', typ)
            r = len(cov)
            r1 = len(ebol)
            r2 = len(av)
            r3 = len(typ)
            r11 = r / (len(liste[0]) - 16) * 100
            r12 = r1 / (len(liste[1]) - 5) * 100
            r13 = r2 / len(liste[2]) * 100
            r14 = r3 / (len(liste[3]) - 5) * 100

            mini = 0

            l1 = [r11, r12, r13, r14]
            u = max(l1)
            if l1[0] == u:
                x = "covid"
                k = wikipedia.search(x)
                print(k)
                for r in k:
                    print(r)
                r = r
            if l1[1] == u:
                x = "ebola"
                k = wikipedia.search(x)
                print(k)
            if l1[2] == u:
                x = "avc"
                k = wikipedia.search(x)
                print(k)
            if l1[3] == u:
                x = "typhoide"
                k = wikipedia.search(x)
                print(k)
            if l1[0] == u and l1[1] == u:
                x = "covid"
                o = "ebola"
                l15 = [x, o]
                l14 = random.sample(l15, 1)
                if l14 == l15[0]:
                    x = "covid"
                    k = wikipedia.search(x)
                    print(k)
                if l14 == l15[1]:
                    o = "ebola"
                    k = wikipedia.search(x)
                    print(k)
                return render(request, 'acceuil.html', {'p': p, 'countries': countries, 'u': u, 'x': x, 'o': o, 'k': k})
            dico = {'covid': r11, 'ebola': r12, 'avc': r13, 'typhoide': r14}
            for i in range(len(l1)):
                if l1[i] > maxi:
                    maxi = l1[i]

                elif l1[i] < mini:
                    mini = l1[i]

            for k, v in dico.items():
                if v > maxi:
                    maxi = v
                    print(k, ':', v)

            Prediction.objects.create(nom_patient=request.user, maladie=x, probabilite=u)
            print("le maxi", maxi)
            print("le min", mini)

            # classement par symptome et maladie
            # for i in range(len(l1)):
            #    u = sorted(l1)
            #    print(u)
            # for k in u:
            #    print(k)

    return render(request, 'acceuil.html', {'p': p, 'countries': countries, 'u': u, 'x': x})


def chatlive(request):
    robot = User.objects.get(username='azimut')
    message = request.POST.getlist('countries[]')
    print(message)
    message2 = "Vous avez le paludisme"
    date = datetime.datetime.now()
    mess1 = Message.objects.create(sender=request.user, text=message, receive=robot, date_sender=date)
    mess2 = Message.objects.create(sender=robot, text=message2, receive=request.user, date_sender=date)
    return JsonResponse({'text': mess1.text, 'date_sender': mess1.date_sender, 'sender': mess1.sender.username
                            , 'text2': mess2.text, 'date_sender2': mess2.date_sender, 'sender2': mess2.sender.username})


def chat(request):
    robot = User.objects.get(username='azimut')
    date = datetime.datetime.now()
    lien = "https://127.0.0.1:8000/info_patient/"
    lien1 = "https://127.0.0.1:8000/liste_consultation/"
    message_boot = f"Salut {request.user}, je suis {robot.username} ton robot consultant \n !"
    message_boot2 = "Que voulez vous faire?"
    message_boot3 = "Consulter le bilan de santé"
    message_boot4 = "Voir les informations des patients"
    message_boot5 = "Ou entrer vos symptomes dans le formulaire"
    try:
        Message.objects.get(sender=robot, text=message_boot, receive=request.user)
    except:
        Message.objects.create(sender=robot, text=message_boot, receive=request.user, date_sender=date)
    try:
        Message.objects.get(sender=robot, text=message_boot2, receive=request.user)
    except:
        Message.objects.create(sender=robot, text=message_boot2, receive=request.user, date_sender=date)
    try:
        Message.objects.get(sender=robot, text=message_boot3, receive=request.user)
    except:
        Message.objects.create(sender=robot, text=message_boot3, receive=request.user, date_sender=date,lien=lien)
    try:
        Message.objects.get(sender=robot, text=message_boot4, receive=request.user)
    except:
        Message.objects.create(sender=robot, text=message_boot4, receive=request.user, date_sender=date,lien=lien1)
    try:
        Message.objects.get(sender=robot, text=message_boot5, receive=request.user)
    except:
        Message.objects.create(sender=robot, text=message_boot5, receive=request.user, date_sender=date)
    maladie = Malaria.objects.all()
    a = len(Message.objects.all())
    return render(request, 'chat.html', {
        'mess': Message.objects.filter(receive=request.user, sender=robot).order_by('date_sender') | Message.objects.filter(receive=robot,
                                                                                                    sender=request.user).order_by('date_sender') ,
        'robot': robot, 'a': a, 'symptomes': maladie})


def adminAddMalaria(request):
    palu = []

    context = {}
    mess = "pas trouver"
    if request.method == "POST":
        nom_m = request.POST.get('nom_m')
        symptomes = request.POST.get('symptomes')
        Malaria.objects.create(nom_m=nom_m, symptomes=symptomes)
        p = Malaria.objects.all()
        if symptomes in getcovid():
            return render(request, 'adminAddMalaria.html', {'symptomes': symptomes, 'p': p})
        else:
            print("pas trouver")

    return render(request, 'adminAddMalaria.html')


def info_patient(request):
    P = GetMalaria.objects.filter(user=request.user)
    p1 = User.objects.filter()
    p2 = Custumer.objects.filter(user=request.user)
    p3 = Prediction.objects.filter(nom_patient=f"{request.user}")
    p = Malaria.objects.all()
    if request.method == 'POST':
        countries = request.POST.getlist('countries[]')

    print(p3)
    a = request.user

    context = {'P': P, 'p1': p1, 'p2': p2, 'p3': p3, 'a': a}
    return render(request, 'info_patient.html', context)


def liste_consultation(request):
    p4 = Prediction.objects.all()

    p1 = User.objects.all()
    p2 = Custumer.objects.all()
    p3 = Prediction.objects.all()
    context = {'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4}
    return render(request, 'liste_consultation.html', context)


def logout_app(request):
    logout(request)
    return redirect('SingIn')
