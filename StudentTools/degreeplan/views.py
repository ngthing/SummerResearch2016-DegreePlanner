from django.shortcuts import render, render_to_response, get_list_or_404, Http404, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from .forms import UserForm, StudentForm, EnrollForm
from .models import Student, Enroll, Interest, Plan,AllGmuCourses, gmu_cs_course_topic_association, Topic, csbs_course
from django.contrib.auth import authenticate, login, logout
from collections import defaultdict, OrderedDict

# Create your views here.

def home(request):
	return render(request, 'base.html', {"current_user" : request.user})

def contact_us(request):
	return render(request, 'contact_us.html', {"current_user" : request.user})

def login(request):
	return render(request, 'login.html')

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = authenticate(username=username, password=password)
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/degreeplan/loggedin')
	else:
		return HttpResponseRedirect('/degreeplan/invalid')

def loggedin(request):
	return render_to_response('loggedin.html',{'current_user': request.user})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

def signup(request):

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and StudentForm.
		user_form = UserForm(data=request.POST)
		profile_form = StudentForm(data=request.POST)

        # If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

			# Now sort out the Student instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user

        
			# Now we save the Student model instance.
			profile.save()

			# Update our variable to tell the template registration was successful.
			registered = True

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print (user_form.errors, profile_form.errors)

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		profile_form = StudentForm()

	# Render the template depending on the context.
	return render(request, 
			'signup.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_profile(request):
	if request.user.is_authenticated:
	# Do something for authenticated users.
		context = {
		"current_user" : request.user,
		"student": request.user.student}
		return render(request, 'myprofile.html', context)
	else:
		return render(request, 'login.html')

def get_transcript(request):
	if request.method == 'POST':
		enroll_form = EnrollForm(data=request.POST)
		if enroll_form.is_valid():
			enrollment = enroll_form.save(commit= False)
			enrollment.student = request.user
			enrollment.save()
		else:
			print (enroll_form.errors)
	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		enroll_form = EnrollForm()
	# Render the template depending on the context.
	return render(request, 
			'get_transcript_data.html',
			{'enroll_form': enroll_form, 'current_user': request.user,})

#Show student's transcript information. The taken courses are ordered by year/semester
def transcript(request):
	transcript_added = True
	if request.user.is_authenticated:
	# Do something for authenticated users
		taken_courses = list(Enroll.objects.filter(student=request.user.username))
		if not taken_courses:
			transcript_added = False
		# Sort the Enrollments by year order, and by semester order in each year (e.g. SP->SUM->F)
		# Create a list of all (enrollment.year, enrollment) tuples 
		enrollments_by_year = []
		for e in taken_courses:
			t = [ e.year, e]
			enrollments_by_year.append(t)
		# Create a defautdict that group the enrollments in enrollments_by_year by year
		d = defaultdict(list)
		for y, e in enrollments_by_year:
			d[y].append(e)
		# Sort d (e.g. enrollment in 2015 before enrollment in 2015)
		od = OrderedDict(sorted(d.items(),key=lambda t:t[0]))
		context = {
		"takencourses_ordered_by_year": od,
		"transcript_added": transcript_added,
		"taken_courses":taken_courses,
		"current_user" : request.user,
		"student": request.user.student}
		return render(request, 'transcript.html', context)
	else:
		return render(request, 'login.html')

def program_of_study(request):
	return render(request, 'programs_of_study.html', {"current_user" : request.user})

def all_courses(request):
	courses = get_list_or_404(AllGmuCourses)
	context = {
		"courses":courses,
		"current_user" : request.user,
		}
	return render(request, 'all_courses.html', context)

# This view will show the list of courses related to Computer Science,BS degree, the description of the courses and related topics. 
# This view also indicates the courses that the user had already taken (if user is login).
def cs_bscourses(request):
	courses = get_list_or_404(csbs_course)
	for c in courses:
		cnumber = c.number 
		cts = gmu_cs_course_topic_association.objects.filter(course_id__number=cnumber)
		if cts:
			c_related_topics = []
			for ct in cts:
				topic = Topic.objects.get(topic_id=ct.topic_id, result_set_id=ct.result_set_id)
				topic_words = topic.words.split(",")
				for t in topic_words:
					if t not in c_related_topics:
						c_related_topics.append(t)	
			related_topics = ",".join(c_related_topics)
			c.related_topics = related_topics
			c.save()
	taken_cids = []
	added_cids =[]
	if request.user.is_authenticated:
		taken_courses = list(Enroll.objects.filter(student=request.user.username))
		added_to_folder_courses = list(Interest.objects.filter(student=request.user.username))
		for c in taken_courses:
			taken_cids.append(c.course_id.cid)
		for c in added_to_folder_courses:
			added_cids.append(c.course_id.cid)

	context = {
		"added_cids": added_cids,
		"taken_cids":taken_cids,
		"courses":courses,
		"current_user" : request.user,
		}
	return render(request, 'cs_bscourses.html', context)

def addToFolder(request):
	if request.user.is_authenticated:
		cid = None
		if request.method == 'POST':
			cid = request.POST['courseid']
			if cid: 
				toAddCourse = get_object_or_404(csbs_course, cid = cid)
				if toAddCourse:
					courseToFolder = Interest(student= request.user, course_id = toAddCourse)
					courseToFolder.save()
		return HttpResponse(toAddCourse)
	
# This view shows list of courses that user added to folder. 
def folder(request):
	folder_empty = False
	has_planned_course = False
	if request.user.is_authenticated:
	# Do something for authenticated users
		added_courses = list(Interest.objects.filter(student=request.user.username))
		if not added_courses:
			folder_empty = True
		planned_course = list(Plan.objects.filter(student=request.user.username))
		if planned_course:
			has_planned_course =True
			planned_course_id =[]
			for pc in planned_course:
				# print(pc.course_id)
				planned_course_id.append(pc.course_id)
		context = {
		"folder_empty": folder_empty,
		"added_courses":added_courses,
		"current_user" : request.user,
		}
		if has_planned_course:
			context["planned_course_id"] = planned_course_id
		return render(request, 'folder.html', context)
	else:
		return render(request, 'login.html')

def removeFromFolder(request):
	cid = None
	if request.method == 'POST':
		cid = request.POST['course_id']
		if cid: 
			toRemoveCourse = get_object_or_404(Interest, course_id = cid)
			if toRemoveCourse:
				toRemoveCourse.delete()
	return HttpResponse(toRemoveCourse.course_id)

def addToPlanner(request):
	cid = None
	if request.method == 'POST':
		cid = request.POST['course_id']
		sem_year= request.POST['sem_year']
		if cid and sem_year: 
			semyearsplit = sem_year.split(" ")
			semester = semyearsplit[0]
			year = semyearsplit[1]
			toAddCourse = get_object_or_404(csbs_course, cid = cid)
			if toAddCourse:
				courseToPlanner = Plan(student= request.user, course_id = toAddCourse,
				 semester=semester, year= int(year), sem_year = sem_year)
				courseToPlanner.save()
	return HttpResponse(toAddCourse)

# This view shows taken courses and courses the student plan to take in the future. 
# Note: This view hasn't implemented the deletion of planned courses. 
def degreePlanner(request):
	has_enrolled_course = False
	has_planned_course = False
	if request.user.is_authenticated:
	# For authenticated users, get all the courses user had taken
		enrolled_courses = list(Enroll.objects.filter(student=request.user.username))
		if enrolled_courses:
			has_enrolled_course = True
		enrolled_year_sem = []
		for e in enrolled_courses:
			t = [e.year, e.semester] # create tuples of enrollment's year and semester
			if t not in enrolled_year_sem: 
				enrolled_year_sem.append(t)
		dict_enrolled_year_sem = defaultdict(list)
		for y, s in enrolled_year_sem: # create a dictionary which keys are year, and items in each year are semesters 
			dict_enrolled_year_sem[y].append(s) 
		# order year in ascending order
		ordered_dict_enrolled_year_sem = OrderedDict(sorted(dict_enrolled_year_sem.items(), key=lambda t:t[0]))

		enrollments_by_year = []
		for e in enrolled_courses:
			t = [ e.year, e]
			enrollments_by_year.append(t)
		# Create a defautdict that group the enrollments in enrollments_by_year by year
		dict_enrollments_by_year = defaultdict(list)
		for y, e in enrollments_by_year:
			dict_enrollments_by_year[y].append(e)
		# Sort d (e.g. enrollment in 2015 before enrollment in 2016)
		ordered_dict_enrollments_by_year = OrderedDict(sorted(dict_enrollments_by_year.items(),key=lambda t:t[0]))

	# For authenticated users, get all the courses the user had added to planner
		planned_courses = list(Plan.objects.filter(student=request.user.username))
		if planned_courses:
			has_planned_course = True
		
		planned_year_sem = []
		for e in planned_courses:
			t = [e.year, e.semester]
			if t not in planned_year_sem:
				planned_year_sem.append(t)
		dict_planned_year_sem = defaultdict(list)
		for y, s in planned_year_sem:
			dict_planned_year_sem[y].append(s)
		# order year in ascending order
		ordered_dict_planned_year_sem = OrderedDict(sorted(dict_planned_year_sem.items(), key=lambda t:t[0]))
		plans_by_year = []
		for e in planned_courses:
			t = [ e.year, e]
			plans_by_year.append(t)
		# Create a defautdict that group the courses in planner by year
		dict_plans_by_year = defaultdict(list)
		for y, e in plans_by_year:
			dict_plans_by_year[y].append(e)
		# Sort d (e.g. courses plan in 2015 before courses plan for 2016)
		ordered_dict_plans_by_year = OrderedDict(sorted(dict_plans_by_year.items(),key=lambda t:t[0]))
		context = {
		"ordered_dict_enrolled_year_sem": ordered_dict_enrolled_year_sem,
		"has_enrolled_course": has_enrolled_course,
		"ordered_dict_enrollments_by_year": ordered_dict_enrollments_by_year,
		"enrolled_courses":enrolled_courses,
		"ordered_dict_planned_year_sem": ordered_dict_planned_year_sem,
		"has_planned_course": has_planned_course,
		"ordered_dict_plans_by_year":ordered_dict_plans_by_year,
		"planned_courses": planned_courses,
		"current_user" : request.user,
		}
		return render(request, 'degreeplanner.html', context)
	else:
		return render(request, 'login.html')
	
