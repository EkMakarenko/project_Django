from django.urls import reverse
from django.views import generic

from comment.form import CommentForm


# Create your views here.

class CommentCreateView(generic.CreateView):
    template_name = 'comment/comment_create.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('hotel-detail')

    def form_valid(self, form):
        form.instance.hotel_id = self.kwargs.get('hotel_id')
        return super().form_valid(form)

