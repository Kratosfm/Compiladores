resultType = {
	int : {
		int : {
			"+" : int,
			"-" : int,
			"*" : int,
			"/" : int,
			">" : bool,
			"<" : bool,
			">=" : bool,
			"<=" : bool,
			"==" : bool,
			"!=" : bool,
			"||" : "err",
			"&&" : "err"
		},
		float : {
			"+" : float,
			"-" : float,
			"*" : float,
			"/" : float,
			">" : bool,
			"<" : bool,
			">=" : bool,
			"<=" : bool,
			"==" : bool,
			"!=" : bool,
			"||" : "err",
			"&&" : "err"
		},
		str : {
			"+" : "err",
			"-" : "err",
			"*" : "err",
			"/" : "err",
			">" : "err",
			"<" : "err",
			">=" : "err",
			"<=" : "err",
			"==" : "err",
			"!=" : "err",
			"||" : "err",
			"&&" : "err"
		},
		bool : {
			"+" : "err",
			"-" : "err",
			"*" : "err",
			"/" : "err",
			">" : "err",
			"<" : "err",
			">=" : "err",
			"<=" : "err",
			"==" : "err",
			"!=" : "err",
			"||" : "err",
			"&&" : "err"
		}
	},
	float : {
		int : {
			"+" : float,
			"-" : float,
			"*" : float,
			"/" : float,
			">" : bool,
			"<" : bool,
			">=" : bool,
			"<=" : bool,
			"==" : bool,
			"!=" : bool,
			"||" : "err",
			"&&" : "err"
		},
		float : {
			"+" : float,
			"-" : float,
			"*" : float,
			"/" : float,
			">" : bool,
			"<" : bool,
			">=" : bool,
			"<=" : bool,
			"==" : bool,
			"!=" : bool,
			"||" : "err",
			"&&" : "err"
		},
		str : {
			"+" : "err",
			"-" : "err",
			"*" : "err",
			"/" : "err",
			">" : "err",
			"<" : "err",
			">=" : "err",
			"<=" : "err",
			"==" : "err",
			"!=" : "err",
			"||" : "err",
			"&&" : "err"
		},
		bool : {
			"+" : "err",
			"-" : "err",
			"*" : "err",
			"/" : "err",
			">" : "err",
			"<" : "err",
			">=" : "err",
			"<=" : "err",
			"==" : "err",
			"!=" : "err",
			"||" : "err",
			"&&" : "err"
		}
	},
	str : {
		int : {
			"+" : "err",
			"-" : "err",
			"*" : "err",
			"/" : "err",
			">" : "err",
			"<" : "err",
			">=" : "err",
			"<=" : "err",
			"==" : "err",
			"!=" : "err",
			"||" : "err",
			"&&" : "err"
		},
		float : {
			"+" : "err",
			"-" : "err",
			"*" : "err",
			"/" : "err",
			">" : "err",
			"<" : "err",
			">=" : "err",
			"<=" : "err",
			"==" : "err",
			"!=" : "err",
			"||" : "err",
			"&&" : "err"
		},
		str : {
			"+" : str,
			"-" : "err",
			"*" : "err",
			"/" : "err",
			">" : "err",
			"<" : "err",
			">=" : "err",
			"<=" : "err",
			"==" : bool,
			"!=" : bool,
			"||" : "err",
			"&&" : "err"
		},
		bool : {
			"+" : "err",
			"-" : "err",
			"*" : "err",
			"/" : "err",
			">" : "err",
			"<" : "err",
			">=" : "err",
			"<=" : "err",
			"==" : "err",
			"!=" : "err",
			"||" : "err",
			"&&" : "err"
		}
	},
	bool : {
		int : {
			"+" : "err",
			"-" : "err",
			"*" : "err",
			"/" : "err",
			">" : "err",
			"<" : "err",
			">=" : "err",
			"<=" : "err",
			"==" : "err",
			"!=" : "err",
			"||" : "err",
			"&&" : "err"
		},
		float : {
			"+" : "err",
			"-" : "err",
			"*" : "err",
			"/" : "err",
			">" : "err",
			"<" : "err",
			">=" : "err",
			"<=" : "err",
			"==" : "err",
			"!=" : "err",
			"||" : "err",
			"&&" : "err"
		},
		str : {
			"+" : "err",
			"-" : "err",
			"*" : "err",
			"/" : "err",
			">" : "err",
			"<" : "err",
			">=" : "err",
			"<=" : "err",
			"==" : "err",
			"!=" : "err",
			"||" : "err",
			"&&" : "err"
		},
		bool : {
			"+" : "err",
			"-" : "err",
			"*" : "err",
			"/" : "err",
			">" : "err",
			"<" : "err",
			">=" : "err",
			"<=" : "err",
			"==" : bool,
			"!=" : bool,
			"||" : bool,
			"&&" : bool
		}
	}
}

def getReturnType(op1, op2, operator):
	return resultType[op1][op2][operator]

#
def isSymbol(sym):
	if (sym == '+' or sym == '-' or sym == "*" or sym == "/" or sym == ">" or sym == "<" or sym == ">=" or sym == "<=" or sym == "==" or sym == "!=" or sym == "||" or sym == "&&"):
		return True
	else:
		return False

def cuadruplos(expres):
	popper = []
	pilaid = []
	pilaTipos = []
	pilaSaltos = []
	t = []
