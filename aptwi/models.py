from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime 
import uuid

class Aluno(models.Model):

	ra = models.CharField(max_length=10, null=False, help_text="Digite o seu RA")
	nome_escola = models.CharField(max_length=50, null=False, help_text="Digite o nome da escola")

	def __unicode__(self):

		return self.ra

class Avaliacao(models.Model):
	
	aluno = models.ForeignKey('Aluno')
	sugestao = models.CharField(max_length=200, null=True, help_text="Escreva sua sugestao")
	data_hora = models.DateTimeField(auto_now_add=True)
	resp_quest1 = models.CharField(max_length=2, null=True, help_text="Digite a resposta")
	resp_quest2 = models.CharField(max_length=2, null=True, help_text="Digite a resposta")
	resp_quest3 = models.CharField(max_length=2, null=True, help_text="Digite a resposta")
	
	def __unicode__(self):

		return self.data_hora

class Questao(models.Model):

	questao = models.CharField(max_length=200, null=False, help_text="Escreva a questao")

	def __unicode__(self):

		return self.questao

class Resposta(models.Model):

	questao = models.ForeignKey('Questao')
	resposta = models.CharField(max_length=200, null=False, help_text="Escreva a resposta")

	def __unicode__(self):

		return self.resposta
