from django import forms
from courseinfo.models import Instructor, Section, Student, Semester, Course, Registration


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = "__all__"

    def clean_first_name(self):
        # for clean the space accidentally created by users
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            return self.cleaned_data['disambiguator']
        else:
            return self.cleaned_data['disambiguator'].strip()


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = "__all__"

    def clean_section_name(self):
        # for clean the space accidentally created by users
        return self.cleaned_data['section_name'].strip()


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def clean_first_name(self):
        # for clean the space accidentally created by users
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            return self.cleaned_data['disambiguator']
        else:
            return self.cleaned_data['disambiguator'].strip()


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = "__all__"

    # It seems following code is useless
    # def clean_period_name(self):
    #     # for clean the space accidentally created by users
    #     return self.cleaned_data['semesters.period_name'].strip()
    #
    # def clean_year(self):
    #     return self.cleaned_data['semesters.year'].strip()


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

    def clean_course_name(self):
        # for clean the space accidentally created by users
        return self.cleaned_data['course_name'].strip()

    def clean_course_number(self):
        # for clean the space accidentally created by users
        return self.cleaned_data['course_number'].strip()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
