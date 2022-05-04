/**
 * Recebe uma string com o nome completo de uma pessoa 
 * (primeiro e último nome apenas) 
 * e devolve o primeiro nome.
 * Exemplos:
 *  - Yuri Dirickson -> Yuri
 *  - João Silva -> João
 *  - Maria -> Maria
 * 
 * @param {String} nomeCompleto nome completo da pessoa.
 * @return string com o primeiro nome apenas
 */
function primeiro_nome(nomeCompleto) {
    nomeCompleto = nomeCompleto.split(' ');
    return nomeCompleto[0]
}

/**
 * Recebe uma string com o nome completo de uma pessoa
 *  (primeiro e último nome apenas) 
 * e devolve o nome com o sobrenome abreviado.
 *  Caso só o primeiro nome seja passado, não faça nada.
 * Exemplos:
 *  - Yuri Dirickson -> Yuri D.
 *  - João Silva -> João S.
 *  - Maria -> Maria
 *  
 * @param {String} nomeCompleto nome completo da pessoa.
 * @return string com o segundo nome abreviado
 */
function abreviadorNomes(nomeCompleto) {
    nomeCompleto = nomeCompleto.split(' ');
    if (nomeCompleto[1] != undefined){
        return nomeCompleto[0]+' '+nomeCompleto[1][0]+'.'
    }else{return nomeCompleto[0]}
}

/**
 * Escreva uma função que recebe uma String com a data no formato brasileiro
 *  (dia/mês/ano) e
 * converta para o formato: 'Dia de Mês Extenso de Ano'. 
 * Exemplos:
 *  - 10/11/2019 -> 10 de Novembro de 2019
 *  - 03/02/2000 -> 03 de Fevereiro de 2000
 * OBS: Note a letra maiúscula do mês.
 * OBS2: Para ficar menos tedioso, vou mandar apenas meses Novembro, 
 * Maio e Fevereiro 
 * @param {String} data 
 * @returns {String} data no formato 
 */


function converteDataParaFormaCompleta(data){
    if(data == ''){return null}
    else {
    let dic_data = {};
    dic_data['05'] = 'Maio';
    dic_data['02'] = 'Fevereiro';
    dic_data['11'] = 'Novembro';
    data = data.split('/');
    let temp = data[1]
    let mes = dic_data[temp]
    return data[0]+' de '+mes+' de '+data[2]
    }
}
