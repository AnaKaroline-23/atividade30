# crie uma funcao que calcule a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7

def média_notas (nota1, nota2, nota3):
    média = (nota1 + nota2 + nota3) / 3
    if média >= 7:
        return f"média: {média:.2f} - Aprovado"
    else:
        return f"média: {média:.2f} - Reprovado"
    
nota1 = float(input(F"Digite a primeira nota "))
nota2 = float(input(f"Digite a segunda nota "))
nota3 = float(input(f"Digite a terceira nota "))   
Resultado = média_notas (nota1, nota2, nota3,)
print (Resultado)


