from django.shortcuts import redirect, render


class ObjectCreateMixin:
    form_class = None
    template_name = ''
    # when you send a get, server will send a blank form
    def get(self, request):
        return render(request, self.template_name, {'form':self.form_class})

    # when you send a post, server will try to send the created form
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            return render(request, self.template_name, {'form':self.bound_form})
