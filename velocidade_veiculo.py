def classificar_velocidade():

    
    velocidade = float(input("Digite a velocidade do veículo em km/h: "))
    


    if velocidade <= 40:
        print("Classificação: Lenta \n Alerta: Velocidade abaixo do ideal. Pode atrapalhar o fluxo de trânsito.")
    elif velocidade > 40 and velocidade <= 80:
        print("Classificação: Moderada \n Velocidade segura e adequada para a maioria das vias urbanas.")
    elif velocidade > 80 and velocidade <= 120:
        print("Classificação: Rápida \n Atenção: Dirija com responsabilidade. Mantenha distância e atenção redobrada.")
    else:
        print("Classificação: Perigosa \n Alerta crítico: Risco alto de acidentes! Reduza a velocidade imediatamente.")


print("Bem-vindo ao classificador de velocidade de veículos!")
classificar_velocidade()