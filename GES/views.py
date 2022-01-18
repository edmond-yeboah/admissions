from django.core import paginator
from django.shortcuts import get_object_or_404, render
from .models import school,degree_programs,hnd_programs,diploma_programs
from django.db.models import Q, query
from django.core.paginator import Paginator
from itertools import chain

#homepage view
def home(request):
    context = {} #declaring an empty list
    
    #fetching degree courses
    degree_courses = degree_programs.objects.all()[:5]
    context["courses"] = degree_courses
    
    
    #fetching schools
    allschools = school.objects.all()[:6]
    context["schools"] = allschools
    
    return render(request,"index.html",context)




def schools(request):
    context={}
    
    if request.method=="POST":
        keyword = request.POST["keyword"]
        location = request.POST["location"]
        
        #searching for schools 
        school_result = school.objects.filter(Q(name__icontains=keyword) and Q(location__icontains=location))
        if len(school_result)>0:
            paginator = Paginator(school_result,3)
            
            page_number = request.GET.get('page')
            context["schools"] = paginator.get_page(page_number)
            context["clear"] ="clear search"
        else:
            context["noo"] = "No search results"
    
    else:
        #getting all schools
        all_schools = school.objects.all()
        paginator = Paginator(all_schools,3)
        
        page_number = request.GET.get('page')
        context["schools"] = paginator.get_page(page_number)
        
    return render(request,"schools.html",context)


def courses(request):
    context={}
    
    if request.method == "POST":
        keyword = request.POST["keyword"]
        
        #getting degree programs with keyword
        degree_results = degree_programs.objects.filter(name__icontains=keyword)
        #getting hnd programs with keyword
        hnd_results = hnd_programs.objects.filter(name__icontains=keyword)
        #getting diploma programs with keyword
        dip_results = diploma_programs.objects.filter(name__icontains=keyword)
        
        all_results = degree_results.union(hnd_results).union(dip_results)
        
        if len(all_results)>0:
            paginator = Paginator(all_results,6)
            page_number = request.GET.get('page')
            context["courses"] = paginator.get_page(page_number)
            context["clear"] = "clear"
        else:
            context["nooo"] = "No search result found"
    else:
        
        #getting all course
        degree = degree_programs.objects.all()
        hnd = hnd_programs.objects.all()
        dip = diploma_programs.objects.all()
        
        all_courses = degree.union(hnd).union(dip)
        
        paginator = Paginator(all_courses,6)
        page_number = request.GET.get('page')
        context["courses"] = paginator.get_page(page_number)
        
    return render(request,"courses.html",context)


def search(request):
    context={}
    degree=True
    hnd=True
    dip=True
    
    if "query" in request.GET:
        q = request.GET["query"]
        query = q.strip()
        
        if len(query)>0:
            #searching schools using search query
            school_results = school.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query) | Q(location__icontains=query))
            print(school_results)
            #checking if results were found
            if len(school_results)>0:
                context["sch_result"] = school_results
            else:
                context["noschools"] = "No schools or courses match your search query"
                
            #searching for hnd courses
            hndresults = hnd_programs.objects.filter(Q(name__icontains=query))
            #checking if results were found
            if len(hndresults)>0:
                hnd=True
                context["hnd_result"] = hndresults
            else:
                hnd=False
                context["nohnd"] = "No hnd courses found"
                
            
            #searching for degree courses
            degreeresults = degree_programs.objects.filter(Q(name__icontains=query))
            #checking if results were found
            if len(degreeresults)>0:
                degree=True
                context["degree_result"] = degreeresults
            else:
                degree=False
                context["nodegree"] = "No degree courses found"
                
            
            #searching for diploma courses
            diplomaresults = diploma_programs.objects.filter(Q(name__icontains=query))
            #checking if results were found
            if len(diplomaresults)>0:
                dip=True
                context["diploma_result"] = diplomaresults
            else:
                dip=False
                context["nodiploma"] = "No diploma courses found"
                
            if dip==False and hnd==False and degree==False:
                context["noo"]="Nooo"
            else:
                pass
        else:
            context["noo"]="Noo"
            
    return render(request,"search.html",context)



def school_details(request):
    context={}
    
    if "sid" in request.GET:
        sid = request.GET["sid"]
        sch = school.objects.get(id=sid)
        context["sch"] = sch
        
        #getting school's degree programs
        deg = degree_programs.objects.filter(school=sch)
        print(len(deg))
        if len(deg)>0:
            if len(deg)==9:
                context["deg"] = degree_programs.objects.filter(school=sch)[:3]
                context["deg1"] = degree_programs.objects.filter(school=sch)[3:6]
                context["deg2"] = degree_programs.objects.filter(school=sch)[6:9]
                
            elif len(deg)==6:
                context["deg"] = degree_programs.objects.filter(school=sch)[:3]
                context["deg1"] = degree_programs.objects.filter(school=sch)[3:6]
            elif len(deg)==3:
                context["deg"] = degree_programs.objects.filter(school=sch)[:3]
            else:
                context["deg"] = deg
        else:
            pass
        
        #getting school's hnd programs
        hnd = hnd_programs.objects.filter(school=sch)
        if len(hnd)>0:
            context["hnd"] = hnd
        else:
            pass
        
        #getting school's diploma programs
        dip = diploma_programs.objects.filter(school=sch)
        if len(dip)>0:
            context["dip"] = dip
        else:
            pass
    return render(request,"school-details.html",context)



def course_details(request):
    context={}
    
    if "cid" in request.GET:
        cid = request.GET["cid"]
        ty = request.GET["type"]
        
        #checking where to query
        if ty=="Degree":
            #query from degree
            cou = degree_programs.objects.get(id=cid)
            context["course"] = cou
            others = degree_programs.objects.all().exclude(name=cou.name)[:5]
            context["others"] = others
        elif ty=="HND":
            #query from hnd
            cou = hnd_programs.objects.get(id=cid)
            context["course"] = cou
            others = hnd_programs.objects.all().exclude(name=cou.name)[:5]
            context["others"] = others
        elif ty=="Diploma":
            #query from diploma
            cou = diploma_programs.objects.get(id=cid)
            context["course"] = cou
            others = diploma_programs.objects.all().exclude(name=cou.name)[:5]
            context["others"] = others
        else:
            pass
    return render(request,"course-details.html",context)
