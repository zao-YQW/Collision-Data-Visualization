from django.forms import forms

from courseinfo.models import Instructor, Student


class InstructorForm(forms.ModelFrom):
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


class StudentForm(forms.ModelFrom):
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
