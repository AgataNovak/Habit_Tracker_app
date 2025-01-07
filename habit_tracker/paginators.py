from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """Пагинатор выполняет пагинацию с разделением до 5 объектов класса Habit на странице"""

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 5


class NiceHabitPaginator(PageNumberPagination):
    """Пагинатор выполняет пагинацию с разделением до 5 объектов класса NiceHabit на странице"""

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 5
