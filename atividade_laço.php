<?php 
// CRIE UM SCRIPT CAPAZ DE PRODUZIR, ATRAVÉS DO LAÇO DE REPETIÇÃO, UM ARRAY COM 6 ELEMENTOS
//NUMÉRICOS ALEATÓRIOS ENTRE 1 E 60, SIMULANDO O FUNCIONAMENTO DO SORTEIO DA MEGA SENA.
//ATENTE-SE AO FATO DE QUE OS NÚMEROS CONTIDOS NO ARRAY NÃO PODEM SER REPETIDOS.

    $numeros = array();
    while(count($numeros) <= 5){
        $num = rand(1,60);
        if(!in_array($num, $numeros)){
            $numeros[] = $num;
        }
    }
    print_r($numeros);
?>