#Final Project (Lowe's Survey Questionnaire Form) - James Wilson


from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import Toplevel, Tk
import tkinter as tk
import tkinter.font as tkFont


#Application 
app= tk.Tk()
app.title("Lowe's Survey Form")
app.geometry("950x400")
app.configure(background="#305cde")

#Labels 
heading_label = tk.Label(app, text="Lowe's Survey Form", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6" )
name_label= tk.Label(app, text="Name: ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
email_label = tk.Label(app, text="Email: ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
age_label = tk.Label(app, text="Age: ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
affiliation_label = tk.Label(app, text="What is your current affiliation with Lowe's: ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
recommendation_label = tk.Label(app, text="Would you Recommend Lowe's to others? ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
experience_label = tk.Label(app, text="How was your experience shopping at Lowe's? ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
improvement_label = tk.Label(app, text="What improvements would you like to see at Lowe's? (Check all that apply) ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
comment_label = tk.Label(app, text="Any comments or suggestions for this survey", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")

#Entry Fields
name_entry = tk.Entry(app) 
email_entry = tk.Entry(app)
age_entry = tk.Entry(app)
affiliation_entry = tk.Entry(app)
recommendation_entry = tk.Entry(app)
experience_entry = tk.Entry(app)
improvement_entry = tk.Entry(app)
comment_entry = tk.Entry(app)


#Create the submission 
def submission_form():
    #Empty List
    survey_results = []

    #Title for Survey Results
    survey_results.append("Lowe's Survey Results: ")


    #Values of the Survey
    name = name_entry.get() #Text-entry option
    email = email_entry.get() #Text-entry option
    age = age_entry.get() #Text-entry option
    affiliation = selected_affiliation.get() #Dropdown Menu option
    recommendation = recommendation_var.get() #Input-radio option
    experience = selected_affiliation.get() #Dropdown Menu option
    improvements = [
        ("Better Service (Both Customer & Pro)", improvement_var1),
        ("Special Pricing", improvement_var2), 
        ("Free Delivery & Installation", improvement_var3), 
        ("Credit Cards (MyLowesRewards, Pro, MVP, Business Rewards, etc.)", improvement_var4), 
        ("Vendor Seminars on New Products", improvement_var5),
        ("Contractor Referrals", improvement_var6)
] 
    improvement = [text for text, var in improvements if var.get() == 1]#Checkbox option
    comment = comment_entry.get() #Comment section option

    #Add values to the list
    survey_results.append("Name: ")
    survey_results.append([name])
    survey_results.append("E-Mail: ")
    survey_results.append([email])
    survey_results.append("Age: ")
    survey_results.append([age])
    survey_results.append("Affiliation: ")
    survey_results.append([affiliation])
    survey_results.append("Recommendation: ")
    survey_results.append([recommendation])
    survey_results.append("Experience: ")
    survey_results.append([experience])
    survey_results.append("Improvement: ")
    survey_results.append([improvement])
    survey_results.append("Comment: ")
    survey_results.append([comment])

    #Print the Survey List
    for items in survey_results:
        print(items)

#Submission Button Window
    submission_button = messagebox.askquestion("Submit", "Are you ready to submit this form!")
    if submission_button == "yes":
        thank_you_window = Toplevel(app)
        thank_you_window.title("Thank You!")
        Label(thank_you_window, text="Thank you for your Response!").grid()
    else:
        messagebox.showerror("Submit No", "Submission Aboarded")


#Heading
heading_label.grid(row=0, column=1)

#Name Section
name_label.grid(row=1, column=1)
name_entry.grid(row=1, column=2, columnspan=4, sticky= "ew")

#Email Section
email_label.grid(row=2, column=1)
email_entry.grid(row=2, column=2,  columnspan=4, sticky= "ew")

#Age Section
age_label.grid(row=4, column=1)
age_entry.grid(row=4, column=2,  columnspan=4, sticky= "ew")

#Affiliation Section
affiliation_label.grid(row=7, column=1)
affiliation_label = ["None", "Customer", "Customer (with Lowe's Card)", "Lowe's Pro Customer or Member", "Employee (Current or Former)"]
selected_affiliation = tk.StringVar()
selected_affiliation.set("Select current affiliation")
affiliation_label = tk.OptionMenu(app, selected_affiliation, *affiliation_label)
affiliation_label.grid (row=7, column=2,  columnspan=4, sticky= "ew")
affiliation_label.config (bg="#addae6", fg="#305cde")

#Recommendation Section
recommendation_label.grid(row=9, column=1)
recommendation_var = tk.StringVar()
recommendation_var.set("Yes")
recommendation_radio1=tk.Radiobutton(app, text="Yes", variable=recommendation_var, value="Yes", bg="#305cde", fg="#addae6")
recommendation_radio2=tk.Radiobutton(app, text="No", variable=recommendation_var, value="No", bg="#305cde", fg="#addae6")
recommendation_radio1.grid(row=9, column=2)
recommendation_radio2.grid(row=10, column=2)

#Experience Section
experience_label.grid(row=11, column=1)
experience_label = ["Very Poor", "Poor", "Neutral", "Great", "Excellent"]
selected_affiliation = tk.StringVar()
selected_affiliation.set("Select an option")
experience_label = tk.OptionMenu(app, selected_affiliation, *experience_label)
experience_label.grid(row=11, column=2, columnspan=4, sticky= "ew")
experience_label.config (bg="#addae6", fg="#305cde")

#Improvement Section
improvement_label.grid(row=13, column=1)
improvement_var1 = tk.IntVar()
improvement_var2 =tk.IntVar()
improvement_var3 = tk.IntVar()
improvement_var4 =tk.IntVar()
improvement_var5 = tk.IntVar()
improvement_var6 =tk.IntVar()
improvement_checkbox1 = tk.Checkbutton(app, text="Better Service (Both Customer & Pro)",  bg="#305cde", fg="#addae6", variable=improvement_var1)
improvement_checkbox2 = tk.Checkbutton(app, text="Special Pricing",  bg="#305cde", fg="#addae6", variable=improvement_var2)
improvement_checkbox3 = tk.Checkbutton(app, text="Free Delivery & Installation",  bg="#305cde", fg="#addae6", variable=improvement_var3)
improvement_checkbox4 = tk.Checkbutton(app, text="Credit Cards (MyLowesRewards, Pro, MVP, Business Rewards, etc.)", bg="#305cde", fg="#addae6",variable=improvement_var4)
improvement_checkbox5 = tk.Checkbutton(app, text="Vendor Seminars on New Products",  bg="#305cde", fg="#addae6", variable=improvement_var5)
improvement_checkbox6 = tk.Checkbutton(app, text="Contractor Referrals", bg="#305cde", fg="#addae6", variable=improvement_var6)
improvement_checkbox1.grid(row=14, column=1)
improvement_checkbox2.grid(row=14, column=2)
improvement_checkbox3.grid(row=15, column=1)
improvement_checkbox4.grid(row=15, column=2)
improvement_checkbox5.grid(row=16, column=1)
improvement_checkbox6.grid(row=16, column=2)


#Comment Section
comment_label.grid(row=21, column=1)
comment_entry.grid(row=21, column=2,  columnspan=4, sticky= "ew")

#Submit Button
submission_button = tk.Button(app, text="Submit", font=("Ariel, Helvetica, sans-serif", 10), bg="#addae6", fg="#305cde" , height=1, width=100, command=submission_form)
submission_button.grid(row=23, column=1, columnspan=2)


app.mainloop()
