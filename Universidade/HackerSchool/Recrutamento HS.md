# Ideia (inicial) de Projecto Integral
Como já tinha falado na reunião, tento a opinião que o recrutamento deveria consistir num protejo integral que era acompanhado de workshops. Estes projectos iriam abranger quase todas as areas que lhes queremos ensinar, como:
-  Programação (Python/C/C++)
-  Electrónica (Sensores/Actuadores/*design**)
-  WebDev (HTML/CSS)
-  Modelação 3D
- etc...

Acredito que não precise de ter a carga igualmente distribuída por todas as areas mas era porreiro **abordar no mínimo 3 areas**.

De modo a encorajar o trabalho em equipa (e a poupar custos de material), seria bom os projetos serem feitos em grupos de 2 a 3 alunos. 2 idealmente mas depende muito dos custos.
Não sei se a ideia de cada membro do grupo ter uma parte electronica funcionaria tão bem como vocês estão à espera para evitar penduras, however, é uma óptima maneira de eles se juntarem em equipas.

## Projeto 1: Synth

Mini-sintetizador para eles construírem; não foi proposto por mim e não sei as especificações que os autores idealizaram, mas acredito que envolveria as áreas de:
- Prog - Programar interface;
- Eletrónica - Montagem do circuito, design da pcb e soldadura;
- 3dMod - Modelação da caixa, botẽs, etc. Impressão 3D;
- Mixing *(?)*;
É um projeto fixe, mas quão simples de aprender seria o circuito? Se for maioritariamente analógico como seria o debug para a malta que não percebe de eletro?

## Projeto 2: Medidor qualidade de plantas.

No ano de 23/24, eletro teve o PIC1, no meu grupo fizemos um ecossistema de sensores capazes de medir a qualidade do terreno/plantação a nível industrial por LoRa e assins... Se quiserem ver mais está aqui o [blog](https://web.tecnico.ulisboa.pt/ist1103681/).
Descomplicando um bocado (e esuqecendo a *rede* de sensores), acho que seria interessante eles fazerem um pequeno dispositivo que se espetasse na terra e medisse a qualidade de umas flores que tenham em casa ou até uma mini-horta. Envolveria:
 
- Prog - programar o controlador em micropython (seguimento do workshop de python);
- Eletrónica - dar assemble no circuito, maioritariamente digital; design da pcb e soldadura;
- WebDev - Criar uma webapp que dava display dos dados recolhidos, dar host em Micropython? [Sim](https://github.com/miguelgrinberg/microdot);
- 3dMod - Modelar caixa, imprimir;

Talvez seja bastante simples, mas envolveria várias areas, desde dimensionamento de baterias para o circuito até criação de uma pequena base de dados com uma webapp. Cada uma destas tarefas seria na verdade simples.

## Projeto 3: Macro's Keyboard

Acho que foi o Fecha que sugeriu ontem na reunião, um "teclado extra" que permite adicionar Macro's facilmente. Ou seja, botões que tem um atalho pré-programado, como por exemplo abrir programas, executar scripts, atalhos para determinadas aplicações (Photoshop, Blender, etc.).
Tal como as anteriores, esta parece-me simples e tem a sua utilidade. Envolveria:

- Prog - programar a interface e fazer um GUI *(?)*;
- Eletrónica - dar assemble no circuito, design pcb e soldadura;
- 3dMod - Modelar caixa, botões, etc. Imprimir;

Contudo, não temos webdev... acho que seria interessante e compensar com um workshop dedicado a GUI's.

## Conclusão

Os projetos que aqui mencionei são simples e mesmo que não envolvam todas as areas, acho que se mantém fazível um workshop isolado para as abordar.
Não me ocorreu nenhuma ideia para AppDev (um bocado biased pq tenho 0 experiência). Mas a WebApp que mencionei no [Projeto 2] pode ser trocada por APPDev...