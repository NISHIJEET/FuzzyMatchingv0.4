from django.conf.urls import url
from Home import views as vHome
from Input import views as vInput
from Output import views as vOutput
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', vHome.Home, name='Home'),
    url(r'^Input/$', vInput.Input, name='Input'),
    url(r'^Input/Source$', vInput.Source, name='Source'),

    # Main template
    url(r'^Input/SelectColumns$', vInput.column_list, name='SelectColumns'),
    # Recusive template
    url(r'^Input/SelectColumns/CommonField ', vInput.CommonField, name='CommonField'),

    # Main template
    url(r'^Input/SelectColumns/ConcatCommonFields ', vInput.ConcatCommonFields, name='ConcatCommonFields'),
    # Recusive template
    url(r'^Input/SelectColumns/ConcatFields ', vInput.ConcatFields, name='ConcatFields'),

    # url(r'^Input/SelectColumns/SelectCommon$',vInput.ColumnList, name='ColumnList'),

    # Main template
    url(r'^Input/CatFieldSelection ', vInput.CatFieldSelection, name='CatFieldSelection'),
    # Recusive template
    url(r'^Input/CatFieldSelection/SavedWeights ', vInput.SavedWeights, name='SavedWeights'),

    url(r'^Input/ReplaceWords$', vInput.ReplaceWords, name='ReplaceWords'),
    url(r'^Input/ReplaceWords/ReplaceWordsResults',vInput.ReplaceWordsResults,name="ReplaceWordsResults"),



    url(r'^Input/ControlSettings', vInput.ControlSettings, name='ControlSettings'),

    url(r'^Output/$', vInput.Output, name='Output'),
    url(r'^Output/Download$', vInput.Download, name='Download'),


    url('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
