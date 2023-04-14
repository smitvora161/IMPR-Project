from django.shortcuts import render,redirect
from .detection import FaceRecognition
from .forms import *
from django.contrib import messages
import pyttsx3

faceRecognition = FaceRecognition()

def home(request):
   
    return render(request,'home.html')


def register(request):
    if request.method == "POST":
        i = request.POST['fid']
        nm = request.POST['name']
        add = request.POST['address']
        ph = request.POST['phone']
        em = request.POST['email']
        img = request.FILES.get("im")
        form = UserProfile()
        form.face_id= i
        form.name = nm
        form.address = add
        form.phone = ph
        form.email = em
        form.image = img
        
        form.save()
        print("IN HERE")
        # engine = pyttsx3.init()
        # engine.say("SuceessFully registered")
        # engine.runAndWait()
        messages.success(request,"SuceessFully registered")
        addFace(request.POST['fid'])
        redirect('home')
   

    return render(request, 'register.html')

def addFace(face_id):
    face_id = face_id
    faceRecognition.faceDetect(face_id)
    faceRecognition.trainFace()
    return redirect('/')

def login(request):
    
    face_id = faceRecognition.recognizeFace()
    print(face_id)
    

    return redirect('greeting' ,str(face_id))

def Greeting(request,face_id):
    face_id = int(face_id)
    # engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[1].id)   
    # engine = pyttsx3.init()
    # engine.say("you are successfully login")
    # engine.runAndWait()
    context ={
        'user' : UserProfile.objects.get(face_id = face_id)
    }
    return render(request,'greeting.html',context=context)
