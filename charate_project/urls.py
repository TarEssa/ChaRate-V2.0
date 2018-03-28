"""charate_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from ChaRate import views, urls


# Registration view that moves to index page right after
# a successful registration process
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/ChaRate/'


urlpatterns = [
                  # Index Url
                  url(r'^$', views.index, name='index'),
                  # Accounts Urls that are used by Django Reg Redux
                  url('accounts/', include('django.contrib.auth.urls')),
                  # Included the Html Urls in The Template Folder
                  url(r'^ChaRate/', include('ChaRate.urls')),
                  # Admin Page URls
                  url(r'^admin/', admin.site.urls),
                  # Registration redux Registration URL
                  url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
                  # Django Registration Redux Template names urls for easier linkage
                  url(r'^accounts/', include('registration.backends.simple.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
