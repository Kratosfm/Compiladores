
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL COLON COMA CTE_B CTE_F CTE_I CTE_S DIFFERENT DIVIDE ELSE EQUAL FLOAT FUNCTION ID IF INT LBRACE LKEY LOWEREQ LOWERTHAN LPAREN MAIN MINUS MOREEQ MORETHAN OR PLUS PRINT PROGRAM RBRACE READ RETURN RKEY RPAREN SAME SEMICOLON STRING TIMES VAR VECTOR VOID WHILE\n  \tprogram : PROGRAM COLON global program2 finglobal program3 MAIN main1 mainc finmain\n        | PROGRAM COLON global program2 finglobal MAIN main1 mainc finmain\n        | PROGRAM COLON MAIN main1 mainc finmain\n  \n  \tprogram2 : crear program2\n    \t| crear\n  \n  \tprogram3 : function program3\n    \t| function\n  \n  \tcrear : var\n    \t| vector\n  global :finglobal :main1 :finmain :\n  \tvar : VAR tipo ID SEMICOLON\n  \n  \ttipo : INT\n    \t| FLOAT\n        | STRING\n        | BOOL\n  \n  \tvector : VECTOR ID LBRACE CTE_I RBRACE SEMICOLON\n  \n  \tfunction : FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY localvar bloq return expres RKEY\n    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar RKEY\n    | FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY localvar bloq RKEY\n    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar bloq return expres RKEY\n    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar bloq RKEY\n    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY RKEY\n\n  \n  \tfunctype : INT\n    | FLOAT\n    | STRING\n    | BOOL\n    | VOID\n  \n    addInTable :\n    \n    funci : tipo ID\n    | tipo ID COMA funci\n    | empty\n  \n     localvar : var\n     | vector\n     | var localvar\n     | vector localvar\n     \n    return : RETURN expres\n    | empty\n    \n    mainc : LKEY RKEY\n    | LKEY bloq RKEY\n    | LKEY mainc2 bloq RKEY\n    | LKEY mainc2 RKEY\n    \n    mainc2 : var\n    | var mainc2\n    | vector\n    | vector mainc2\n    \n  \t bloq : bloqi\n    \n  \tbloqi : estat\n        | estat bloqi\n  \n  \testat : asign\n        | cond\n        | escrit\n        | ciclo\n        | leer\n  \n    asign : ID pushid EQUAL pushop expres resolverasignacion SEMICOLON\n        | ID pushid LBRACE exr RBRACE EQUAL pushop expres SEMICOLON\n  \n    cond : IF LPAREN expres RPAREN LKEY bloq RKEY\n        | IF LPAREN expres RPAREN LKEY bloq RKEY ELSE LKEY bloq RKEY\n  \n    escrit : PRINT LPAREN escriti RPAREN SEMICOLON\n  \n  \tescriti : expres\n    \t| expres COMA escriti\n  \n    ciclo : WHILE LPAREN expres RPAREN LKEY bloq RKEY\n  \n  \tleer : READ LPAREN ID RPAREN SEMICOLON\n  \n  expres : exr\n        | exr log expres\n  \n  \texr : ex\n    \t| ex reslog rel exr\n  \n  \tex : term resterm\n    \t| term resterm PLUS pushop ex\n    \t| term resterm MINUS pushop ex\n  \n  \tterm : fact resfact\n    \t| fact resfact TIMES pushop term\n        | fact resfact DIVIDE pushop term\n  \n  \tfact : LPAREN pushop expres RPAREN popop\n        | var_cte\n        | PLUS var_cte\n        | MINUS var_cte\n  \n  \trel : LOWERTHAN pushop\n    \t| MORETHAN pushop\n        | LOWEREQ pushop\n        | MOREEQ pushop\n        | SAME pushop\n        | DIFFERENT pushop\n  \n  \tlog : OR\n        | AND\n  \n  \tvar_cte : ID pushid\n        | CTE_I pushcte\n        | CTE_F pushcte\n        | CTE_B pushcte\n        | CTE_S pushcte\n        | fcall\n        | vcall\n  \n  \tfcall : ID LPAREN fcall1 RPAREN\n        | ID LPAREN RPAREN\n  \n  \tfcall1 : expres\n        | expres COMA fcall1\n  \n  \tvcall : ID LBRACE expres RBRACE\n  \n    empty :\n    pushcte :pushid :pushop :popop :resolverasignacion :resfact :resterm :reslog :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,21,29,30,58,60,70,73,96,97,123,],[0,-13,-3,-41,-42,-44,-13,-43,-13,-2,-1,]),'COLON':([2,],[3,]),'MAIN':([3,6,7,8,9,13,14,23,25,49,56,99,187,194,203,208,213,214,],[5,-11,-5,-8,-9,24,-4,47,-7,-6,-14,-19,-25,-21,-24,-22,-23,-20,]),'VAR':([3,4,7,8,9,22,34,35,56,99,173,185,188,189,],[-10,10,10,-8,-9,10,10,10,-14,-19,10,10,10,10,]),'VECTOR':([3,4,7,8,9,22,34,35,56,99,173,185,188,189,],[-10,11,11,-8,-9,11,11,11,-14,-19,11,11,11,11,]),'LKEY':([5,12,24,47,48,69,103,121,150,172,192,],[-12,22,-12,-12,22,22,128,147,173,185,200,]),'FUNCTION':([6,7,8,9,13,14,25,56,99,187,194,203,208,213,214,],[-11,-5,-8,-9,26,-4,26,-14,-19,-25,-21,-24,-22,-23,-20,]),'INT':([10,26,124,190,],[16,51,16,16,]),'FLOAT':([10,26,124,190,],[17,52,17,17,]),'STRING':([10,26,124,190,],[18,53,18,18,]),'BOOL':([10,26,124,190,],[19,54,19,19,]),'ID':([11,15,16,17,18,19,22,32,33,34,35,36,38,39,40,41,42,50,51,52,53,54,55,56,61,62,63,65,66,67,68,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,99,100,102,104,105,106,108,109,110,111,112,113,114,115,116,117,118,120,128,129,130,131,132,133,134,135,136,137,138,139,140,142,145,147,148,151,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,170,175,176,177,178,179,180,181,182,184,186,188,189,193,195,196,197,199,200,201,202,204,205,207,210,211,],[20,27,-15,-16,-17,-18,37,37,-49,-45,-47,37,-52,-53,-54,-55,-56,71,-26,-27,-28,-29,-30,-14,-46,-48,-51,85,85,85,95,-103,85,-103,-66,-68,-107,85,85,-106,-77,-102,-101,-101,-101,-101,-93,-94,-19,85,85,85,-86,-87,-70,-78,-79,-73,-88,85,85,-89,-90,-91,-92,85,37,-67,85,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-96,-61,37,-65,174,-103,-104,-69,-80,-81,-82,-83,-84,-85,85,85,85,85,-95,85,-99,-57,85,-76,-59,-71,-72,-74,-75,-64,37,-35,-36,37,-100,-37,-38,-58,37,-100,85,85,-40,85,-39,-60,]),'LBRACE':([20,37,64,85,],[28,-102,75,114,]),'RKEY':([22,31,32,33,34,35,36,38,39,40,41,42,56,59,61,62,63,78,79,80,83,84,85,86,87,88,89,90,91,99,108,109,110,111,112,115,116,117,118,129,142,145,148,155,156,157,168,170,171,173,175,177,178,179,180,181,182,184,186,188,189,195,196,197,199,201,206,209,211,212,],[30,58,60,-49,-45,-47,-50,-52,-53,-54,-55,-56,-14,73,-46,-48,-51,-66,-68,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,-19,-70,-78,-79,-73,-88,-89,-90,-91,-92,-67,-96,-61,-65,-104,178,-69,-95,-99,184,187,-57,-76,-59,-71,-72,-74,-75,-64,194,-35,-36,203,-37,-38,-58,208,211,213,-60,214,]),'IF':([22,32,34,35,36,38,39,40,41,42,56,61,62,99,128,145,147,148,175,178,184,186,188,189,193,196,197,199,200,211,],[43,43,-45,-47,43,-52,-53,-54,-55,-56,-14,-46,-48,-19,43,-61,43,-65,-57,-59,-64,43,-35,-36,43,-37,-38,-58,43,-60,]),'PRINT':([22,32,34,35,36,38,39,40,41,42,56,61,62,99,128,145,147,148,175,178,184,186,188,189,193,196,197,199,200,211,],[44,44,-45,-47,44,-52,-53,-54,-55,-56,-14,-46,-48,-19,44,-61,44,-65,-57,-59,-64,44,-35,-36,44,-37,-38,-58,44,-60,]),'WHILE':([22,32,34,35,36,38,39,40,41,42,56,61,62,99,128,145,147,148,175,178,184,186,188,189,193,196,197,199,200,211,],[45,45,-45,-47,45,-52,-53,-54,-55,-56,-14,-46,-48,-19,45,-61,45,-65,-57,-59,-64,45,-35,-36,45,-37,-38,-58,45,-60,]),'READ':([22,32,34,35,36,38,39,40,41,42,56,61,62,99,128,145,147,148,175,178,184,186,188,189,193,196,197,199,200,211,],[46,46,-45,-47,46,-52,-53,-54,-55,-56,-14,-46,-48,-19,46,-61,46,-65,-57,-59,-64,46,-35,-36,46,-37,-38,-58,46,-60,]),'VOID':([26,],[55,]),'SEMICOLON':([27,72,78,79,80,83,84,85,86,87,88,89,90,91,108,109,110,111,112,115,116,117,118,119,122,125,129,142,153,155,157,168,170,177,179,180,181,182,191,],[56,99,-66,-68,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,-70,-78,-79,-73,-88,-89,-90,-91,-92,145,148,-105,-67,-96,175,-104,-69,-95,-99,-76,-71,-72,-74,-75,199,]),'CTE_I':([28,33,36,38,39,40,41,42,63,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,100,102,104,105,106,108,109,110,111,112,113,114,115,116,117,118,120,129,130,131,132,133,134,135,136,137,138,139,140,142,145,148,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,170,175,176,177,178,179,180,181,182,184,195,199,201,202,204,205,207,210,211,],[57,-49,-50,-52,-53,-54,-55,-56,-51,86,86,86,-103,86,-103,-66,-68,-107,86,86,-106,-77,-102,-101,-101,-101,-101,-93,-94,86,86,86,-86,-87,-70,-78,-79,-73,-88,86,86,-89,-90,-91,-92,86,-67,86,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-96,-61,-65,-103,-104,-69,-80,-81,-82,-83,-84,-85,86,86,86,86,-95,86,-99,-57,86,-76,-59,-71,-72,-74,-75,-64,-100,-58,-100,86,86,-40,86,-39,-60,]),'RETURN':([33,36,38,39,40,41,42,63,145,148,175,178,184,195,199,201,211,],[-49,-50,-52,-53,-54,-55,-56,-51,-61,-65,-57,-59,-64,204,-58,204,-60,]),'LPAREN':([33,36,38,39,40,41,42,43,44,45,46,63,65,66,67,71,74,75,76,78,79,80,83,84,85,86,87,88,89,90,91,98,100,102,104,105,106,108,109,110,111,112,113,114,115,116,117,118,120,129,130,131,132,133,134,135,136,137,138,139,140,142,145,148,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,170,175,176,177,178,179,180,181,182,184,195,199,201,202,204,205,207,210,211,],[-49,-50,-52,-53,-54,-55,-56,65,66,67,68,-51,76,76,76,-31,-103,76,-103,-66,-68,-107,-106,-77,113,-101,-101,-101,-101,-93,-94,124,76,76,76,-86,-87,-70,-78,-79,-73,-88,76,76,-89,-90,-91,-92,76,-67,76,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-96,-61,-65,-103,-104,-69,-80,-81,-82,-83,-84,-85,76,76,76,76,-95,76,-99,-57,76,-76,-59,-71,-72,-74,-75,-64,-100,-58,-100,76,76,-40,76,-39,-60,]),'PLUS':([33,36,38,39,40,41,42,63,65,66,67,74,75,76,78,79,80,83,84,85,86,87,88,89,90,91,100,102,104,105,106,108,109,110,111,112,113,114,115,116,117,118,120,129,130,131,132,133,134,135,136,137,138,139,140,142,145,148,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,170,175,176,177,178,179,180,181,182,184,195,199,201,202,204,205,207,210,211,],[-49,-50,-52,-53,-54,-55,-56,-51,81,81,81,-103,81,-103,-66,-68,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,81,81,81,-86,-87,137,-78,-79,-73,-88,81,81,-89,-90,-91,-92,81,-67,81,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-96,-61,-65,-103,-104,-69,-80,-81,-82,-83,-84,-85,81,81,81,81,-95,81,-99,-57,81,-76,-59,-71,-72,-74,-75,-64,-100,-58,-100,81,81,-40,81,-39,-60,]),'MINUS':([33,36,38,39,40,41,42,63,65,66,67,74,75,76,78,79,80,83,84,85,86,87,88,89,90,91,100,102,104,105,106,108,109,110,111,112,113,114,115,116,117,118,120,129,130,131,132,133,134,135,136,137,138,139,140,142,145,148,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,170,175,176,177,178,179,180,181,182,184,195,199,201,202,204,205,207,210,211,],[-49,-50,-52,-53,-54,-55,-56,-51,82,82,82,-103,82,-103,-66,-68,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,82,82,82,-86,-87,138,-78,-79,-73,-88,82,82,-89,-90,-91,-92,82,-67,82,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-96,-61,-65,-103,-104,-69,-80,-81,-82,-83,-84,-85,82,82,82,82,-95,82,-99,-57,82,-76,-59,-71,-72,-74,-75,-64,-100,-58,-100,82,82,-40,82,-39,-60,]),'CTE_F':([33,36,38,39,40,41,42,63,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,100,102,104,105,106,108,109,110,111,112,113,114,115,116,117,118,120,129,130,131,132,133,134,135,136,137,138,139,140,142,145,148,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,170,175,176,177,178,179,180,181,182,184,195,199,201,202,204,205,207,210,211,],[-49,-50,-52,-53,-54,-55,-56,-51,87,87,87,-103,87,-103,-66,-68,-107,87,87,-106,-77,-102,-101,-101,-101,-101,-93,-94,87,87,87,-86,-87,-70,-78,-79,-73,-88,87,87,-89,-90,-91,-92,87,-67,87,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-96,-61,-65,-103,-104,-69,-80,-81,-82,-83,-84,-85,87,87,87,87,-95,87,-99,-57,87,-76,-59,-71,-72,-74,-75,-64,-100,-58,-100,87,87,-40,87,-39,-60,]),'CTE_B':([33,36,38,39,40,41,42,63,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,100,102,104,105,106,108,109,110,111,112,113,114,115,116,117,118,120,129,130,131,132,133,134,135,136,137,138,139,140,142,145,148,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,170,175,176,177,178,179,180,181,182,184,195,199,201,202,204,205,207,210,211,],[-49,-50,-52,-53,-54,-55,-56,-51,88,88,88,-103,88,-103,-66,-68,-107,88,88,-106,-77,-102,-101,-101,-101,-101,-93,-94,88,88,88,-86,-87,-70,-78,-79,-73,-88,88,88,-89,-90,-91,-92,88,-67,88,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-96,-61,-65,-103,-104,-69,-80,-81,-82,-83,-84,-85,88,88,88,88,-95,88,-99,-57,88,-76,-59,-71,-72,-74,-75,-64,-100,-58,-100,88,88,-40,88,-39,-60,]),'CTE_S':([33,36,38,39,40,41,42,63,65,66,67,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,100,102,104,105,106,108,109,110,111,112,113,114,115,116,117,118,120,129,130,131,132,133,134,135,136,137,138,139,140,142,145,148,154,155,157,158,159,160,161,162,163,164,165,166,167,168,169,170,175,176,177,178,179,180,181,182,184,195,199,201,202,204,205,207,210,211,],[-49,-50,-52,-53,-54,-55,-56,-51,89,89,89,-103,89,-103,-66,-68,-107,89,89,-106,-77,-102,-101,-101,-101,-101,-93,-94,89,89,89,-86,-87,-70,-78,-79,-73,-88,89,89,-89,-90,-91,-92,89,-67,89,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-96,-61,-65,-103,-104,-69,-80,-81,-82,-83,-84,-85,89,89,89,89,-95,89,-99,-57,89,-76,-59,-71,-72,-74,-75,-64,-100,-58,-100,89,89,-40,89,-39,-60,]),'EQUAL':([37,64,126,],[-102,74,154,]),'RBRACE':([57,78,79,80,83,84,85,86,87,88,89,90,91,101,108,109,110,111,112,115,116,117,118,129,142,144,155,157,168,170,177,179,180,181,182,],[72,-66,-68,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,126,-70,-78,-79,-73,-88,-89,-90,-91,-92,-67,-96,170,-104,-69,-95,-99,-76,-71,-72,-74,-75,]),'RPAREN':([77,78,79,80,83,84,85,86,87,88,89,90,91,92,93,94,95,108,109,110,111,112,113,115,116,117,118,124,127,129,141,142,143,146,149,152,155,157,168,170,174,177,179,180,181,182,183,190,198,],[103,-66,-68,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,119,-62,121,122,-70,-78,-79,-73,-88,142,-89,-90,-91,-92,150,155,-67,168,-96,-97,-63,172,-34,-104,-69,-95,-99,-32,-76,-71,-72,-74,-75,-98,-100,-33,]),'COMA':([78,79,80,83,84,85,86,87,88,89,90,91,93,108,109,110,111,112,115,116,117,118,129,142,143,155,157,168,170,174,177,179,180,181,182,],[-66,-68,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,120,-70,-78,-79,-73,-88,-89,-90,-91,-92,-67,-96,169,-104,-69,-95,-99,190,-76,-71,-72,-74,-75,]),'OR':([78,79,80,83,84,85,86,87,88,89,90,91,108,109,110,111,112,115,116,117,118,142,155,157,168,170,177,179,180,181,182,],[105,-68,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,-70,-78,-79,-73,-88,-89,-90,-91,-92,-96,-104,-69,-95,-99,-76,-71,-72,-74,-75,]),'AND':([78,79,80,83,84,85,86,87,88,89,90,91,108,109,110,111,112,115,116,117,118,142,155,157,168,170,177,179,180,181,182,],[106,-68,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,-70,-78,-79,-73,-88,-89,-90,-91,-92,-96,-104,-69,-95,-99,-76,-71,-72,-74,-75,]),'LOWERTHAN':([79,80,83,84,85,86,87,88,89,90,91,107,108,109,110,111,112,115,116,117,118,142,155,168,170,177,179,180,181,182,],[-108,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,131,-70,-78,-79,-73,-88,-89,-90,-91,-92,-96,-104,-95,-99,-76,-71,-72,-74,-75,]),'MORETHAN':([79,80,83,84,85,86,87,88,89,90,91,107,108,109,110,111,112,115,116,117,118,142,155,168,170,177,179,180,181,182,],[-108,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,132,-70,-78,-79,-73,-88,-89,-90,-91,-92,-96,-104,-95,-99,-76,-71,-72,-74,-75,]),'LOWEREQ':([79,80,83,84,85,86,87,88,89,90,91,107,108,109,110,111,112,115,116,117,118,142,155,168,170,177,179,180,181,182,],[-108,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,133,-70,-78,-79,-73,-88,-89,-90,-91,-92,-96,-104,-95,-99,-76,-71,-72,-74,-75,]),'MOREEQ':([79,80,83,84,85,86,87,88,89,90,91,107,108,109,110,111,112,115,116,117,118,142,155,168,170,177,179,180,181,182,],[-108,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,134,-70,-78,-79,-73,-88,-89,-90,-91,-92,-96,-104,-95,-99,-76,-71,-72,-74,-75,]),'SAME':([79,80,83,84,85,86,87,88,89,90,91,107,108,109,110,111,112,115,116,117,118,142,155,168,170,177,179,180,181,182,],[-108,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,135,-70,-78,-79,-73,-88,-89,-90,-91,-92,-96,-104,-95,-99,-76,-71,-72,-74,-75,]),'DIFFERENT':([79,80,83,84,85,86,87,88,89,90,91,107,108,109,110,111,112,115,116,117,118,142,155,168,170,177,179,180,181,182,],[-108,-107,-106,-77,-102,-101,-101,-101,-101,-93,-94,136,-70,-78,-79,-73,-88,-89,-90,-91,-92,-96,-104,-95,-99,-76,-71,-72,-74,-75,]),'TIMES':([83,84,85,86,87,88,89,90,91,109,110,111,112,115,116,117,118,142,155,168,170,177,],[-106,-77,-102,-101,-101,-101,-101,-93,-94,-78,-79,139,-88,-89,-90,-91,-92,-96,-104,-95,-99,-76,]),'DIVIDE':([83,84,85,86,87,88,89,90,91,109,110,111,112,115,116,117,118,142,155,168,170,177,],[-106,-77,-102,-101,-101,-101,-101,-93,-94,-78,-79,140,-88,-89,-90,-91,-92,-96,-104,-95,-99,-76,]),'ELSE':([178,],[192,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'global':([3,],[4,]),'program2':([4,7,],[6,14,]),'crear':([4,7,],[7,7,]),'var':([4,7,22,34,35,173,185,188,189,],[8,8,34,34,34,188,188,188,188,]),'vector':([4,7,22,34,35,173,185,188,189,],[9,9,35,35,35,189,189,189,189,]),'main1':([5,24,47,],[12,48,69,]),'finglobal':([6,],[13,]),'tipo':([10,124,190,],[15,151,151,]),'mainc':([12,48,69,],[21,70,96,]),'program3':([13,25,],[23,49,]),'function':([13,25,],[25,25,]),'finmain':([21,70,96,],[29,97,123,]),'bloq':([22,32,128,147,186,193,200,],[31,59,156,171,195,201,206,]),'mainc2':([22,34,35,],[32,61,62,]),'bloqi':([22,32,36,128,147,186,193,200,],[33,33,63,33,33,33,33,33,]),'estat':([22,32,36,128,147,186,193,200,],[36,36,36,36,36,36,36,36,]),'asign':([22,32,36,128,147,186,193,200,],[38,38,38,38,38,38,38,38,]),'cond':([22,32,36,128,147,186,193,200,],[39,39,39,39,39,39,39,39,]),'escrit':([22,32,36,128,147,186,193,200,],[40,40,40,40,40,40,40,40,]),'ciclo':([22,32,36,128,147,186,193,200,],[41,41,41,41,41,41,41,41,]),'leer':([22,32,36,128,147,186,193,200,],[42,42,42,42,42,42,42,42,]),'functype':([26,],[50,]),'pushid':([37,85,],[64,112,]),'expres':([65,66,67,100,102,104,113,114,120,169,176,202,204,207,],[77,93,94,125,127,129,143,144,93,143,191,209,210,212,]),'exr':([65,66,67,75,100,102,104,113,114,120,130,169,176,202,204,207,],[78,78,78,101,78,78,78,78,78,78,157,78,78,78,78,78,]),'ex':([65,66,67,75,100,102,104,113,114,120,130,164,165,169,176,202,204,207,],[79,79,79,79,79,79,79,79,79,79,79,179,180,79,79,79,79,79,]),'term':([65,66,67,75,100,102,104,113,114,120,130,164,165,166,167,169,176,202,204,207,],[80,80,80,80,80,80,80,80,80,80,80,80,80,181,182,80,80,80,80,80,]),'fact':([65,66,67,75,100,102,104,113,114,120,130,164,165,166,167,169,176,202,204,207,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'var_cte':([65,66,67,75,81,82,100,102,104,113,114,120,130,164,165,166,167,169,176,202,204,207,],[84,84,84,84,109,110,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,]),'fcall':([65,66,67,75,81,82,100,102,104,113,114,120,130,164,165,166,167,169,176,202,204,207,],[90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,]),'vcall':([65,66,67,75,81,82,100,102,104,113,114,120,130,164,165,166,167,169,176,202,204,207,],[91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,]),'escriti':([66,120,],[92,146,]),'addInTable':([71,],[98,]),'pushop':([74,76,131,132,133,134,135,136,137,138,139,140,154,],[100,102,158,159,160,161,162,163,164,165,166,167,176,]),'log':([78,],[104,]),'reslog':([79,],[107,]),'resterm':([80,],[108,]),'resfact':([83,],[111,]),'pushcte':([86,87,88,89,],[115,116,117,118,]),'rel':([107,],[130,]),'fcall1':([113,169,],[141,183,]),'funci':([124,190,],[149,198,]),'empty':([124,190,195,201,],[152,152,205,205,]),'resolverasignacion':([125,],[153,]),'popop':([155,],[177,]),'localvar':([173,185,188,189,],[186,193,196,197,]),'return':([195,201,],[202,207,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM COLON global program2 finglobal program3 MAIN main1 mainc finmain','program',10,'p_program','lexPar.py',147),
  ('program -> PROGRAM COLON global program2 finglobal MAIN main1 mainc finmain','program',9,'p_program','lexPar.py',148),
  ('program -> PROGRAM COLON MAIN main1 mainc finmain','program',6,'p_program','lexPar.py',149),
  ('program2 -> crear program2','program2',2,'p_program2','lexPar.py',154),
  ('program2 -> crear','program2',1,'p_program2','lexPar.py',155),
  ('program3 -> function program3','program3',2,'p_program3','lexPar.py',160),
  ('program3 -> function','program3',1,'p_program3','lexPar.py',161),
  ('crear -> var','crear',1,'p_crear','lexPar.py',166),
  ('crear -> vector','crear',1,'p_crear','lexPar.py',167),
  ('global -> <empty>','global',0,'p_global','lexPar.py',171),
  ('finglobal -> <empty>','finglobal',0,'p_finglobal','lexPar.py',177),
  ('main1 -> <empty>','main1',0,'p_main1','lexPar.py',181),
  ('finmain -> <empty>','finmain',0,'p_finmain','lexPar.py',187),
  ('var -> VAR tipo ID SEMICOLON','var',4,'p_var','lexPar.py',192),
  ('tipo -> INT','tipo',1,'p_tipo','lexPar.py',205),
  ('tipo -> FLOAT','tipo',1,'p_tipo','lexPar.py',206),
  ('tipo -> STRING','tipo',1,'p_tipo','lexPar.py',207),
  ('tipo -> BOOL','tipo',1,'p_tipo','lexPar.py',208),
  ('vector -> VECTOR ID LBRACE CTE_I RBRACE SEMICOLON','vector',6,'p_vector','lexPar.py',214),
  ('function -> FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY localvar bloq return expres RKEY','function',13,'p_function','lexPar.py',221),
  ('function -> FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar RKEY','function',9,'p_function','lexPar.py',222),
  ('function -> FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY localvar bloq RKEY','function',11,'p_function','lexPar.py',223),
  ('function -> FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar bloq return expres RKEY','function',12,'p_function','lexPar.py',224),
  ('function -> FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar bloq RKEY','function',10,'p_function','lexPar.py',225),
  ('function -> FUNCTION functype ID addInTable LPAREN RPAREN LKEY RKEY','function',8,'p_function','lexPar.py',226),
  ('functype -> INT','functype',1,'p_functype','lexPar.py',234),
  ('functype -> FLOAT','functype',1,'p_functype','lexPar.py',235),
  ('functype -> STRING','functype',1,'p_functype','lexPar.py',236),
  ('functype -> BOOL','functype',1,'p_functype','lexPar.py',237),
  ('functype -> VOID','functype',1,'p_functype','lexPar.py',238),
  ('addInTable -> <empty>','addInTable',0,'p_addInTable','lexPar.py',244),
  ('funci -> tipo ID','funci',2,'p_funci','lexPar.py',253),
  ('funci -> tipo ID COMA funci','funci',4,'p_funci','lexPar.py',254),
  ('funci -> empty','funci',1,'p_funci','lexPar.py',255),
  ('localvar -> var','localvar',1,'p_localvar','lexPar.py',260),
  ('localvar -> vector','localvar',1,'p_localvar','lexPar.py',261),
  ('localvar -> var localvar','localvar',2,'p_localvar','lexPar.py',262),
  ('localvar -> vector localvar','localvar',2,'p_localvar','lexPar.py',263),
  ('return -> RETURN expres','return',2,'p_return','lexPar.py',268),
  ('return -> empty','return',1,'p_return','lexPar.py',269),
  ('mainc -> LKEY RKEY','mainc',2,'p_mainc','lexPar.py',274),
  ('mainc -> LKEY bloq RKEY','mainc',3,'p_mainc','lexPar.py',275),
  ('mainc -> LKEY mainc2 bloq RKEY','mainc',4,'p_mainc','lexPar.py',276),
  ('mainc -> LKEY mainc2 RKEY','mainc',3,'p_mainc','lexPar.py',277),
  ('mainc2 -> var','mainc2',1,'p_mainc2','lexPar.py',282),
  ('mainc2 -> var mainc2','mainc2',2,'p_mainc2','lexPar.py',283),
  ('mainc2 -> vector','mainc2',1,'p_mainc2','lexPar.py',284),
  ('mainc2 -> vector mainc2','mainc2',2,'p_mainc2','lexPar.py',285),
  ('bloq -> bloqi','bloq',1,'p_bloq','lexPar.py',290),
  ('bloqi -> estat','bloqi',1,'p_bloqi','lexPar.py',295),
  ('bloqi -> estat bloqi','bloqi',2,'p_bloqi','lexPar.py',296),
  ('estat -> asign','estat',1,'p_estat','lexPar.py',301),
  ('estat -> cond','estat',1,'p_estat','lexPar.py',302),
  ('estat -> escrit','estat',1,'p_estat','lexPar.py',303),
  ('estat -> ciclo','estat',1,'p_estat','lexPar.py',304),
  ('estat -> leer','estat',1,'p_estat','lexPar.py',305),
  ('asign -> ID pushid EQUAL pushop expres resolverasignacion SEMICOLON','asign',7,'p_asign','lexPar.py',310),
  ('asign -> ID pushid LBRACE exr RBRACE EQUAL pushop expres SEMICOLON','asign',9,'p_asign','lexPar.py',311),
  ('cond -> IF LPAREN expres RPAREN LKEY bloq RKEY','cond',7,'p_cond','lexPar.py',316),
  ('cond -> IF LPAREN expres RPAREN LKEY bloq RKEY ELSE LKEY bloq RKEY','cond',11,'p_cond','lexPar.py',317),
  ('escrit -> PRINT LPAREN escriti RPAREN SEMICOLON','escrit',5,'p_escrit','lexPar.py',322),
  ('escriti -> expres','escriti',1,'p_escriti','lexPar.py',327),
  ('escriti -> expres COMA escriti','escriti',3,'p_escriti','lexPar.py',328),
  ('ciclo -> WHILE LPAREN expres RPAREN LKEY bloq RKEY','ciclo',7,'p_ciclo','lexPar.py',333),
  ('leer -> READ LPAREN ID RPAREN SEMICOLON','leer',5,'p_leer','lexPar.py',338),
  ('expres -> exr','expres',1,'p_expres','lexPar.py',343),
  ('expres -> exr log expres','expres',3,'p_expres','lexPar.py',344),
  ('exr -> ex','exr',1,'p_exr','lexPar.py',349),
  ('exr -> ex reslog rel exr','exr',4,'p_exr','lexPar.py',350),
  ('ex -> term resterm','ex',2,'p_ex','lexPar.py',355),
  ('ex -> term resterm PLUS pushop ex','ex',5,'p_ex','lexPar.py',356),
  ('ex -> term resterm MINUS pushop ex','ex',5,'p_ex','lexPar.py',357),
  ('term -> fact resfact','term',2,'p_term','lexPar.py',362),
  ('term -> fact resfact TIMES pushop term','term',5,'p_term','lexPar.py',363),
  ('term -> fact resfact DIVIDE pushop term','term',5,'p_term','lexPar.py',364),
  ('fact -> LPAREN pushop expres RPAREN popop','fact',5,'p_fact','lexPar.py',369),
  ('fact -> var_cte','fact',1,'p_fact','lexPar.py',370),
  ('fact -> PLUS var_cte','fact',2,'p_fact','lexPar.py',371),
  ('fact -> MINUS var_cte','fact',2,'p_fact','lexPar.py',372),
  ('rel -> LOWERTHAN pushop','rel',2,'p_rel','lexPar.py',377),
  ('rel -> MORETHAN pushop','rel',2,'p_rel','lexPar.py',378),
  ('rel -> LOWEREQ pushop','rel',2,'p_rel','lexPar.py',379),
  ('rel -> MOREEQ pushop','rel',2,'p_rel','lexPar.py',380),
  ('rel -> SAME pushop','rel',2,'p_rel','lexPar.py',381),
  ('rel -> DIFFERENT pushop','rel',2,'p_rel','lexPar.py',382),
  ('log -> OR','log',1,'p_log','lexPar.py',387),
  ('log -> AND','log',1,'p_log','lexPar.py',388),
  ('var_cte -> ID pushid','var_cte',2,'p_var_cte','lexPar.py',393),
  ('var_cte -> CTE_I pushcte','var_cte',2,'p_var_cte','lexPar.py',394),
  ('var_cte -> CTE_F pushcte','var_cte',2,'p_var_cte','lexPar.py',395),
  ('var_cte -> CTE_B pushcte','var_cte',2,'p_var_cte','lexPar.py',396),
  ('var_cte -> CTE_S pushcte','var_cte',2,'p_var_cte','lexPar.py',397),
  ('var_cte -> fcall','var_cte',1,'p_var_cte','lexPar.py',398),
  ('var_cte -> vcall','var_cte',1,'p_var_cte','lexPar.py',399),
  ('fcall -> ID LPAREN fcall1 RPAREN','fcall',4,'p_fcall','lexPar.py',404),
  ('fcall -> ID LPAREN RPAREN','fcall',3,'p_fcall','lexPar.py',405),
  ('fcall1 -> expres','fcall1',1,'p_fcall1','lexPar.py',410),
  ('fcall1 -> expres COMA fcall1','fcall1',3,'p_fcall1','lexPar.py',411),
  ('vcall -> ID LBRACE expres RBRACE','vcall',4,'p_vcall','lexPar.py',416),
  ('empty -> <empty>','empty',0,'p_empty','lexPar.py',421),
  ('pushcte -> <empty>','pushcte',0,'p_pushcte','lexPar.py',432),
  ('pushid -> <empty>','pushid',0,'p_pushid','lexPar.py',436),
  ('pushop -> <empty>','pushop',0,'p_pushop','lexPar.py',440),
  ('popop -> <empty>','popop',0,'p_popop','lexPar.py',444),
  ('resolverasignacion -> <empty>','resolverasignacion',0,'p_resolverasignacion','lexPar.py',448),
  ('resfact -> <empty>','resfact',0,'p_resfact','lexPar.py',453),
  ('resterm -> <empty>','resterm',0,'p_resterm','lexPar.py',457),
  ('reslog -> <empty>','reslog',0,'p_reslog','lexPar.py',461),
]
