# -*- Mode: Python; coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from proposta.core.models import Cliente, Proposta
from orcamento.models import Fornecedor, Compra, Produto, Material


# Proposta
@login_required(redirect_field_name='redirect_to')
def proposta(request, id=None, *args, **kwargs):
	contexto = {}
	contexto['proposta_base'] = Proposta.objects.get(id=id)

	return render(request, "proposta.html", contexto)
# Orcamento
@login_required(redirect_field_name='redirect_to')
def orcamento(request, id=None, *args, **kwargs):
	contexto = {}
	contexto['orcamento'] = Compra.objects.get(id=id)

	return render(request, "orcamento.html", contexto)

