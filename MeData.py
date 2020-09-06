import math
import numpy as np
from tkinter import *
from functools import partial
import csv

def validateLogin():
    print("New Patient Data")
    print("Index Number: ", index.get())
    print("Age: ", age.get())
    if sex.get() == False:
        print("Sex: Male")
    else:
        print("Sex: Female")
    print("Height: ", height.get())
    print("Weight: ", weight.get())
    #current conditions
    if injury.get()==1 and pain.get()==1:
        print("Primary Medical Condition: Traumatic injury and chronic pain")
    elif injury.get()==1 and pain.get()==0:
        print("Primary Medical Condition: Traumatic injury")
    elif injury.get()==0 and pain.get()==1:
        print("Primary Medical Condition: Chronic Pain")
    elif injury.get()==0 and pain.get()==0:
        print("Primary Medical Condition: Neither injury nor pain")
    #previous conditions
    prevOut = "Previous/Ongoing Conditions:"
    if asthma.get()==True:
        prevOut+=" Asthma/Breathing Issues "
    if coma.get()==True:
        prevOut+=" Coma "
    if aids.get()==True:
        prevOut+=" HIV/AIDS "
    print(prevOut)
    #ongoing meds
    medsOut = "Other Ongoing Medication: "
    if antibiotics.get()==True:
        medsOut+=" Antibiotics "
    if antifungal.get()==True:
        medsOut+=" Antifungal Medication "
    if mental.get()==True:
        medsOut+=" Psychiatric Drugs "
    if relaxant.get()==True:
        medsOut+=" Muscle Relaxant "
    if hivmed.get()==True:
        medsOut+=" HIV/AIDS Medication "
    if sedatives.get()==True:
        medsOut+=" Sedatives "
    print(medsOut)
    #substances
    subsOut = "Substance(s) Used:"
    if alcohol.get()==True:
        subsOut+=" Alcohol "
    if tobacco.get()==True:
        subsOut+=" Tobacco "
    if marijuana.get()==True:
        subsOut+=" Marijuana "
    if street.get()==True:
        subsOut+=" Street Drugs "
    print(subsOut)
    return

def close_window():
    tkWindow.destroy()

def new_window():
    resultWindow = Tk()

#window
tkWindow = Tk()  
tkWindow.geometry('700x280')  
tkWindow.title('MeData New Patient Portal')

#Patient index
indexLabel = Label(tkWindow, text="Patient Number").grid(row=0, column=0)
index = IntVar()
indexEntry = Entry(tkWindow, textvariable=index).grid(row=0, column=1)  

#Age
ageLabel = Label(tkWindow,text="Age").grid(row=1, column=0)  
age = IntVar()
ageEntry = Entry(tkWindow, textvariable=age).grid(row=1, column=1)  

#Sex
sexLabel = Label(tkWindow,text="Sex").grid(row=2, column=0)  
sex = BooleanVar()
r1 = Radiobutton(tkWindow, text='Male', variable=sex, value=False).grid(row=2, column=1)
r2 = Radiobutton(tkWindow, text='Female', variable=sex, value=True).grid(row=2, column=2)


#Height
heightLabel = Label(tkWindow,text="Height").grid(row=4, column=0)  
height = IntVar()
heightEntry = Entry(tkWindow, textvariable=height).grid(row=4, column=1)

#Weight
weightLabel = Label(tkWindow,text="Weight").grid(row=5, column=0)  
weight = IntVar()
weightEntry = Entry(tkWindow, textvariable=weight).grid(row=5, column=1)

#Current condition
conditionLabel = Label(tkWindow,text="Current Medical Condition").grid(row=6, column=0)  
injury = IntVar()
pain = IntVar()
c1 = Checkbutton(tkWindow, text='Traumatic Injury', variable=injury, onvalue=1, offvalue=0).grid(row=6, column=1)
c2 = Checkbutton(tkWindow, text='Chronic Pain', variable=pain, onvalue=1, offvalue=0).grid(row=6, column=2)

#Previous/ongoing conditions
prevLabel = Label(tkWindow,text="Previous/Ongoing Conditions").grid(row=7, column=0)  
asthma = BooleanVar()
coma = BooleanVar()
aids = BooleanVar()
c3 = Checkbutton(tkWindow, text='Asthma/Breathing Issues', variable=asthma, onvalue=True, offvalue=False).grid(row=7, column=1)
c4 = Checkbutton(tkWindow, text='Coma', variable=coma, onvalue=True, offvalue=False).grid(row=7, column=2)
c5 = Checkbutton(tkWindow, text='HIV/AIDS', variable=aids, onvalue=True, offvalue=False).grid(row=7, column=3)

#other ongoing medication
otherLabel = Label(tkWindow,text="Other Ongoing Medications").grid(row=8, column=0)  
antibiotics = BooleanVar()
antifungal = BooleanVar()
mental = BooleanVar()
relaxant = BooleanVar()
hivmed = BooleanVar()
sedatives = BooleanVar()
c6 = Checkbutton(tkWindow, text='Antibiotics', variable=antibiotics, onvalue=True, offvalue=False).grid(row=8, column=1)
c7 = Checkbutton(tkWindow, text='Antifungal Medication', variable=antifungal, onvalue=True, offvalue=False).grid(row=8, column=2)
c8 = Checkbutton(tkWindow, text='Psychiatric Drugs', variable=mental, onvalue=True, offvalue=False).grid(row=8, column=3)
c9 = Checkbutton(tkWindow, text='Muscle Relaxants', variable=relaxant, onvalue=True, offvalue=False).grid(row=9, column=1)
c10 = Checkbutton(tkWindow, text='AIDS/HIV Medication', variable=hivmed, onvalue=True, offvalue=False).grid(row=9, column=2)
c11 = Checkbutton(tkWindow, text='Sedatives', variable=sedatives, onvalue=True, offvalue=False).grid(row=9, column=3)

#substances
substanceLabel = Label(tkWindow,text="Substance Use").grid(row=10, column=0)  
alcohol = BooleanVar()
tobacco = BooleanVar()
marijuana = BooleanVar()
street = BooleanVar()
c11 = Checkbutton(tkWindow, text='Alcohol', variable=alcohol, onvalue=True, offvalue=False).grid(row=10, column=1)
c12 = Checkbutton(tkWindow, text='Tobacco', variable=tobacco, onvalue=True, offvalue=False).grid(row=10, column=2)
c13 = Checkbutton(tkWindow, text='Marijuana', variable=marijuana, onvalue=True, offvalue=False).grid(row=10, column=3)
c14 = Checkbutton(tkWindow, text='Street Drugs', variable=street, onvalue=True, offvalue=False).grid(row=10, column=4)

#login button
submitButton = Button(tkWindow, text="Submit", command=validateLogin).grid(row=11, column=0)
resultButton = Button(tkWindow, text="Close", command=close_window).grid(row=11, column=1)

tkWindow.mainloop()


#backend
def countSetBits(num): 
  
     # convert given number into binary 
     # output will be like bin(11)=0b1101 
     binary = bin(num) 
  
     # now separate out all 1's from binary string 
     # we need to skip starting two characters 
     # of binary string i.e; 0b 
     setBits = [ones for ones in binary[2:] if ones=='1'] 
       
     return len(setBits)
 
"""
p_age = np.uint8(18);
p_weight = np.uint8(140);
p_height = np.uint8(70);
p_sex = bool(1);
p_traum_inj = bool(0);
p_chron_pain = bool(1);
p_asthma = bool(0);
p_coma = bool(0);
p_HIV = bool(0);
p_antibio = bool(1);
p_fung_med = bool(0);
p_mental_ill = bool(1);
p_muscle_rel = bool(0);
p_HIV_meds = bool(0);
p_sed = bool(0); 
p_alc = bool(0);
p_tob = bool(1);
p_mar = bool(0);
p_street = bool(0);
"""
p_age = np.uint8(age.get());
p_weight = np.uint8(weight.get());
p_height = np.uint8(height.get());
p_sex = bool(sex.get());
p_traum_inj = bool(injury.get());
p_chron_pain = bool(pain.get());
p_asthma = bool(asthma.get());
p_coma = bool(coma.get());
p_HIV = bool(aids.get());
p_antibio = bool(antibiotics.get());
p_fung_med = bool(antifungal.get());
p_mental_ill = bool(mental.get());
p_muscle_rel = bool(relaxant.get());
p_HIV_meds = bool(hivmed.get());
p_sed = bool(sedatives.get()); 
p_alc = bool(alcohol.get());
p_tob = bool(tobacco.get());
p_mar = bool(marijuana.get());
p_street = bool(street.get());


p_stream1 = np.uint8(p_sex + (p_traum_inj<<1) + (p_chron_pain<<2) + (p_asthma<<3) + (p_coma<<4) + (p_HIV<<5) + (p_antibio<<6) + (p_fung_med<<7))
p_stream2 = np.uint8(p_mental_ill + (p_muscle_rel<<1) + (p_HIV_meds<<2) + (p_sed<<3) + (p_alc<<4) + (p_tob<<5) + (p_mar<<6) + (p_street<<7))

#data = np.array([[0, 0, 0, 1, 18, 140, 70, 69, 33, 50], [0, 0, 0, 2, 24, 155, 74, 68, 21, 32]], dtype=np.uint8)
data = np.empty([113153, 10], dtype=np.uint8)
with open('PatientData.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    i = 0
    for row in csv_reader:
        if i == 0:
            #print("Column names are:")
            #for j in row:
            #    print(j, " ")
            i += 1
        
        else:
            data[i-1, 0] = np.uint8(int(row[0])>>24 & 255)
            data[i-1, 1] = np.uint8(int(row[0])>>16 & 255)
            data[i-1, 2] = np.uint8(int(row[0])>>8 & 255)
            data[i-1, 3] = np.uint8(int(row[0]) & 255)
            data[i-1, 4] = np.uint8(int(row[1]))
            data[i-1, 5] = np.uint8(int(row[2]))
            data[i-1, 6] = np.uint8(int(row[3]))
            byte1 = np.uint8(0)
            byte2 = np.uint8(0)
            for j in range(4,12,1):
                bit = int(row[j])
                byte1 += np.uint8(bit<<(j-4))
            for j in range(12,20,1):
                bit = int(row[j])
                byte2 += np.uint8(bit<<(j-12))
            data[i-1, 7] = byte1
            data[i-1, 8] = byte2
            data[i-1, 9] = np.uint8(row[20])
            i += 1

matches = 0
dosageSum = 0

for row in data:
    a_diff = abs(int(row[4]) - int(p_age)) > 5;
    w_diff = abs(int(row[5]) - int(p_weight)) > 20;
    h_diff = abs(int(row[6]) - int(p_height)) > 3;
    xorv1 = row[7]^p_stream1;
    xorv2 = row[8]^p_stream2;
    boolv1 = countSetBits(xorv1);
    boolv2 = countSetBits(xorv2);
    diffN = (a_diff + w_diff + h_diff + boolv1 + boolv2);
    
    if (diffN < 3):
        print("\nPatient ID: ", ((row[0]<<24) + (row[1]<<16) + (row[2]<<8) + row[3]))
        if (diffN == 0):
            print("Identical")
        else:
            print("Differences:")
            if (a_diff):
                print("Age - ",row[4]," years")
            if (w_diff):
                print("Weight - ",row[5]," lbs")
            if (h_diff):
                print("Height - ",row[6]," in")
            if (xorv1):
                if (xorv1 & 1):
                    if (row[7] & 1):
                        print("Female")
                    else:
                        print("Male")
                if ((xorv1>>1) & 1):
                    if ((row[7]>>1) & 1):
                        print("Has Traumatic Injury")
                    else:
                        print("No Traumatic Injury")
                if ((xorv1>>2) & 1):
                    if ((row[7]>>2) & 1):
                        print("Has Chronic Pain")
                    else:
                        print("No Chronic Pain")
                if ((xorv1>>3) & 1):
                    if ((row[7]>>3) & 1):
                        print("Has Asthma or Other Breathing Issues")
                    else:
                        print("No Asthma or Other Breathing Issues")
                if ((xorv1>>4) & 1):
                    if ((row[7]>>4) & 1):
                        print("In Coma")
                    else:
                        print("Not in Coma")
                if ((xorv1>>5) & 1):
                    if ((row[7]>>5) & 1):
                        print("Has HIV/AIDS")
                    else:
                        print("No HIV/AIDS")
                if ((xorv1>>6) & 1):
                    if ((row[7]>>6) & 1):
                        print("Taking Antibiotics")
                    else:
                        print("Not Taking Antibiotics")
                if ((xorv1>>7) & 1):
                    if ((row[7]>>7) & 1):
                        print("Taking Antifungal Medication")
                    else:
                        print("Not Taking Antifungal Medication")
            if (xorv2):
                if (xorv2 & 1):
                    if (row[8] & 1):
                        print("Taking Psychiatric Medication")
                    else:
                        print("Not Taking Psychiatric Medication")
                if ((xorv2>>1) & 1):
                    if ((row[8]>>1) & 1):
                        print("Taking Muscle Relaxants")
                    else:
                        print("Not Taking Muscle Relaxants")
                if ((xorv2>>2) & 1):
                    if ((row[8]>>2) & 1):
                        print("Taking HIV Medication")
                    else:
                        print("Not Taking HIV Medication")
                if ((xorv2>>3) & 1):
                    if ((row[8]>>3) & 1):
                        print("Taking Sedatives")
                    else:
                        print("Not Taking Sedatives")
                if ((xorv2>>4) & 1):
                    if ((row[8]>>4) & 1):
                        print("Drinks Alcohol")
                    else:
                        print("Does Not Drink Alcohol")
                if ((xorv2>>5) & 1):
                    if ((row[8]>>5) & 1):
                        print("Uses Tobacco")
                    else:
                        print("Does Not Use Tobacco")
                if ((xorv2>>6) & 1):
                    if ((row[8]>>6) & 1):
                        print("Uses Marijuana")
                    else:
                        print("Does Not Use Marijuana")
                if ((xorv2>>7) & 1):
                    if ((row[8]>>7) & 1):
                        print("Uses Street Drugs")
                    else:
                        print("Does Not Use Street Drugs")
        print("Prescription:",row[9],"mg")
        matches += 1
        dosageSum += row[9]
#print recommended dosage
avgDose = dosageSum/matches
recDose = 0
if 15<=avgDose<20:
    recDose = 15
elif 70<=avgDose<80:
    recDose = 60
else:
    recDose = 10*math.floor(avgDose/10)
print("\nThe recommended dose for patient no. " + str(index.get()) + " is " + str(recDose) + " mg.")
    
