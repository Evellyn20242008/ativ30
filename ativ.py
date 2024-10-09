# crie uma duncao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7
def media(nota1,nota2,nota3):
    media = (nota1 + nota2 + nota3)/3
    if media >=7:
        print('aprovado')
    else:
        print('reprovado')

    return media 
    
nota1 = float(input("digite a nota"))
nota2 = float(input("digite a nota"))
nota3 = float(input("digite a nota"))
resultado = media(nota1,nota2,nota3)

print(resultado)
