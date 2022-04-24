class RegistrationDelete(View):

    def get(self, request, pk):
        registration = self.get_object(pk)
        return render(
            request,
            'courseinfo/registration_confirm_delete.html',
            {'registration': registration}
        )

    def get_object(self, pk):
        registration = get_object_or_404(
            Registration,
            pk=pk
        )
        return registration

    def post(self, request, pk):
        registration = self.get_object(pk)
        registration.delete()
        return redirect('courseinfo_registration_list_urlpattern')
