#Final Project (Lowe's Survey Questionnaire Form) - James Wilson

#Module 06 Project Status II - This project is still in development, but overall wanted to go ahead and get an early start. 

#This program is a Lowe's Survey Questionnaire Form that will be used to gather statistical information based on Lowe's customer inputs, attributes, attitudes, or actions based on a series of questions listed. The purspose is to gain feedback and see what Lowe's can improve towards it's business based on customer feedback. Therefore, this program will contain a series of questions that will relate towards Lowe's customer actions.

#Overall, I have completed the layout portion of the project. In terms of the order in which the questions will be displayed and users can input their opinions towards Lowe's based on their input.

#However, there is still work that needs to be done in terms of the style in which I want the GUI to appear as. The type of input options related to the questions, such as a dropdown menu, radio buttons, and a checkbox options to gain feedback.

import tkinter as tk

#Name Lists

name_list = []
email_list = []
age_list = []
affiliation_list = []
recommendation_list = []
experience_list = []
improvement_list = []
comment_list = []

#Application 
app= tk.Tk()
app.title("Lowe's Survey Form")
app.geometry("500x500")

#Labels 
name_label = tk.Label(app, text="Name: ")
email_label = tk.Label(app, text="Email: ")
age_label = tk.Label(app, text="Age: ")
affiliation_label = tk.Label(app, text="What is your current affiliation with Lowe's: ")
recommendation_label = tk.Label(app, text="Would you Recommend other to Lowe's? ")
experience_label = tk.Label(app, text="How is your experience shopping at Lowe's? ")
improvement_label = tk.Label(app, text="What would you like to see Lowe's improve on? (Check all that apply) ")
comment_label = tk.Label(app, text="Any comments or suggestions for this survey")

#Entry Fields
name_entry = tk.Entry(app)
email_entry = tk.Entry(app)
age_entry = tk.Entry(app)
affiliation_entry = tk.Entry(app)
recommendation_entry = tk.Entry(app)
experience_entry = tk.Entry(app)
improvement_entry = tk.Entry(app)
comment_entry = tk.Entry(app)

#Create the submission button
def submission_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    affiliation = affiliation_entry.get() #Will be a Dropdown Menu option
    recommendation = recommendation_entry.get() #Will be an Input-radio option
    experience = experience_entry.get() #Will be a Dropdown Menu option
    improvement = improvement_entry.get() #Will be a checkbox option
    comment = comment_entry.get() #Will be a comment section option

    name_list.append(name)
    email_list.append(email)
    age_list.append(age)
    affiliation_list.append(affiliation)
    recommendation_list.append(recommendation)
    experience_list.append(experience)
    improvement_list.append(improvement)
    comment_list.append(comment)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=1)

age_label.grid(row=2, column=0)
age_entry.grid(row=2, column=1)

affiliation_label.grid(row=3, column=0)
affiliation_entry.grid(row=3, column=1)

recommendation_label.grid(row=4, column=0)
recommendation_entry.grid(row=4, column=1)

experience_label.grid(row=5, column=0)
experience_entry.grid(row=5, column=1)

improvement_label.grid(row=6, column=0)
improvement_entry.grid(row=6, column=1)

comment_label.grid(row=7, column=0)
comment_entry.grid(row=7, column=1)

submission_button = tk.Button(app, text="Submit", command=submission_form)
submission_button.grid(row=8, columnspan=2)
#Run Application
app.mainloop()