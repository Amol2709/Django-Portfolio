from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import mysql.connector
# Create your views here.



def home(request):
	context = {
		'name': 'Amol'
	}
	return render(request,'home.html',context)


def takeaway(request):
	return render(request,'takeaway.html')


def form(request):
	if request.method == 'GET':
		print(list(request.GET.keys())[0])

		context = {
		'papername':list(request.GET.keys())[0]
		}
		return render(request,'form.html',context)
	# if request.method == 'GET' and 'yolo' in request.GET:
	# 	context = {
	# 	'papername':'yolo'
	# 	}
	# 	return render(request,'form.html',context)
	# if request.method == 'GET' and 'seq2seq' in request.GET:
	# 	context = {
	# 	'papername':'seq2seq'
	# 	}
	# 	return render(request,'form.html',context)


def viewpaper(request):
	if request.method == 'GET':
		print(list(request.GET.keys()))
		research_paper = list(request.GET.keys())[-1]

		Fname= request.GET['fname']
		Lname= request.GET['lname']
		Email= request.GET['email']
		print(Fname)
		record = (Fname,Lname,Email,research_paper)



		try:
			conn = mysql.connector.connect(host='localhost',database='my-db',user='root',password='root@123root@123',port=3307)
			mySql_insert_query = """INSERT INTO djangodb (firstname, lastname, email,paper) VALUES (%s,%s,%s,%s) """

			cursor = conn.cursor()
			cursor.execute(mySql_insert_query,record)
			conn.commit()
			print(cursor.rowcount, "Record inserted successfully into djangodb table")
			cursor.close()

		except mysql.connector.Error as error:
			print("Failed to insert record into djangodb table {}".format(error))
		finally:
			if conn.is_connected():
				conn.close()
				print("MySQL connection is closed")
				return HttpResponseRedirect('http://127.0.0.1:8000/static/'+research_paper+'.pdf')

	# if request.method == 'POST' and 'yolo' in request.POST:
	# 	return HttpResponseRedirect('http://127.0.0.1:8000/static/yolo.pdf')
	# if request.method == 'POST' and 'seq2seq' in request.POST:
	# 	return HttpResponseRedirect('http://127.0.0.1:8000/static/seq2seq.pdf')



def contact(request):
	return render(request,'contact.html')
# def index(request):
	
# 	return HttpResponse('this is index page')