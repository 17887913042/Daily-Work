from  django.urls import path, include
from app.views import Books
# from django.urls import path, include


urlpatterns = [
    path(r'book/', Books.as_view())
    # path('admin/', admin.site.urls),
    # path(r'', TemplateView.as_view(template_name='index.html'), name='home'),
    # path(r'', include('avl.urls')),
]