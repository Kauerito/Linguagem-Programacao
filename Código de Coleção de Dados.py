se  iniciar  ==  '3' :
    print ( " \ 033 [1; 32mO Cárdapio é esse:" )
    lanche1 = { 'Nº do lanche' : '001' , 'Nome' : 'Burgão' , 'Sabor' :'Divino' , 'Valor' : 'R $ 12,00' , 'Descrição' : 'Carne 250g, cheddar, churrasco e pão' }
    imprimir ( lanche1 )
    
    
    lanche2  = { 'Nº do lanche' : '002' , 'Nome' : 'ovinho' , 'Sabor' : 'Gostosão' , 'Valor' : 'R $ 5,00' , 'Descrição' : 'Pão com carne e ovo ' }
    imprimir ( lanche2 )

    pedir  =  input ( ' \ 033 [1; 39mQual lanche voce quer ??' )

    if  pedir  ==  '001' : 
        detalhe1 = DetalhePedido ( 'Código pedido: 1345' , 'Nome do lanche: Burgão' , 'Código Produto: 001' , 'Quantidade: 01' , 'O lanche é R $ 12,00' , 'Taxa de Entrega: R $ 0, 00 ' , ' Valor final: R $ 12,00 ' )
        detalhe1 . exibirDetalhes ()
        intervalo
  
    if  pedir  ==  '002' :
      detalhe2 = [ 'Código pedido: 1342' , 'Nome do lanche: Ovinho' , 'Código Produto: 002' , 'Quantidade: 01' , 'O lanche é R $ 5,00' , 'Valor final: R $ 5,00' ]
      detalhe2 . anexo ( "Valor Final: R $ 5,00" )
      detalhe2 . pop ( 5 )
      detalhe2 . inserir ( 5 , 'Taxa de entrega: R $ 0,00' )
      imprimir ( detalhe2 )
      intervaloSepa
