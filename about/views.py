from django.shortcuts import render

def about(request):
	courses = [
		('img/advanced-courses.jpg', 'fas fa-graduation-cap', 'Advanced Courses', 'Dive deep into language intricacies and advanced communication skills with our specialized courses.'), 
		('img/intermediate-courses.jpg', 'fas fa-graduation-cap', 'Intermediate Courses', 'Build on your existing language foundation and enhance your proficiency with our intermediate courses.'), 
		('img/beginner-courses-3.jpg', 'fas fa-graduation-cap', 'Beginner Courses', 'Lay a solid foundation for your language journey with our beginner-friendly courses designed to make learning engaging and effective.'), 
		('img/group-lessons.jpg', 'fas fa-users', 'Group Lessons', 'Collaborate and learn in a supportive group setting, fostering a sense of community and shared progress.'), 
		('img/private-lessons.jpg', 'fas fa-user', 'Private Lessons', 'Receive personalized attention and guidance from our expert instructors with one-on-one private lessons.'), 
		('img/adult-courses.jpg', 'fas fa-user', 'Adult Courses', 'Tailored for adult learners, our courses cater to the specific needs and goals of individuals at all proficiency levels.'), 
		('img/classes-for-children.jpg', 'fas fa-child', 'Classes for Children', 'Nurture a love for languages in young minds with our engaging and age-appropriate language classes for children.'), 
		('img/academic-support-for-each-level(1).jpg', 'fas fa-book', 'Academic Support for Each Level', 'Our commitment to your success goes beyond the classroom. Benefit from academic support tailored to your specific proficiency level.'),
	]
	teammembers = [
		('1', 'Instructor Name', 'Designation'), 
		('2', 'Instructor Name', 'Designation'), 
		('3', 'Instructor Name', 'Designation'), 
		('4', 'Instructor Name', 'Designation'),
	]
	return render(request, 'about/about.html', {'courses': courses, 'teammembers': teammembers})