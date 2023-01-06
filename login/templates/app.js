const cui = document.getElementById("cui")
const pass = document.getElementById("password")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexCui = /^([0-9]{8})*$/;
    parrafo.innerHTML = ""
    if(cui.value==""){
        warnings += `El CUI no es valido <br>`
        entrar = true
    }
    if(!regexCui.test(cui.value)){
        warnings += `El CUI no es valido <br>`
        entrar = true
    }
    if(pass.value.length < 8){
        warnings += `La contraseña no es valida <br>`
        entrar = true
    }

    if(entrar){
        parrafo.innerHTML = warnings
    }else{
        alert("Ingreso exitoso")
    }
})