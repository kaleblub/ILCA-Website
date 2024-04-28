from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404, handler500, handler400
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

from main import views as main_views
from registration import views as registration_views
from about import views as about_views
from contact import views as contact_views
from accounts import views as account_views

urlpatterns = [
    # Front End URLs
    # path('admin/', admin.site.urls),
    # path('register/', registration_views.registration, name='register'),
    path('', main_views.home, name='home'),
    path('about/', about_views.about, name='about'),
    path('contact/', contact_views.contact, name='contact'),
    path('<str:language>/', main_views.set_language, name="set_language"),
    
    # LMS URLs
    path('app/', include('app.urls')),
    path('accounts/', include('accounts.urls')),
    path('programs/', include('course.urls')),
    path('result/', include('result.urls')),
    path('search/', include('search.urls')),
    path('quiz/', include('quiz.urls')),

    # path('payments/', include('payments.urls')),

    # path('accounts/api/', include('accounts.api.urls', namespace='accounts-api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'app.views.handler404'
# handler500 = 'app.views.handler500'
# handler400 = 'app.views.handler400'