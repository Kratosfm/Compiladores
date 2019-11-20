GlobalVars = {}
GlobalFuncs = {}
GlobalVectors = {}

MainVars = {}
MainVectors = {}

/* -------- Variables para agregar en el html -------- */

function addGlobalVar(variable){
  var divVarHTML = document.createElement("div");
  divVarHTML.classList.add("is-variable");
  divVarHTML.setAttribute("id", variable)
  var varHtml = document.createTextNode(GlobalVars[variable]);
  divVarHTML.appendChild(varHtml);
  document.getElementById("divVariablesGlobales").appendChild(divVarHTML);
  hideModal();
  return ;
}

function editGlobalVar(variable){
  var editVar = document.getElementById(variable)
  editVar.innerHTML = GlobalVars[variable]
  hideModal();
  return ;
}

function addFunction(func_name){
  var buttonText;
  var divFuncHTML = document.createElement("div");
  var divVariablesHTML = document.createElement("div")
  divVariablesHTML.setAttribute("id", func_name);
  var divButtonsHTML = document.createElement("div");
  divFuncHTML.classList.add("is-function");
  divFuncHTML.setAttribute("id", "name" + func_name);

  var buttons = document.createElement("div");
  buttons.classList.add("buttons", "has-addons", "is-centered");
  buttons.setAttribute("style", "margin-bottom: 15px;")

  var buttonVariable = document.createElement("button");
  buttonVariable.classList.add("button", "is-success");
  onClickFunc = 'addVariableLocalModal("' + func_name + '")'
  buttonVariable.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Variable");
  buttonVariable.appendChild(buttonText);

  var buttonOperation = document.createElement("button");
  buttonOperation.classList.add("button", "is-primary")
  onClickFunc = 'addOperacionLocalModal("' + func_name + '")'
  buttonOperation.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Operacion");
  buttonOperation.appendChild(buttonText);

  var buttonVector = document.createElement("button");
  buttonVector.classList.add("button", "is-warning");
  onClickFunc = 'addVectorLocalModal("' + func_name + '")'
  buttonVector.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Vector");
  buttonVector.appendChild(buttonText)

  var buttonCondicion = document.createElement("button");
  buttonCondicion.classList.add("button", "is-light");
  onClickFunc = 'addCondition("' + func_name + '")'
  buttonCondicion.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Condicion");
  buttonCondicion.appendChild(buttonText)

  var buttonLoop = document.createElement("button");
  buttonLoop.classList.add("button", "is-dark");
  onClickFunc = 'addLoop("' + func_name + '")'
  buttonLoop.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Ciclo");
  buttonLoop.appendChild(buttonText)

  var buttonReturn = document.createElement("button");
  buttonReturn.classList.add("button", "is-danger");
  onClickFunc = 'addReturn("' + func_name + '")'
  buttonReturn.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Regresa");
  buttonReturn.appendChild(buttonText)

  buttons.appendChild(buttonVariable);
  buttons.appendChild(buttonOperation);
  buttons.appendChild(buttonVector);
  buttons.appendChild(buttonCondicion);
  buttons.appendChild(buttonLoop);
  buttons.appendChild(buttonReturn);
  divButtonsHTML.appendChild(buttons)

  var divUnifyHTML = document.createElement("div");
  divUnifyHTML.classList.add("is-function");

  var varHtml = document.createTextNode(GlobalFuncs[func_name].header);
  divFuncHTML.appendChild(varHtml)

  divUnifyHTML.appendChild(divFuncHTML);
  divUnifyHTML.appendChild(divVariablesHTML)
  divUnifyHTML.appendChild(divButtonsHTML)
  document.getElementById("divFuncs").appendChild(divUnifyHTML);
  hideModal();
  return ;
}

function editFunction(func_name){
  var editVar = document.getElementById("name" + func_name)
  editVar.innerHTML = GlobalFuncs[func_name].header
  hideModal();
  return;
}

function addLocalVar(func_name, varname){
  var divVarHTML = document.createElement("div");
  divVarHTML.classList.add("is-variable");
  divVarHTML.setAttribute("id", varname)
  var varHtml = document.createTextNode(GlobalFuncs[func_name][varname]);
  divVarHTML.appendChild(varHtml);
  document.getElementById(func_name).appendChild(divVarHTML);
  hideModal();
  return ;
}

function editLocalVar(func_name, variable){
  var editVar = document.getElementById(func_name).querySelector("#" + variable);
  editVar.innerHTML = GlobalFuncs[func_name][variable]
  hideModal();
  return ;
}

function addLocalOperator(func_name){
  console.log("op in func", func_name);
}

function addLocalVector(func_name){
  console.log("vector in func", func_name);
}

function addCondition(id){
  console.log("condition", id);
}

function addLoop(id){
  console.log("loop",id);
}

function addReturn(id){
  console.log("return",id);
}

/* -------- Funciones para crear globales en el codigo y run -------- */
function execute(){
  for (i in GlobalVars){
    console.log(GlobalVars[i]);
  }
}

function createGlobalVariable(){
  var global_var = "var "
  if(document.getElementById("globalInt").checked == true){
    global_var += "int "
  }
  if(document.getElementById("globalFloat").checked == true){
    global_var += "float "
  }
  if(document.getElementById("globalBool").checked == true){
    global_var += "bool "
  }
  if(document.getElementById("globalString").checked == true){
    global_var += "string "
  }
  varName = document.getElementById("globalVarName").value
  global_var += varName
  global_var += " ;"
  if(GlobalVars[varName] != undefined){
    GlobalVars[varName] = global_var
    editGlobalVar(varName)
    return ;
  }
  GlobalVars[varName] = global_var
  addGlobalVar(varName);
  return ;
}

function createFunction(){
  var function_var = "Function "
  if(document.getElementById("functionInt").checked == true){
    function_var += "int "
  }
  if(document.getElementById("functionFloat").checked == true){
    function_var += "float "
  }
  if(document.getElementById("functionBool").checked == true){
    function_var += "bool "
  }
  if(document.getElementById("functionString").checked == true){
    function_var += "string "
  }
  if(document.getElementById("functionVoid").checked == true){
    function_var += "void "
  }
  functionName = document.getElementById("functionName").value
  function_var += functionName
  if(GlobalFuncs[functionName] != undefined){
    GlobalFuncs[functionName].header = function_var
    editFunction(functionName);
    return;
  }
  GlobalFuncs[functionName] = {header: function_var}
  addFunction(functionName)
  return ;
}

function createLocalVar(func_name){
  var local_var = "var "
  if(document.getElementById("localInt").checked == true){
  local_var += "int "
  }
  if(document.getElementById("localFloat").checked == true){
    local_var += "float "
  }
  if(document.getElementById("localBool").checked == true){
    local_var += "bool "
  }
  if(document.getElementById("localString").checked == true){
    local_var += "string "
  }
  varName = document.getElementById("localVarName").value
  local_var += varName
  local_var += " ;"
  if(GlobalFuncs[func_name][varName] != undefined){
    GlobalFuncs[func_name][varName] = local_var
    editLocalVar(func_name, varName)
    return ;
  }
  GlobalFuncs[func_name][varName] = local_var
  addLocalVar(func_name, varName);
  return ;
}

function createLocalOperator(func_name){

}

function createLocalVector(func_name){

}


/* -------- Funciones de modales -------- */

function hideModal(){
  var modal = document.querySelector('.is-active');
  if(modal != null){
      modal.classList.toggle('is-active');
  }
}

function addVariableGlobalModal(){
  var modal = document.getElementById('addVariableGlobalModal');
  modal.classList.toggle('is-active');
}

function addFunctionModal(){
  var modal = document.getElementById('addFunctionModal');
  modal.classList.toggle('is-active');
}

function addVariableLocalModal(func_name){
  var button = document.getElementById('addVariableLocalButton');
  onClickFunc = 'createLocalVar("'+ func_name +'")'
  button.setAttribute("onclick", onClickFunc)
  var modal = document.getElementById('addVariableLocalModal');
  modal.classList.toggle('is-active');
}

function addVectorLocalModal(){
  var modal = document.getElementById('addVectorLocalModal');
  modal.classList.toggle('is-active');
}

function addOperacionLocalModal(){
  var modal = document.getElementById('addOperacionLocalModal');
  modal.classList.toggle('is-active');
}

function addCondicionModal(){
  var modal = document.getElementById('addOperacionLocalModal');
  modal.classList.toggle('is-active');
}
