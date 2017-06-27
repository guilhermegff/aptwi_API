from aptwi.models import Aluno, Avaliacao, Questao, Resposta
from aptwi.serializers import AlunoSerializer, AvaliacaoSerializer, QuestaoSerializer, RespostaSerializer
from rest_framework import generics

class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()

class VerificaAluno(generics.ListAPIView):
    lookup_url_kwarg = ('ra')
    serializer_class = AlunoSerializer
    
    def get_queryset(self):
	ra = self.kwargs.get(self.lookup_url_kwarg)
	aluno = Aluno.objects.filter(ra=ra)
	return aluno

class AvaliacaoExiste(generics.ListAPIView):
    lookup_url_kwarg = ('ra')
    serializer_class = AvaliacaoSerializer
    
    def get_queryset(self):
	ra = self.kwargs.get(self.lookup_url_kwarg)
	avaliacao = Avaliacao.objects.filter(aluno=ra)
	return avaliacao

class AvaliacaoVerifica(generics.ListAPIView):
    lookup_url_kwarg = ('ra')
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
	ra = self.kwargs.get(self.lookup_url_kwarg)
	avaliacao = list(Avaliacao.objects.raw("select * from aptwi_avaliacao where data_hora >= current_timestamp - INTERVAL 		'24 hours'  and data_hora <= current_timestamp and aluno_id = %s group by data_hora, id",[ra]))
	return avaliacao

class AvaliacaoList(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class AvaliacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class QuestaoList(generics.ListCreateAPIView):
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer

class QuestaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer

class RespostaList(generics.ListCreateAPIView):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer

class RespostaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer
