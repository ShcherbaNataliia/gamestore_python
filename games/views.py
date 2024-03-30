from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Game, Publisher, Category
from .forms import PublisherForm, GameForm, CategoryForm


def home(request):
    # Retrieve all games from the database
    games = Game.objects.all()
    publishers = Publisher.objects.all()
    return render(request, 'home.html', {'games': games, 'publishers': publishers})


def add_game(request):
    publishers = Publisher.objects.all()
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GameForm()
    return render(request, 'game/add_game.html', {'form': form, 'publishers': publishers})


def game_detail(request, game_id):
    game = get_object_or_404(Game.objects.prefetch_related('categories', 'publisher'), pk=game_id)
    return render(request, 'game/game_detail.html', {'game': game})


def delete_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        game.delete()
        return redirect('home')
    return render(request, 'game/delete_game_confirmation.html', {'game': game})


def update_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('game_detail', game_id=game.id)  # Redirect to the game detail page
    else:
        form = GameForm(instance=game)
    return render(request, 'game/update_game.html', {'form': form})


def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            new_publisher = form.save(commit=False)
            new_publisher.save()
            return redirect('home')
    else:
        form = PublisherForm()
    return render(request, 'publisher/add_publisher.html', {'form': form})


def publisher_detail(request, publisher_id):
    publisher = get_object_or_404(Publisher.objects.prefetch_related('game_set'), pk=publisher_id)
    return render(request, 'publisher/publisher_detail.html', {'publisher': publisher})


def delete_publisher(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    if request.method == 'POST':
        publisher.delete()
        return redirect('home')
    return render(request, 'publisher/delete_publisher_confirmation.html', {'publisher': publisher})


def update_publisher(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publisher_detail', publisher_id=publisher.id)  # Redirect to the game detail page
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'publisher/update_publisher.html', {'form': form})


def publishers(request):
    # Retrieve all games from the database
    publishers = Publisher.objects.all()
    return render(request, 'publisher/publishers.html', {'publishers': publishers})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'category/add_category.html', {'form': form})


def categories(request):
    # Retrieve all games from the database
    categories = Category.objects.all()
    return render(request, 'category/categories.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category.objects.prefetch_related('game_set'), pk=category_id)
    return render(request, 'category/category_detail.html', {'category': category})


def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('home')
    return render(request, 'category/delete_category_confirmation.html', {'category': category})


def update_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/update_category.html', {'form': form})
