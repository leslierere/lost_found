from django.shortcuts import redirect, render

# dont need it anymore after refactoring in week12-part4
class ObjectCreateMixin:
    form_class = None
    template_name = ''

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)  # take us to the detail page
        else:
            # not only we get value we sent but also the error and message
            return render(request, self.template_name, {'form': bound_form})

