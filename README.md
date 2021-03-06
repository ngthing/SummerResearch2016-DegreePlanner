# DegreePlannerWebApp

This Web App is an in-process project. It was developed as part of an NSF funded Research Project:
BIGDATA: IA: DKA: Collaborative Research: Learning Data Analytics: Providing Actionable Insights to Increase College Student Success,
Link: https://nsf.gov/awardsearch/showAward?AWD_ID=1447489&HistoricalAwards=false

All data i.e. all courses (scraped from George Mason University Catalog http://catalog.gmu.edu/index.php ) and Computer Science courses' related topics used in this app are provided by other researchers.

This app currently allows:
- Student registers/logins.
- Student creates a profile, including: pursued degree (currently supported Computer Science, BS degree), transcript data.
- Student can see the remaining courses he/she needs to take to complete degree.
- Student can add a course to his/her folder to evaluate such as view predicted grade for the course, view related topics to the course (not yet supported).
- After evaluating the course, student can add to his/her planner.
- Student can view his/her degree planner.

To run the app in your local machine:
After cloning, in the directory that contains SummerResearch2016-DegreePlannerWebApp:
- Activate virtual environment:<br/>
source SummerResearch2016-DegreePlannerWebApp/bin/activate

- Inside SummerResearch2016-DegreePlannerWebApp/StudentTools, activate the server: <br/>
python manage.py runserver


![alt text](screenshots/00-sign-up.png "Sign up view")
![alt text](screenshots/01-input-enrollment-history.png "01-input-enrollment-history")
![alt text](screenshots/02-display-transcript-info.png "02-display-transcript-info")
![alt text](screenshots/03-view-degree-requirement.png "03-view-degree-requirement")
![alt text](screenshots/04-add-course-to-folder.png "04-add-course-to-folder")
![alt text](screenshots/05-view-folder.png "05-view-folder")
![alt text](screenshots/06-view-folder.png "06-view-folder")
![alt text](screenshots/07-add-course-to-planner.png "07-add-course-to-planner")
![alt text](screenshots/08-in-planner.png "08-in-planner")
![alt text](screenshots/09-view-planner.png "09-view-planner")
![alt text](screenshots/10-view-planner.png "10-view-planner")
![alt text](screenshots/11-view-plannerr.png "11-view-planner")
![alt text](screenshots/12-view-planner.png "12-view-plannerr")
