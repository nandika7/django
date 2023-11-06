from django.shortcuts import render
from django.http import HttpResponse
import pickle
from .models import User, HealthDetails, Doctor

def home(request):
    return render(request, "myapp/home.html")

def diabetes(request):
    return render(request, "myapp/diabetes.html")

def register(request):
    if request.method == "POST":
        user_type = request.POST.get('user_type')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if user_type == 'doctor':
            specialization = request.POST.get('specialization')
            years_of_experience = request.POST.get('years_of_experience')
            doctor = Doctor(name = name, email = email, password = password, specialization = specialization, years_of_experience = years_of_experience, rating = 5)

            existing_doctor = Doctor.objects.get(email = email)
            
            if existing_doctor is None:
                doctor.save()
            else:
                return HttpResponse("A Doctor already exists with this email!")

        else:
            age = int(request.POST.get('age'))
            gender_value = request.POST.get('gender')

            user = User(age=age, gender=gender_value, name=name, email=email, password=password)

            existing_user = User.objects.get(email = email)
            
            if existing_user is None:
                user.save()
            else:
                return HttpResponse("User already exists with this email!")
        

    if 'user_id' in request.session:
        logged_in_user = User.objects.get(id=request.session['user_id'])
        return render(request, "myapp/registration_form.html", {
            "name": logged_in_user.name
        })
    
    return render(request, "myapp/registration_form.html")


def update_health_details(request):
    if request.method == "POST":
        age = int(request.POST.get('age'))
        pregnancies = int(request.POST.get('pregnancies'))
        glucose = int(request.POST.get('glucose'))
        bloodPressure = int(request.POST.get('bloodPressure'))
        skinThickness = int(request.POST.get('skinThickness'))
        insulin = int(request.POST.get('insulin'))
        bmi = int(request.POST.get('bmi'))
        diabetesPedigreeFunction = int(request.POST.get('diabetesPedigreeFunction'))

        user_logged_in_id = request.session['user_id']
        user_logged_in = User.objects.get(pk=user_logged_in_id)
        health_details = HealthDetails(
            user=user_logged_in,
            age=age,
            pregnancies=pregnancies,
            glucose=glucose,
            blood_pressure=bloodPressure,
            skin_thickness=skinThickness,
            insulin=insulin,
            bmi=bmi,
            diabetes_pedigree_function=diabetesPedigreeFunction,
            is_diabetic=0
        )

        health_details.save()

        return HttpResponse("User details saved")

    return render(request, "myapp/update_health_details.html")

def find_doctors(request):
    if request.method == "POST":
        years_of_experience = request.POST.get('years_of_experience')
        rating = request.POST.get('rating')
        specialization = request.POST.get('specialization')
        
        list_doctors = Doctor.objects.filter()
        #Consider filtering rating and years_of_experience > than
        list_doctors = list_doctors.filter(years_of_experience=years_of_experience)
        list_doctors = list_doctors.filter(rating=rating)
        list_doctors = list_doctors.filter(specialization=specialization)

def login(request):
    error_message = None

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        list_users = User.objects.filter(email=email)
        user = list_users.first()

        if user is not None:
            if password == user.password:
                request.session["user_id"] = user.id
                return render(request, "myapp/login_success.html")
            else:
                error_message = "Invalid Password!"
        else:
            error_message = "User does not exist"

    error = {
        "error_message": error_message
    }

    return render(request, "myapp/login_form.html", error)


def logout(request):
    del request.session["user_id"]
    return render(request, "myapp/login_form.html")


def predict_diabetes(request):
    if request.method == "POST":
        age = int(request.POST.get('age'))
        pregnancies = int(request.POST.get('pregnancies'))
        glucose = int(request.POST.get('glucose'))
        bloodPressure = int(request.POST.get('bloodPressure'))
        skinThickness = int(request.POST.get('skinThickness'))
        insulin = int(request.POST.get('insulin'))
        bmi = int(request.POST.get('bmi'))
        diabetesPedigreeFunction = int(request.POST.get('diabetesPedigreeFunction'))
        inputdata = [pregnancies, glucose, bloodPressure, skinThickness, insulin, bmi, diabetesPedigreeFunction, age]

        with open("myapp/diabetes_model.pickle", "rb") as f:

            diamodel = pickle.load(f)

        diaoutcome = diamodel.predict([inputdata])

        data = {
            "outcome": diaoutcome[0]
        }

        return render(request, "myapp/welcome.html", data)
    
    return render(request, "myapp/predict_diabetes.html")


def about_us(request):
    print("Sameer")
    return render(request, "myapp/about_us.html")

def demo(request):
    peoples = [
        {'name': 'ABC', 'age': 19},
        {'name': 'df', 'age': 91},
        {'name': 'vgsd', 'age': 39},
        {'name': 'dbvhd', 'age': 14}
    ]
    vegetables = [
        'brocolli', 'carrot', 'lettuce'
    ]

    data = {
        'peoples': peoples,
        'vegetables': vegetables
    }

    return render(request, "myapp/demo.html", data)