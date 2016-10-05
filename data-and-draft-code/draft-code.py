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


