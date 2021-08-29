from django.shortcuts import render,redirect, get_list_or_404,get_object_or_404
from aluno.models  import Aluno
from django.contrib import messages
from aluno.forms import AlunoForm


# Create your views here.
def newAluno(request):
    return render(request,'aluno/add_aluno.html',{})


def AddAluno(request):
    template_name = 'aluno/add_aluno.html'
    context = {}
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            form.save()
            messages.success(request, "Usuário salvo com sucesso!")
    form = AlunoForm()
    context['form'] = form
    return render(request,template_name,context)