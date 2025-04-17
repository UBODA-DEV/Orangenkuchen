# Código para fazer um bolo de laranja com interação do usuário

def aguardar_confirmacao(mensagem="Pressione Enter para continuar..."):
    # Esta função interrompe o fluxo e aguarda que o usuário confirme para continuar
    # Exibe a mensagem fornecida e espera que o usuário pressione Enter
    input(mensagem)

def bater_tudo(ovos, acucar, oleo, suco, cascas):
    # Esta função simula o processo de misturar os ingredientes líquidos no liquidificador
    print("Preparando para bater os ingredientes no liquidificador...")
    print(f"Ingredientes disponíveis: {ovos}, {acucar}, {oleo}, {suco} e {cascas}")
    aguardar_confirmacao("Pressione Enter para bater tudo no liquidificador...")
    
    print("Batendo ovos, açúcar, óleo, suco e cascas no liquidificador...")
    aguardar_confirmacao("Batido! Pressione Enter para continuar...")
    return "mistura_pronta"

def passar_para_tigela(mistura):
    # Esta função simula a transferência da mistura do liquidificador para uma tigela
    print(f"A {mistura} está pronta no liquidificador.")
    aguardar_confirmacao("Pressione Enter para passar a mistura para uma tigela...")
    
    print("Passando a mistura para uma tigela...")
    aguardar_confirmacao("Transferência concluída! Pressione Enter para continuar...")
    return mistura

def adicionar(mistura, farinha_de_trigo, fermento):
    # Esta função simula a adição dos ingredientes secos à mistura líquida
    print(f"A {mistura} está na tigela. Preparando para adicionar ingredientes secos.")
    print(f"Ingredientes para adicionar: {farinha_de_trigo} e {fermento}")
    aguardar_confirmacao("Pressione Enter para adicionar farinha e fermento...")
    
    print("Adicionando farinha de trigo e fermento à mistura...")
    aguardar_confirmacao("Ingredientes adicionados! Pressione Enter para continuar...")
    return "massa_pronta"

def preparar_forma(forma):
    # Esta função verifica se a forma está preparada e a prepara se necessário
    print("Verificando a forma...")
    
    if not forma["untada_e_enfarinhada"]:
        print("A forma precisa ser untada e enfarinhada.")
        aguardar_confirmacao("Pressione Enter para untar e enfarinhar a forma...")
        
        print("Untando e enfarinhando a forma...")
        forma["untada_e_enfarinhada"] = True
        aguardar_confirmacao("Forma preparada! Pressione Enter para continuar...")
    else:
        print("A forma já está untada e enfarinhada.")
        aguardar_confirmacao("Pressione Enter para continuar...")
    
    return forma

def transferir_para_forma(mistura, forma):
    # Esta função simula a transferência da massa pronta para a forma
    print(f"A {mistura} está pronta na tigela.")
    print("A forma está untada e enfarinhada.")
    aguardar_confirmacao("Pressione Enter para transferir a massa para a forma...")
    
    print("Transferindo a massa para a forma...")
    forma["conteudo"] = mistura
    aguardar_confirmacao("Massa transferida! Pressione Enter para continuar...")

def assar_bolo(forma, tempo):
    # Esta função simula o processo de assar o bolo
    print(f"A forma está com a massa pronta para assar.")
    aguardar_confirmacao(f"Pressione Enter para assar o bolo por {tempo} minutos...")
    
    print(f"Assando o bolo na forma por {tempo} minutos...")
    print("Aguarde enquanto o bolo assa...")
    aguardar_confirmacao("Tempo concluído! Bolo assado. Pressione Enter para continuar...")
    return "bolo_assado"

def desenformar_bolo(forma):
    # Esta função simula o processo de retirar o bolo da forma
    print("O bolo está assado e pronto para ser desenformado.")
    aguardar_confirmacao("Pressione Enter para desenformar o bolo...")
    
    print("Desenformando o bolo...")
    aguardar_confirmacao("Bolo desenformado! Pressione Enter para continuar...")
    return "bolo_desenformado"

def molhar_bolo(bolo, suco_de_laranja):
    # Esta função simula o processo de molhar o bolo com suco de laranja
    print(f"O {bolo} está desenformado e pronto para receber a calda.")
    aguardar_confirmacao(f"Pressione Enter para molhar o bolo com {suco_de_laranja}...")
    
    print("Molhando o bolo com suco de laranja...")
    aguardar_confirmacao("Bolo molhado! Pressione Enter para finalizar...")
    return "bolo_pronto"

# Ponto de entrada do programa
if __name__ == "__main__":
    print("=== PROGRAMA INTERATIVO DE PREPARO DE BOLO DE LARANJA ===")
    print("Este programa irá guiá-lo no preparo de um bolo de laranja.")
    print("A cada etapa, você será solicitado a confirmar para prosseguir.")
    aguardar_confirmacao("Pressione Enter para começar...")
    
    # Definição dos ingredientes como strings simples
    ovos = "ovos"
    acucar = "açúcar"
    oleo = "óleo"
    suco = "suco de laranja"
    cascas = "cascas de laranja"
    farinha_de_trigo = "farinha de trigo"
    fermento = "fermento"
    
    # Exibindo os ingredientes necessários
    print("\n=== INGREDIENTES NECESSÁRIOS ===")
    print(f"- {ovos}")
    print(f"- {acucar}")
    print(f"- {oleo}")
    print(f"- {suco}")
    print(f"- {cascas}")
    print(f"- {farinha_de_trigo}")
    print(f"- {fermento}")
    aguardar_confirmacao("\nPressione Enter quando tiver todos os ingredientes...")
    
    # Criação do dicionário que representa a forma
    forma = {"untada_e_enfarinhada": False, "conteudo": None}

    # Execução da sequência de passos para fazer o bolo
    print("\n=== INICIANDO O PREPARO DO BOLO ===")
    mistura = bater_tudo(ovos, acucar, oleo, suco, cascas)
    mistura = passar_para_tigela(mistura)
    massa = adicionar(mistura, farinha_de_trigo, fermento)
    forma = preparar_forma(forma)
    transferir_para_forma(massa, forma)
    bolo = assar_bolo(forma, 30)
    bolo = desenformar_bolo(forma)
    bolo = molhar_bolo(bolo, suco)

    # Mensagem final indicando que o bolo está pronto
    print("\n=== PARABÉNS! ===")
    print("Bolo de laranja pronto para servir!")
    print("Aproveite sua deliciosa receita.")