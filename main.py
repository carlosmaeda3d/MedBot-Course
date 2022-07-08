welcome_prompt = "Welcome doctor, what can I help with today?\n -To list all patients, press 1\n -To run a diagnosis," \
                 "press 2\n -To quit, press q\n"

name_prompt = "What is the patients name?\n"

appearance_prompt = "How is the patient's general appearance?\n - 1: Normal Appearance\n - 2: Irritable or " \
                    "lethargic\n"

eye_prompt = "How are the patients eyes?\n - 1: Eyes normal or slightly sunken\n - 2: Eyes very sunken\n"

skin_prompt = "How is the patient's skin when you pinch it?\n - 1: Normal skin pinch\n - 2: Slow skin pinch\n"

severe_dehydration = "Severe Dehydration"
some_dehydration = "Some Dehydration"
no_dehydration = "No Dehydration"

error_message = "Could not save data. Invalid name or diagnosis format"

patients_and_diagnosis = [
    "Mike - Severe Dehydration",
    "John - Some Dehydration",
    "Monica - No Dehydration",
]

def list_patients():
    for patient in patients_and_diagnosis:
        print(patient)

def save_new_diagnosis(name, diagnosis):
    #checking to make sure name & diagnosis is in correct format
    if name == "" or diagnosis == "":
        print(error_message)
        return

    final_diagnosis = name + " - " + diagnosis
    patients_and_diagnosis.append(final_diagnosis)
    print("Final Diagnosis:", final_diagnosis, "\n")

def assess_skin(skin):
    if skin == "1":
        return some_dehydration
    elif skin == "2":
        return severe_dehydration
    else:
        return ""

def assess_eyes(eyes):
    if eyes == "1":
        return no_dehydration
    elif eyes == "2":
        return severe_dehydration
    else:
        return ""

def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        eyes = input(eye_prompt)
        return assess_eyes(eyes)
    elif appearance == "2":
        skin = input(skin_prompt)
        return assess_skin(skin)
    else:
        return ""

def start_new_diagnosis():
    name = input(name_prompt)
    diagnosis = assess_appearance()
    save_new_diagnosis(name, diagnosis)

def main():

    while(True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            return

main()

def test_assess_skin():
    print(assess_skin("1") == some_dehydration)
    print(assess_skin("2") == severe_dehydration)
    print(assess_skin("") == "")

#test_assess_skin()

def test_assess_eyes():
    print(assess_eyes("1") == no_dehydration)
    print(assess_eyes("2") == severe_dehydration)
    print(assess_eyes("") == "")

#test_assess_eyes()

def test_appearance():
    print(assess_appearance())

#test_appearance()
