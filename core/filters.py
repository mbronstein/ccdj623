from admin_auto_filters.filters import AutocompleteFilter


class MatterFilter(AutocompleteFilter):
    title = 'Matter'  # display title
    field_name = 'matter'  # name of the foreign key field


class CategoryFilter(AutocompleteFilter):
    title = 'Category'
    field_name = 'category'
