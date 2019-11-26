GlobalVars = {}
GlobalFuncs = {}
MainBloq = {
  header: "main{",
  oper: {},
  cond: 0,
  loop: 0,
  operat: 0
}

paramCounter = 0;

/* -------- Funciones de modales -------- */

function hideModal(){
  paramCounter = 0
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
  $("#params").empty()
  var modal = document.getElementById('addFunctionModal');
  modal.classList.toggle('is-active');
}

function addVariableLocalModal(id){
  var button = document.getElementById('addVariableLocalButton');
  onClickFunc = 'createLocalVar("'+ id +'")'
  button.setAttribute("onclick", onClickFunc)
  var modal = document.getElementById('addVariableLocalModal');
  modal.classList.toggle('is-active');
}

function addCondicionModal(id){
  var button = document.getElementById('addLocalCondition');
  onClickFunc = 'createLocalCondition("'+ id +'")'
  button.setAttribute("onclick", onClickFunc)
  // butonElse = document.getElementById("addElseButton");
  // onClickButtonFunc = 'addElseToModal("'+ id +'")'
  // butonElse.setAttribute("onclick", onClickButtonFunc)
  var modal = document.getElementById('addConditionLocalModal');
  modal.classList.toggle('is-active');
}

function addLoopLocalModal(id){
  var button = document.getElementById('addLocalLoop');
  onClickFunc = 'createLocalLoop("'+ id +'")'
  button.setAttribute("onclick", onClickFunc)
  var modal = document.getElementById('addLoopLocalModal');
  modal.classList.toggle('is-active');
}

function addOperacionLocalModal(id){
  var button = document.getElementById('addLocalOperator');
  onClickFunc = 'createLocalOperator("'+ id +'")'
  button.setAttribute("onclick", onClickFunc)
  var modal = document.getElementById('addOperacionLocalModal');
  modal.classList.toggle('is-active');
}

function addReturnModal(id){
  var button = document.getElementById('addLocalReturn');
  onClickFunc = 'createReturn("'+ id +'")'
  button.setAttribute("onclick", onClickFunc)
  var modal = document.getElementById('addReturnModal');
  modal.classList.toggle('is-active');
}

function addVariableMainModal(){
  var modal = document.getElementById('addVariableMainModal');
  modal.classList.toggle('is-active');
}

function addConditionMainModal(id){
  var button = document.getElementById('addMainCondition')
  onClickFunc = 'createMainCondition("'+ id +'")'
  button.setAttribute("onclick", onClickFunc)
  // butonElse = document.getElementById("addElseButton");
  // onClickButtonFunc = 'addElseToModal("'+ id +'")'
  // butonElse.setAttribute("onclick", onClickButtonFunc)
  var modal = document.getElementById('addConditionMainModal');
  modal.classList.toggle('is-active');
}

function addOperacionMainModal(id){
  var button = document.getElementById('addMainOperator');
  onClickFunc = 'createMainOperator("'+ id +'")'
  button.setAttribute("onclick", onClickFunc)
  var modal = document.getElementById('addOperacionMainModal');
  modal.classList.toggle('is-active');
}

function addLoopMainModal(id){
  var button = document.getElementById('addMainLoop');
  onClickFunc = 'createMainLoop("'+ id +'")'
  button.setAttribute("onclick", onClickFunc)
  var modal = document.getElementById('addLoopMainModal');
  modal.classList.toggle('is-active');
}

/* -------- Funciones para crear globales en el codigo y run -------- */
function execute(){
  file = "program: \n"

  for( i in GlobalVars){
    file += GlobalVars[i] + "\n";
  }

  for( i in GlobalFuncs){
    file += getCodeFromDict(GlobalFuncs[i])
  }
  if(file[file.length-2] == "{"){
    file += "}\n"
  }
  file += getCodeFromDict(MainBloq);
  if(file[file.length-2] == "{"){
    file += "}\n"
  }


  json_to_send = {data: file}
  $.ajax({
    url: "http://localhost:3000/compile/",
    type: "get",
    data: JSON.stringify(json_to_send),
    headers: {
      'Content-Type': 'application/json'
    },
    //dataType: "json",
    success: function(data) {
      console.log(data)
    },
    error: function(err) {
      console.log(err)
    }
  })
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
    GlobalFuncs[functionName].oper = {}
    GlobalFuncs[functionName].cond = 0
    GlobalFuncs[functionName].loop = 0
    GlobalFuncs[functionName].operat = 0
    createParams(functionName, function_var)
    editFunction(functionName);
    return;
  }
  GlobalFuncs[functionName] = {}
  GlobalFuncs[functionName].oper = {}
  GlobalFuncs[functionName].cond = 0
  GlobalFuncs[functionName].loop = 0
  GlobalFuncs[functionName].operat = 0
  createParams(functionName, function_var)
  addFunction(functionName)
  return ;
}

function createParams(func_name, header){
  header += '('
  param_var = ""
  for(i = 1; i <= paramCounter; i++){
    if(document.getElementById("paramInt" + i).checked == true){
    param_var = "int "
    }
    if(document.getElementById("paramFloat" + i).checked == true){
      param_var = "float "
    }
    if(document.getElementById("paramBool" + i).checked == true){
      param_var = "bool "
    }
    if(document.getElementById("paramString" + i).checked == true){
      param_var = "string "
    }
    param_Name = document.getElementById("paramName" + i).value;
    param_var += param_Name;
    if(i != paramCounter){
      param_var += " ,"
    }
    header += param_var
  }
  header += "){"
  GlobalFuncs[func_name].header = header
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
  if(GlobalFuncs[func_name].oper[varName] != undefined){
    GlobalFuncs[func_name].oper[varName] = local_var
    editLocalVar(func_name, varName)
    return ;
  }
  GlobalFuncs[func_name].oper[varName] = local_var
  addLocalVar(func_name, varName);
  return ;
}

function createLocalCondition(route){
  var local_cond_if = "if ("
  local_cond_if += document.getElementById("conditionInput").value
  local_cond_if += "){"
  path = getPath(route);
  elseFlag = document.getElementById("elseYes").checked
  if(elseFlag){
    var local_cond_else = "else{"
  }

  var auxRoute ;

  if(path[1] == null){
    GlobalFuncs[path[0]].oper["if" + GlobalFuncs[path[0]].cond] = {header: local_cond_if, oper:{}}
    if(elseFlag){
      GlobalFuncs[path[0]].oper["else" + GlobalFuncs[path[0]].cond]= {header: local_cond_else, oper:{}}
    }
  }
  else{
    path.forEach(function(key, index){
      if(index == 0){
        auxRoute = GlobalFuncs[key].oper
      }
      else if (key != null) {
        auxRoute = auxRoute[key].oper
      }
      else{
        auxRoute["if"+ GlobalFuncs[path[0]].cond] = {header: local_cond_if, oper:{}}
        GlobalFuncs = addToDict(auxRoute, index, GlobalFuncs, path, 0)
        if(elseFlag){
          auxRoute["else"+ GlobalFuncs[path[0]].cond] = {header: local_cond_else, oper:{}}
        }
      }
    })
  }
  if(elseFlag){
    addLocalCondition(route, true)
  }
  else {
    addLocalCondition(route, false)
  }
  return ;
}

function createLocalLoop(route){
  var local_loop = "while ("
  local_loop += document.getElementById("loopInput").value
  local_loop += "){"
  path = getPath(route);

  var auxRoute ;

  if(path[1] == null){
    GlobalFuncs[path[0]].oper["while" + GlobalFuncs[path[0]].loop] = {header: local_loop, oper:{}}
  }
  else{
    path.forEach(function(key, index){
      if(index == 0){
        auxRoute = GlobalFuncs[key].oper
      }
      else if (key != null) {
        auxRoute = auxRoute[key].oper
      }
      else{
        auxRoute["while"+ GlobalFuncs[path[0]].loop] = {header: local_loop, oper:{}}
        GlobalFuncs = addToDict(auxRoute, index, GlobalFuncs, path, 0)
      }
    })
  }
  addLocalLoop(route + ">while" + GlobalFuncs[path[0]].loop)
  return ;
}

function createLocalOperator(route){
  local_op = document.getElementById("textbox").value
  local_op += " ;"
  path = getPath(route);

  var auxRoute ;

  if(path[1] == null){
    GlobalFuncs[path[0]].oper["op" + GlobalFuncs[path[0]].operat] = local_op
  }
  else{
    path.forEach(function(key, index){
      if(index == 0){
        auxRoute = GlobalFuncs[key].oper
      }
      else if (key != null) {
        auxRoute = auxRoute[key].oper
      }
      else{
        auxRoute["op"+ GlobalFuncs[path[0]].operat] = local_op
        GlobalFuncs = addToDict(auxRoute, index, GlobalFuncs, path, 0)
      }
    })
  }
  addLocalOperator(route + ">op" + GlobalFuncs[path[0]].operat, local_op)
  return ;
}

function createReturn(func_name){
  var expresion = document.getElementById("returnInput").value;
  var local_return = "return " + expresion + " ;"
  GlobalFuncs[func_name].return = local_return
  addLocalReturn(func_name, local_return);
  return ;
}

function createMainVariable(){
  var main_var = "var "
  if(document.getElementById("mainInt").checked == true){
    main_var += "int "
  }
  if(document.getElementById("mainFloat").checked == true){
    main_var += "float "
  }
  if(document.getElementById("mainBool").checked == true){
    main_var += "bool "
  }
  if(document.getElementById("mainString").checked == true){
    main_var += "string "
  }
  varName = document.getElementById("VarNameMain").value
  main_var += varName
  main_var += " ;"

  if(MainBloq.oper[varName] != undefined){
    MainBloq.oper[varName] = main_var
    editMainVar(varName)
  }
  else {
    MainBloq.oper[varName] = main_var
    addMainVar(varName);
  }
  return ;
}

function createMainCondition(route){
  var main_cond_if = "if ("
  main_cond_if += document.getElementById("conditionInputMain").value
  main_cond_if += "){"
  path = getPath(route);
  elseFlag = document.getElementById("elseYesMain").checked
  if(elseFlag){
    var main_cond_else = "else{"
  }

  var auxRoute ;

  if(path[1] == null){
    MainBloq.oper["if" + MainBloq.cond] = {header: main_cond_if, oper:{}}
    if(elseFlag){
      MainBloq.oper["else" + MainBloq.cond]= {header: main_cond_else, oper:{}}
    }
  }
  else{
    path.forEach(function(key, index){
      if(index == 0){
        auxRoute = MainBloq.oper
      }
      else if (key != null) {
        auxRoute = auxRoute[key].oper
      }
      else{
        auxRoute["if"+ MainBloq.cond] = {header: main_cond_if, oper:{}}
        MainBloq = addToDict(auxRoute, index, MainBloq, path, 0)
        if(elseFlag){
          auxRoute["else"+ MainBloq.cond] = {header: main_cond_else, oper:{}}
        }
      }
    })
  }
  if(elseFlag){
    addMainCondition(route, true)
  }
  else {
    addMainCondition(route, false)
  }
  return ;
}

function createMainOperator(route){
  main_op = document.getElementById("textboxMain").value
  main_op += " ;"
  path = getPath(route);

  var auxRoute ;

  if(path[1] == null){
    MainBloq.oper["op" + MainBloq.operat] = main_op
  }
  else{
    path.forEach(function(key, index){
      if(index == 0){
        auxRoute = MainBloq.oper
      }
      else if (key != null) {
        auxRoute = auxRoute[key].oper
      }
      else{
        auxRoute["op"+ MainBloq.operat] = main_op
        MainBloq = addToDict(auxRoute, index, MainBloq, path, 0)
      }
    })
  }
  addMainOperator(route + ">op" + GlobalFuncs.operat, main_op)
  return ;
}

function createMainLoop(route){
  var local_loop = "while ("
  local_loop += document.getElementById("loopInputMain").value
  local_loop += "){"
  path = getPath(route);

  var auxRoute ;

  if(path[1] == null){
    MainBloq.oper["while" + MainBloq.loop] = {header: local_loop, oper:{}}
  }
  else{
    path.forEach(function(key, index){
      if(index == 0){
        auxRoute = MainBloq.oper
      }
      else if (key != null) {
        auxRoute = auxRoute[key].oper
      }
      else{
        auxRoute["while"+ MainBloq.loop] = {header: local_loop, oper:{}}
        MainBloq = addToDict(auxRoute, index, MainBloq, path, 0)
      }
    })
  }
  addMainLoop(route + ">while" + MainBloq.loop)
  return ;
}

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
  var divBloqHTML = document.createElement("div")
  divBloqHTML.setAttribute("id", func_name);

  var divButtonsHTML = document.createElement("div");
  divFuncHTML.classList.add("is-function");
  divFuncHTML.setAttribute("id", "name" + func_name);

  var buttons = document.createElement("div");
  buttons.classList.add("buttons", "has-addons");
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
  onClickFunc = 'addCondicionModal("' + func_name + '")'
  buttonCondicion.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Condicion");
  buttonCondicion.appendChild(buttonText)

  var buttonLoop = document.createElement("button");
  buttonLoop.classList.add("button", "is-dark");
  onClickFunc = 'addLoopLocalModal("' + func_name + '")'
  buttonLoop.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Ciclo");
  buttonLoop.appendChild(buttonText)

  var buttonReturn = document.createElement("button");
  buttonReturn.classList.add("button", "is-danger");
  onClickFunc = 'addReturnModal("' + func_name + '")'
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

  var divKeyHTML = document.createElement("div")
  var varHtml2 = document.createTextNode("}")
  divKeyHTML.setAttribute("style", "margin-bottom: 15px;")
  divKeyHTML.appendChild(varHtml2)

  var divUnifyHTML = document.createElement("div");
  divUnifyHTML.classList.add("is-function");

  headerText = GlobalFuncs[func_name].header

  var varHtml = document.createTextNode(headerText);
  divFuncHTML.appendChild(varHtml)

  divUnifyHTML.appendChild(divFuncHTML)
  divUnifyHTML.appendChild(divBloqHTML)
  divUnifyHTML.appendChild(divButtonsHTML)
  divUnifyHTML.appendChild(divKeyHTML)

  document.getElementById("divFuncs").appendChild(divUnifyHTML);
  hideModal();
  return ;
}

function editFunction(func_name){
  $("#" + func_name).empty()
  var editVar = document.getElementById("name" + func_name)
  editVar.innerHTML = GlobalFuncs[func_name].header
  hideModal();
  return;
}

function addParamsToModal(){
  paramCounter = paramCounter + 1;
  var paramDiv = '<h5 class="subtitle is-5">Selecciona el tipo del parametro:</h5>'+
  '<div class="control">'+
    '<label class="radio">'+
      '<input id="' + ("paramInt" + paramCounter) + '" class="radio-param"type="radio" name="type' + paramCounter +'">'+
      'Entero'+
    '</label>'+
    '<label class="radio">'+
      '<input id="' + ("paramFloat" + paramCounter) + '" class="radio-param"type="radio" name="type' + paramCounter +'">'+
      'Flotante'+
    '</label>'+
    '<label class="radio">'+
      '<input id="' + ("paramBool" + paramCounter) + '" class="radio-param"type="radio" name="type' + paramCounter +'">'+
      'Booleano'+
    '</label>'+
    '<label class="radio">'+
      '<input id="' + ("paramString" + paramCounter) + '" class="radio-param"type="radio" name="type' + paramCounter +'">'+
      'Frase'+
    '</label>'+
  '</div>'+
  '<br>'+
  '<div class="columns">'+
    '<div class="column is-5">'+
      '<h5 class="subtitle is-5" style="margin-top: 5px;">Nombre del parametro:</h5>'+
    '</div>'+
    '<div class="column" style="margin-left: -50px;">'+
      '<input id="' + ("paramName" + paramCounter) + '" class="input" type="text" placeholder="Nombre">'+
    '</div>'+
  '</div>"'
  $(paramDiv).appendTo("#params")
  return ;
}

function addLocalVar(func_name, varname){
  var divVarHTML = document.createElement("div");
  divVarHTML.classList.add("is-variable");
  id = func_name + ">" + varname
  divVarHTML.setAttribute("id", id)
  var varHtml = document.createTextNode(GlobalFuncs[func_name].oper[varname]);
  divVarHTML.appendChild(varHtml);
  document.getElementById(func_name).appendChild(divVarHTML);
  hideModal();
  return ;
}

function editLocalVar(func_name, variable){
  var editVar = document.getElementById(func_name + ">" + variable);
  editVar.innerHTML = GlobalFuncs[func_name].oper[variable]
  hideModal();
  return ;
}

function addLocalCondition(route, elseFlag){
  var path = getPath(route)


  if(elseFlag){
    divElseHTML = addElseCondition(route + ">else" + GlobalFuncs[path[0]].cond)
  }
  divIfHTML = addIfCondition(route + ">if" + GlobalFuncs[path[0]].cond)

  var divUnifyHTML = document.createElement("div");
  divUnifyHTML.classList.add("is-condition");
  divUnifyHTML.appendChild(divIfHTML)
  if(elseFlag){
    divUnifyHTML.appendChild(divElseHTML)
  }

  document.getElementById(route).appendChild(divUnifyHTML);
  GlobalFuncs[path[0]].cond = GlobalFuncs[path[0]].cond + 1
  hideModal()
}

function addIfCondition(route){
  path = getPath(route);
  var divHeadCondHTML = document.createElement("div");
  divHeadCondHTML.classList.add("is-condition");
  divHeadCondHTML.setAttribute("id", "head:" + route);
  var pointer ;
  var headerText = "";
  path.forEach(function(value, index){
    if(index == 0 ){
      pointer = GlobalFuncs[value].oper
    }
    else if(value != null){
      headerText = pointer[value].header
      pointer = pointer[value].oper
    }
  })

  var varHtml = document.createTextNode(headerText);
  divHeadCondHTML.appendChild(varHtml);

  var divBloqHTML = document.createElement("div");
  divBloqHTML.classList.add("is-condition");
  divBloqHTML.setAttribute("id", route);

  var divButtonsHTML = document.createElement("div");

  var buttons = document.createElement("div");
  buttons.classList.add("buttons", "has-addons");
  buttons.setAttribute("style", "margin-top: 15px;")

  var buttonOperation = document.createElement("button");
  buttonOperation.classList.add("button", "is-primary")
  onClickFunc = 'addOperacionLocalModal("' + route + '")'
  buttonOperation.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Operacion");
  buttonOperation.appendChild(buttonText);

  var buttonCondicion = document.createElement("button");
  buttonCondicion.classList.add("button", "is-light");
  onClickFunc = 'addCondicionModal("' + route + '")'
  buttonCondicion.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Condicion");
  buttonCondicion.appendChild(buttonText)

  var buttonLoop = document.createElement("button");
  buttonLoop.classList.add("button", "is-dark");
  onClickFunc = 'addLoopLocalModal("' + route + '")'
  buttonLoop.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Ciclo");
  buttonLoop.appendChild(buttonText)

  buttons.appendChild(buttonOperation);
  buttons.appendChild(buttonCondicion);
  buttons.appendChild(buttonLoop);
  divButtonsHTML.appendChild(buttons)

  var divKeyHTML = document.createElement("div")
  var varHtml2 = document.createTextNode("}")
  divKeyHTML.setAttribute("style", "margin-bottom: 15px;")
  divKeyHTML.appendChild(varHtml2)

  divReturn = document.createElement("div")
  divReturn.appendChild(divHeadCondHTML)
  divReturn.appendChild(divButtonsHTML)
  divReturn.appendChild(divBloqHTML)
  divReturn.appendChild(divKeyHTML)


  return divReturn;

}

function addElseCondition(route){
  path = getPath(route)

  var divHeadCondHTML = document.createElement("div");
  divHeadCondHTML.classList.add("is-condition");
  divHeadCondHTML.setAttribute("id", "head:" + route);

  var varHtml = document.createTextNode("else{");
  divHeadCondHTML.appendChild(varHtml);

  var divBloqHTML = document.createElement("div");
  divBloqHTML.classList.add("is-condition");
  divBloqHTML.setAttribute("id", route);

  var divButtonsHTML = document.createElement("div");

  var buttons = document.createElement("div");
  buttons.classList.add("buttons", "has-addons");
  buttons.setAttribute("style", "margin-top: 15px;")

  var buttonOperation = document.createElement("button");
  buttonOperation.classList.add("button", "is-primary")
  onClickFunc = 'addOperacionLocalModal("' + route + '")'
  buttonOperation.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Operacion");
  buttonOperation.appendChild(buttonText);

  var buttonCondicion = document.createElement("button");
  buttonCondicion.classList.add("button", "is-light");
  onClickFunc = 'addCondicionModal("' + route + '")'
  buttonCondicion.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Condicion");
  buttonCondicion.appendChild(buttonText)

  var buttonLoop = document.createElement("button");
  buttonLoop.classList.add("button", "is-dark");
  onClickFunc = 'addLoopLocalModal("' + route + '")'
  buttonLoop.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Ciclo");
  buttonLoop.appendChild(buttonText)

  buttons.appendChild(buttonOperation);
  buttons.appendChild(buttonCondicion);
  buttons.appendChild(buttonLoop);
  divButtonsHTML.appendChild(buttons)

  var divKeyHTML = document.createElement("div")
  var varHtml2 = document.createTextNode("}")
  divKeyHTML.setAttribute("style", "margin-bottom: 15px;")
  divKeyHTML.appendChild(varHtml2)

  divReturn = document.createElement("div")
  divReturn.appendChild(divHeadCondHTML)
  divReturn.appendChild(divButtonsHTML)
  divReturn.appendChild(divBloqHTML)
  divReturn.appendChild(divKeyHTML)

  return divReturn;

}

function addLocalLoop(route){
  path = getPath(route)

  var divHeadLoopHTML = document.createElement("div");
  divHeadLoopHTML.classList.add("is-loop");
  divHeadLoopHTML.setAttribute("id", "head:" + route);

  var pointer ;
  var headerText = "";
  path.forEach(function(value, index){
    if(index == 0 ){
      pointer = GlobalFuncs[value].oper
    }
    else if(value != null){
      headerText = pointer[value].header
      pointer = pointer[value].oper
    }
    else{
    }
  })

  var varHtml = document.createTextNode(headerText);
  divHeadLoopHTML.appendChild(varHtml);

  var divBloqHTML = document.createElement("div");
  divBloqHTML.classList.add("is-loop");
  divBloqHTML.setAttribute("id", route);

  var divButtonsHTML = document.createElement("div");

  var buttons = document.createElement("div");
  buttons.classList.add("buttons", "has-addons");
  buttons.setAttribute("style", "margin-top: 15px;")

  var buttonOperation = document.createElement("button");
  buttonOperation.classList.add("button", "is-primary")
  onClickFunc = 'addOperacionLocalModal("' + route + '")'
  buttonOperation.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Operacion");
  buttonOperation.appendChild(buttonText);

  var buttonCondicion = document.createElement("button");
  buttonCondicion.classList.add("button", "is-light");
  onClickFunc = 'addCondicionModal("' + route + '")'
  buttonCondicion.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Condicion");
  buttonCondicion.appendChild(buttonText)

  var buttonLoop = document.createElement("button");
  buttonLoop.classList.add("button", "is-dark");
  onClickFunc = 'addLoopLocalModal("' + route + '")'
  buttonLoop.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Ciclo");
  buttonLoop.appendChild(buttonText)

  buttons.appendChild(buttonOperation);
  buttons.appendChild(buttonCondicion);
  buttons.appendChild(buttonLoop);
  divButtonsHTML.appendChild(buttons)

  var divKeyHTML = document.createElement("div")
  var varHtml2 = document.createTextNode("}")
  divKeyHTML.setAttribute("style", "margin-bottom: 15px;")
  divKeyHTML.appendChild(varHtml2)

  var divUnifyHTML = document.createElement("div");
  divUnifyHTML.classList.add("is-loop");
  divUnifyHTML.appendChild(divHeadLoopHTML)
  divUnifyHTML.appendChild(divButtonsHTML)
  divUnifyHTML.appendChild(divBloqHTML)
  divUnifyHTML.appendChild(divKeyHTML)

  document.getElementById(getWhereToAppend(route)).appendChild(divUnifyHTML);
  GlobalFuncs[path[0]].loop = GlobalFuncs[path[0]].loop + 1
  hideModal();
}

function addLocalOperator(route, value){
  path = getPath(route)

  var divOperatorValueHTML = document.createElement("div");
  divOperatorValueHTML.classList.add("is-op");
  divOperatorValueHTML.setAttribute("id", route);


  var varHtml = document.createTextNode(value);
  divOperatorValueHTML.appendChild(varHtml);

  var divUnifyHTML = document.createElement("div");
  divUnifyHTML.classList.add("is-op");
  divUnifyHTML.appendChild(divOperatorValueHTML)

  document.getElementById(getWhereToAppend(route)).appendChild(divUnifyHTML);
  GlobalFuncs[path[0]].operat = GlobalFuncs[path[0]].operar + 1
  hideModal();
}

function addLocalReturn(route, value){
  html = '<div id="return'+ route +'" class="is-return">'
  html += value
  html += '</div>'
  $(html).appendTo("#" + route)
  hideModal()
}

function addMainVar(varname){
  var divVarHTML = document.createElement("div");
  divVarHTML.classList.add("is-variable");
  id = "main>" + varname
  divVarHTML.setAttribute("id", id)
  var varHtml = document.createTextNode(MainBloq.oper[varname]);
  divVarHTML.appendChild(varHtml);
  document.getElementById("main").appendChild(divVarHTML);
  hideModal();
  return ;
}

function editMainVar(varname){
  var editVar = document.getElementById("main>" + varname);
  editVar.innerHTML = MainBloq.oper[varname]
  hideModal();
  return ;
}

function addMainCondition(route, elseFlag){
  var path = getPath(route)


  if(elseFlag){
    divElseHTML = addElseConditionMain(route + ">else" + MainBloq.cond)
  }
  divIfHTML = addIfConditionMain(route + ">if" + MainBloq.cond)

  var divUnifyHTML = document.createElement("div");
  divUnifyHTML.classList.add("is-condition");
  divUnifyHTML.appendChild(divIfHTML)
  if(elseFlag){
    divUnifyHTML.appendChild(divElseHTML)
  }

  document.getElementById(route).appendChild(divUnifyHTML);
  MainBloq.cond = MainBloq.cond + 1
  hideModal()
}

function addIfConditionMain(route){
  path = getPath(route);
  var divHeadCondHTML = document.createElement("div");
  divHeadCondHTML.classList.add("is-condition");
  divHeadCondHTML.setAttribute("id", "head:" + route);
  var pointer ;
  var headerText = "";
  path.forEach(function(value, index){
    if(index == 0 ){
      pointer = MainBloq.oper
    }
    else if(value != null){
      headerText = pointer[value].header
      pointer = pointer[value].oper
    }
  })

  var varHtml = document.createTextNode(headerText);
  divHeadCondHTML.appendChild(varHtml);

  var divBloqHTML = document.createElement("div");
  divBloqHTML.classList.add("is-condition");
  divBloqHTML.setAttribute("id", route);

  var divButtonsHTML = document.createElement("div");

  var buttons = document.createElement("div");
  buttons.classList.add("buttons", "has-addons");
  buttons.setAttribute("style", "margin-top: 15px;")

  var buttonOperation = document.createElement("button");
  buttonOperation.classList.add("button", "is-primary")
  onClickFunc = 'addOperacionMainModal("' + route + '")'
  buttonOperation.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Operacion");
  buttonOperation.appendChild(buttonText);

  var buttonCondicion = document.createElement("button");
  buttonCondicion.classList.add("button", "is-light");
  onClickFunc = 'addConditionMainModal("' + route + '")'
  buttonCondicion.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Condicion");
  buttonCondicion.appendChild(buttonText)

  var buttonLoop = document.createElement("button");
  buttonLoop.classList.add("button", "is-dark");
  onClickFunc = 'addLoopMainModal("' + route + '")'
  buttonLoop.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Ciclo");
  buttonLoop.appendChild(buttonText)

  buttons.appendChild(buttonOperation);
  buttons.appendChild(buttonCondicion);
  buttons.appendChild(buttonLoop);
  divButtonsHTML.appendChild(buttons)

  var divKeyHTML = document.createElement("div")
  var varHtml2 = document.createTextNode("}")
  divKeyHTML.setAttribute("style", "margin-bottom: 15px;")
  divKeyHTML.appendChild(varHtml2)

  divReturn = document.createElement("div")
  divReturn.appendChild(divHeadCondHTML)
  divReturn.appendChild(divButtonsHTML)
  divReturn.appendChild(divBloqHTML)
  divReturn.appendChild(divKeyHTML)


  return divReturn;

}

function addElseConditionMain(route){
  path = getPath(route)

  var divHeadCondHTML = document.createElement("div");
  divHeadCondHTML.classList.add("is-condition");
  divHeadCondHTML.setAttribute("id", "head:" + route);

  var varHtml = document.createTextNode("else{");
  divHeadCondHTML.appendChild(varHtml);

  var divBloqHTML = document.createElement("div");
  divBloqHTML.classList.add("is-condition");
  divBloqHTML.setAttribute("id", route);

  var divButtonsHTML = document.createElement("div");

  var buttons = document.createElement("div");
  buttons.classList.add("buttons", "has-addons");
  buttons.setAttribute("style", "margin-top: 15px;")

  var buttonOperation = document.createElement("button");
  buttonOperation.classList.add("button", "is-primary")
  onClickFunc = 'addOperacionMainModal("' + route + '")'
  buttonOperation.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Operacion");
  buttonOperation.appendChild(buttonText);

  var buttonCondicion = document.createElement("button");
  buttonCondicion.classList.add("button", "is-light");
  onClickFunc = 'addConditionMainModal("' + route + '")'
  buttonCondicion.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Condicion");
  buttonCondicion.appendChild(buttonText)

  var buttonLoop = document.createElement("button");
  buttonLoop.classList.add("button", "is-dark");
  onClickFunc = 'addLoopMainModal("' + route + '")'
  buttonLoop.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Ciclo");
  buttonLoop.appendChild(buttonText)

  buttons.appendChild(buttonOperation);
  buttons.appendChild(buttonCondicion);
  buttons.appendChild(buttonLoop);
  divButtonsHTML.appendChild(buttons)

  var divKeyHTML = document.createElement("div")
  var varHtml2 = document.createTextNode("}")
  divKeyHTML.setAttribute("style", "margin-bottom: 15px;")
  divKeyHTML.appendChild(varHtml2)

  divReturn = document.createElement("div")
  divReturn.appendChild(divHeadCondHTML)
  divReturn.appendChild(divButtonsHTML)
  divReturn.appendChild(divBloqHTML)
  divReturn.appendChild(divKeyHTML)

  return divReturn;

}

function addMainOperator(route, value){
  path = getPath(route)

  var divOperatorValueHTML = document.createElement("div");
  divOperatorValueHTML.classList.add("is-op");
  divOperatorValueHTML.setAttribute("id", route);


  var varHtml = document.createTextNode(value);
  divOperatorValueHTML.appendChild(varHtml);

  var divUnifyHTML = document.createElement("div");
  divUnifyHTML.classList.add("is-op");
  divUnifyHTML.appendChild(divOperatorValueHTML)

  document.getElementById(getWhereToAppend(route)).appendChild(divUnifyHTML);
  MainBloq.operat = MainBloq.operat + 1
  hideModal();
}

function addMainLoop(route){
  path = getPath(route)

  var divHeadLoopHTML = document.createElement("div");
  divHeadLoopHTML.classList.add("is-loop");
  divHeadLoopHTML.setAttribute("id", "head:" + route);

  var pointer ;
  var headerText = "";
  path.forEach(function(value, index){
    if(index == 0 ){
      pointer = MainBloq.oper
    }
    else if(value != null){
      headerText = pointer[value].header
      pointer = pointer[value].oper
    }
    else{
    }
  })

  var varHtml = document.createTextNode(headerText);
  divHeadLoopHTML.appendChild(varHtml);

  var divBloqHTML = document.createElement("div");
  divBloqHTML.classList.add("is-loop");
  divBloqHTML.setAttribute("id", route);

  var divButtonsHTML = document.createElement("div");

  var buttons = document.createElement("div");
  buttons.classList.add("buttons", "has-addons");
  buttons.setAttribute("style", "margin-top: 15px;")

  var buttonOperation = document.createElement("button");
  buttonOperation.classList.add("button", "is-primary")
  onClickFunc = 'addOperacionMainModal("' + route + '")'
  buttonOperation.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Operacion");
  buttonOperation.appendChild(buttonText);

  var buttonCondicion = document.createElement("button");
  buttonCondicion.classList.add("button", "is-light");
  onClickFunc = 'addConditionMainModal("' + route + '")'
  buttonCondicion.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Condicion");
  buttonCondicion.appendChild(buttonText)

  var buttonLoop = document.createElement("button");
  buttonLoop.classList.add("button", "is-dark");
  onClickFunc = 'addLoopMainModal("' + route + '")'
  buttonLoop.setAttribute("onclick", onClickFunc)
  buttonText = document.createTextNode("Ciclo");
  buttonLoop.appendChild(buttonText)

  buttons.appendChild(buttonOperation);
  buttons.appendChild(buttonCondicion);
  buttons.appendChild(buttonLoop);
  divButtonsHTML.appendChild(buttons)

  var divKeyHTML = document.createElement("div")
  var varHtml2 = document.createTextNode("}")
  divKeyHTML.setAttribute("style", "margin-bottom: 15px;")
  divKeyHTML.appendChild(varHtml2)

  var divUnifyHTML = document.createElement("div");
  divUnifyHTML.classList.add("is-loop");
  divUnifyHTML.appendChild(divHeadLoopHTML)
  divUnifyHTML.appendChild(divButtonsHTML)
  divUnifyHTML.appendChild(divBloqHTML)
  divUnifyHTML.appendChild(divKeyHTML)

  document.getElementById(getWhereToAppend(route)).appendChild(divUnifyHTML);
  MainBloq.loop = MainBloq.loop + 1
  hideModal();
}

/* -------- Funciones extras -------- */

function getPath(id){
  generations = []
  pivote = 0
  for (i in id){
    if (id[i] == '>'){
      generations.push(id.substring(pivote, i))
      pivote = parseInt(i) + 1
    }
  }
  generations.push(id.substring(pivote, id.length))
  generations.push(null)
  return generations
}

function getWhereToAppend(id){
  appendHere = ""
  pivote = 0
  for (i in id){
    if (id[i] == '>'){
      appendHere += id.substring(pivote, i)
      pivote = parseInt(i)
    }
  }
  return appendHere
}

function addToDict(objectToAdd, indexFinal, dict, path, count){
  if(indexFinal == 0){
    return objectToAdd;
  }
  else{
    if(path[count] == 'main'){
      dict.oper = addToDict(objectToAdd, indexFinal-1, dict.oper, path,(count+1))
      return dict
    }
    else{
      dict[path[count]].oper = addToDict(objectToAdd, indexFinal-1, dict[path[count]].oper, path,(count+1))
      return dict
    }
  }
}

function getCodeFromVars(){
  code = "" ;
  for( i in GlobalVars){
    code += GlobalVars[i] + "\n"
  }
  return code
}

function getCodeFromDict(dict){
  var file = ""
  var flag = false;
  if(dict.header != undefined){
    file += dict.header + "\n";
  }
  for(i in dict){
    if(typeof(dict[i]) == "object"){
      file += getCodeFromDict(dict[i]);
    }
    else if((typeof dict[i]) == "string" && i != "header"){
      flag = true
      file += dict[i] + "\n"
    }
  }
  if(flag){
    file += "} \n"
  }
  return file
}
