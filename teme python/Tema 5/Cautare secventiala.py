def cauta_document(lista_documente, document):
    numar_iteratii = 0
    ok=0
    for i in range(0, len(lista_documente)):
        numar_iteratii +=1
        if lista_documente[i]==document:
            ok=1
            break
    if ok==1:
        return(print(f"Documentul cu numărul de referință {document} a fost găsit pe poziția {i} după {numar_iteratii} documente verificate."))
    else:
        return(print(f"Documentul cu numărul de referință {document} nu a fost găsit în dosar. Total documente verificate: {numar_iteratii}."))

