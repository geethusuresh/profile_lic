from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


class HomeView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['user_name'] = "geethu"
        return context

class Login(View):

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']
        print "username = ", username
        print "password = ", password
        return HttpResponseRedirect("/")


class Logout(View):

    def get(self, request):

        logout(request.user)

class ContactView(FormView):

    form_class = ContactForm
    success_url = reverse_lazy('contact')
    template_name = 'contact.html'

    def form_valid(self, form):
        contact_name = self.form.cleaned_data['contact_name']
        contact_email = self.form.cleaned_data['contact_email']
        form_content = self.form.cleaned_data['content']

        template = get_template('contact_template.txt')
        context = Context({
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content
        })
        content = template.render(context)

        email = EmailMessage(
            'New contact form submission',
            content,
            'Your website ' + '',
            ['youremail@gmail.com'],
            headers = {'Reply-To': contact_email}
        )
        email.send()
        return super(ContactView, self).form_valid(form)

# from django.contrib.auth.mixins import LoginRequiredMixin

# class SecretView(LoginRequiredMixin, TemplateView):
#     template_name = "secret.html"



