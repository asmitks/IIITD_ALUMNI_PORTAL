import functools
import json
import os
import flask
from flask import Flask, redirect, url_for, session, request,render_template,make_response,request
from pymongo import MongoClient
from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery
import gmail

import datetime
expire_date = datetime.datetime.now()
expire_date = expire_date + datetime.timedelta(days=90)
#MONGO
emailf=''
namef=''
client = MongoClient()
db=client.alumni_portal
col1=db.events
col2=db.jobs
col3=db.data2
col4=db.testimonial
don=[['ACM ICPC','Our team has qualified.'],['UAV ','Our uav team has qualified....'],['Library','Our library is...']]
check=0

#app
app = flask.Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)

app.register_blueprint(gmail.app)

def stats():
    mt=0
    phd=0
    btech=0
    for i in range(1799):
        if(col3.find()[i]["Roll Number 1"]):
            if col3.find()[i]["Roll Number 1"].find('MT')!=-1:
                mt+=1
            if col3.find()[i]["Roll Number 1"].find('PhD')!=-1:
                phd+=1
            else:
                btech+=1
    return(mt,phd,btech)
testr=[]
for i in col4.find():
    testr.append([i['text'],i['name'],i['job']])


acced=0

def check_iiit():
    if gmail.is_logged_in():
        user_info = gmail.get_user_info()
        name=user_info['given_name']
        surname=user_info['family_name']
        piclink=user_info['picture']
        email=user_info['email']
        if('iiitd.ac.in' not in email and email!='asmitsingh89@gmail.com' and email!='ayushkumarsingh97@gmail.com'):
            return [False,user_info]
        else:
            return [True,user_info]

@app.route('/',methods=['GET','POST'])
def index():
    # doc
    # return render_template('index.html')
    ar=[]
    st=stats()

    # for i in range(1799):
    #     ar.append(col3.find()[i])
    # print(request.form['title'])
    a=[]
    b=[]
    for jj in col1.find():
        kk=jj
        a.append(kk)
    for jj in col2.find():
        xx=jj
        b.append(xx)
    if gmail.is_logged_in():
        if 'email' in request.cookies and (request.cookies.get('email').find('asmit')!=-1 or request.cookies.get('email').find('iiitd.ac.in')!=-1):
            email=request.cookies.get('email')
            name=request.cookies.get('name')
            piclink=request.cookies.get('piclink')
            surname=request.cookies.get('surname')
            name=request.cookies.get('name')
            piclink=request.cookies.get('piclink')
            surname=request.cookies.get('surname')
            print("cookies..................")

            print("Agaya...")
            # return("agaya")

            
            st=stats()  
            # return("x")
            # return name
            
            if('iiitd.ac.in' not in email and email!='asmitsingh89@gmail.com' and email!='ayushkumarsingh97@gmail.com'):
                return render_template('index_galat.html')

            elif(email=='asmitsingh89@gmail.com'):
                return render_template('admin.html',ss=(st[0]+st[1]+st[2]),mt=st[0],phd=st[1],btech=st[2])
            i=0
            a=[]
            b=[]
            ok=0
            # piclink='https://lh5.googleusercontent.com/-HiiQH16HJfY/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3rdtZGLwcMrjxyCByhDkG0iUrNiJlQ/photo.jpg'
            # name='js'
            # surname='lkl'
            for jj in col1.find():
                    kk=jj
                    a.append(kk)
            for jj in col2.find():
                    xx=jj
                    b.append(xx)
            for jj in col3.find():
                if jj['Email ID']==email:
                    ok=1
            if ok==0:
                # myquery = { }
                newvalues=  {"Email ID": email  ,"Birth date" : None, "Full Name" : str(name+surname), "Roll Number 1" : None, "Employer 1" : None, "Designation 1" : None, "Employer 2" : None, "Designation 2" : None, "Mobile Number" : None, "email2" : None, "Class Year 1" : None, "Degree 1" : None} 
                col3.insert_one(newvalues)
            return render_template('loggedin.html',don=don,testimonial=testr,l=(st[0]+st[1]+st[2]),mt=st[0],phd=st[1],btech=st[2],name=name,surname=surname,eventname=a[-1]['title'],eventtext=a[-1]['text'],eventname1=a[-2]['title'],eventtext1=a[-2]['text'],eventname2=a[-3]['title'],eventtext2=a[-3]['text'],jobtitle=b[-1]['jobtitle'],jobtext=b[-1]['jobtext'],jobtitle1=b[-2]['jobtitle'],jobtext2=b[-2]['jobtext'])

            # ,jobtitle=xx['jobtitle'],jobtext=xx['jobtext'])
            # return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"
        else:
            

            print("Agaya...")
            # return("agaya")

            
            st=stats()  
            # return("x")
            # return name
            check=1
            name='12'
            surname='13'
            name='sad'
            surname='asdasl'
            acced=1
            user_info = gmail.get_user_info()
            name=user_info['given_name']
            surname=user_info['family_name']
            piclink=user_info['picture']
            email=user_info['email']
            # response.set_cookie('email',email)
            # response.set_cookie('name',name)
            # response.set_cookie('piclink',piclink)
            # response.set_cookie('surname',surname)
            
            if('iiitd.ac.in' not in email and email!='asmitsingh89@gmail.com' and email!='ayushkumarsingh97@gmail.com'):
                return render_template('index_galat.html')

            elif(email=='asmitsingh89@gmail.com'):
                response=make_response(render_template('admin.html',ss=(st[0]+st[1]+st[2]),mt=st[0],phd=st[1],btech=st[2]))
                response.set_cookie('email',email,expires=expire_date)
                response.set_cookie('name',name,expires=expire_date)
                response.set_cookie('piclink',piclink,expires=expire_date)
                response.set_cookie('surname',surname,expires=expire_date)
                return response
            i=0
            a=[]
            b=[]
            ok=0
            # piclink='https://lh5.googleusercontent.com/-HiiQH16HJfY/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3rdtZGLwcMrjxyCByhDkG0iUrNiJlQ/photo.jpg'
            # name='js'
            # surname='lkl'
            for jj in col1.find():
                    kk=jj
                    a.append(kk)
            for jj in col2.find():
                    xx=jj
                    b.append(xx)
            for jj in col3.find():
                if jj['Email ID']==email:
                    ok=1
            if ok==0:
                # myquery = { }
                newvalues=  {"Email ID": email  ,"Birth date" : None, "Full Name" : str(name+surname), "Roll Number 1" : None, "Employer 1" : None, "Designation 1" : None, "Employer 2" : None, "Designation 2" : None, "Mobile Number" : None, "email2" : None, "Class Year 1" : None, "Degree 1" : None} 
                col3.insert_one(newvalues)
                response=make_response(render_template('loggedin.html',don=don,testimonial=testr,l=(st[0]+st[1]+st[2]),mt=st[0],phd=st[1],btech=st[2],name=name,surname=surname,eventname=a[-1]['title'],eventtext=a[-1]['text'],eventname1=a[-2]['title'],eventtext1=a[-2]['text'],eventname2=a[-3]['title'],eventtext2=a[-3]['text'],jobtitle=b[-1]['jobtitle'],jobtext=b[-1]['jobtext'],jobtitle1=b[-2]['jobtitle'],jobtext2=b[-2]['jobtext']))
                response.set_cookie('email',email,expires=expire_date)
                response.set_cookie('name',name,expires=expire_date)
                response.set_cookie('piclink',piclink,expires=expire_date)
                response.set_cookie('surname',surname,expires=expire_date)
                return response
            # ,jobtitle=xx['jobtitle'],jobtext=xx['jobtext'])
            else:
                response=make_response(render_template('loggedin.html',don=don,testimonial=testr,l=(st[0]+st[1]+st[2]),mt=st[0],phd=st[1],btech=st[2],name=name,surname=surname,eventname=a[-1]['title'],eventtext=a[-1]['text'],eventname1=a[-2]['title'],eventtext1=a[-2]['text'],eventname2=a[-3]['title'],eventtext2=a[-3]['text'],jobtitle=b[-1]['jobtitle'],jobtext=b[-1]['jobtext'],jobtitle1=b[-2]['jobtitle'],jobtext2=b[-2]['jobtext']))
                response.set_cookie('email',email,expires=expire_date)
                response.set_cookie('name',name,expires=expire_date)
                response.set_cookie('piclink',piclink,expires=expire_date)
                response.set_cookie('surname',surname,expires=expire_date)
                return response

            # return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + 
    return render_template('index.html',l=(st[0]+st[1]+st[2]),mt=st[0],phd=st[1],btech=st[2],eventname=a[-1]['title'],eventtext=a[-1]['text'],eventname1=a[-2]['title'],eventtext1=a[-2]['text'],eventname2=a[-3]['title'],eventtext2=a[-3]['text'],jobtitle=b[-1]['jobtitle'],jobtext=b[-1]['jobtext'],jobtitle1=b[-2]['jobtitle'],jobtext2=b[-2]['jobtext'],don=don)
    # return redirect(url_for('google_auth.login'))
dic={}
if check==1:
    if check_iiit()[0]:
        dic=check_iiit()[1]



@app.route('/changeevent',methods=['GET','POST'])
def a():
    # return(request.form['title'])
    # db=col1.alumni_portal

    # col1=db.events
    dic={}
    dic['title']=str(request.form['title'])
    dic['text']=str(request.form['text'])
    col1.insert(dic)
    # user_info = gmail.get_user_info()
    #  return redirect(url_for('index'))  
    st=stats()
    return render_template('admin.html',ss=(st[0]+st[1]+st[2]),mt=st[0],phd=st[1],btech=st[2])

@app.route('/changejobs',methods=['GET','POST'])
def b():
    # return(request.form['title'])
    # db=col1.alumni_portal

    # col1=db.events
    dic={}
    dic['jobtitle']=str(request.form['jobtitle'])
    dic['jobtext']=str(request.form['jobtext'])
    col2.insert(dic)
    # user_info = gmail.get_user_info()
    st=stats()
    return  url_for('index')
    return render_template('admin.html',ss=(st[0]+st[1]+st[2]),mt=st[0],phd=st[1],btech=st[2])
# @app.route('/changetestimonial',methods=['GET','POST'])
# def b():
#     # return(request.form['title'])
#     # db=col1.alumni_portal

#     # col1=db.events
#     dic={}
#     dic['text']=str(request.form['testtext'])
#     dic['name']=str(request.form['testname'])
#     dic['job']=str(request.form['testjob'])

#     col4.insert(dic)
#     user_info = gmail.get_user_info()
#     return render_template('admin.html',piclink=user_info['picture'])
@app.route('/data',methods=['GET','POST'])
def data():
    fields=['Birth date', 'Full Name', 'Roll Number 1' ,'Employer 1' ,'Designation 1' ,'Employer 2' ,'Designation 2' ,'Mobile Number' ,'Email ID' ,'Class Year 1' ,'Degree 1' ,'email2' ]
    ar=[]
    for i in col3.find():
        ar.append(i)
    return render_template('Data.html',arr=ar,field=fields)



@app.route('/profile')
def sa():
    if 'piclink' in request.cookies:
        email=request.cookies.get('email')
        name=request.cookies.get('name')
        piclink=request.cookies.get('piclink')
        surname=request.cookies.get('surname')

        for i in col3.find():
            if i['Email ID']==email:
                print('hey')
                emp1=i['Employer 1']
                des1=i['Designation 1']
                emp2=i['Employer 2']
                des2=i['Designation 2']
                rollno=i['Roll Number 1']
                bdate=i['Birth date']
                cont=str(i['Mobile Number'])
                print(cont)
                deg=str(i['Degree 1'])
                cly=i['Class Year 1']

                break
        response=make_response(render_template('Profile.html',piclink=piclink,name=name+' '+surname,bdate=str(bdate),emp1=emp1,des1=des1,emp2=emp2,des2=des2,rollno=rollno,cly=cly,cont=cont,deg=deg))  
        response.set_cookie('email',email,expires=expire_date)
        response.set_cookie('name',name,expires=expire_date)
        response.set_cookie('piclink',piclink,expires=expire_date)
        response.set_cookie('surname',surname,expires=expire_date)


        return response
        return render_template('Profile.html',piclink=piclink,name=name+' '+surname,bdate=str(bdate),emp1=emp1,des1=des1,emp2=emp2,des2=des2,rollno=rollno,cly=cly,cont=cont,deg=deg)
    else:

        ok=0
        if gmail.is_logged_in():
            user_info = gmail.get_user_info()
            name=user_info['given_name']
            surname=user_info['family_name']
            piclink=user_info['picture']
            email=user_info['email']
            for jj in col3.find():
                if jj['Email ID']==email:
                    ok=1
            if ok==0:
                # myquery = { }
                newvalues=  {"Email ID": email  ,"Birth date" : None, "Full Name" : str(name+surname), "Roll Number 1" : None, "Employer 1" : None, "Designation 1" : None, "Employer 2" : None, "Designation 2" : None, "Mobile Number" : None, "email2" : None, "Class Year 1" : None, "Degree 1" : None} 
                col3.insert_one(newvalues)
        for i in col3.find():
            if i['Email ID']==email:
                print('hey')
                emp1=i['Employer 1']
                des1=i['Designation 1']
                emp2=i['Employer 2']
                des2=i['Designation 2']
                rollno=i['Roll Number 1']
                bdate=i['Birth date']
                cont=str(i['Mobile Number'])
                print(cont)
                deg=str(i['Degree 1'])
                cly=i['Class Year 1']

                break
        response=make_response(render_template('Profile.html',piclink=piclink,name=name+' '+surname,bdate=str(bdate),emp1=emp1,des1=des1,emp2=emp2,des2=des2,rollno=rollno,cly=cly,cont=cont,deg=deg))  
        response.set_cookie('email',email,expires=expire_date)
        response.set_cookie('name',name,expires=expire_date)
        response.set_cookie('piclink',piclink,expires=expire_date)
        response.set_cookie('surname',surname,expires=expire_date)

        return response
        return render_template('Profile.html',piclink=piclink,name=name+' '+surname,bdate=str(bdate),emp1=emp1,des1=des1,emp2=emp2,des2=des2,rollno=rollno,cly=cly,cont=cont,deg=deg)

@app.route('/profile' ,methods=['POST'])
def funch():
    if 'piclink' in request.cookies:
        email=request.cookies.get('email')
        name=request.cookies.get('name')
        piclink=request.cookies.get('piclink')
        surname=request.cookies.get('surname')
        for i in col3.find():
            if i['Email ID']==email:
                print('hey')
                # i['Employer 2']=request.form['emp2']
                emp1=str(request.form.get('emp1'))
                emp2=str(request.form.get('emp2'))
                des1=str(request.form.get('des1'))
                des2=str(request.form.get('des2'))
                # email2=str(request.form.get('email2'))
                name1=str(request.form.get('name1'))
                rollno=str(request.form.get('rollno'))
                bdate=str(request.form.get('bdate'))
                cont=str(request.form.get('cont'))
                # cont=cont.replace(' ','%')
                print(cont)
                cly=str(request.form.get('cly'))
                deg=str(request.form.get('deg'))

                myquery = { "Email ID": email }
                newvalues = { "$set": {"Birth date" : bdate, "Full Name" : name1, "Roll Number 1" : rollno, "Employer 1" : emp1, "Designation 1" : des1, "Employer 2" : emp2, "Designation 2" : des2, "Mobile Number" : cont, "Email ID" : email, "Class Year 1" : cly, "Degree 1" : deg} }
                col3.update_one(myquery, newvalues)
                # return(str(name1+" "+emp1+" " +des1+" "+emp2+" "+des2+" "+" "+rollno+" "+bdate))


                # col3.update_one({"Email ID":email}, {'Employer 2' : str(request.form['emp2']) } )
        #         return render_template([])
        for i in col3.find():
            if i['Email ID']==email:
                print('hey')
                emp1=i['Employer 1']
                des1=i['Designation 1']
                emp2=i['Employer 2']
                des2=i['Designation 2']
                rollno=i['Roll Number 1']
                bdate=i['Birth date']
                cont=str(i['Mobile Number'])
                print(cont)
                deg=str(i['Degree 1'])
                cly=i['Class Year 1']
                break
        # return render_template('i.html')
        response=make_response(render_template('Profile.html',piclink=piclink,name=name+' '+surname,bdate=str(bdate),emp1=emp1,des1=des1,emp2=emp2,des2=des2,rollno=rollno,cly=cly,cont=cont,deg=deg))  
        response.set_cookie('email',email,expires=expire_date)
        response.set_cookie('name',name,expires=expire_date)
        response.set_cookie('piclink',piclink,expires=expire_date)
        response.set_cookie('surname',surname,expires=expire_date)
        return response
        return render_template('Profile.html',piclink=piclink,name=name+' '+surname,bdate='11-12-2000',emp1=emp1,des1=des1,emp2=emp2,des2=des2,rollno=rollno)

        
    else:
    
        if gmail.is_logged_in():
            user_info = gmail.get_user_info()
            # user_info=dic
            name=user_info['given_name']
            surname=user_info['family_name']
            piclink=user_info['picture']
            email=user_info['email']
        for i in col3.find():
            if i['Email ID']==email:
                print('hey')
                # i['Employer 2']=request.form['emp2']
                emp1=str(request.form.get('emp1'))
                emp2=str(request.form.get('emp2'))
                des1=str(request.form.get('des1'))
                des2=str(request.form.get('des2'))
                # email2=str(request.form.get('email2'))
                name1=str(request.form.get('name1'))
                rollno=str(request.form.get('rollno'))
                bdate=str(request.form.get('bdate'))
                cont=str(request.form.get('cont'))
                # cont=cont.replace(' ','%')
                print(cont)
                cly=str(request.form.get('cly'))
                deg=str(request.form.get('deg'))

                myquery = { "Email ID": email }
                newvalues = { "$set": {"Birth date" : bdate, "Full Name" : name1, "Roll Number 1" : rollno, "Employer 1" : emp1, "Designation 1" : des1, "Employer 2" : emp2, "Designation 2" : des2, "Mobile Number" : cont, "Email ID" : email, "Class Year 1" : cly, "Degree 1" : deg} }
                col3.update_one(myquery, newvalues)
                # return(str(name1+" "+emp1+" " +des1+" "+emp2+" "+des2+" "+" "+rollno+" "+bdate))


                # col3.update_one({"Email ID":email}, {'Employer 2' : str(request.form['emp2']) } )
        #         return render_template([])
        for i in col3.find():
            if i['Email ID']==email:
                print('hey')
                emp1=i['Employer 1']
                des1=i['Designation 1']
                emp2=i['Employer 2']
                des2=i['Designation 2']
                rollno=i['Roll Number 1']
                break
        # return render_template('i.html')
        response=make_response(render_template('Profile.html',piclink=piclink,name=name+' '+surname,bdate=str(bdate),emp1=emp1,des1=des1,emp2=emp2,des2=des2,rollno=rollno,cly=cly,cont=cont,deg=deg))  
        response.set_cookie('email',email,expires=expire_date)
        response.set_cookie('name',name,expires=expire_date)
        response.set_cookie('piclink',piclink,expires=expire_date)
        response.set_cookie('surname',surname,expires=expire_date)
        return response
        return render_template('Profile.html',piclink=piclink,name=name+' '+surname,bdate='11-12-2000',emp1=emp1,des1=des1,emp2=emp2,des2=des2,rollno=rollno)

@app.route('/events',methods=['GET','POST'])
def events():
    a=[]
    for jj in col1.find():
            kk=jj
            a.append(kk)
    return render_template('events.html',eventname=a[-1]['title'],eventtext=a[-1]['text'],eventname1=a[-2]['title'],eventtext1=a[-2]['text'],eventname2=a[-3]['title'],eventtext2=a[-3]['text'])



@app.route('/donations',methods=['GET','POST'])
def donations():
    # return('s')
    return render_template('Donations.html',don=don)