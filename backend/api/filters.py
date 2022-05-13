from django_filters import filters, FilterSet, widgets
from django_filters.filters import (
    BooleanFilter, CharFilter, ModelChoiceFilter,
    ModelMultipleChoiceFilter, NumberFilter 
)
from recipes.models import Recipe, Ingredient, Tag
from users.models import CustomUser


class RecipeFilter(FilterSet):
    tags = ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        lookup_type='in',
        queryset=Tag.objects.all()
    )
    author = ModelChoiceFilter(
        queryset=CustomUser.objects.all()
    )
    is_in_shopping_cart = BooleanFilter(
        widget=widgets.BooleanWidget(),
        label='in shopping cart'
    )
    is_favorited = BooleanFilter(
        widget=widgets.BooleanWidget(),
        label='in favorite'
    )

    class Meta:
        model = Recipe
        fields = ('tags', 'author', 'is_favorited', 'is_in_shopping_cart')


class IngredientFilter(FilterSet):
    name = CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ('name',)