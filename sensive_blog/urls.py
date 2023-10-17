from django.contrib import admin
from blog import views
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format
from django.db.models import QuerySet


def print_sql(queryset: QuerySet):
    formatted = format(str(queryset.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/<int:page>', views.index, name='index'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('tag/<slug:tag_title>', views.tag_filter, name='tag_filter'),
    path('contacts/', views.contacts, name='contacts'),
    path('', views.index, name='index'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]