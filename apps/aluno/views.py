from django.shortcuts import render,redirect, get_list_or_404,get_object_or_404
from aluno.models  import Aluno
from django.contrib import messages



# Create your views here.
def newAluno(request):
    return render(request,'aluno/add_aluno.html',{})


def AddAluno(request):
    return ''