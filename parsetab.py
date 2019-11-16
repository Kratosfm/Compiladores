
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL COLON COMA CTE_F CTE_I CTE_S DIFFERENT DIVIDE ELSE EQUAL FALSE FLOAT FUNCTION ID IF INT LBRACE LKEY LOWEREQ LOWERTHAN LPAREN MAIN MINUS MOREEQ MORETHAN OR PLUS PRINT PROGRAM RBRACE READ RETURN RKEY RPAREN SAME SEMICOLON STRING TIMES TRUE VAR VECTOR VOID WHILE\n  \tprogram : PROGRAM COLON global program2 finglobal program3 MAIN main1 mainc finmain\n        | PROGRAM COLON global program2 finglobal MAIN main1 mainc finmain\n        | PROGRAM COLON MAIN main1 mainc finmain\n  \n  \tprogram2 : crear program2\n    \t| crear\n  \n  \tprogram3 : function program3\n    \t| function\n  \n  \tcrear : var\n    \t| vector\n  global :finglobal :main1 :finmain :\n  \tvar : VAR tipo ID SEMICOLON\n  \n  \ttipo : INT\n    \t| FLOAT\n        | STRING\n        | BOOL\n  \n  \tvector : VECTOR ID LBRACE CTE_I RBRACE SEMICOLON\n  \n  \tfunction : FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY localvar bloq return expres RKEY\n    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar RKEY\n    | FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY localvar bloq RKEY\n    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar bloq return expres RKEY\n    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar bloq RKEY\n    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY RKEY\n\n  \n  \tfunctype : INT\n    | FLOAT\n    | STRING\n    | BOOL\n    | VOID\n  \n    addInTable :\n    \n    funci : tipo ID\n    | tipo ID COMA funci\n    | empty\n  \n     localvar : var\n     | vector\n     | var localvar\n     | vector localvar\n     \n    return : RETURN expres\n    | empty\n    \n    mainc : LKEY RKEY\n    | LKEY bloq RKEY\n    | LKEY mainc2 bloq RKEY\n    | LKEY mainc2 RKEY\n    \n    mainc2 : var\n    | var mainc2\n    | vector\n    | vector mainc2\n    \n  \t bloq : estat\n         | estat bloq\n    \n  \testat : asign\n        | cond\n        | escrit\n        | ciclo\n        | leer\n  \n    asign : ID pushid EQUAL pushop expres resolverasignacion SEMICOLON\n        | ID pushid LBRACE exr RBRACE EQUAL pushop expres SEMICOLON\n  \n    cond : IF LPAREN expres RPAREN LKEY resif finif RKEY\n        | IF LPAREN expres RPAREN LKEY resif bloq finif RKEY\n        | IF LPAREN expres RPAREN LKEY resif bloq finif RKEY ELSE LKEY bloq RKEY\n  \n    escrit : PRINT LPAREN escriti RPAREN SEMICOLON\n  \n  \tescriti : expres\n    \t| expres COMA escriti\n  \n    ciclo : WHILE LPAREN expres RPAREN LKEY bloq RKEY\n  \n  \tleer : READ LPAREN ID RPAREN SEMICOLON\n  \n  expres : exr\n        | exr log expres\n  \n  \texr : ex\n    \t| ex rel exr resrel\n  \n  \tex : term resterm\n    \t| term resterm PLUS pushop ex\n    \t| term resterm MINUS pushop ex\n  \n  \tterm : fact resfact\n    \t| fact resfact TIMES pushop term\n        | fact resfact DIVIDE pushop term\n  \n  \tfact : LPAREN pushop expres RPAREN popop\n        | var_cte\n        | PLUS var_cte\n        | MINUS var_cte\n  \n  \trel : LOWERTHAN\n    \t| MORETHAN\n        | LOWEREQ\n        | MOREEQ\n        | SAME\n        | DIFFERENT\n  \n  \tlog : OR\n        | AND\n  \n  \tvar_cte : ID pushid\n        | CTE_I pushcte\n        | CTE_F pushcte\n        | CTE_S pushcte\n        | TRUE pushcte\n        | FALSE pushcte\n        | fcall\n        | vcall\n  \n  \tfcall : ID LPAREN fcall1 RPAREN\n        | ID LPAREN RPAREN\n  \n  \tfcall1 : expres\n        | expres COMA fcall1\n  \n  \tvcall : ID LBRACE expres RBRACE\n  \n    empty :\n    pushcte :pushid :pushop :popop :resolverasignacion :resfact :resterm :resrel :resif :finif :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,21,29,30,57,59,69,72,96,97,130,],[0,-13,-3,-41,-42,-44,-13,-43,-13,-2,-1,]),'COLON':([2,],[3,]),'MAIN':([3,6,7,8,9,13,14,23,25,48,55,99,183,191,200,205,210,212,],[5,-11,-5,-8,-9,24,-4,46,-7,-6,-14,-19,-25,-21,-24,-22,-23,-20,]),'VAR':([3,4,7,8,9,22,34,35,55,99,168,181,184,185,],[-10,10,10,-8,-9,10,10,10,-14,-19,10,10,10,10,]),'VECTOR':([3,4,7,8,9,22,34,35,55,99,168,181,184,185,],[-10,11,11,-8,-9,11,11,11,-14,-19,11,11,11,11,]),'LKEY':([5,12,24,46,47,68,103,128,151,167,203,],[-12,22,-12,-12,22,22,135,148,168,181,208,]),'FUNCTION':([6,7,8,9,13,14,25,55,99,183,191,200,205,210,212,],[-11,-5,-8,-9,26,-4,26,-14,-19,-25,-21,-24,-22,-23,-20,]),'INT':([10,26,131,186,],[16,50,16,16,]),'FLOAT':([10,26,131,186,],[17,51,17,17,]),'STRING':([10,26,131,186,],[18,52,18,18,]),'BOOL':([10,26,131,186,],[19,53,19,19,]),'ID':([11,15,16,17,18,19,22,32,33,34,35,36,37,38,39,40,49,50,51,52,53,54,55,60,61,62,64,65,66,67,73,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,99,100,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,127,135,136,137,138,139,140,141,143,146,148,149,152,155,156,157,158,159,160,161,162,163,164,165,170,171,172,175,176,177,178,180,182,184,185,188,190,192,193,194,196,197,198,199,201,202,204,207,208,213,],[20,27,-15,-16,-17,-18,41,41,41,-45,-47,-51,-52,-53,-54,-55,70,-26,-27,-28,-29,-30,-14,-50,-46,-48,84,84,84,95,-104,84,-104,-66,-68,-108,84,84,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,-19,84,84,84,-86,-87,84,-80,-81,-82,-83,-84,-85,-70,-78,-79,-73,-88,84,84,-89,-90,-91,-92,-93,84,-110,-67,-109,-104,-104,-104,-104,-97,-61,41,-65,169,-104,-105,41,-69,84,84,84,84,-96,84,-100,-56,84,-76,-71,-72,-74,-75,-64,41,-35,-36,-58,41,-101,-37,-38,-57,-59,-101,84,84,-40,84,-39,41,-60,]),'LBRACE':([20,41,63,84,],[28,-103,74,120,]),'RKEY':([22,31,32,33,34,35,36,37,38,39,40,55,58,60,61,62,77,78,79,82,83,84,85,86,87,88,89,90,91,99,114,115,116,117,118,121,122,123,124,125,135,136,137,143,146,149,156,157,158,163,165,166,168,170,172,173,174,175,176,177,178,180,182,184,185,188,189,192,193,194,196,197,198,206,209,211,213,],[30,57,59,-49,-45,-47,-51,-52,-53,-54,-55,-14,72,-50,-46,-48,-66,-68,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,-19,-70,-78,-79,-73,-88,-89,-90,-91,-92,-93,-110,-67,-109,-97,-61,-65,-105,-111,-69,-96,-100,180,183,-56,-76,188,-111,-71,-72,-74,-75,-64,191,-35,-36,-58,197,200,-37,-38,-57,-59,205,210,212,213,-60,]),'IF':([22,32,33,34,35,36,37,38,39,40,55,61,62,99,135,146,148,149,157,170,180,182,184,185,188,190,193,194,196,197,208,213,],[42,42,42,-45,-47,-51,-52,-53,-54,-55,-14,-46,-48,-19,-110,-61,42,-65,42,-56,-64,42,-35,-36,-58,42,-37,-38,-57,-59,42,-60,]),'PRINT':([22,32,33,34,35,36,37,38,39,40,55,61,62,99,135,146,148,149,157,170,180,182,184,185,188,190,193,194,196,197,208,213,],[43,43,43,-45,-47,-51,-52,-53,-54,-55,-14,-46,-48,-19,-110,-61,43,-65,43,-56,-64,43,-35,-36,-58,43,-37,-38,-57,-59,43,-60,]),'WHILE':([22,32,33,34,35,36,37,38,39,40,55,61,62,99,135,146,148,149,157,170,180,182,184,185,188,190,193,194,196,197,208,213,],[44,44,44,-45,-47,-51,-52,-53,-54,-55,-14,-46,-48,-19,-110,-61,44,-65,44,-56,-64,44,-35,-36,-58,44,-37,-38,-57,-59,44,-60,]),'READ':([22,32,33,34,35,36,37,38,39,40,55,61,62,99,135,146,148,149,157,170,180,182,184,185,188,190,193,194,196,197,208,213,],[45,45,45,-45,-47,-51,-52,-53,-54,-55,-14,-46,-48,-19,-110,-61,45,-65,45,-56,-64,45,-35,-36,-58,45,-37,-38,-57,-59,45,-60,]),'VOID':([26,],[54,]),'SEMICOLON':([27,71,77,78,79,82,83,84,85,86,87,88,89,90,91,114,115,116,117,118,121,122,123,124,125,126,129,132,136,137,143,154,156,158,163,165,172,175,176,177,178,187,],[55,99,-66,-68,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,-70,-78,-79,-73,-88,-89,-90,-91,-92,-93,146,149,-106,-67,-109,-97,170,-105,-69,-96,-100,-76,-71,-72,-74,-75,196,]),'CTE_I':([28,33,36,37,38,39,40,60,64,65,66,73,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,100,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,127,136,137,138,139,140,141,143,146,149,155,156,158,159,160,161,162,163,164,165,170,171,172,175,176,177,178,180,188,192,196,197,198,199,201,202,204,207,213,],[56,-49,-51,-52,-53,-54,-55,-50,85,85,85,-104,85,-104,-66,-68,-108,85,85,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,85,85,85,-86,-87,85,-80,-81,-82,-83,-84,-85,-70,-78,-79,-73,-88,85,85,-89,-90,-91,-92,-93,85,-67,-109,-104,-104,-104,-104,-97,-61,-65,-104,-105,-69,85,85,85,85,-96,85,-100,-56,85,-76,-71,-72,-74,-75,-64,-58,-101,-57,-59,-101,85,85,-40,85,-39,-60,]),'RETURN':([33,36,37,38,39,40,60,146,149,170,180,188,192,196,197,198,213,],[-49,-51,-52,-53,-54,-55,-50,-61,-65,-56,-64,-58,201,-57,-59,201,-60,]),'LPAREN':([33,36,37,38,39,40,42,43,44,45,60,64,65,66,70,73,74,75,77,78,79,82,83,84,85,86,87,88,89,90,91,98,100,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,127,136,137,138,139,140,141,143,146,149,155,156,158,159,160,161,162,163,164,165,170,171,172,175,176,177,178,180,188,192,196,197,198,199,201,202,204,207,213,],[-49,-51,-52,-53,-54,-55,64,65,66,67,-50,75,75,75,-31,-104,75,-104,-66,-68,-108,-107,-77,119,-102,-102,-102,-102,-102,-94,-95,131,75,75,75,-86,-87,75,-80,-81,-82,-83,-84,-85,-70,-78,-79,-73,-88,75,75,-89,-90,-91,-92,-93,75,-67,-109,-104,-104,-104,-104,-97,-61,-65,-104,-105,-69,75,75,75,75,-96,75,-100,-56,75,-76,-71,-72,-74,-75,-64,-58,-101,-57,-59,-101,75,75,-40,75,-39,-60,]),'PLUS':([33,36,37,38,39,40,60,64,65,66,73,74,75,77,78,79,82,83,84,85,86,87,88,89,90,91,100,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,127,136,137,138,139,140,141,143,146,149,155,156,158,159,160,161,162,163,164,165,170,171,172,175,176,177,178,180,188,192,196,197,198,199,201,202,204,207,213,],[-49,-51,-52,-53,-54,-55,-50,80,80,80,-104,80,-104,-66,-68,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,80,80,80,-86,-87,80,-80,-81,-82,-83,-84,-85,138,-78,-79,-73,-88,80,80,-89,-90,-91,-92,-93,80,-67,-109,-104,-104,-104,-104,-97,-61,-65,-104,-105,-69,80,80,80,80,-96,80,-100,-56,80,-76,-71,-72,-74,-75,-64,-58,-101,-57,-59,-101,80,80,-40,80,-39,-60,]),'MINUS':([33,36,37,38,39,40,60,64,65,66,73,74,75,77,78,79,82,83,84,85,86,87,88,89,90,91,100,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,127,136,137,138,139,140,141,143,146,149,155,156,158,159,160,161,162,163,164,165,170,171,172,175,176,177,178,180,188,192,196,197,198,199,201,202,204,207,213,],[-49,-51,-52,-53,-54,-55,-50,81,81,81,-104,81,-104,-66,-68,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,81,81,81,-86,-87,81,-80,-81,-82,-83,-84,-85,139,-78,-79,-73,-88,81,81,-89,-90,-91,-92,-93,81,-67,-109,-104,-104,-104,-104,-97,-61,-65,-104,-105,-69,81,81,81,81,-96,81,-100,-56,81,-76,-71,-72,-74,-75,-64,-58,-101,-57,-59,-101,81,81,-40,81,-39,-60,]),'CTE_F':([33,36,37,38,39,40,60,64,65,66,73,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,100,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,127,136,137,138,139,140,141,143,146,149,155,156,158,159,160,161,162,163,164,165,170,171,172,175,176,177,178,180,188,192,196,197,198,199,201,202,204,207,213,],[-49,-51,-52,-53,-54,-55,-50,86,86,86,-104,86,-104,-66,-68,-108,86,86,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,86,86,86,-86,-87,86,-80,-81,-82,-83,-84,-85,-70,-78,-79,-73,-88,86,86,-89,-90,-91,-92,-93,86,-67,-109,-104,-104,-104,-104,-97,-61,-65,-104,-105,-69,86,86,86,86,-96,86,-100,-56,86,-76,-71,-72,-74,-75,-64,-58,-101,-57,-59,-101,86,86,-40,86,-39,-60,]),'CTE_S':([33,36,37,38,39,40,60,64,65,66,73,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,100,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,127,136,137,138,139,140,141,143,146,149,155,156,158,159,160,161,162,163,164,165,170,171,172,175,176,177,178,180,188,192,196,197,198,199,201,202,204,207,213,],[-49,-51,-52,-53,-54,-55,-50,87,87,87,-104,87,-104,-66,-68,-108,87,87,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,87,87,87,-86,-87,87,-80,-81,-82,-83,-84,-85,-70,-78,-79,-73,-88,87,87,-89,-90,-91,-92,-93,87,-67,-109,-104,-104,-104,-104,-97,-61,-65,-104,-105,-69,87,87,87,87,-96,87,-100,-56,87,-76,-71,-72,-74,-75,-64,-58,-101,-57,-59,-101,87,87,-40,87,-39,-60,]),'TRUE':([33,36,37,38,39,40,60,64,65,66,73,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,100,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,127,136,137,138,139,140,141,143,146,149,155,156,158,159,160,161,162,163,164,165,170,171,172,175,176,177,178,180,188,192,196,197,198,199,201,202,204,207,213,],[-49,-51,-52,-53,-54,-55,-50,88,88,88,-104,88,-104,-66,-68,-108,88,88,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,88,88,88,-86,-87,88,-80,-81,-82,-83,-84,-85,-70,-78,-79,-73,-88,88,88,-89,-90,-91,-92,-93,88,-67,-109,-104,-104,-104,-104,-97,-61,-65,-104,-105,-69,88,88,88,88,-96,88,-100,-56,88,-76,-71,-72,-74,-75,-64,-58,-101,-57,-59,-101,88,88,-40,88,-39,-60,]),'FALSE':([33,36,37,38,39,40,60,64,65,66,73,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,100,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,127,136,137,138,139,140,141,143,146,149,155,156,158,159,160,161,162,163,164,165,170,171,172,175,176,177,178,180,188,192,196,197,198,199,201,202,204,207,213,],[-49,-51,-52,-53,-54,-55,-50,89,89,89,-104,89,-104,-66,-68,-108,89,89,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,89,89,89,-86,-87,89,-80,-81,-82,-83,-84,-85,-70,-78,-79,-73,-88,89,89,-89,-90,-91,-92,-93,89,-67,-109,-104,-104,-104,-104,-97,-61,-65,-104,-105,-69,89,89,89,89,-96,89,-100,-56,89,-76,-71,-72,-74,-75,-64,-58,-101,-57,-59,-101,89,89,-40,89,-39,-60,]),'EQUAL':([41,63,133,],[-103,73,155,]),'RBRACE':([56,77,78,79,82,83,84,85,86,87,88,89,90,91,101,114,115,116,117,118,121,122,123,124,125,136,137,143,145,156,158,163,165,172,175,176,177,178,],[71,-66,-68,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,133,-70,-78,-79,-73,-88,-89,-90,-91,-92,-93,-67,-109,-97,165,-105,-69,-96,-100,-76,-71,-72,-74,-75,]),'RPAREN':([76,77,78,79,82,83,84,85,86,87,88,89,90,91,92,93,94,95,114,115,116,117,118,119,121,122,123,124,125,131,134,136,137,142,143,144,147,150,153,156,158,163,165,169,172,175,176,177,178,179,186,195,],[103,-66,-68,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,126,-62,128,129,-70,-78,-79,-73,-88,143,-89,-90,-91,-92,-93,151,156,-67,-109,163,-97,-98,-63,167,-34,-105,-69,-96,-100,-32,-76,-71,-72,-74,-75,-99,-101,-33,]),'COMA':([77,78,79,82,83,84,85,86,87,88,89,90,91,93,114,115,116,117,118,121,122,123,124,125,136,137,143,144,156,158,163,165,169,172,175,176,177,178,],[-66,-68,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,127,-70,-78,-79,-73,-88,-89,-90,-91,-92,-93,-67,-109,-97,164,-105,-69,-96,-100,186,-76,-71,-72,-74,-75,]),'OR':([77,78,79,82,83,84,85,86,87,88,89,90,91,114,115,116,117,118,121,122,123,124,125,137,143,156,158,163,165,172,175,176,177,178,],[105,-68,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,-70,-78,-79,-73,-88,-89,-90,-91,-92,-93,-109,-97,-105,-69,-96,-100,-76,-71,-72,-74,-75,]),'AND':([77,78,79,82,83,84,85,86,87,88,89,90,91,114,115,116,117,118,121,122,123,124,125,137,143,156,158,163,165,172,175,176,177,178,],[106,-68,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,-70,-78,-79,-73,-88,-89,-90,-91,-92,-93,-109,-97,-105,-69,-96,-100,-76,-71,-72,-74,-75,]),'LOWERTHAN':([78,79,82,83,84,85,86,87,88,89,90,91,114,115,116,117,118,121,122,123,124,125,143,156,163,165,172,175,176,177,178,],[108,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,-70,-78,-79,-73,-88,-89,-90,-91,-92,-93,-97,-105,-96,-100,-76,-71,-72,-74,-75,]),'MORETHAN':([78,79,82,83,84,85,86,87,88,89,90,91,114,115,116,117,118,121,122,123,124,125,143,156,163,165,172,175,176,177,178,],[109,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,-70,-78,-79,-73,-88,-89,-90,-91,-92,-93,-97,-105,-96,-100,-76,-71,-72,-74,-75,]),'LOWEREQ':([78,79,82,83,84,85,86,87,88,89,90,91,114,115,116,117,118,121,122,123,124,125,143,156,163,165,172,175,176,177,178,],[110,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,-70,-78,-79,-73,-88,-89,-90,-91,-92,-93,-97,-105,-96,-100,-76,-71,-72,-74,-75,]),'MOREEQ':([78,79,82,83,84,85,86,87,88,89,90,91,114,115,116,117,118,121,122,123,124,125,143,156,163,165,172,175,176,177,178,],[111,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,-70,-78,-79,-73,-88,-89,-90,-91,-92,-93,-97,-105,-96,-100,-76,-71,-72,-74,-75,]),'SAME':([78,79,82,83,84,85,86,87,88,89,90,91,114,115,116,117,118,121,122,123,124,125,143,156,163,165,172,175,176,177,178,],[112,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,-70,-78,-79,-73,-88,-89,-90,-91,-92,-93,-97,-105,-96,-100,-76,-71,-72,-74,-75,]),'DIFFERENT':([78,79,82,83,84,85,86,87,88,89,90,91,114,115,116,117,118,121,122,123,124,125,143,156,163,165,172,175,176,177,178,],[113,-108,-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,-70,-78,-79,-73,-88,-89,-90,-91,-92,-93,-97,-105,-96,-100,-76,-71,-72,-74,-75,]),'TIMES':([82,83,84,85,86,87,88,89,90,91,115,116,117,118,121,122,123,124,125,143,156,163,165,172,],[-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,-78,-79,140,-88,-89,-90,-91,-92,-93,-97,-105,-96,-100,-76,]),'DIVIDE':([82,83,84,85,86,87,88,89,90,91,115,116,117,118,121,122,123,124,125,143,156,163,165,172,],[-107,-77,-103,-102,-102,-102,-102,-102,-94,-95,-78,-79,141,-88,-89,-90,-91,-92,-93,-97,-105,-96,-100,-76,]),'ELSE':([197,],[203,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'global':([3,],[4,]),'program2':([4,7,],[6,14,]),'crear':([4,7,],[7,7,]),'var':([4,7,22,34,35,168,181,184,185,],[8,8,34,34,34,184,184,184,184,]),'vector':([4,7,22,34,35,168,181,184,185,],[9,9,35,35,35,185,185,185,185,]),'main1':([5,24,46,],[12,47,68,]),'finglobal':([6,],[13,]),'tipo':([10,131,186,],[15,152,152,]),'mainc':([12,47,68,],[21,69,96,]),'program3':([13,25,],[23,48,]),'function':([13,25,],[25,25,]),'finmain':([21,69,96,],[29,97,130,]),'bloq':([22,32,33,148,157,182,190,208,],[31,58,60,166,174,192,198,211,]),'mainc2':([22,34,35,],[32,61,62,]),'estat':([22,32,33,148,157,182,190,208,],[33,33,33,33,33,33,33,33,]),'asign':([22,32,33,148,157,182,190,208,],[36,36,36,36,36,36,36,36,]),'cond':([22,32,33,148,157,182,190,208,],[37,37,37,37,37,37,37,37,]),'escrit':([22,32,33,148,157,182,190,208,],[38,38,38,38,38,38,38,38,]),'ciclo':([22,32,33,148,157,182,190,208,],[39,39,39,39,39,39,39,39,]),'leer':([22,32,33,148,157,182,190,208,],[40,40,40,40,40,40,40,40,]),'functype':([26,],[49,]),'pushid':([41,84,],[63,118,]),'expres':([64,65,66,100,102,104,119,120,127,164,171,199,201,204,],[76,93,94,132,134,136,144,145,93,144,187,206,207,209,]),'exr':([64,65,66,74,100,102,104,107,119,120,127,164,171,199,201,204,],[77,77,77,101,77,77,77,137,77,77,77,77,77,77,77,77,]),'ex':([64,65,66,74,100,102,104,107,119,120,127,159,160,164,171,199,201,204,],[78,78,78,78,78,78,78,78,78,78,78,175,176,78,78,78,78,78,]),'term':([64,65,66,74,100,102,104,107,119,120,127,159,160,161,162,164,171,199,201,204,],[79,79,79,79,79,79,79,79,79,79,79,79,79,177,178,79,79,79,79,79,]),'fact':([64,65,66,74,100,102,104,107,119,120,127,159,160,161,162,164,171,199,201,204,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'var_cte':([64,65,66,74,80,81,100,102,104,107,119,120,127,159,160,161,162,164,171,199,201,204,],[83,83,83,83,115,116,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'fcall':([64,65,66,74,80,81,100,102,104,107,119,120,127,159,160,161,162,164,171,199,201,204,],[90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,]),'vcall':([64,65,66,74,80,81,100,102,104,107,119,120,127,159,160,161,162,164,171,199,201,204,],[91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,]),'escriti':([65,127,],[92,147,]),'addInTable':([70,],[98,]),'pushop':([73,75,138,139,140,141,155,],[100,102,159,160,161,162,171,]),'log':([77,],[104,]),'rel':([78,],[107,]),'resterm':([79,],[114,]),'resfact':([82,],[117,]),'pushcte':([85,86,87,88,89,],[121,122,123,124,125,]),'fcall1':([119,164,],[142,179,]),'funci':([131,186,],[150,195,]),'empty':([131,186,192,198,],[153,153,202,202,]),'resolverasignacion':([132,],[154,]),'resif':([135,],[157,]),'resrel':([137,],[158,]),'popop':([156,],[172,]),'finif':([157,174,],[173,189,]),'localvar':([168,181,184,185,],[182,190,193,194,]),'return':([192,198,],[199,204,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM COLON global program2 finglobal program3 MAIN main1 mainc finmain','program',10,'p_program','lexPar.py',148),
  ('program -> PROGRAM COLON global program2 finglobal MAIN main1 mainc finmain','program',9,'p_program','lexPar.py',149),
  ('program -> PROGRAM COLON MAIN main1 mainc finmain','program',6,'p_program','lexPar.py',150),
  ('program2 -> crear program2','program2',2,'p_program2','lexPar.py',155),
  ('program2 -> crear','program2',1,'p_program2','lexPar.py',156),
  ('program3 -> function program3','program3',2,'p_program3','lexPar.py',161),
  ('program3 -> function','program3',1,'p_program3','lexPar.py',162),
  ('crear -> var','crear',1,'p_crear','lexPar.py',167),
  ('crear -> vector','crear',1,'p_crear','lexPar.py',168),
  ('global -> <empty>','global',0,'p_global','lexPar.py',172),
  ('finglobal -> <empty>','finglobal',0,'p_finglobal','lexPar.py',178),
  ('main1 -> <empty>','main1',0,'p_main1','lexPar.py',182),
  ('finmain -> <empty>','finmain',0,'p_finmain','lexPar.py',188),
  ('var -> VAR tipo ID SEMICOLON','var',4,'p_var','lexPar.py',193),
  ('tipo -> INT','tipo',1,'p_tipo','lexPar.py',206),
  ('tipo -> FLOAT','tipo',1,'p_tipo','lexPar.py',207),
  ('tipo -> STRING','tipo',1,'p_tipo','lexPar.py',208),
  ('tipo -> BOOL','tipo',1,'p_tipo','lexPar.py',209),
  ('vector -> VECTOR ID LBRACE CTE_I RBRACE SEMICOLON','vector',6,'p_vector','lexPar.py',215),
  ('function -> FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY localvar bloq return expres RKEY','function',13,'p_function','lexPar.py',222),
  ('function -> FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar RKEY','function',9,'p_function','lexPar.py',223),
  ('function -> FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY localvar bloq RKEY','function',11,'p_function','lexPar.py',224),
  ('function -> FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar bloq return expres RKEY','function',12,'p_function','lexPar.py',225),
  ('function -> FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar bloq RKEY','function',10,'p_function','lexPar.py',226),
  ('function -> FUNCTION functype ID addInTable LPAREN RPAREN LKEY RKEY','function',8,'p_function','lexPar.py',227),
  ('functype -> INT','functype',1,'p_functype','lexPar.py',235),
  ('functype -> FLOAT','functype',1,'p_functype','lexPar.py',236),
  ('functype -> STRING','functype',1,'p_functype','lexPar.py',237),
  ('functype -> BOOL','functype',1,'p_functype','lexPar.py',238),
  ('functype -> VOID','functype',1,'p_functype','lexPar.py',239),
  ('addInTable -> <empty>','addInTable',0,'p_addInTable','lexPar.py',245),
  ('funci -> tipo ID','funci',2,'p_funci','lexPar.py',254),
  ('funci -> tipo ID COMA funci','funci',4,'p_funci','lexPar.py',255),
  ('funci -> empty','funci',1,'p_funci','lexPar.py',256),
  ('localvar -> var','localvar',1,'p_localvar','lexPar.py',261),
  ('localvar -> vector','localvar',1,'p_localvar','lexPar.py',262),
  ('localvar -> var localvar','localvar',2,'p_localvar','lexPar.py',263),
  ('localvar -> vector localvar','localvar',2,'p_localvar','lexPar.py',264),
  ('return -> RETURN expres','return',2,'p_return','lexPar.py',269),
  ('return -> empty','return',1,'p_return','lexPar.py',270),
  ('mainc -> LKEY RKEY','mainc',2,'p_mainc','lexPar.py',275),
  ('mainc -> LKEY bloq RKEY','mainc',3,'p_mainc','lexPar.py',276),
  ('mainc -> LKEY mainc2 bloq RKEY','mainc',4,'p_mainc','lexPar.py',277),
  ('mainc -> LKEY mainc2 RKEY','mainc',3,'p_mainc','lexPar.py',278),
  ('mainc2 -> var','mainc2',1,'p_mainc2','lexPar.py',283),
  ('mainc2 -> var mainc2','mainc2',2,'p_mainc2','lexPar.py',284),
  ('mainc2 -> vector','mainc2',1,'p_mainc2','lexPar.py',285),
  ('mainc2 -> vector mainc2','mainc2',2,'p_mainc2','lexPar.py',286),
  ('bloq -> estat','bloq',1,'p_bloq','lexPar.py',291),
  ('bloq -> estat bloq','bloq',2,'p_bloq','lexPar.py',292),
  ('estat -> asign','estat',1,'p_estat','lexPar.py',297),
  ('estat -> cond','estat',1,'p_estat','lexPar.py',298),
  ('estat -> escrit','estat',1,'p_estat','lexPar.py',299),
  ('estat -> ciclo','estat',1,'p_estat','lexPar.py',300),
  ('estat -> leer','estat',1,'p_estat','lexPar.py',301),
  ('asign -> ID pushid EQUAL pushop expres resolverasignacion SEMICOLON','asign',7,'p_asign','lexPar.py',306),
  ('asign -> ID pushid LBRACE exr RBRACE EQUAL pushop expres SEMICOLON','asign',9,'p_asign','lexPar.py',307),
  ('cond -> IF LPAREN expres RPAREN LKEY resif finif RKEY','cond',8,'p_cond','lexPar.py',312),
  ('cond -> IF LPAREN expres RPAREN LKEY resif bloq finif RKEY','cond',9,'p_cond','lexPar.py',313),
  ('cond -> IF LPAREN expres RPAREN LKEY resif bloq finif RKEY ELSE LKEY bloq RKEY','cond',13,'p_cond','lexPar.py',314),
  ('escrit -> PRINT LPAREN escriti RPAREN SEMICOLON','escrit',5,'p_escrit','lexPar.py',319),
  ('escriti -> expres','escriti',1,'p_escriti','lexPar.py',324),
  ('escriti -> expres COMA escriti','escriti',3,'p_escriti','lexPar.py',325),
  ('ciclo -> WHILE LPAREN expres RPAREN LKEY bloq RKEY','ciclo',7,'p_ciclo','lexPar.py',330),
  ('leer -> READ LPAREN ID RPAREN SEMICOLON','leer',5,'p_leer','lexPar.py',335),
  ('expres -> exr','expres',1,'p_expres','lexPar.py',340),
  ('expres -> exr log expres','expres',3,'p_expres','lexPar.py',341),
  ('exr -> ex','exr',1,'p_exr','lexPar.py',346),
  ('exr -> ex rel exr resrel','exr',4,'p_exr','lexPar.py',347),
  ('ex -> term resterm','ex',2,'p_ex','lexPar.py',352),
  ('ex -> term resterm PLUS pushop ex','ex',5,'p_ex','lexPar.py',353),
  ('ex -> term resterm MINUS pushop ex','ex',5,'p_ex','lexPar.py',354),
  ('term -> fact resfact','term',2,'p_term','lexPar.py',359),
  ('term -> fact resfact TIMES pushop term','term',5,'p_term','lexPar.py',360),
  ('term -> fact resfact DIVIDE pushop term','term',5,'p_term','lexPar.py',361),
  ('fact -> LPAREN pushop expres RPAREN popop','fact',5,'p_fact','lexPar.py',366),
  ('fact -> var_cte','fact',1,'p_fact','lexPar.py',367),
  ('fact -> PLUS var_cte','fact',2,'p_fact','lexPar.py',368),
  ('fact -> MINUS var_cte','fact',2,'p_fact','lexPar.py',369),
  ('rel -> LOWERTHAN','rel',1,'p_rel','lexPar.py',374),
  ('rel -> MORETHAN','rel',1,'p_rel','lexPar.py',375),
  ('rel -> LOWEREQ','rel',1,'p_rel','lexPar.py',376),
  ('rel -> MOREEQ','rel',1,'p_rel','lexPar.py',377),
  ('rel -> SAME','rel',1,'p_rel','lexPar.py',378),
  ('rel -> DIFFERENT','rel',1,'p_rel','lexPar.py',379),
  ('log -> OR','log',1,'p_log','lexPar.py',386),
  ('log -> AND','log',1,'p_log','lexPar.py',387),
  ('var_cte -> ID pushid','var_cte',2,'p_var_cte','lexPar.py',392),
  ('var_cte -> CTE_I pushcte','var_cte',2,'p_var_cte','lexPar.py',393),
  ('var_cte -> CTE_F pushcte','var_cte',2,'p_var_cte','lexPar.py',394),
  ('var_cte -> CTE_S pushcte','var_cte',2,'p_var_cte','lexPar.py',395),
  ('var_cte -> TRUE pushcte','var_cte',2,'p_var_cte','lexPar.py',396),
  ('var_cte -> FALSE pushcte','var_cte',2,'p_var_cte','lexPar.py',397),
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
  ('resfact -> <empty>','resfact',0,'p_resfact','lexPar.py',460),
  ('resterm -> <empty>','resterm',0,'p_resterm','lexPar.py',464),
  ('resrel -> <empty>','resrel',0,'p_resrel','lexPar.py',468),
  ('resif -> <empty>','resif',0,'p_resif','lexPar.py',472),
  ('finif -> <empty>','finif',0,'p_finif','lexPar.py',476),
]
