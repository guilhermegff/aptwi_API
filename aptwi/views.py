from aptwi.models import Aluno, Avaliacao, Questao, Resposta
from aptwi.serializers import AlunoSerializer, AvaliacaoSerializer, QuestaoSerializer, RespostaSerializer
from rest_framework import generics

class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

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

















































