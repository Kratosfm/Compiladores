const express = require('express')
const router = express.Router()
const cors = require('cors')
var fs = require('fs');
var exec = require('child_process').exec;

//Funcion que ejecuta scripts
function execute(command, callback){
    exec(command, function(error, stdout, stderr){ callback(stdout); });
};

//Funcion que ejecuta el script de python
var cmd = function(){
  execute("python3 lexPar.py", function(compilation){
    console.log(compilation);
  });
};

//Funcion que se llama desde el IDE para compilar
var compile = function(req, res){
  fs.writeFile('prueba.txt', req.body.data, function (err) {
    if (err){res.send("BIG ERROR")};
  });
  execute("python3 lexPar.py", function(compilation){
    res.send({"response": compilation})
  });
}

//Rutas de la API
router.all('*', cors());
router.post('/compile', compile);
router.get('*', function(req, res) {
  res.send({
    error: 'This route does not exist... But at least you have internet conecction!'
  })
})

const app = express()
const port = 3000

app.use(express.json())
app.use(router)

app.listen(port);
