from django.conf.urls import url
from Home import views as vHome
from Input import views as vInput
from Output import views as vOutput
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [

    url(r'^$', vHome.Home, name='Home'),
    url(r'^Input/$', vInput.Input, name='Input'),
    url(r'^Input/Source$', vInput.Source, name='Source'),
    url(r'^Input/SelectColumns$', vInput.column_list, name='SelectColumns'),
    url(r'^Input/SelectColumns/ConcatFields ', vInput.ConcatFields, name='ConcatFields'),
    url(r'^Input/SelectColumns/SelectCommon$',vInput.ColumnList, name='ColumnList'),
    url(r'^Input/PreRun', vInput.PreRun, name='PreRun'),
    url(r'^Input/CatFieldSelection', vInput.CatFieldSelection, name='CatFieldSelection'),
    url(r'^Input/ControlSettings', vInput.ControlSettings, name='ControlSettings'),
    url(r'^Input/ReplaceWords', vInput.ReplaceWords, name='ReplaceWords'),
    url(r'^Output/$', vOutput.Output, name='Output'),
    url('admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)