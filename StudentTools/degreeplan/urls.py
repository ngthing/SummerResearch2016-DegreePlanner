from django.conf.urls import url

from .views import (
	signup, login, auth_view, loggedin, invalid_login, 
	logout, home, user_profile, get_transcript, transcript,
	program_of_study, contact_us,cs_bscourses, addToFolder, folder,
	removeFromFolder,addToPlanner,degreePlanner, all_courses
	)

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^contact_us/$', contact_us, name='contact_us'),
	url(r'^signup/$', signup, name='signup'),
	url(r'^login/$', login, name='login'),
	url(r'^auth/$', auth_view, name='auth_view'),
	url(r'^loggedin/$', loggedin, name='loggedin'),
	url(r'^invalid/$', invalid_login, name='invalid_login'),
	url(r'^logout/$', logout, name='logout'),
	url(r'^myprofile/$', user_profile, name='myprofile'),
	url(r'^myprofile/(?P<username>)/$', user_profile, name='myprofile'),
	url(r'^transcript/$', transcript, name='transcript'),
	url(r'^get_transcript/$', get_transcript, name='get_transcript'),
	url(r'^program_of_study/$', program_of_study, name='program_of_study'),
	url(r'^cs_bscourses/$', cs_bscourses, name='cs_bscourses'),
	url(r'^addToFolder/$', addToFolder, name='addToFolder'),
	url(r'^folder/$', folder, name='folder'),
	url(r'^removeFromFolder/$', removeFromFolder, name='removeFromFolder'),
	url(r'^addToPlanner/$', addToPlanner, name='addToPlanner'),
	url(r'^degreeplanner/$', degreePlanner, name='degreePlanner'),
	url(r'^all_courses/$', all_courses, name='all_courses'),
]