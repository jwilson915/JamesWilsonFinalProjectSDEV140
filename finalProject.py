#Final Project (Lowe's Survey Questionnaire Form) - James Wilson

#For my final project

#I created a Survey Questionnaire Form based on the home improvement retail firm, Lowe's Home Improvement. The purpose of this project is to create a survey form to gather information based on Lowe's customer input, attributes, attitudes, or actions that spring from a series of questions listed. The purpose is to gain feedback from our customers to see what Lowe's can improve on in order to provide better service towards those who shop at Lowe's. The questions relate to the following areas:
    #A user's minor information: Name, E-Mail, and Age
    #Affilaiton with Lowe's: (Current Affiliation, Shopping Experience, Improvements)
    #Any comments or suggestions from customers
    #Submission of Survey Form

#Please take your time into taking this survey, Have a Lowe's Safe Day!


#Import Tkinter into Python Code
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import Toplevel, Tk
import tkinter as tk
import tkinter.font as tkFont


#Application Layout Itself
app= tk.Tk()
app.title("Lowe's Survey Form")
app.geometry("950x450")
app.configure(background="#305cde")

#The Labels that will be used for the Survey
    #Displays:
        #Text
        #Font
        #Background Color 
        #Font Color
heading_label = tk.Label(app, text="Lowe's Survey Form", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6" ) 
name_label= tk.Label(app, text="Name: ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
email_label = tk.Label(app, text="Email: ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
age_label = tk.Label(app, text="Age: ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
affiliation_label = tk.Label(app, text="What is your current affiliation with Lowe's: ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
recommendation_label = tk.Label(app, text="Would you Recommend Lowe's to others? ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
experience_label = tk.Label(app, text="How was your experience shopping at Lowe's? ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
improvement_label = tk.Label(app, text="What improvements would you like to see at Lowe's? (Check all that apply) ", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")
comment_label = tk.Label(app, text="Any comments or suggestions for this survey", font=("Ariel, Helvetica, sans-serif", 12), bg="#305cde", fg="#addae6")

#The entry fields related the labels
name_entry = tk.Entry(app) 
email_entry = tk.Entry(app)
age_entry = tk.Entry(app)
affiliation_entry = tk.Entry(app)
recommendation_entry = tk.Entry(app)
experience_entry = tk.Entry(app)
improvement_entry = tk.Entry(app)
comment_entry = tk.Entry(app)


#Create the submission form for the survey
def submission_form():
    #Create an empty list to display the survey results
    survey_results = []

    #The Title for Survey Results
    survey_results.append("Lowe's Survey Results: ")

    #The entries for the Survey Form
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

    #The values for the survey list
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

    #Print the Survey List (initally was set to create a program to gather statistical information on the form, However due to time constraints, for this project only, we are just going to print the results instead.)
    for items in survey_results:
        print(items)

#Submission Button Window (once the survey is complete)
    submission_button = messagebox.askquestion("Submit", "Are you ready to submit this form!")
    if submission_button == "yes":
        thank_you_window = Toplevel(app)
        thank_you_window.title("Thank You!")
        Label(thank_you_window, text="Thank you for your Response!").grid()
    else:
        messagebox.showerror("Submit No", "Submission Aboarded")

#Heading Label
heading_label.grid(row=0, column=1)

#Name Section (Text Entry)
name_label.grid(row=1, column=1)
name_entry.grid(row=1, column=2, columnspan=4, sticky= "ew")

#Email Section (Text Entry)
email_label.grid(row=2, column=1)
email_entry.grid(row=2, column=2,  columnspan=4, sticky= "ew")

#Age Section (Text Entry)
age_label.grid(row=4, column=1)
age_entry.grid(row=4, column=2,  columnspan=4, sticky= "ew")

#Affiliation Section (Dropdown menu 1)
affiliation_label.grid(row=7, column=1)
affiliation_label = ["None", "Customer", "Customer (with Lowe's Card)", "Lowe's Pro Customer or Member", "Employee (Current or Former)"]
selected_affiliation = tk.StringVar()
selected_affiliation.set("Select current affiliation")
affiliation_label = tk.OptionMenu(app, selected_affiliation, *affiliation_label)
affiliation_label.grid (row=7, column=2,  columnspan=4, sticky= "ew")
affiliation_label.config (bg="#addae6", fg="#305cde")

#Recommendation Section (Input radio button)
recommendation_label.grid(row=9, column=1)
recommendation_var = tk.StringVar()
recommendation_var.set("Yes")
recommendation_radio1=tk.Radiobutton(app, text="Yes", variable=recommendation_var, value="Yes", bg="#305cde", fg="#addae6")
recommendation_radio2=tk.Radiobutton(app, text="No", variable=recommendation_var, value="No", bg="#305cde", fg="#addae6")
recommendation_radio1.grid(row=9, column=2)
recommendation_radio2.grid(row=10, column=2)

#Experience Section (Dropdown menu 2)
experience_label.grid(row=11, column=1)
experience_label = ["Very Poor", "Poor", "Neutral", "Great", "Excellent"]
selected_affiliation = tk.StringVar()
selected_affiliation.set("Select an option")
experience_label = tk.OptionMenu(app, selected_affiliation, *experience_label)
experience_label.grid(row=11, column=2, columnspan=4, sticky= "ew")
experience_label.config (bg="#addae6", fg="#305cde")

#Improvement Section (Checkbox options, total 6)
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

#Three Buttons that will be used in this code
#Submit Button (To Submit the Survey)
submission_button = tk.Button(app, text="Submit", font=("Ariel, Helvetica, sans-serif", 10), bg="#addae6", fg="#305cde" , height=1, width=100, command=submission_form)
submission_button.grid(row=23, column=1, columnspan=2)

#Exit Function (To Exit the Survey)
def exit():
    app.destroy()

#Exit Button
exit_button = tk.Button(app, text="Exit", font=("Ariel, Helvetica, sans-serif", 10), bg="#ff0000", fg="#ffffff" , height=1, width=100, command=exit)
exit_button.grid(row=24, column=1, columnspan=2)

#Restart Button (To Restart the Survey)
def restart():
    #Clear all of the input fields
    name_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    age_entry.delete(0, 'end')
    affiliation_entry.delete(0, 'end')
    recommendation_entry.delete(0, 'end')
    experience_entry.delete(0, 'end')
    improvement_entry.delete(0, 'end')
    comment_entry.delete(0, 'end')

#Create the Restart Button (in case there is any mistakes or errors, you can restart the survey)
restart_button = tk.Button(app, text="Restart", height=1, width=100, command=restart)
restart_button.grid(row=26, column=1, columnspan=2)

#Run the Application
app.mainloop()
