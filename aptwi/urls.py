from django.conf.urls import url
from aptwi import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^aptwi/schema/$', schema_view),
    url(r'^alunos/$', views.AlunoList.as_view()),
    url(r'^aluno/(?P<pk>[0-9]+)/$', views.AlunoDetail.as_view()),
    url(r'^questoes/$', views.QuestaoList.as_view()),
    url(r'^alunos/(?P<ra>[0-9]+)/$', views.VerificaAluno.as_view()),
    url(r'^questao/(?P<pk>[0-9]+)/$', views.QuestaoDetail.as_view()),
    url(r'^respostas$', views.RespostaList.as_view()),
    url(r'^resposta/(?P<pk>[0-9]+)/$', views.RespostaDetail.as_view()),
    url(r'^avaliacoes/$', views.AvaliacaoList.as_view()),
    url(r'^avaliacao/(?P<pk>[0-9]+)/$', views.AvaliacaoDetail.as_view()),
    url(r'^avaliacoesData/(?P<ra>[0-9]+)/$', views.AvaliacaoVerifica.as_view()),
    url(r'^avaliacoesExiste/(?P<ra>[0-9]+)/$', views.AvaliacaoExiste.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
