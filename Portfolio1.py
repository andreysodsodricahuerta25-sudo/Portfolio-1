#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Code by Andrey S. Ricahuerta, BS Chemical Engineering 1A


# In[2]:


# Daily Sleep Calculator
"""This program asks the user for their total available hours and hobby durations. It computes the total hours spent and remaining sleep time for the night."""


# In[3]:


# Ask for the user's name and total available hours 
name = input("Enter your name: ")
total_hours = float(input("Enter total hours available in the day: "))

# Ask for the user's hobby durations
doom_scrolling = float(input("Enter hours spent Doom Scrolling: "))
studying = float(input("Enter hours spent Studying: "))
relapse = float(input("Enter hours spent on Relapse: "))
eating = float(input("Enter hours spent Eating: "))
chores = float(input("Enter hours spent on Chores: "))
personal_hygiene = float(input("Enter hours spent on Personal Hygiene: "))
basketball = float(input("Enter hours spent on Basketball: "))
reading_books = float(input("Enter hours spent Reading Books: "))
exercise = float(input("Enter hours spent on Exercise: "))
chatting = float(input("Enter hours spent Chatting with Friends and Family: "))
chess = float(input("Enter hours spent on Chess: "))
watching_tv = float(input("Enter hours spent Watching TV: "))


# In[5]:


# Compute the total hours spent and remaining sleep time
total_hobby_hours = (doom_scrolling + studying + relapse + eating + chores + personal_hygiene +
                     basketball + reading_books + exercise +
                     chatting + chess + watching_tv)
sleep_hours = total_hours - total_hobby_hours

# Display the daily sleep summary
print()
print("Daily Sleep Summary")
print("Name:", name)
print("Total hours available:", total_hours, "hours")
print("Doom Scrolling:", doom_scrolling, "hours")
print("Studying:", studying, "hours")
print("Relapse:", relapse, "hours")
print("Eating:", eating, "hours")
print("Chores:", chores, "hours")
print("Personal Hygiene:", personal_hygiene, "hours")
print("Basketball:", basketball, "hours")
print("Reading Books:", reading_books, "hours")
print("Exercise:", exercise, "hours")
print("Chatting with Friends and Family:", chatting, "hours")
print("Chess:", chess, "hours")
print("Watching TV:", watching_tv, "hours")
print("Total hours spent on hobbies:", total_hobby_hours, "hours")
print("Remaining sleep time:", sleep_hours, "hours")

