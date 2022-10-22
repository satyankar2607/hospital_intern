from django.http import HttpResponse
from django.shortcuts import render
from hospital1.models import doctor, patient

# will store all emails of patients and doctors
all_email = []

# will store all usernames of patients and doctors
usernames = []

# importing all objects of module doctor
x = doctor.objects.raw('SELECT id,f_name,l_name,picture,username,emailed,pwd,cnf_pwd,address FROM hospital1_doctor')
doc_emails = []
doc_passwords = []

for i in x:
    doc_emails.append(i.emailed)
    doc_passwords.append(i.pwd)
    all_email.append(i.emailed)
    usernames.append(i.username)


# importing all objects of module patient
y = patient.objects.raw('SELECT id,f_name,l_name,picture,username,emailed,pwd,cnf_pwd,address FROM hospital1_patient')
pat_emails = []
pat_passwords = []
for i in y:
    pat_emails.append(i.emailed)
    pat_passwords.append(i.pwd)
    all_email.append(i.emailed)
    usernames.append((i.username))


def index(request):
    return render(request, 'index.html')

# action on index page form (taking details for registration)
def signup(request):
    entity = request.POST.get('entity')
    email = request.POST.get('email')
    password = request.POST.get('pwd')
    cnf_pwd = request.POST.get('cnf_pwd')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    address = request.POST.get('address')
    username = request.POST.get('username')
    picture = request.POST.get('picture')

    # checking if password and confirm password is same or not
    if password == cnf_pwd:
        # checking if username already exist or not
        if username not in usernames:
            # if user is a doctor
            if entity == "doctor":
                if email not in doc_emails:
                    savingdata = doctor(emailed=email,pwd=password,f_name=fname,l_name=lname,picture=picture,username=username,
                                        cnf_pwd=cnf_pwd,address=address)
                    savingdata.save()
                    return HttpResponse("Doctor is Registered")
                else:
                    return HttpResponse("Already Exist!!")
            # if user is a patient
            elif entity == "patient":
                if email not in pat_emails:
                    savingdata = patient(emailed=email, pwd=password,f_name=fname,l_name=lname,picture=picture,username=username,
                                        cnf_pwd=cnf_pwd,address=address)
                    savingdata.save()
                    return HttpResponse("Patient is Registered")
                else:
                    return HttpResponse("Already Exist!!")
            else:
                return HttpResponse("Please select type of user")
        else:
            return HttpResponse("username not availaible!Choose new")
    else:
        return HttpResponse("password and confirm password do not match")

def login(request):
    return render(request, 'login.html')

# action on login page form
def logch(request):
    email = request.POST.get('email')
    password = request.POST.get('pwd')
    r = doctor.objects.filter(emailed = email)
    o = patient.objects.filter(emailed = email)
    content ={"message":r}
    content1 = {"message":o}
    # checking if email is registered or not for doctor
    if email in doc_emails:
        a = doc_emails.index(email)
        # checking if password get matched or not for doctor
        if password == doc_passwords[a]:
            return render(request, 'doctor.html',content)
        else:
            return HttpResponse("Wrong Password!!")
    # checking if email is registered or not for patient
    elif email in pat_emails:
        a = pat_emails.index(email)
        # checking if password get matched or not for patient
        if password == pat_passwords[a]:
            return render(request, 'patient.html',content1)
        else:
            return HttpResponse("Wrong Password!!")
    else:
        return HttpResponse("Wrong email id!!")

