from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime, re

# Create your models here.

PROGRAM_OF_STUDY = (
	('BIO_ENG','Bioengineering, BS'),
	('APPLIED_CS', 'Applied Computer Science, BS'),
	('COMPUTER_SCIENCE_BS', 'Computer Science, BS'),
	('COMPUTER_ENGINEERING_BS', 'Computer Engineering, BS'),
	)

class Student(models.Model):
	# This line is required. Links Student to a User model instance.
	user = models.OneToOneField(User,to_field='username', related_name="student", primary_key=True, on_delete=models.CASCADE, null=False, blank=True)
	# sid = models.CharField("Gnumber",primary_key=True, max_length=10)
	program_of_study = models.CharField(max_length=50, choices = PROGRAM_OF_STUDY, default='Computer Science, BS')
	
	def __str__(self):
		return '%s %s ' % (self.user.username, self.program_of_study)
	def get_absolute_url(self):
		return reverse('myprofile', kwargs={"username": self.user.username})

	
GRADING_CHART = (
		(0.00, 'S = Satisfactory/No Credit'),
		(4.00, 'A+ = 4.0'),
		(4.00, 'A = 4.0'),
		(3.67,'A- = 3.67'),
		(3.33,'B+ = 3.33'),
		(3.00,'B = 3.00'),
		(2.67,'B- = 2.67'),
		(2.33,'C+ = 2.33'),
		(2.00, 'C = 2.00'),
		(1.67, 'C- = 1.67'),
		(1.00, 'D = 1.00'),
		(0.00, 'F = 0.00'),
		)


SEMESTER = (
		('Fall', "Fall"),
		('Spring', "Spring"),
		('Summer', "Summer"),
	)

YEAR_CHOICES = []
for r in range(2010, (datetime.datetime.now().year+10)):
    YEAR_CHOICES.append((r,r))


class ResultSet(models.Model):
	id = models.IntegerField(primary_key=True)  # AutoField?
	timestamp = models.DateTimeField()
	alpha = models.FloatField(blank=True, null=True)  # This field type is a guess.
	beta = models.FloatField(blank=True, null=True)  # This field type is a guess.
	iterations = models.FloatField(blank=True, null=True)  # This field type is a guess.
	num_topics = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return '%d ' % (self.id)
	class Meta:
		db_table = 'result_set'

class gmu_cs_courses(models.Model):
	id = models.IntegerField(primary_key=True)  # AutoField?
	number = models.IntegerField()
	title = models.CharField(db_column='title',max_length=50,blank=True, null=True)
	description = models.CharField(db_column='description',max_length=350,blank=True, null=True)
	# description_raw = models.CharField(db_column='description_raw',max_length=350,blank=True, null=True)
	
	def _get_cid(self):
		return 'CS' + str(self.number)
	cid = property(_get_cid)

	def __str__(self):
		return '%d %d %s ' % (self.id, self.number, self.title)
	class Meta:
		db_table = 'gmu_cs_courses'

class Topic(models.Model):
	id = models.IntegerField(primary_key=True)
	topic_id = models.IntegerField(default =0 )
	words = models.CharField(db_column='words',max_length=350,blank=True, null=True)
	result_set_id = models.ForeignKey(ResultSet, db_column="result_set_id", default=0)
	
	def __str__(self):
		return '%d %s ' % (self.topic_id, self.words)
	class Meta:
		db_table = 'topic'
		unique_together = ('topic_id', 'result_set_id')

class gmu_cs_course_topic_association(models.Model):
	id = models.IntegerField(primary_key=True)
	topic_id = models.IntegerField(db_column='topic_id',default=0)
	result_set_id = models.IntegerField(db_column='result_set_id', default=0)
	proportion = models.FloatField(blank=True, null=True)
	course_id = models.ForeignKey(gmu_cs_courses, default='0', db_column='course_id' )
	
	def _get_cid(self):
		return 'CS' + str(self.course_id.number)
	cid = property(_get_cid)
	
	def __str__(self):
		return '%d %d' %  (self.course_id.id, self.topic_id)
	class Meta:
		db_table = 'gmu_cs_course_topic_association'
		unique_together = ('course_id', 'topic_id', 'result_set_id')

class AllGmuCourses(models.Model):
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
	schedule_type = models.CharField(db_column='Schedule_Type', max_length=100,blank=True, null=True)  
	hours_of_lect_perweek = models.IntegerField(default=3, blank=True, null=True)
	hours_of_lab_perweek = models.IntegerField(default=0, blank=True, null=True)
	when_offer = models.CharField(max_length=50, default="See GMU Catalog")
	notes = models.CharField(db_column='Notes', max_length=100, blank=True, null=True)  # Field name made lowercase.
	grading = models.CharField(db_column='Grading', max_length=50,blank=True, null=True)  # Field name made lowercase.
	corequisite = models.CharField(db_column='Corequisite', max_length=50, blank=True, null=True)

	def __str__(self):
		return '%s %s ' % (self.course_id, self.title)
	class Meta:
		db_table = 'all_courses'

class csbs_course(models.Model):
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
	schedule_type = models.CharField(db_column='Schedule_Type', max_length=100,blank=True, null=True)  
	hours_of_lect_perweek = models.IntegerField(default=3, blank=True, null=True)
	hours_of_lab_perweek = models.IntegerField(default=0, blank=True, null=True)
	when_offer = models.CharField(max_length=50, default="See GMU Catalog")
	notes = models.CharField(db_column='Notes', max_length=100, blank=True, null=True)  # Field name made lowercase.
	grading = models.CharField(db_column='Grading', max_length=50,blank=True, null=True)  # Field name made lowercase.
	corequisite = models.CharField(db_column='Corequisite', max_length=50, blank=True, null=True)
	status = models.CharField(max_length=10)

	def _get_number(self):
		strcid = str(self.cid)
		return int(re.search(r'\d+', strcid).group())
	number = property(_get_number)

	def __str__(self):
		return '%s %s ' % (self.course_id, self.title)
	class Meta:
		db_table = 'csbs_course'


class Enroll(models.Model):
	student = models.ForeignKey(User,to_field='username', on_delete=models.CASCADE)
	course_id = models.ForeignKey(AllGmuCourses, on_delete=models.CASCADE)
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

class Interest(models.Model):
	student = models.ForeignKey(User,to_field='username', on_delete=models.CASCADE)
	course_id = models.ForeignKey(csbs_course,to_field='cid', on_delete=models.CASCADE)
	def __str__(self):
		return '%s %s' % (self.student.username, self.course_id)

	class Meta:
		unique_together =("student","course_id")


class Plan(models.Model):
	student = models.ForeignKey(User,to_field='username', on_delete=models.CASCADE)
	course_id = models.ForeignKey(csbs_course,to_field='cid', on_delete=models.CASCADE)
	semester = models.CharField(max_length=6, choices=SEMESTER, default = 'Fall' )
	year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
	sem_year = models.CharField(max_length=15, null=True)
	predicted_grade = models.FloatField(null = True)

	def __str__(self):
		return '%s %s %s %d' % (self.student.username, self.course_id, self.semester, self.year)

	class Meta:
		unique_together =("student","course_id")
