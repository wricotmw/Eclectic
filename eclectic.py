'''
20/11/22 as per the live model with nine total and pdf report

added error for date and round

23/1/22 modify reportlab output 
24/11/22 transfer to new_eclectic
26/11/22 start to create ammendment - new window
1/12/22 ammendment works in treeview and tv data can be collected in a list
3/12/22 update to round table and saved to eclectic_round_update in security

3/12/22 select rounds by name and use max to get best scores
4/12/22 write ammended totals to database
26/1/24 Added the use of ttkbootsttrap to enhance the appearance of the program
		Added the functionality to clear all scores  and the possibility to clear names.
		Created executable to  be tested elsewhere.
		Save a copy of the file to 

'''


# eclectic golf test
import tkinter as tk
from tkinter import *
import sqlite3
from sqlite3 import Error
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

from ttkbootstrap.constants import *
import ttkbootstrap as tb 
from ttkbootstrap.scrolled import ScrolledText


from ttkbootstrap.tableview import Tableview
#from tkinter.ttk import *
#root = tk.Tk()

root=tb.Window(themename="terry")
root.geometry("1600x1000")
root.title("Eclectic")

#Change the default Font that will affect in all the widgets
root.option_add( "*font", "Helvetica 10" )
conn = sqlite3.connect('eclectic.db')




#called from insert round to see if golfer exists in totals if not
# call insert_golfer if exists call insert_round

def check_golfer():
	if  g_round.get() == "" or g_date.entry.get() == "":
		messagebox.showerror('Input Error', 'Error: You Must Enter Round and Date!')
	else:
		n = g_name.get()
		cur = conn.cursor()
		cur.execute("SELECT name from totals where name=?", (n,))
		data = cur.fetchall()
		if not data:
			print('not found')
			insert_golfer()
		else:
			print('found')
			insert_round()

# --------------------------------------------------------------------------------		

#called if golfer does not exist in totals therefore the score is the first and can be 
# inserted ito totals  
def insert_golfer():
	

	cursor = conn.cursor()

	sql = """INSERT INTO totals(name, hole1, hole2, hole3, hole4, hole5, hole6, hole7, hole8, hole9, hole10, 
		hole11, hole12, hole13, hole14, hole15, hole16, hole17, hole18, total)
	VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""

	x = g_name.get()
	a = g_score1.get()
	b = g_score2.get()
	c = g_score3.get()
	d = g_score4.get()
	e = g_score5.get()
	f = g_score6.get()
	g = g_score7.get()
	h = g_score8.get()
	i = g_score9.get()
	j = g_score10.get()
	k = g_score11.get()
	l = g_score12.get()
	m = g_score13.get()
	n = g_score14.get()
	o = g_score15.get()
	p = g_score16.get()
	q = g_score17.get()
	r = g_score18.get()
	y = int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) + int(h) + int(i) + int(j) + int(k) + int(l) + int(m) + int(n) + int(o) + int(p) + int(q) + int(r)

	cursor.execute(sql, (x, int(a), int(b), int(c), int(d), int(e), int(f), int(g), int(h), int(i), int(j), int(k), int(l), int(m), int(n), int(o), int(p), int(q), int(r), int(y)))


	print("insert")

	insert_round()
	conn.commit()
	#conn.close()

# -------------------------------------------------------------------------




#called if golfer exists in totals or from insert golfer
# This function then inserts the round and performs the check against previous totals
# If the score hole by hole is better then the total is updated

def insert_round():
	# insert the scores into the round database

	cursor = conn.cursor()

	sql = """INSERT INTO round(round_num, round_date,name,hole1, hole2, hole3, hole4, hole5, hole6, hole7, hole8, hole9, hole10, 
		hole11, hole12, hole13, hole14, hole15, hole16, hole17, hole18, total)
	VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
	num = g_round.get()
	dat = g_date.entry.get()
	x = g_name.get()
	a = g_score1.get()
	b = g_score2.get()
	c = g_score3.get()
	d = g_score4.get()
	e = g_score5.get()
	f = g_score6.get()
	g = g_score7.get()
	h = g_score8.get()
	i = g_score9.get()
	j = g_score10.get()
	k = g_score11.get()
	l = g_score12.get()
	m = g_score13.get()
	n = g_score14.get()
	o = g_score15.get()
	p = g_score16.get()
	q = g_score17.get()
	r = g_score18.get()
	y = int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) + int(h) + int(i) + int(j) + int(k) + int(l) + int(m) + int(n) + int(o) + int(p) + int(q) + int(r)

	cursor.execute(sql, (num, dat, x, int(a), int(b), int(c), int(d), int(e), int(f), int(g), int(h), int(i), int(j), int(k), int(l), int(m), int(n), int(o), int(p), int(q), int(r), int(y)))




	conn.commit()

	#collect the current totals for comparison with thiis round

	sql2 = """SELECT hole1, hole2, hole3, hole4, hole5, hole6, hole7, hole8, hole9,
		hole10, hole11, hole12, hole13, hole14, hole15, hole16, hole17, hole18 FROM totals WHERE name = ?"""


	cursor.execute(sql2, (x,))

	record = cursor.fetchone()

	#compare scores with totals and change if better

	if record[0]>= int(a):
		a =  record[0]
	if record[1] >= int(b):
		b =  record[1]
	if record[2] >= int(c):
		c =  record[2]
	if record[3]>= int(d):
		d =  record[3]
	if record[4] >= int(e):
		e =  record[4]
	if record[5] >= int(f):
		f =  record[5]
	if record[6]>= int(g):
		g =  record[6]
	if record[7] >= int(h):
		h =  record[7]
	if record[8] >= int(i):
		i =  record[8]
	if record[9]>= int(j):
		j =  record[9]
	if record[10] >= int(k):
		k =  record[10]
	if record[11] >= int(l):
		l =  record[11]
	if record[12]>= int(m):
		m =  record[12]
	if record[13] >= int(n):
		n =  record[13]
	if record[14] >= int(o):
		o =  record[14]
	if record[15]>= int(p):
		p =  record[15]
	if record[16] >= int(q):
		q =  record[16]
	if record[17] >= int(r):
		r =  record[17]
	#calcualate total score and update the totals db

	y = int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) + int(h) + int(i) + int(j) + int(k) + int(l) + int(m) + int(n) + int(o) + int(p) + int(q) + int(r)


	sql3 = """ UPDATE totals SET hole1 = ?, hole2 = ?, hole3 = ?, hole4 = ?, hole5 = ?, hole6 = ?,
		 hole7 = ?, hole8 = ?, hole9 = ?, hole10 = ?, hole11 = ?, hole12 = ?,
		 hole13 = ?, hole14 = ?, hole15 = ?, hole16 = ?, hole17 = ?, hole18 = ?, total = ? WHERE name =?"""

	cursor.execute(sql3, (int(a), int(b), int(c), int(d), int(e), int(f), int(g), int(h), int(i), int(j), int(k), int(l), int(m), int(n), int(o), int(p), int(q), int(r), int(y), x))

	conn.commit()

	# clear entry boxes and total label for next entry

	g_name.delete(0,END); g_score1.delete(0,END); g_score2.delete(0,END); g_score3.delete(0,END); 
	g_score4.delete(0,END); g_score5.delete(0,END); g_score6.delete(0,END);
	g_score7.delete(0,END); g_score8.delete(0,END); g_score9.delete(0,END);
	g_score10.delete(0,END); g_score11.delete(0,END); g_score12.delete(0,END);
	g_score13.delete(0,END); g_score14.delete(0,END); g_score15.delete(0,END);
	g_score16.delete(0,END); g_score17.delete(0,END); g_score18.delete(0,END);
	g_total.configure(text= 'xx')



# --------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
 # called from def report

# This function reads the totals table and produces a report sorted bythe total score
# Then produces a pdf of the result using reportlab and a new screen for the report
def produce_report():

	if  g_round.get() == "" :
		messagebox.showerror('Input Error', 'Error: You Must Enter Round Number!')
		

	else:

	   
	    cursor = conn.cursor()

	    # print out the scores in descending order 
	    cursor.execute("SELECT * FROM totals ORDER BY total DESC")
	    rows = cursor.fetchall()

	    print_records = ""

	    rnd = g_round.get()

	    data = [['Eclectic Leaderboard \n ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
	    		['After Round ' + rnd +' \n ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
	    		['             Hole', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', 'Total']]
	    
	    for row in rows:
	        #printrecords is created with the full block of data formatted in tabular form

	        print_records += (str("{:20} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:5}".format(row[0],
	         row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
	         row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19]))
	         + "\n" + "------------------------------------------------------------------------------------" + "\n")

	        

	        data.append(row)
	 
	    # Create a new window on screen and display the data

	    top = Toplevel() 
	    top.title("report")   

	    win_frame = Frame(top, height = 35, width = 350, relief = "sunken")
	    win_frame.grid(row= 0, column = 1, padx = 10, pady = 10)


	    T = ScrolledText(win_frame, height=30, width=120, font=('Courier New', 11),bootstyle='success')
	    T.grid(row=0, column=0, sticky= N,columnspan=5, padx=10,pady=15)
	    T.insert(END, ("{:21} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:5} ".format("Name        Hole",
	    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18","Total")) + "\n" + "\n")
	    T.insert(END, print_records)

	    btn_close_top = tb.Button(top, text = "Dismiss", command= top.destroy,
	    bootstyle="light",
	    style= "success.TButton",
		width=14)
	    btn_close_top.grid(row= 1, column= 0, padx= 30, pady= 10)

		# report using reportlab

	    doc = SimpleDocTemplate("simple_table.pdf")
	    flowables = []
	    t=Table(data,style=[('GRID',(0,0),(-1,-1),1,colors.black),
	                    ('BOX',(0,2),(0,-1),2,colors.red),
	                    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
	                    ('BOX',(-1,2),(-1,-1),2,colors.red),
	                    ('FONTNAME', (-1,1), (-1,-1), 'Helvetica-Bold'),
	                    ('LINEBELOW',(0,2),(-1,2),2,colors.blue),
	                    ('FONTNAME', (0,2), (19,2), 'Helvetica-Bold'),
	                    ('SPAN',(0,0),(-1,0)),
	                    ('SPAN',(0,1),(19,1)),
	                    ('ALIGN',(0,0),(-1,0), 'CENTER'),
	                    ('ALIGN',(0,1),(19,1), 'CENTER'),
	                    ('FONTNAME', (0,0), (0,0), 'Courier-Bold'),
	                    ('FONTSIZE', (0, 0), (0, 0), 16),
	                    ])
		
	    flowables.append(t)
	    doc.build(flowables)


#------------------------------------------------------------------------------------------------

def round_report():
	# called from btn round_report
	# This is more or less a repeat of the reprot function above but onle the scores from the round


	if  g_round.get() == "" :
		
		messagebox.showerror('Input Error', 'Error: You Must Enter Round Number!')
		

	else:
	    cursor = conn.cursor()
	    rnd = g_round.get()
	    # print out the scores in descending order 
	    cursor.execute("""SELECT  name,  hole1, hole2, hole3, hole4, hole5, hole6, hole7, hole8, hole9, hole10,
			hole11, hole12, hole13, hole14, hole15, hole16, hole17, hole18, total FROM round WHERE round_num = ? ORDER BY total DESC""",(rnd,))
	    rows = cursor.fetchall()

	    round_records = ""

	   

	    round_data = [['Eclectic Leaderboard \n ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
	    		['Round ' + rnd +' \n ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
	    		['             Hole', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', 'Total']]
	    
	    for row in rows:
	        #printrecords is created with the full block of data formatted in tabular form

	        round_records += (str("{:20} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:5}".format(row[0],
	         row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
	         row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19]))
	         + "\n" + "------------------------------------------------------------------------------------" + "\n")

	        

	        round_data.append(row)
	        



	 
	    # Create a new window on screen and display the data

	    round_top = Toplevel() 
	    round_top.title("Round report")   

	    round_frame = Frame(round_top, height = 35, width = 350, bd = 2, relief = "sunken")
	    round_frame.grid(row= 0, column = 1, padx = 10, pady = 10)


	    T = ScrolledText(round_frame, height=30, width=120, font=('Courier New', 11),bootstyle='success')
	    T.grid(row=0, column=0, sticky= N,columnspan=5, padx=10,pady=15)
	    T.insert(END, ("{:21} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2} {:5} ".format("Name        Hole",
	    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18","Total")) + "\n" + "\n")
	    T.insert(END, round_records)

	    btn_close_round = tb.Button(round_top, text = "Dismiss", command= round_top.destroy,
	    bootstyle="light",
	    style= "success.TButton",
		width=14)
	    btn_close_round.grid(row= 1, column= 0, padx= 30, pady= 10)


	    doc = SimpleDocTemplate("round_table.pdf")
	    flowables = []
	    t=Table(round_data,style=[('GRID',(0,0),(-1,-1),1,colors.black),
	                    ('BOX',(0,2),(0,-1),2,colors.red),
	                    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
	                    ('BOX',(-1,2),(-1,-1),2,colors.red),
	                    ('FONTNAME', (-1,1), (-1,-1), 'Helvetica-Bold'),
	                    ('LINEBELOW',(0,2),(-1,2),2,colors.blue),
	                    ('FONTNAME', (0,2), (19,2), 'Helvetica-Bold'),
	                    ('SPAN',(0,0),(-1,0)),
	                    ('SPAN',(0,1),(19,1)),
	                    ('ALIGN',(0,0),(-1,0), 'CENTER'),
	                    ('ALIGN',(0,1),(19,1), 'CENTER'),
	                    ('FONTNAME', (0,0), (0,0), 'Courier-Bold'),
	                    ('FONTSIZE', (0, 0), (0, 0), 16),
	                    ])
		
	    flowables.append(t)
	    doc.build(flowables)


#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------

# called from list button to fill member listbox

def query():
    
    my_listbox.delete(0,'end')
    c = conn.cursor()
    c.execute("SELECT name	FROM totals ORDER BY name " )
    records = c.fetchall()
    # Loop through results
    print_records = " "
    for record in records:
    	my_listbox.insert(END, record[0])


    conn.commit()
    #conn.close()

#---------------------------------------------------------------------------------------------------


def select():
    #called from the Select button enters name selected in the list into the g_name entry box

    x= my_listbox.get(ANCHOR)
    print(x)
    g_name.delete(0,END)
    #g_name.configure(state="normal")
    g_name.insert(END,x)
    g_score1.focus()

#----------------------------------------------------------------------------------------------

#  detects the entry of a value in g_score18 then put total in total label

def mytrace(a,b,c):
	test =g_score1.get()
	if  not (test == ''):
		my_total = (int(g_score1.get()) + int(g_score2.get()) + int(g_score3.get()) + int(g_score4.get())
		 + int(g_score5.get()) + int(g_score6.get()) + int(g_score7.get()) + int(g_score8.get())
		 + int(g_score9.get()) + int(g_score10.get()) + int(g_score11.get()) + int(g_score12.get())
		  + int(g_score13.get()) + int(g_score14.get()) + int(g_score15.get()) + int(g_score16.get())
		   + int(g_score17.get()) + int(g_score18.get()))
		g_total.configure(text = my_total)

#  detects the entry of a value in g_score9 then put total in total label
def ninetrace(a,b,c):
	test =g_score1.get()
	if  not (test == ''):
		nine_total = (int(g_score1.get()) + int(g_score2.get()) + int(g_score3.get()) + int(g_score4.get())
		 + int(g_score5.get()) + int(g_score6.get()) + int(g_score7.get()) + int(g_score8.get())
		 + int(g_score9.get()))
		g_total.configure(text = nine_total)


#==============================================================================================================
# Ammendment window allows the correction of a score in the system and updates totals accordingly
# Creates a new window with a treeview widget to allow display of a single round's scores

def update_item():
	ammend = tb.Toplevel()
	ammend.title("Ammend Entry")
	ammend.geometry("1200x800")

	#s = ttk.Style()
	#s.theme_use('clam')

	c_round = tb.Entry(ammend, width=2)
	c_round.grid(row=0, column=1, padx=10, pady=10)
	round_lbl =tb.Label(ammend, text="Round Number")
	round_lbl.grid(row=0, column=0, padx=10, pady=10)
	c_name = tb.Entry(ammend, width= 22)
	c_name.grid(row=1,column=1, padx=10, pady=10)
	name_lbl = tb.Label(ammend, text= "name")
	name_lbl.grid(row=1, column= 0, padx=10, pady=10)

	c = conn.cursor()
	list_sql = ("""SELECT hole1, hole2, hole3, hole4, hole5, hole6, hole7, hole8, hole9, hole10,
		hole11, hole12, hole13, hole14, hole15, hole16, hole17, hole18 FROM round WHERE round_num = ? AND name = ? """)
	c.execute(list_sql, (c_round.get(), c_name.get()))
	records = c.fetchall()



	
	
	


	# Add a Treeview widget
	tree = tb.Treeview(ammend, column=("c1", "c2"), show='headings', height=9, bootstyle="success")
	tree.grid(row= 4, column= 0, columnspan=2, padx=10, pady=20)

	tree.column("# 1", anchor=CENTER)
	tree.heading("# 1", text="Hole")
	tree.column("# 2", anchor=CENTER)
	tree.heading("# 2", text="Score")


	# Read the round to be ammended and place in treeview
	def load_data():
		c = conn.cursor()
		data_sql= ("""SELECT hole1, hole2, hole3, hole4, hole5, hole6, hole7, hole8, hole9, hole10,
		hole11, hole12, hole13, hole14, hole15, hole16, hole17, hole18 FROM round WHERE round_num = ? AND name = ? """)
		c.execute(data_sql, (c_round.get(), c_name.get()))
		records = c.fetchall()	

		for record in records:
			tree.insert('', 'end', text="1", values=("1", record[0]))
			tree.insert('', 'end', text="1", values=("2", record[1]))
			tree.insert('', 'end', text="1", values=("3", record[2]))
			tree.insert('', 'end', text="1", values=("4", record[3]))
			tree.insert('', 'end', text="1", values=("5", record[4]))
			tree.insert('', 'end', text="1", values=("6", record[5]))
			tree.insert('', 'end', text="1", values=("7", record[6]))
			tree.insert('', 'end', text="1", values=("8", record[7]))
			tree.insert('', 'end', text="1", values=("9", record[8]))
			tree.insert('', 'end', text="1", values=("10", record[9]))
			tree.insert('', 'end', text="1", values=("11", record[10]))
			tree.insert('', 'end', text="1", values=("12", record[11]))
			tree.insert('', 'end', text="1", values=("13", record[12]))
			tree.insert('', 'end', text="1", values=("14", record[13]))
			tree.insert('', 'end', text="1", values=("15", record[14]))
			tree.insert('', 'end', text="1", values=("16", record[15]))
			tree.insert('', 'end', text="1", values=("17", record[16]))
			tree.insert('', 'end', text="1", values=("18", record[17]))

	def update():
		selected = tree.focus()
		temp = tree.item(selected, 'values')
		tree.item(selected, values=(temp[0], newscore.get())) 

		
		
		# Write the ammended round to the round table in the database.

	def write_ammend():

		x = []

		listOfEntriesInTreeView=tree.get_children()
		for each in listOfEntriesInTreeView:
			x.append(tree.item(each)['values'][1])  #e.g. prints data in clicked cell
			#tree.detach(each) #e.g. detaches entry from treeview
		#print(x)
		

		up = conn.cursor()

		a1 = x[0]
		a2 = x[1]
		a3 = x[2]
		a4 = x[3]
		a5 = x[4]
		a6 = x[5]
		a7 = x[6]
		a8 = x[7]
		a9 = x[8]
		a10 = x[9]
		a11 = x[10]
		a12 = x[11]
		a13 = x[12]
		a14 = x[13]
		a15 = x[14]
		a16 = x[15]
		a17 = x[16]
		a18 = x[17]

		tot = sum(x)

		#y = int(a1) + int(a2) + int(a3) + int(a4) + int(a5) + int(a6) + int(a7) + int(a8) + int(a9) + int(a10) + int(a11) + int(a12) + int(a13) + int(a14) + int(a15) + int(a16) + int(a17) + int(a18)

			

		sqlu = """ UPDATE 	round SET hole1 = ?, hole2 = ?, hole3 = ?, hole4 = ?, hole5 = ?, hole6 = ?, hole7 = ?, hole8 = ?, hole9 = ?,
		 hole10 = ?, hole11 = ?, hole12 = ?, hole13 = ?, hole14 = ?, hole15 = ?, hole16 = ?, hole17 = ?, hole18 = ?, total = ? WHERE round_num = ? AND name = ?"""

		up.execute(sqlu, (int(a1), int(a2), int(a3), int(a4), int(a5), int(a6), int(a7), int(a8), int(a9), int(a10),
		int(a11), int(a12), int(a13), int(a14), int(a15),int(a16), int(a17), int(a18), tot, c_round.get(), c_name.get()))

		

			
		conn.commit()

		update_totals()

	def update_totals():

		c = conn.cursor()
		list_sql = ("""SELECT hole1, hole2, hole3, hole4, hole5, hole6, hole7, hole8, hole9, hole10,
		hole11, hole12, hole13, hole14, hole15, hole16, hole17, hole18 FROM round WHERE  name = ? """)
		c.execute(list_sql, (c_name.get(),))
		records = c.fetchall()
		print(len(records))
		print(records)
		best=[]
		tot = 0

		

		for i in range(0,18):
			max_value = max(sublist[i] for sublist in records)
			best.append(max_value)

		tot= sum(best)


		print(tot)		

		print(best)
		sql3 = """ UPDATE totals SET hole1 = ?, hole2 = ?, hole3 = ?, hole4 = ?, hole5 = ?, hole6 = ?,
		hole7 = ?, hole8 = ?, hole9 = ?, hole10 = ?, hole11 = ?, hole12 = ?,
		hole13 = ?, hole14 = ?, hole15 = ?, hole16 = ?, hole17 = ?, hole18 = ?, total = ? WHERE name =?"""

		c.execute(sql3, (best[0], best[1], best[2], best[3], best[4], best[5], best[6], best[7], best[8], best[9], 
			best[10], best[11], best[12], best[13], best[14], best[15], best[16], best[17], tot, c_name.get()))

		conn.commit()

		messagebox.showinfo(title='saved', message='corections saved',command= ammend.destroy())


	edit_btn = tb.Button(ammend, text="Edit", command=update,
	bootstyle="light",
	style= "success.TButton",
	width=10)
	
	edit_btn.grid(row=4,column=4)
	newscore = tb.Entry(ammend)
	newscore.grid(row= 4,column= 3, padx=10)
	read_btn = tb.Button(ammend, text="read", command=load_data,
	bootstyle="light",
	style= "success.TButton",
	width=10)
	read_btn.grid(row=3, column=1,padx=10)
	write_btn = tb.Button(ammend, text="Write Corrections", command=write_ammend,
	style= "success.TButton",
	width=15)
	write_btn.grid(row=5, column=3,padx=10)

	

	
#===================================================================================================================

def clear_scores():
	clear = conn.cursor()
	sql1 = ('DELETE FROM round')
	sql2 = ('DELETE FROM totals') 
	sql3 = ("""UPDATE totals SET hole1=0, hole2=0, hole3=0, hole4=0, hole5=0, hole6=0, hole7=0, hole8=0, hole9=0, hole10=0,
			hole11=0, hole12=0, hole13=0, hole14=0, hole15=0, hole16=0, hole17=0, hole18=0, total=0 """)

	res = messagebox.askquestion(title='Delete Scores', message='WARNING! This will delete all scores')
	if res == 'yes':
		#clear the round table and set all scores in totals to zero

		clear.execute(sql1)
		clear.execute(sql3)
		
		res2 = messagebox.askquestion(title='Delete Golfers', message='Do you want to delete golfer names as well?')
		if res2 == 'yes':

			#Clear the totals table to set system back to startup 
			clear.execute(sql2)

			print ('yes')
		
		conn.commit()


	else:
		messagebox.showinfo(title='Cancel', message='Operation Cancelled')
		




#=====================================================================================================================


# -------------------------------------------------------------------------------------
my_style = tb.Style()
my_style.configure('success.TButton',font = ('Helvetica', 12))

space_label = tb.Label(root,text=" ")
space_label.grid(row = 6, column=0, padx=20, pady=30)


box_frame =Frame(root, height= 400, width=400,bd=2, relief="sunken")
box_frame.grid(row = 7, column=0,sticky=W, padx=10)

button_frame =Frame(root, height= 500, width=400,bd=2, relief="sunken")
button_frame.grid(row = 7, column=0, padx=10)




nine_var = StringVar()
nine_var.set('')
nine_var.trace('w',ninetrace)


list_frame = Frame(box_frame, height = 100,width=100, bd = 2, bg="yellow", relief = "sunken")
list_frame.grid(row=2, column=0,sticky= E, padx=10, pady=30)

my_listbox=Listbox(list_frame)
my_listbox.pack(padx=0,pady=15, side = LEFT)

my_scrollbar = tb.Scrollbar(list_frame, bootstyle="success")
my_scrollbar.pack(side = RIGHT, fill = BOTH)

my_listbox.config(yscrollcommand = my_scrollbar.set)
my_scrollbar.config(command = my_listbox.yview)



btn_select = tb.Button(box_frame, text='Select', command= select,
 bootstyle="light",
 style= "success.TButton",
 width=10)
btn_select.grid(row=2, column=1, padx=10, pady=10)



btn_report = tb.Button(button_frame, text='Report', command=produce_report,
 bootstyle="light",
 style= "success.TButton",
  width=15)
btn_report.grid(row=2, column=3,padx=20, pady=10)
#-----------------------------------------------------------------------------------

btn_round_report = tb.Button(button_frame, text='Round Report', command= round_report,
 bootstyle="light",
 style= "success.TButton",
  width=15)
btn_round_report.grid(row=4, column=3, padx=20, pady=10)

# correction window settings
btn_correct = tb.Button(button_frame, text='Correct', command= update_item,
 bootstyle="light",
 style= "success.TButton",
  width=15)
btn_correct.grid(row=5, column=3, padx=20, pady=10)

btn_clear_scores = tb.Button(button_frame, text='Clear Scores', command= clear_scores,
 bootstyle="light",
 style= "success.TButton",
  width=15)
btn_clear_scores.grid(row=7, column=3, padx=20, pady=10)






#------------------------------------------------------------------------------------
btn_list = tb.Button(box_frame, text='List', command= query,
 bootstyle="light", 
 style= "success.TButton",
  width=15)
btn_list.grid(row=0, column=0, padx=10, pady=10)

#space_frame = Frame(root, bd=2, relief="sunken")
#space_frame.grid(row=1, column=0, padx=10)

spacer = tb.Label(root, text="Eclectic Data Entry")
spacer.grid(row=1, column=0,padx=30, pady=10)

score_frame = Frame(root, bd=2, relief="sunken")
score_frame.grid(row=3, column=0, padx=10)




g_name = tb.Entry(score_frame)
g_name.grid(row=3, column=0,padx = 10)

g_score1 = tb.Entry(score_frame,width=3); g_score1.grid(row=3, column=2)

g_score2 = tb.Entry(score_frame,width =3); g_score2.grid(row=3, column=3)

g_score3 = tb.Entry(score_frame,width =3); g_score3.grid(row=3, column=4)

g_score4 = tb.Entry(score_frame,width=3); g_score4.grid(row=3, column=5)

g_score5 = tb.Entry(score_frame,width=3); g_score5.grid(row=3, column=6)

g_score6 = tb.Entry(score_frame,width=3); g_score6.grid(row=3, column=7)

g_score7 = tb.Entry(score_frame,width=3); g_score7.grid(row=3, column=8)

g_score8 = tb.Entry(score_frame,width=3); g_score8.grid(row=3, column=9)

g_score9 = tb.Entry(score_frame,width=3, textvariable = nine_var); g_score9.grid(row=3, column=10)

g_score10 = tb.Entry(score_frame,width=3); g_score10.grid(row=3, column=11)

g_score11 = tb.Entry(score_frame,width =3); g_score11.grid(row=3, column=12)

g_score12= tb.Entry(score_frame,width =3); g_score12.grid(row=3, column=13)

g_score13= tb.Entry(score_frame,width=3); g_score13.grid(row=3, column=14)

g_score14= tb.Entry(score_frame,width=3); g_score14.grid(row=3, column=15)

g_score15= tb.Entry(score_frame,width=3); g_score15.grid(row=3, column=16)

g_score16= tb.Entry(score_frame,width=3); g_score16.grid(row=3, column=17)

g_score17= tb.Entry(score_frame,width=3); g_score17.grid(row=3, column=18)

#g_score18= Entry(score_frame,width=3); g_score18.grid(row=3, column=19)




myvar = StringVar()
myvar.set('')
g_score18 = tb.Entry(score_frame,textvariable=myvar, width=3)
g_score18.grid(row=3, column=19)
myvar.trace('w',mytrace)


g_total = tb.Label(score_frame, text= 'xx',font=("Helvetica",12)); g_total.grid(row=3,column=20, padx=20)

btn_insert_round = tb.Button(score_frame, text='Insert Round', command= check_golfer,
 bootstyle="light",
  style= "success.TButton",
  width=14)
btn_insert_round.grid(row=3, column=21, padx=10, pady=10)

g_round = tb.Entry(score_frame,w=2)
g_round.grid(row=0, column=1,padx = 10)

g_date = tb.DateEntry(score_frame, bootstyle="success")#Entry(score_frame)
g_date.grid(row=0, column=5,columnspan= 6,padx = 10)

lbl_date = tb.Label(score_frame,text="Date")
lbl_date.grid(row=0, column=2,columnspan=3, padx=10)

lbl_round = tb.Label(score_frame,text="Round")
lbl_round.grid(row=0, column=0, padx=10)

lbl_golfer = tb.Label(score_frame,text="Name")
lbl_golfer.grid(row=2, column=0, padx=10)


lbl_score1 = tb.Label(score_frame,text=" 1", width =3); lbl_score2 = tb.Label(score_frame,text=" 2", width =3)
lbl_score1.grid(row=2, column=2); lbl_score2.grid(row=2, column=3)

lbl_score3 = tb.Label(score_frame,text=" 3", width =3); lbl_score4 = tb.Label(score_frame,text=" 4", width =3)
lbl_score3.grid(row=2, column=4); lbl_score4.grid(row=2, column=5)

lbl_score5 = tb.Label(score_frame,text=" 5", width =3); lbl_score6 = tb.Label(score_frame,text=" 6", width=3)
lbl_score5.grid(row=2, column=6); lbl_score6.grid(row=2, column=7)

lbl_score7 = tb.Label(score_frame,text=" 7", width =3); lbl_score8 = tb.Label(score_frame,text=" 8", width=3)
lbl_score7.grid(row=2, column=8); lbl_score8.grid(row=2, column=9)

lbl_score9 = tb.Label(score_frame,text=" 9", width =3); lbl_score10 = tb.Label(score_frame,text="10", width=3)
lbl_score9.grid(row=2, column=10); lbl_score10.grid(row=2, column=11)

lbl_score11 = tb.Label(score_frame,text="11", width =3); lbl_score12 = tb.Label(score_frame,text="12", width=3)
lbl_score11.grid(row=2, column=12); lbl_score12.grid(row=2, column=13)

lbl_score13 = tb.Label(score_frame,text="13", width =3); lbl_score14 = tb.Label(score_frame,text="14", width=3)
lbl_score13.grid(row=2, column=14); lbl_score14.grid(row=2, column=15)

lbl_score15 = tb.Label(score_frame,text="15", width =3); lbl_score16 = tb.Label(score_frame,text="16", width=3)
lbl_score15.grid(row=2, column=16); lbl_score16.grid(row=2, column=17)

lbl_score17 = tb.Label(score_frame,text="17", width =3); lbl_score18 = tb.Label(score_frame,text="18", width=3)
lbl_score17.grid(row=2, column=18); lbl_score18.grid(row=2, column=19)





#btn_create = Button(root, text='create tables', command= create_tables)
#btn_create.grid(row=1, column=1, padx=10, pady=10)



root.mainloop()