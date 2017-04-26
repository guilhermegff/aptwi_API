from django.conf.urls import url
from aptwi import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

'''
#Primeira e segunda versao
urlpatterns = [
    url(r'^livros/$', views.genre_list),
    url(r'^livros/(?P<pk>[0-9]+)/$', views.genre_detail),
]
'''

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^aptwi/schema/$', schema_view),
    url(r'^aptwi/$', views.GenreList.as_view()),
    url(r'^aptwi/(?P<pk>[0-9]+)/$', views.GenreDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
