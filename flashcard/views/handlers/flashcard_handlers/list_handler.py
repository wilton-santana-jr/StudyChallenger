from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from ....models import Flashcard, Categoria


class FlashcardListRequestHandler(LoginRequiredMixin, ListView):
    model = Flashcard
    template_name = "flashcard/flashcard_list.html"
    context_object_name = "flashcards"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categoria.objects.all()
        context["dificulties"] = Flashcard.DIFICULDADE_CHOICES
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get("category")
        difficulty = self.request.GET.get("dificulty")

        queryset = queryset.filter(user=self.request.user)

        if category:
            queryset = queryset.filter(categoria__id=category)

        if difficulty:
            queryset = queryset.filter(dificuldade=difficulty)

        return queryset