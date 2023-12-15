from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from CardGame.models import PokemonCard, Trainer, Collection
from .form import TrainerForm, CollectionForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import json

# Create your views here.
class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'home'
        return context
    
class PokemonCardListView(ListView):
    model = PokemonCard
    context_object_name = 'pokemoncard'
    template_name = "pokemoncards.html"
    json_file_path = 'data/pokemon_data.json'
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['segment'] = 'pokemon-card'
        pokemon_data = self.get_pokemon_data()
        context['pokemon_data'] = pokemon_data
        return context
    
    def get_pokemon_data(self):
        with open(self.json_file_path, 'r') as json_file:
            pokemon_data = json.load(json_file)
    
        return pokemon_data
    
    
    
class TrainerListView(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by = 5
    ordering = ['-create_at'] 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'trainer-list'
        return context
    
    

class CollectionListView(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collection.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'collection-list'
        return context
    

class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')


class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')


class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list')


class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_add.html'
    success_url = reverse_lazy('collection-list')
    

class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_edit.html'
    success_url = reverse_lazy('collection-list')


class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection_del.html'
    success_url = reverse_lazy('collection-list')

class PokemonCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'pokemon_add.html'
    success_url = reverse_lazy('pokemoncard-list')
    paginate = 3

class PokemonUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'pokemon_edit.html'
    success_url = reverse_lazy('pokemoncard-list')


class PokemonDeleteView(DeleteView):
    model = Collection
    template_name = 'pokemon_del.html'
    success_url = reverse_lazy('pokemoncard-list')
