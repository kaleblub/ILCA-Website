from django.shortcuts import render

def about(request):
	courses_and_info = {
		'Advanced Courses':'Dive deep into language intricacies and advanced communication skills with our specialized courses.', 
		'Intermediate Courses':'Build on your existing language foundation and enhance your proficiency with our intermediate courses.', 
		'Beginner Courses':'Lay a solid foundation for your language journey with our beginner-friendly courses designed to make learning engaging and effective.', 
		'Group Lessons':'Collaborate and learn in a supportive group setting, fostering a sense of community and shared progress.', 
		'Private Lessons':'Receive personalized attention and guidance from our expert instructors with one-on-one private lessons.', 
		'Adult Courses':'Tailored for adult learners, our courses cater to the specific needs and goals of individuals at all proficiency levels.', 
		'Classes for Children':'Nurture a love for languages in young minds with our engaging and age-appropriate language classes for children.', 
		'Academic Support for Each Level':'Our commitment to your success goes beyond the classroom. Benefit from academic support tailored to your specific proficiency level.'}
	teammembers = [
		('1', 'Instructor Name', 'Designation'), 
		('2', 'Instructor Name', 'Designation'), 
		('3', 'Instructor Name', 'Designation'), 
		('4', 'Instructor Name', 'Designation'),
	]
	return render(request, 'about/about.html', {'courses_and_info': courses_and_info, 'teammembers': teammembers})