from rest_framework import serializers
from aptwi.models import Aluno, Avaliacao, Questao, Resposta

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
	model = Aluno
	fields = ('id', 'ra', 'nome_escola')

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
	model = Avaliacao
	fields = ('id', 'aluno', 'sugestao', 'data_hora', 'resp_quest1', 'resp_quest2', 'resp_quest3')

class QuestaoSerializer(serializers.ModelSerializer):
    class Meta:
	model = Questao
	fields = ('id', 'questao')

class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
	model = Resposta
	fields = ('id', 'questao', 'resposta')
