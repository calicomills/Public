from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from ads.models import Ad   


class AdListView(ListView):
    model = Ad
    def get_queryset(self):
        """Return Ads """
        return Ad.objects.order_by('id')


class AdDetailView(DetailView):
    """
    Sub-class the DetailView to pass the request to the form.
    """
    model = Ad
class AdCreateView(LoginRequiredMixin, CreateView):
    """
    Sub-class of the CreateView to automatically pass the Request to the Form
    and add the owner to the saved object.
    """
    model = Ad
    fields = ['title','price','text']
    # Saves the form instance, sets the current object for the view, and redirects to get_success_url().
    def form_valid(self, form):
        print('form_valid called')
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(AdCreateView, self).form_valid(form)

class AdUpdateView(LoginRequiredMixin, UpdateView):
    """
    Sub-class the UpdateView to pass the request to the form and limit the
    queryset to the requesting user.
    """
    model = Ad
    fields = ['title','price','text']
    def get_queryset(self):
        print('update get_queryset called')
        """ Limit a User to only modifying their own data. """
        qs = super(AdUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class AdDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class the DeleteView to restrict a User from deleting other
    user's data.
    """
    model = Ad
    def get_queryset(self):
        print('delete get_queryset called')
        qs = super(AdDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)
