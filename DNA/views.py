
from .genes import GENES
from django.http import JsonResponse


def getGenes (request):
    return JsonResponse(GENES, safe=False)

def getGene(request,id):
    for gene in GENES:
        if gene["id"] == id:
            return JsonResponse(gene)