from django.db.models import Q
from django.shortcuts import render

from .models import Categoria, Vacante


def inicio(request):
    vacantes = (
        Vacante.objects.filter(activa=True)
        .select_related('empresa', 'categoria')
        .order_by('-destacada', '-fecha_publicacion')
    )

    busqueda = request.GET.get('q', '').strip()
    categoria_id = request.GET.get('categoria', '')

    if busqueda:
        vacantes = vacantes.filter(
            Q(titulo__icontains=busqueda)
            | Q(descripcion__icontains=busqueda)
            | Q(empresa__nombre__icontains=busqueda)
        )
    if categoria_id:
        vacantes = vacantes.filter(categoria_id=categoria_id)

    contexto = {
        'vacantes': vacantes,
        'categorias': Categoria.objects.all(),
        'busqueda': busqueda,
        'categoria_id': categoria_id,
    }
    return render(request, 'vacantes/inicio.html', contexto)