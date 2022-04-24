from django.shortcuts import render, get_object_or_404
from django.views import View

from courseinfo.forms import InstructorForm
from courseinfo.models import Instructor, Section, Course, Semester, Student, Registration

# def instructor_list_view(request):
#     instructor_list = Instructor.objects.all()  # to get the data from the corrensponding place, return: list
#     # instructor_list = Instructor.objects.none()
#     return render(request, 'courseinfo/instructor_list.html', {"instructor_list": instructor_list})
#     # render(request, name of our template, content:a dictionary stores the data we need pass to the webpage <format:{key:value, key:value,...}>)
#     # keys in the render function would be used in the corresponding html file, it should match the function's parameter(?).


class InstructorList(View):

    def get(self, request):
        return render(request, 'courseinfo/instructor_list.html', {"instructor_list": Instructor.objects.all()})


class InstructorDetail(View):

    def get(self, request, pk):
        instructor = get_object_or_404(
            Instructor,
            pk=pk
        )
        section_list = instructor.sections.all()
        return render(
            request,
            'courseinfo/instructor_detail.html',
            {'instructor': instructor, 'section_list': section_list}
        )


class InstructorCreate(ObjectCreateMixin,View):
    form_class = InstructorForm
    template_name = 'corseinfo/instructor_form.html'


class SectionList(View):

    def get(self, request):
        return render(request, 'courseinfo/section_list.html', {"section_list": Section.objects.all()})


class SectionDetail(View):

    def get(self, request, pk):
        section = get_object_or_404(Section, pk=pk)
        semester = section.semester
        course = section.course
        instructor = section.instructor
        registration_list = section.registrations.all()

        return render(request,
                      'courseinfo/section_detail.html',
                      {"section": section,
                       'semester': semester,
                       'course': course,
                       'instructor': instructor,
                       'registration_list': registration_list})


class CourseList(View):

    def get(self, request):
        return render(request, 'courseinfo/course_list.html', {"course_list": Course.objects.all()})


class CourseDetail(View):

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course_number = course.course_number
        course_name = course.course_name
        section_list = course.sections.all()
        return render(request,
                      'courseinfo/course_detail.html',
                      {"course": course,
                       "course_number": course_number,
                       "course_name": course_name,
                       'section_list': section_list})


class SemesterList(View):

    def get(self, request):
        return render(request, 'courseinfo/semester_list.html', {"semester_list": Semester.objects.all()})


class SemesterDetail(View):

    def get(self, request, pk):
        semester = get_object_or_404(Semester, pk=pk)
        section_list = semester.sections.all()

        return render(request,
                      'courseinfo/semester_detail.html',
                      {'semester': semester,
                       "section_list": section_list})

class StudentList(View):

    def get(self, request):
        return render(request, 'courseinfo/student_list.html', {"student_list": Student.objects.all()})


class StudentDetail(View):

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        first_name = student.first_name
        last_name = student.last_name
        disambiguator = student.disambiguator
        registration_list = student.registrations.all()
        return render(request,
                      'courseinfo/student_detail.html',
                      {"student": student,
                       'first_name': first_name,
                       'last_name': last_name,
                       'disambiguator': disambiguator,
                       'registration_list': registration_list})


class RegistrationList(View):

    def get(self, request):
        return render(request, 'courseinfo/registration_list.html', {"registration_list": Registration.objects.all()})


class RegistrationDetail(View):

    def get(self, request, pk):
        registration = get_object_or_404(Registration, pk=pk)
        student = registration.student
        section = registration.section
        return render(request,
                      'courseinfo/registration_detail.html',
                      {"registration": registration,
                       'student': student,
                       'section': section})

