/**
 * Escreva uma função que recebe um objeto JSON com os dados da pessoa,
 *  calule o IMC dela colocando o valor obtido
 * na propriedade IMC deste objeto e retorne uma String contendo
 * o estado do peso dessa pessoa.
 * 
 * Fórmula do IMC massa / (altura * altura)
 * Tabela de estados do IMC:
 *  - Menor de 18.5 -> Abaixo do peso
 *  - Entre 18,5 e 24.9 -> Normal
 *  - Entre 25.0 e 29.9 -> Excesso de peso
 *  - Entre 30.0 e 34.9 -> Obesidade Leve (Grau I)
 *  - Entre 35.0 e 39.9 -> Obesidade Severa (Grau II)
 *  - Maior e igual a 40,0 -> Obesidade Mórbida (Grau III)
 * 
 * @param {Object} pessoa json's com dados da pesssoa
 * @param {String} pessoa.nome nome da pessoa
 * @param {Number} pessoa.peso massa da pessoa em kg, com uma casa decimal
 * @param {Number} pessoa.altura altura da pessoa em metros, com duas casas decimais
 * @returns {String} estado do peso da pessoa
 */
function calculaImcs(pessoa){
    let IMC = (pessoa.peso / (pessoa.altura * pessoa.altura));
    if (IMC < 18.5){return "Abaixo do peso"}
    else if (IMC >= 18.5 && IMC <= 24.9){return "Normal"}
    else if (IMC >= 25 && IMC <= 29.9){return "Excesso de peso"}
    else if (IMC >= 30 && IMC <= 34.9){return "Obesidade Leve (Grau I)"}
    else if (IMC >= 35 && IMC <= 39.9){return "Obesidade Severa (Grau II)"}
    else if (IMC >= 40){return "Obesidade Mórbida (Grau III)"}
 }