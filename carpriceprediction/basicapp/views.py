import pickle
from django.shortcuts import render
from pickle import load
with open('./saved models/random_forest.pkl','rb') as f:
    model = pickle.load(f)


def predictor(request):
    if request.method == 'POST':
        Yr = request.POST['Year']
        Year=2022-int(Yr)
        KMS = request.POST['KMS']
        Power = request.POST['Power']
        Owners = request.POST['Owners']
        if Owners=='Test_drive_car':
            Owner_testcar=1
            Owner_secondcar=0
            Owner_thirdcar=0
            Owner_fouth=0
        elif Owners=='Second Owner':
            Owner_testcar=0
            Owner_secondcar=1
            Owner_thirdcar=0
            Owner_fouth=0
        elif Owners=='Third Owner':
            Owner_testcar=0
            Owner_secondcar=0
            Owner_thirdcar=1
            Owner_fouth=0
        elif Owners=='Fouth & above Owners':
            Owner_testcar=0
            Owner_secondcar=0
            Owner_thirdcar=0
            Owner_fouth=1
        else:
            Owner_testcar=0
            Owner_secondcar=0
            Owner_thirdcar=0
            Owner_fouth=0
        Fuel = request.POST['Fuel']
        if Fuel=='Petrol':
            Fuel_petrol=1
            Fuel_Diesel=0
            Fuel_LPG=0
        elif Fuel=='Diesel':
            Fuel_petrol=0
            Fuel_Diesel=1
            Fuel_LPG=0
        elif Fuel=='LPG':
            Fuel_petrol=0
            Fuel_Diesel=0
            Fuel_LPG=1
        else:
            Fuel_petrol=0
            Fuel_Diesel=0
            Fuel_LPG=0
        Seller = request.POST['Seller']
        if Seller=='Individual':
            Seller_individual=1
            Seller_trustmark=0
        elif Seller=='Trustmarks_Dealer':
            Seller_individual=0
            Seller_trustmark=1
        else:
            Seller_individual=0
            Seller_trustmark=0
        Mileage = request.POST['Mileage']
        Engine = request.POST['Engine']
        Seats = request.POST['Seats']
        Transmission = request.POST['Transmission']
        if Transmission=='Manual':
            Transmission_Manual=1
        else:
            Transmission_Manual=0
        y_pred=model.predict([[Year,KMS,Mileage,Engine,Power,Seats,Fuel_Diesel,Fuel_LPG,Fuel_petrol,Seller_individual,Seller_trustmark,Transmission_Manual,Owner_fouth,Owner_secondcar,Owner_testcar,Owner_thirdcar]])
        y_temp=y_pred[0]
        return render(request,'index.html',{'result': y_temp})
    return render(request, 'index.html')




    


# Create your views here.
