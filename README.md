AEC Educational Platform — OOP Rewrite

A full rewrite of my Tkinter learning platform for elementary students (Grades 1–6), restructured around classes instead of procedural code.

Original version: aec-educational-platform

Why rewrite it

The first version worked, but adding anything meant touching several unrelated functions, and the application state was scattered across the file. I rewrote it to find out whether object-oriented design actually solved that or just moved it somewhere else.

It did solve it, in one specific way I did not expect: [FILL — one concrete sentence. Example: "adding a new exercise type went from editing four functions to writing one subclass."]

What changed
	Version 1	This version
Structure	Procedural, [FILL: single file? a few modules?]	Classes: [FILL: list your actual class names, e.g. User, Student, Teacher, Exercise, Session]
State	[FILL: how it was held before]	Held on the objects that own it
Adding an exercise type	[FILL]	[FILL]
What it does
Student and teacher roles with separate views
Exercises organised by grade level (1–6)
Score tracking and session history
Tech
	
Language	Python 3
GUI	Tkinter
Design	Object-oriented: [FILL: inheritance? composition? name what you actually used]
Data storage	[FILL]
Interface language	French
Running it
bash
git clone https://github.com/angelb-47/aec-educational-platform-oop.git
cd aec-educational-platform-oop
python [FILL: entry point]
Screenshots

[FILL: 2 screenshots.]

What I would change next
[FILL: an honest limitation you can defend for three minutes in an interview.]
Status

Personal rewrite, [FILL: month/year]. Not actively maintained.
