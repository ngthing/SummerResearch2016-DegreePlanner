enrollments_by_sem_year = []
for e in enrollments:
	t = [ e.sem_year, e]
	enrollments_by_sem_year.append(t)

enrollments_by_year = []
for e in enrollments:
	t = [ e.year, e]
	enrollments_by_year.append(t)

d = defautdict(list)
for sy, e in enrollments_by_sem_year:
	d[sy].append(e)

d = defaultdict(list)
for y, e in enrollments_by_year:
	d[y].append(e)
 
 sorted(d.items())

for key, value in d.items():
    for k, v in value:
        print k, v

for y, ey in d.items():
	print(y)
	e_by_sem = []
	for e in ey:
		t = [ e.sem_code, e]
		e_by_sem.append(t)
		ds = defaultdict(list)
		for sc, es in e_by_sem:
			ds[sc].append(e)
		for sc, es in ds.items():
			print(es)

# Sort the Enrollments by year order, and by semester order in each year (e.g. SP->SUM->F)
# Create a list of all (enrollment.year, enrollment) tuples 
enrollments_by_year = []
for e in enrollments:
	t = [ e.year, e]
	enrollments_by_year.append(t)
# Create a defautdict that group the enrollments in enrollments_by_year by year
d = defaultdict(list)
for y, e in enrollments_by_year:
	d[y].append(e)
# Sort d (e.g. enrollment in 2015 before enrollment in 2015)
od = OrderedDict(sorted(d.items(),key=lambda t:t[0]))
for y, ey in od.items():
	print(y)
	e_by_sem = []
	ds = defaultdict(list)
	for e in ey:
		t = [ e.sem_order, e]
		e_by_sem.append(t)
	for so, es in e_by_sem:
		ds[so].append(es)	
	ods = OrderedDict(sorted(ds.items(),key=lambda t:t[0]))
	for so, es in ods.items():
		if so == 0:
			print("\tSpring")
		elif so == 1:
			print("\tSummer")
		elif so == 2:
			print("\tFall")
		for e in es:
			print("%s Grade: %s" % (e.course_id, e.grade))
	print()


if ( thisId == 'addToPlanner') {
    	var cid , formData;
 		cid = $(this).attr("this-course-id");
 		formData = $("#dropdown-sem option:selected").text();
 		// var $this = $(this);
 		
        $.ajax(
        {
        	url: "/degreeplan/addToPlanner/", 
        	method: "POST",
        	data: 
        	{ csrfmiddlewaretoken: '{{csrf_token}}',course_id: cid, sem_year: formData},
        	success: function(data,status)
        	{
        		alert(data + "is added to your Planner\nStatus: " + status);
        		//$this.closest('tr').remove();

        	},
    	});    
enrolled_year_sem = []   
for e in enrolled_courses:
	t = [e.year, e.semester]
	if t not in enrolled_year_sem:
		enrolled_year_sem.append(t)
dict_enrolled_year_sem = defaultdict(list)
for y, s in enrolled_year_sem:
	dict_enrolled_year_sem[y].append(e)
# order year in ascending order
od = OrderedDict(sorted(dict_enrolled_year_sem.items(), key=lambda t:t[0]))
   
for y, sem in od.items():
	print(y)
	for s in sem:
		print(s)
		if s == "Spring":
			print(s)
		elif s =="Summer":
			print(s)
		elif s == "Fall":
			print(s)

writeto = open('cscid-elect1','w')
readfrom = open('cscid-elect','r')
for line in readfrom:
	fl = line.replace(' ','')
	writeto.write(fl)

writeto.close()
readfrom.close()

from degreeplan.models import gmu_cs_course_topic_association, Topic
c_topics = gmu_cs_course_topic_association.objects.filter(course_id__number=101)
c_related_topics = []
for ct in c_topics:
	topic = Topic.objects.get(topic_id=ct.topic_id, result_set_id=ct.result_set_id)
	topic_words = topic.words.split(",")
	for t in topic_words:
		if t not in c_related_topics:
			c_related_topics.append(t)
print(c_related_topics)
print(",".join(c_related_topics))

print(t.words)
print(ct.proportion)

create table csbscourse as select all_courses.* from all_courses, CSBSCourses where all_courses.cid = CSBSCourses.cid;

class Courses(models.Model):
	cid = models.CharField(primary_key=True, max_length=50, default="null")
	url = models.CharField(max_length=100, blank=True, null=True)
	catalog_year = models.CharField(max_length=50,default="2016-2017")
	course_id = models.CharField(max_length=50,default="null")
	title = models.CharField(max_length=50,blank=True, null=True)
	credits = models.IntegerField(default=3, blank=True, null=True)
	attempts = models.CharField(max_length=50, default="Limited to 2 Attempts")
	department = models.CharField(max_length=50,blank=True, null=True)
	description = models.CharField(db_column='Description', max_length=350,blank=True, null=True)  # Field name made lowercase.
	prerequisite = models.CharField(db_column='Prerequisite', max_length=50, blank=True, null=True)  # Field name made lowercase.
	corequisite = models.CharField(db_column='Corequisite', max_length=50, blank=True, null=True)  # Field name made lowercase.
	notes = models.CharField(db_column='Notes', max_length=100, blank=True, null=True)  # Field name made lowercase.
	schedule_type = models.CharField(db_column='Schedule_Type', max_length=100,blank=True, null=True)  # Field name made lowercase. This field type is a guess.
	hours_of_lect_perweek = models.IntegerField(default=3, blank=True, null=True)
	hours_of_lab_perweek = models.IntegerField(default=0, blank=True, null=True)
	grading = models.CharField(db_column='Grading', max_length=50,blank=True, null=True)  # Field name made lowercase.
	when_offer = models.CharField(max_length=50, default="See GMU Catalog")
	related_topics = models.CharField(max_length=500, blank=True, null=True)

	def _get_number(self):
		strcid = str(self.cid)
		return int(re.search(r'\d+', strcid).group())
	number = property(_get_number)

	def __str__(self):
		return '%s %s ' % (self.course_id, self.title)
	class Meta:
		db_table = 'courses'

class CSBSCourses(models.Model):
	cid = models.CharField(max_length=10)
	status = models.CharField(max_length=10)

	def __str__(self):
		return '%s %s ' % (self.cid, self.status)
	class Meta:
		db_table = 'CSBSCourses'
		
class Enrollment(models.Model):
	student = models.ForeignKey(User,to_field='username', on_delete=models.CASCADE)
	course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
	grade = models.FloatField(choices = GRADING_CHART,default= 'A+ = 4.0')
	semester = models.CharField(max_length=6, choices=SEMESTER, default = 'Fall' )
	year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
	
	def _get_sem_year(self):
		return '%s %s' % (self.semester, self.year)
	sem_year = property(_get_sem_year)

	def __str__(self):
		return '%s %s %d %s %d' % (self.student.username, self.course_id, self.grade, self.semester, self.year)

	class Meta:
		unique_together =("student","course_id")

