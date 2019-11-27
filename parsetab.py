
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL COLON COMA CTE_F CTE_I CTE_S DIFFERENT DIVIDE ELSE EQUAL FALSE FIND FLOAT FUNCTION ID IF INT LBRACE LKEY LOWEREQ LOWERTHAN LPAREN MAIN MINUS MOREEQ MORETHAN OR PLUS PRINT PROGRAM RBRACE READ RETURN RKEY RPAREN SAME SEMICOLON SORT STRING TIMES TRUE VAR VECTOR VOID WHILE\n  \tprogram : PROGRAM COLON gotomain global program2 finglobal program3 llenarmain MAIN main1 mainc finmain\n        | PROGRAM COLON gotomain global program2 finglobal llenarmain MAIN main1 mainc finmain\n        | PROGRAM COLON gotomain global finglobal program3 llenarmain MAIN main1 mainc finmain\n        | PROGRAM COLON gotomain llenarmain MAIN main1 mainc finmain\n  gotomain :\n  \tprogram2 : crear program2\n    \t| crear\n  \n  \tprogram3 : function program3\n    \t| function\n  llenarmain :\n  \tcrear : var\n    \t| vector\n  global :finglobal :main1 :finmain :\n  \tvar : VAR tipo ID SEMICOLON\n  \n  \ttipo : INT\n    \t| FLOAT\n        | STRING\n        | BOOL\n  \n  \tvector : VECTOR initvector tipo ID LBRACE CTE_I RBRACE SEMICOLON\n  initvector :\n  \tfunction : FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY localvar bloq return1 RKEY\n    | FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY bloq return1 RKEY\n    | FUNCTION pushvoid ID addInTable LPAREN funci RPAREN LKEY localvar bloq RKEY\n    | FUNCTION pushvoid ID addInTable LPAREN funci RPAREN LKEY bloq RKEY\n    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar RKEY\n    | FUNCTION pushvoid ID addInTable LPAREN RPAREN LKEY localvar RKEY\n    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar bloq return1 RKEY\n    | FUNCTION pushvoid ID addInTable LPAREN RPAREN LKEY localvar bloq RKEY\n    | FUNCTION pushvoid ID addInTable  LPAREN RPAREN LKEY bloq RKEY\n    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY bloq return1 RKEY\n    | FUNCTION functype ID addInTable LPAREN RPAREN LKEY RKEY\n  \n  \tfunctype : INT\n    | FLOAT\n    | STRING\n    | BOOL\n  \n  \tpushvoid : VOID\n  \n    addInTable :\n    \n    funci : tipo ID sumparam\n    | tipo ID sumparam COMA funci\n  \n     localvar : var\n     | vector\n     | var localvar\n     | vector localvar\n     \n     sumparam :\n     \n    return1 : RETURN pushop expres resreturn SEMICOLON\n    | empty\n    \n    resreturn :\n    \n    mainc : LKEY RKEY\n    | LKEY localvar bloq RKEY\n    | LKEY localvar RKEY\n    | LKEY bloq RKEY\n    \n  \t bloq : estat\n         | estat bloq\n    \n  \testat : asign\n        | cond\n        | escrit\n        | ciclo\n        | leer\n        | fcallvoid\n        | findvec\n        | sorti\n\n  \n    asign : ID pushid EQUAL pushop fcall SEMICOLON\n        | ID pushid EQUAL pushop expres resolverasignacion SEMICOLON\n        | ID LBRACE exr RBRACE EQUAL pushop expres resasignvec SEMICOLON\n  \n    cond : IF LPAREN expres RPAREN LKEY resif bloq RKEY finif\n        | IF LPAREN expres RPAREN LKEY resif bloq RKEY ELSE LKEY reselse bloq RKEY finif\n  \n    escrit : PRINT pushop LPAREN escriti RPAREN SEMICOLON\n  \n  \tescriti : expres escrit1\n    \t| expres escrit2 COMA escriti\n  \n    escrit1 :\n    \n    escrit2 :\n    \n    ciclo : WHILE while1 LPAREN expres RPAREN while2 LKEY bloq RKEY while3\n  \n  \tleer : READ pushop LPAREN ID pushid RPAREN readid SEMICOLON\n  \n  \treadid :\n  \n  expres : exr\n        | exr log expres reslog\n  \n  \texr : ex\n    \t| ex rel exr resrel\n  \n    reslog :\n    \n  \tex : term resterm\n    \t| term resterm PLUS pushop ex\n    \t| term resterm MINUS pushop ex\n  \n  \tterm : fact resfact\n    \t| fact resfact TIMES pushop term\n        | fact resfact DIVIDE pushop term\n  \n  \tfact : LPAREN pushop expres RPAREN popop\n        | var_cte\n        | PLUS pushop var_cte\n        | MINUS pushop var_cte\n  \n  \trel : LOWERTHAN\n    \t| MORETHAN\n        | LOWEREQ\n        | MOREEQ\n        | SAME\n        | DIFFERENT\n  \n  \tlog : OR\n        | AND\n  \n  \tvar_cte : ID pushid\n        | CTE_I pushcte\n        | CTE_F pushcte\n        | CTE_S pushcte\n        | TRUE pushcte\n        | FALSE pushcte\n        | asigvector\n  findvec : FIND pushop LPAREN ID LBRACE ex RBRACE RPAREN SEMICOLON\n    sorti : SORT pushop LPAREN ID LBRACE RBRACE RPAREN SEMICOLON\n    \n    asigvector : ID pushid LBRACE ex RBRACE\n    \n  \tfcall : ID existfunc LPAREN startera fcall1 RPAREN\n        | ID existfunc LPAREN startera RPAREN\n  \n    fcallvoid : ID existfunc LPAREN startera fcall1 RPAREN SEMICOLON\n    | ID existfunc LPAREN startera RPAREN SEMICOLON\n    existfunc :startera :\n  \tfcall1 : expres generateparam\n        | expres generateparam COMA fcall1\n  generateparam :\n    empty :\n    pushcte :pushid :pushop :popop :resolverasignacion :resasignvec :resfact :resterm :resrel :resif :reselse :finif :while1 :while2 :while3 :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,40,49,50,78,79,93,94,98,123,124,125,163,],[0,-16,-4,-51,-53,-54,-16,-16,-52,-16,-2,-3,-1,]),'COLON':([2,],[3,]),'VAR':([3,4,5,9,10,11,41,47,53,54,165,168,169,195,200,],[-5,-13,12,12,-11,-12,12,-17,12,12,12,12,-22,12,12,]),'VECTOR':([3,4,5,9,10,11,41,47,53,54,165,168,169,195,200,],[-5,-13,13,13,-11,-12,13,-17,13,13,13,13,-22,13,13,]),'FUNCTION':([3,4,5,7,8,9,10,11,15,17,19,47,169,197,227,235,237,258,262,263,273,274,276,284,],[-5,-13,-14,-14,18,-7,-11,-12,18,18,-6,-17,-22,-34,-28,-29,-32,-33,-27,-31,-25,-30,-26,-24,]),'MAIN':([3,4,6,7,9,10,11,15,16,17,19,27,28,29,30,42,47,169,197,227,235,237,258,262,263,273,274,276,284,],[-5,-10,14,-14,-7,-11,-12,-10,-10,-9,-6,-10,43,44,-8,71,-17,-22,-34,-28,-29,-32,-33,-27,-31,-25,-30,-26,-24,]),'INT':([12,13,18,25,95,96,232,],[21,-23,33,21,21,21,21,]),'FLOAT':([12,13,18,25,95,96,232,],[22,-23,34,22,22,22,22,]),'STRING':([12,13,18,25,95,96,232,],[23,-23,35,23,23,23,23,]),'BOOL':([12,13,18,25,95,96,232,],[24,-23,36,24,24,24,24,]),'LKEY':([14,26,43,44,71,72,73,92,127,130,153,164,167,191,221,281,],[-15,41,-15,-15,-15,41,41,41,165,168,186,195,200,-134,251,287,]),'VOID':([18,],[37,]),'ID':([20,21,22,23,24,31,32,33,34,35,36,37,39,41,47,51,53,54,55,57,58,59,60,61,62,63,64,80,81,84,86,99,104,105,107,115,118,119,120,121,122,128,132,135,136,137,138,139,140,141,143,144,146,152,154,155,156,165,168,169,173,174,176,177,180,181,186,193,195,196,200,201,204,207,209,210,211,212,215,217,219,220,225,230,233,238,239,247,248,251,259,264,267,269,271,279,280,282,283,287,288,290,292,293,],[38,-18,-19,-20,-21,45,46,-35,-36,-37,-38,-39,48,56,-17,56,-43,-44,56,-57,-58,-59,-60,-61,-62,-63,-64,-45,-46,100,100,-123,-123,-123,-123,-116,100,100,160,161,162,166,170,100,-93,-94,-95,-96,-97,-98,100,100,100,100,100,-99,-100,56,56,-22,100,-123,-123,-123,-123,-123,-130,100,56,56,56,56,-65,100,100,100,100,100,-114,56,-70,100,56,-123,56,-116,-66,-113,100,56,100,100,-132,-76,-109,-67,-68,-135,-108,-131,-75,56,-132,-69,]),'SEMICOLON':([38,100,102,103,106,108,109,110,111,112,113,114,117,131,133,142,145,147,148,149,150,151,170,171,172,175,178,179,184,187,188,205,208,213,214,218,222,240,241,242,243,244,245,246,252,254,265,270,275,278,285,286,],[47,-122,-80,-128,-127,-90,-121,-121,-121,-121,-121,-107,-78,169,-101,-83,-86,-102,-103,-104,-105,-106,-122,204,-125,-129,-91,-92,215,-82,219,239,-81,-124,247,-79,-77,-110,-126,-84,-85,-87,-88,-89,269,271,279,283,-50,-112,289,-111,]),'RKEY':([41,47,51,52,53,54,55,57,58,59,60,61,62,63,64,77,80,81,82,165,169,196,198,201,202,204,215,219,226,228,229,231,234,236,239,247,249,255,256,257,261,267,268,269,271,272,279,280,282,283,288,289,291,292,293,],[50,-17,78,79,-43,-44,-55,-57,-58,-59,-60,-61,-62,-63,-64,98,-45,-46,-56,197,-22,227,-120,235,237,-65,-114,-70,-120,-120,258,-49,262,263,-66,-113,267,-120,273,274,276,-132,282,-76,-109,284,-67,-68,-135,-108,-75,-48,292,-132,-69,]),'IF':([41,47,51,53,54,55,57,58,59,60,61,62,63,64,80,81,165,168,169,186,195,196,200,201,204,215,217,219,225,233,239,247,251,267,269,271,279,280,282,283,287,288,290,292,293,],[65,-17,65,-43,-44,65,-57,-58,-59,-60,-61,-62,-63,-64,-45,-46,65,65,-22,-130,65,65,65,65,-65,-114,65,-70,65,65,-66,-113,65,-132,-76,-109,-67,-68,-135,-108,-131,-75,65,-132,-69,]),'PRINT':([41,47,51,53,54,55,57,58,59,60,61,62,63,64,80,81,165,168,169,186,195,196,200,201,204,215,217,219,225,233,239,247,251,267,269,271,279,280,282,283,287,288,290,292,293,],[66,-17,66,-43,-44,66,-57,-58,-59,-60,-61,-62,-63,-64,-45,-46,66,66,-22,-130,66,66,66,66,-65,-114,66,-70,66,66,-66,-113,66,-132,-76,-109,-67,-68,-135,-108,-131,-75,66,-132,-69,]),'WHILE':([41,47,51,53,54,55,57,58,59,60,61,62,63,64,80,81,165,168,169,186,195,196,200,201,204,215,217,219,225,233,239,247,251,267,269,271,279,280,282,283,287,288,290,292,293,],[67,-17,67,-43,-44,67,-57,-58,-59,-60,-61,-62,-63,-64,-45,-46,67,67,-22,-130,67,67,67,67,-65,-114,67,-70,67,67,-66,-113,67,-132,-76,-109,-67,-68,-135,-108,-131,-75,67,-132,-69,]),'READ':([41,47,51,53,54,55,57,58,59,60,61,62,63,64,80,81,165,168,169,186,195,196,200,201,204,215,217,219,225,233,239,247,251,267,269,271,279,280,282,283,287,288,290,292,293,],[68,-17,68,-43,-44,68,-57,-58,-59,-60,-61,-62,-63,-64,-45,-46,68,68,-22,-130,68,68,68,68,-65,-114,68,-70,68,68,-66,-113,68,-132,-76,-109,-67,-68,-135,-108,-131,-75,68,-132,-69,]),'FIND':([41,47,51,53,54,55,57,58,59,60,61,62,63,64,80,81,165,168,169,186,195,196,200,201,204,215,217,219,225,233,239,247,251,267,269,271,279,280,282,283,287,288,290,292,293,],[69,-17,69,-43,-44,69,-57,-58,-59,-60,-61,-62,-63,-64,-45,-46,69,69,-22,-130,69,69,69,69,-65,-114,69,-70,69,69,-66,-113,69,-132,-76,-109,-67,-68,-135,-108,-131,-75,69,-132,-69,]),'SORT':([41,47,51,53,54,55,57,58,59,60,61,62,63,64,80,81,165,168,169,186,195,196,200,201,204,215,217,219,225,233,239,247,251,267,269,271,279,280,282,283,287,288,290,292,293,],[70,-17,70,-43,-44,70,-57,-58,-59,-60,-61,-62,-63,-64,-45,-46,70,70,-22,-130,70,70,70,70,-65,-114,70,-70,70,70,-66,-113,70,-132,-76,-109,-67,-68,-135,-108,-131,-75,70,-132,-69,]),'LPAREN':([45,46,56,65,66,67,68,69,70,74,75,84,85,86,87,88,89,90,91,99,107,115,118,119,132,135,136,137,138,139,140,141,146,152,154,155,156,170,173,174,176,177,180,181,193,203,207,209,210,211,212,220,230,238,248,259,264,],[-40,-40,-115,86,-123,-133,-123,-123,-123,95,96,107,115,107,118,119,120,121,122,-123,-123,-116,107,107,107,107,-93,-94,-95,-96,-97,-98,107,107,107,-99,-100,-115,107,-123,-123,-123,-123,-123,107,238,107,107,107,107,107,107,-123,-116,107,107,107,]),'LBRACE':([48,56,100,133,161,162,170,],[76,84,-122,173,193,194,-122,]),'RETURN':([55,57,58,59,60,61,62,63,64,82,198,204,215,219,226,228,239,247,255,267,269,271,279,280,282,283,288,292,293,],[-55,-57,-58,-59,-60,-61,-62,-63,-64,-56,230,-65,-114,-70,230,230,-66,-113,230,-132,-76,-109,-67,-68,-135,-108,-75,-132,-69,]),'EQUAL':([56,83,134,],[-122,99,174,]),'CTE_I':([76,84,86,99,104,105,107,115,118,119,132,135,136,137,138,139,140,141,143,144,146,152,154,155,156,173,174,176,177,180,181,193,207,209,210,211,212,220,230,238,248,259,264,],[97,109,109,-123,-123,-123,-123,-116,109,109,109,109,-93,-94,-95,-96,-97,-98,109,109,109,109,109,-99,-100,109,-123,-123,-123,-123,-123,109,109,109,109,109,109,109,-123,-116,109,109,109,]),'PLUS':([84,86,99,100,103,106,107,108,109,110,111,112,113,114,115,118,119,132,133,135,136,137,138,139,140,141,142,145,146,147,148,149,150,151,152,154,155,156,170,173,174,176,177,178,179,180,181,193,207,209,210,211,212,213,220,230,238,240,244,245,246,248,259,264,],[104,104,-123,-122,-128,-127,-123,-90,-121,-121,-121,-121,-121,-107,-116,104,104,104,-101,104,-93,-94,-95,-96,-97,-98,176,-86,104,-102,-103,-104,-105,-106,104,104,-99,-100,-122,104,-123,-123,-123,-91,-92,-123,-123,104,104,104,104,104,104,-124,104,-123,-116,-110,-87,-88,-89,104,104,104,]),'MINUS':([84,86,99,100,103,106,107,108,109,110,111,112,113,114,115,118,119,132,133,135,136,137,138,139,140,141,142,145,146,147,148,149,150,151,152,154,155,156,170,173,174,176,177,178,179,180,181,193,207,209,210,211,212,213,220,230,238,240,244,245,246,248,259,264,],[105,105,-123,-122,-128,-127,-123,-90,-121,-121,-121,-121,-121,-107,-116,105,105,105,-101,105,-93,-94,-95,-96,-97,-98,177,-86,105,-102,-103,-104,-105,-106,105,105,-99,-100,-122,105,-123,-123,-123,-91,-92,-123,-123,105,105,105,105,105,105,-124,105,-123,-116,-110,-87,-88,-89,105,105,105,]),'CTE_F':([84,86,99,104,105,107,115,118,119,132,135,136,137,138,139,140,141,143,144,146,152,154,155,156,173,174,176,177,180,181,193,207,209,210,211,212,220,230,238,248,259,264,],[110,110,-123,-123,-123,-123,-116,110,110,110,110,-93,-94,-95,-96,-97,-98,110,110,110,110,110,-99,-100,110,-123,-123,-123,-123,-123,110,110,110,110,110,110,110,-123,-116,110,110,110,]),'CTE_S':([84,86,99,104,105,107,115,118,119,132,135,136,137,138,139,140,141,143,144,146,152,154,155,156,173,174,176,177,180,181,193,207,209,210,211,212,220,230,238,248,259,264,],[111,111,-123,-123,-123,-123,-116,111,111,111,111,-93,-94,-95,-96,-97,-98,111,111,111,111,111,-99,-100,111,-123,-123,-123,-123,-123,111,111,111,111,111,111,111,-123,-116,111,111,111,]),'TRUE':([84,86,99,104,105,107,115,118,119,132,135,136,137,138,139,140,141,143,144,146,152,154,155,156,173,174,176,177,180,181,193,207,209,210,211,212,220,230,238,248,259,264,],[112,112,-123,-123,-123,-123,-116,112,112,112,112,-93,-94,-95,-96,-97,-98,112,112,112,112,112,-99,-100,112,-123,-123,-123,-123,-123,112,112,112,112,112,112,112,-123,-116,112,112,112,]),'FALSE':([84,86,99,104,105,107,115,118,119,132,135,136,137,138,139,140,141,143,144,146,152,154,155,156,173,174,176,177,180,181,193,207,209,210,211,212,220,230,238,248,259,264,],[113,113,-123,-123,-123,-123,-116,113,113,113,113,-93,-94,-95,-96,-97,-98,113,113,113,113,113,-99,-100,113,-123,-123,-123,-123,-123,113,113,113,113,113,113,113,-123,-116,113,113,113,]),'RPAREN':([95,96,100,102,103,106,108,109,110,111,112,113,114,115,116,117,126,129,133,142,145,147,148,149,150,151,152,157,158,159,160,166,175,178,179,182,183,185,187,189,192,199,208,213,216,218,224,238,240,242,243,244,245,246,250,253,260,264,266,277,],[127,130,-122,-80,-128,-127,-90,-121,-121,-121,-121,-121,-107,-116,153,-78,164,167,-101,-83,-86,-102,-103,-104,-105,-106,184,188,-73,191,-122,-47,-129,-91,-92,213,214,-119,-82,-71,222,-41,-81,-124,-117,-79,254,-116,-110,-84,-85,-87,-88,-89,-72,270,-42,278,-118,286,]),'RBRACE':([97,100,101,102,103,106,108,109,110,111,112,113,114,133,142,145,147,148,149,150,151,175,178,179,194,206,208,213,223,240,242,243,244,245,246,],[131,-122,134,-80,-128,-127,-90,-121,-121,-121,-121,-121,-107,-101,-83,-86,-102,-103,-104,-105,-106,-129,-91,-92,224,240,-81,-124,253,-110,-84,-85,-87,-88,-89,]),'TIMES':([100,106,108,109,110,111,112,113,114,133,145,147,148,149,150,151,170,178,179,213,240,246,],[-122,-127,-90,-121,-121,-121,-121,-121,-107,-101,180,-102,-103,-104,-105,-106,-122,-91,-92,-124,-110,-89,]),'DIVIDE':([100,106,108,109,110,111,112,113,114,133,145,147,148,149,150,151,170,178,179,213,240,246,],[-122,-127,-90,-121,-121,-121,-121,-121,-107,-101,181,-102,-103,-104,-105,-106,-122,-91,-92,-124,-110,-89,]),'LOWERTHAN':([100,102,103,106,108,109,110,111,112,113,114,133,142,145,147,148,149,150,151,170,178,179,213,240,242,243,244,245,246,],[-122,136,-128,-127,-90,-121,-121,-121,-121,-121,-107,-101,-83,-86,-102,-103,-104,-105,-106,-122,-91,-92,-124,-110,-84,-85,-87,-88,-89,]),'MORETHAN':([100,102,103,106,108,109,110,111,112,113,114,133,142,145,147,148,149,150,151,170,178,179,213,240,242,243,244,245,246,],[-122,137,-128,-127,-90,-121,-121,-121,-121,-121,-107,-101,-83,-86,-102,-103,-104,-105,-106,-122,-91,-92,-124,-110,-84,-85,-87,-88,-89,]),'LOWEREQ':([100,102,103,106,108,109,110,111,112,113,114,133,142,145,147,148,149,150,151,170,178,179,213,240,242,243,244,245,246,],[-122,138,-128,-127,-90,-121,-121,-121,-121,-121,-107,-101,-83,-86,-102,-103,-104,-105,-106,-122,-91,-92,-124,-110,-84,-85,-87,-88,-89,]),'MOREEQ':([100,102,103,106,108,109,110,111,112,113,114,133,142,145,147,148,149,150,151,170,178,179,213,240,242,243,244,245,246,],[-122,139,-128,-127,-90,-121,-121,-121,-121,-121,-107,-101,-83,-86,-102,-103,-104,-105,-106,-122,-91,-92,-124,-110,-84,-85,-87,-88,-89,]),'SAME':([100,102,103,106,108,109,110,111,112,113,114,133,142,145,147,148,149,150,151,170,178,179,213,240,242,243,244,245,246,],[-122,140,-128,-127,-90,-121,-121,-121,-121,-121,-107,-101,-83,-86,-102,-103,-104,-105,-106,-122,-91,-92,-124,-110,-84,-85,-87,-88,-89,]),'DIFFERENT':([100,102,103,106,108,109,110,111,112,113,114,133,142,145,147,148,149,150,151,170,178,179,213,240,242,243,244,245,246,],[-122,141,-128,-127,-90,-121,-121,-121,-121,-121,-107,-101,-83,-86,-102,-103,-104,-105,-106,-122,-91,-92,-124,-110,-84,-85,-87,-88,-89,]),'OR':([100,102,103,106,108,109,110,111,112,113,114,117,133,142,145,147,148,149,150,151,170,175,178,179,208,213,240,242,243,244,245,246,],[-122,-80,-128,-127,-90,-121,-121,-121,-121,-121,-107,155,-101,-83,-86,-102,-103,-104,-105,-106,-122,-129,-91,-92,-81,-124,-110,-84,-85,-87,-88,-89,]),'AND':([100,102,103,106,108,109,110,111,112,113,114,117,133,142,145,147,148,149,150,151,170,175,178,179,208,213,240,242,243,244,245,246,],[-122,-80,-128,-127,-90,-121,-121,-121,-121,-121,-107,156,-101,-83,-86,-102,-103,-104,-105,-106,-122,-129,-91,-92,-81,-124,-110,-84,-85,-87,-88,-89,]),'COMA':([100,102,103,106,108,109,110,111,112,113,114,117,133,142,145,147,148,149,150,151,158,166,175,178,179,185,187,190,199,208,213,216,218,240,242,243,244,245,246,],[-122,-80,-128,-127,-90,-121,-121,-121,-121,-121,-107,-78,-101,-83,-86,-102,-103,-104,-105,-106,-74,-47,-129,-91,-92,-119,-82,220,232,-81,-124,248,-79,-110,-84,-85,-87,-88,-89,]),'ELSE':([267,],[281,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'gotomain':([3,],[4,]),'global':([4,],[5,]),'llenarmain':([4,15,16,27,],[6,28,29,42,]),'program2':([5,9,],[7,19,]),'finglobal':([5,7,],[8,15,]),'crear':([5,9,],[9,9,]),'var':([5,9,41,53,54,165,168,195,200,],[10,10,53,53,53,53,53,53,53,]),'vector':([5,9,41,53,54,165,168,195,200,],[11,11,54,54,54,54,54,54,54,]),'program3':([8,15,17,],[16,27,30,]),'function':([8,15,17,],[17,17,17,]),'tipo':([12,25,95,96,232,],[20,39,128,128,128,]),'initvector':([13,],[25,]),'main1':([14,43,44,71,],[26,72,73,92,]),'functype':([18,],[31,]),'pushvoid':([18,],[32,]),'mainc':([26,72,73,92,],[40,93,94,123,]),'finmain':([40,93,94,123,],[49,124,125,163,]),'localvar':([41,53,54,165,168,195,200,],[51,80,81,196,201,225,233,]),'bloq':([41,51,55,165,168,195,196,200,201,217,225,233,251,290,],[52,77,82,198,202,226,228,234,236,249,255,261,268,291,]),'estat':([41,51,55,165,168,195,196,200,201,217,225,233,251,290,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'asign':([41,51,55,165,168,195,196,200,201,217,225,233,251,290,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'cond':([41,51,55,165,168,195,196,200,201,217,225,233,251,290,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'escrit':([41,51,55,165,168,195,196,200,201,217,225,233,251,290,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'ciclo':([41,51,55,165,168,195,196,200,201,217,225,233,251,290,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'leer':([41,51,55,165,168,195,196,200,201,217,225,233,251,290,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'fcallvoid':([41,51,55,165,168,195,196,200,201,217,225,233,251,290,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'findvec':([41,51,55,165,168,195,196,200,201,217,225,233,251,290,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'sorti':([41,51,55,165,168,195,196,200,201,217,225,233,251,290,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'addInTable':([45,46,],[74,75,]),'pushid':([56,100,160,170,],[83,133,192,133,]),'existfunc':([56,170,],[85,203,]),'pushop':([66,68,69,70,99,104,105,107,174,176,177,180,181,230,],[87,89,90,91,132,143,144,146,207,209,210,211,212,259,]),'while1':([67,],[88,]),'exr':([84,86,118,119,132,135,146,152,154,207,220,248,259,264,],[101,117,117,117,117,175,117,117,117,117,117,117,117,117,]),'ex':([84,86,118,119,132,135,146,152,154,173,193,207,209,210,220,248,259,264,],[102,102,102,102,102,102,102,102,102,206,223,102,242,243,102,102,102,102,]),'term':([84,86,118,119,132,135,146,152,154,173,193,207,209,210,211,212,220,248,259,264,],[103,103,103,103,103,103,103,103,103,103,103,103,103,103,244,245,103,103,103,103,]),'fact':([84,86,118,119,132,135,146,152,154,173,193,207,209,210,211,212,220,248,259,264,],[106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,]),'var_cte':([84,86,118,119,132,135,143,144,146,152,154,173,193,207,209,210,211,212,220,248,259,264,],[108,108,108,108,108,108,178,179,108,108,108,108,108,108,108,108,108,108,108,108,108,108,]),'asigvector':([84,86,118,119,132,135,143,144,146,152,154,173,193,207,209,210,211,212,220,248,259,264,],[114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,]),'expres':([86,118,119,132,146,152,154,207,220,248,259,264,],[116,158,159,172,182,185,187,241,158,185,275,185,]),'funci':([95,96,232,],[126,129,260,]),'rel':([102,],[135,]),'resterm':([103,],[142,]),'resfact':([106,],[145,]),'pushcte':([109,110,111,112,113,],[147,148,149,150,151,]),'startera':([115,238,],[152,264,]),'log':([117,],[154,]),'escriti':([118,220,],[157,250,]),'fcall':([132,],[171,]),'fcall1':([152,248,264,],[183,266,277,]),'escrit1':([158,],[189,]),'escrit2':([158,],[190,]),'sumparam':([166,],[199,]),'resolverasignacion':([172,],[205,]),'resrel':([175,],[208,]),'generateparam':([185,],[216,]),'resif':([186,],[217,]),'reslog':([187,],[218,]),'while2':([191,],[221,]),'return1':([198,226,228,255,],[229,256,257,272,]),'empty':([198,226,228,255,],[231,231,231,231,]),'popop':([213,],[246,]),'readid':([222,],[252,]),'resasignvec':([241,],[265,]),'finif':([267,292,],[280,293,]),'resreturn':([275,],[285,]),'while3':([282,],[288,]),'reselse':([287,],[290,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM COLON gotomain global program2 finglobal program3 llenarmain MAIN main1 mainc finmain','program',12,'p_program','lexPar.py',152),
  ('program -> PROGRAM COLON gotomain global program2 finglobal llenarmain MAIN main1 mainc finmain','program',11,'p_program','lexPar.py',153),
  ('program -> PROGRAM COLON gotomain global finglobal program3 llenarmain MAIN main1 mainc finmain','program',11,'p_program','lexPar.py',154),
  ('program -> PROGRAM COLON gotomain llenarmain MAIN main1 mainc finmain','program',8,'p_program','lexPar.py',155),
  ('gotomain -> <empty>','gotomain',0,'p_gotomain','lexPar.py',161),
  ('program2 -> crear program2','program2',2,'p_program2','lexPar.py',166),
  ('program2 -> crear','program2',1,'p_program2','lexPar.py',167),
  ('program3 -> function program3','program3',2,'p_program3','lexPar.py',172),
  ('program3 -> function','program3',1,'p_program3','lexPar.py',173),
  ('llenarmain -> <empty>','llenarmain',0,'p_llenarmain','lexPar.py',177),
  ('crear -> var','crear',1,'p_crear','lexPar.py',182),
  ('crear -> vector','crear',1,'p_crear','lexPar.py',183),
  ('global -> <empty>','global',0,'p_global','lexPar.py',187),
  ('finglobal -> <empty>','finglobal',0,'p_finglobal','lexPar.py',194),
  ('main1 -> <empty>','main1',0,'p_main1','lexPar.py',198),
  ('finmain -> <empty>','finmain',0,'p_finmain','lexPar.py',204),
  ('var -> VAR tipo ID SEMICOLON','var',4,'p_var','lexPar.py',209),
  ('tipo -> INT','tipo',1,'p_tipo','lexPar.py',222),
  ('tipo -> FLOAT','tipo',1,'p_tipo','lexPar.py',223),
  ('tipo -> STRING','tipo',1,'p_tipo','lexPar.py',224),
  ('tipo -> BOOL','tipo',1,'p_tipo','lexPar.py',225),
  ('vector -> VECTOR initvector tipo ID LBRACE CTE_I RBRACE SEMICOLON','vector',8,'p_vector','lexPar.py',232),
  ('initvector -> <empty>','initvector',0,'p_initvector','lexPar.py',247),
  ('function -> FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY localvar bloq return1 RKEY','function',12,'p_function','lexPar.py',252),
  ('function -> FUNCTION functype ID addInTable LPAREN funci RPAREN LKEY bloq return1 RKEY','function',11,'p_function','lexPar.py',253),
  ('function -> FUNCTION pushvoid ID addInTable LPAREN funci RPAREN LKEY localvar bloq RKEY','function',11,'p_function','lexPar.py',254),
  ('function -> FUNCTION pushvoid ID addInTable LPAREN funci RPAREN LKEY bloq RKEY','function',10,'p_function','lexPar.py',255),
  ('function -> FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar RKEY','function',9,'p_function','lexPar.py',256),
  ('function -> FUNCTION pushvoid ID addInTable LPAREN RPAREN LKEY localvar RKEY','function',9,'p_function','lexPar.py',257),
  ('function -> FUNCTION functype ID addInTable LPAREN RPAREN LKEY localvar bloq return1 RKEY','function',11,'p_function','lexPar.py',258),
  ('function -> FUNCTION pushvoid ID addInTable LPAREN RPAREN LKEY localvar bloq RKEY','function',10,'p_function','lexPar.py',259),
  ('function -> FUNCTION pushvoid ID addInTable LPAREN RPAREN LKEY bloq RKEY','function',9,'p_function','lexPar.py',260),
  ('function -> FUNCTION functype ID addInTable LPAREN RPAREN LKEY bloq return1 RKEY','function',10,'p_function','lexPar.py',261),
  ('function -> FUNCTION functype ID addInTable LPAREN RPAREN LKEY RKEY','function',8,'p_function','lexPar.py',262),
  ('functype -> INT','functype',1,'p_functype','lexPar.py',284),
  ('functype -> FLOAT','functype',1,'p_functype','lexPar.py',285),
  ('functype -> STRING','functype',1,'p_functype','lexPar.py',286),
  ('functype -> BOOL','functype',1,'p_functype','lexPar.py',287),
  ('pushvoid -> VOID','pushvoid',1,'p_pushvoid','lexPar.py',293),
  ('addInTable -> <empty>','addInTable',0,'p_addInTable','lexPar.py',300),
  ('funci -> tipo ID sumparam','funci',3,'p_funci','lexPar.py',310),
  ('funci -> tipo ID sumparam COMA funci','funci',5,'p_funci','lexPar.py',311),
  ('localvar -> var','localvar',1,'p_localvar','lexPar.py',319),
  ('localvar -> vector','localvar',1,'p_localvar','lexPar.py',320),
  ('localvar -> var localvar','localvar',2,'p_localvar','lexPar.py',321),
  ('localvar -> vector localvar','localvar',2,'p_localvar','lexPar.py',322),
  ('sumparam -> <empty>','sumparam',0,'p_sumparam','lexPar.py',327),
  ('return1 -> RETURN pushop expres resreturn SEMICOLON','return1',5,'p_return1','lexPar.py',334),
  ('return1 -> empty','return1',1,'p_return1','lexPar.py',335),
  ('resreturn -> <empty>','resreturn',0,'p_resreturn','lexPar.py',341),
  ('mainc -> LKEY RKEY','mainc',2,'p_mainc','lexPar.py',346),
  ('mainc -> LKEY localvar bloq RKEY','mainc',4,'p_mainc','lexPar.py',347),
  ('mainc -> LKEY localvar RKEY','mainc',3,'p_mainc','lexPar.py',348),
  ('mainc -> LKEY bloq RKEY','mainc',3,'p_mainc','lexPar.py',349),
  ('bloq -> estat','bloq',1,'p_bloq','lexPar.py',354),
  ('bloq -> estat bloq','bloq',2,'p_bloq','lexPar.py',355),
  ('estat -> asign','estat',1,'p_estat','lexPar.py',360),
  ('estat -> cond','estat',1,'p_estat','lexPar.py',361),
  ('estat -> escrit','estat',1,'p_estat','lexPar.py',362),
  ('estat -> ciclo','estat',1,'p_estat','lexPar.py',363),
  ('estat -> leer','estat',1,'p_estat','lexPar.py',364),
  ('estat -> fcallvoid','estat',1,'p_estat','lexPar.py',365),
  ('estat -> findvec','estat',1,'p_estat','lexPar.py',366),
  ('estat -> sorti','estat',1,'p_estat','lexPar.py',367),
  ('asign -> ID pushid EQUAL pushop fcall SEMICOLON','asign',6,'p_asign','lexPar.py',373),
  ('asign -> ID pushid EQUAL pushop expres resolverasignacion SEMICOLON','asign',7,'p_asign','lexPar.py',374),
  ('asign -> ID LBRACE exr RBRACE EQUAL pushop expres resasignvec SEMICOLON','asign',9,'p_asign','lexPar.py',375),
  ('cond -> IF LPAREN expres RPAREN LKEY resif bloq RKEY finif','cond',9,'p_cond','lexPar.py',380),
  ('cond -> IF LPAREN expres RPAREN LKEY resif bloq RKEY ELSE LKEY reselse bloq RKEY finif','cond',14,'p_cond','lexPar.py',381),
  ('escrit -> PRINT pushop LPAREN escriti RPAREN SEMICOLON','escrit',6,'p_escrit','lexPar.py',386),
  ('escriti -> expres escrit1','escriti',2,'p_escriti','lexPar.py',391),
  ('escriti -> expres escrit2 COMA escriti','escriti',4,'p_escriti','lexPar.py',392),
  ('escrit1 -> <empty>','escrit1',0,'p_escrit1','lexPar.py',397),
  ('escrit2 -> <empty>','escrit2',0,'p_escrit2','lexPar.py',403),
  ('ciclo -> WHILE while1 LPAREN expres RPAREN while2 LKEY bloq RKEY while3','ciclo',10,'p_ciclo','lexPar.py',410),
  ('leer -> READ pushop LPAREN ID pushid RPAREN readid SEMICOLON','leer',8,'p_leer','lexPar.py',415),
  ('readid -> <empty>','readid',0,'p_readid','lexPar.py',420),
  ('expres -> exr','expres',1,'p_expres','lexPar.py',426),
  ('expres -> exr log expres reslog','expres',4,'p_expres','lexPar.py',427),
  ('exr -> ex','exr',1,'p_exr','lexPar.py',432),
  ('exr -> ex rel exr resrel','exr',4,'p_exr','lexPar.py',433),
  ('reslog -> <empty>','reslog',0,'p_reslog','lexPar.py',438),
  ('ex -> term resterm','ex',2,'p_ex','lexPar.py',444),
  ('ex -> term resterm PLUS pushop ex','ex',5,'p_ex','lexPar.py',445),
  ('ex -> term resterm MINUS pushop ex','ex',5,'p_ex','lexPar.py',446),
  ('term -> fact resfact','term',2,'p_term','lexPar.py',451),
  ('term -> fact resfact TIMES pushop term','term',5,'p_term','lexPar.py',452),
  ('term -> fact resfact DIVIDE pushop term','term',5,'p_term','lexPar.py',453),
  ('fact -> LPAREN pushop expres RPAREN popop','fact',5,'p_fact','lexPar.py',458),
  ('fact -> var_cte','fact',1,'p_fact','lexPar.py',459),
  ('fact -> PLUS pushop var_cte','fact',3,'p_fact','lexPar.py',460),
  ('fact -> MINUS pushop var_cte','fact',3,'p_fact','lexPar.py',461),
  ('rel -> LOWERTHAN','rel',1,'p_rel','lexPar.py',466),
  ('rel -> MORETHAN','rel',1,'p_rel','lexPar.py',467),
  ('rel -> LOWEREQ','rel',1,'p_rel','lexPar.py',468),
  ('rel -> MOREEQ','rel',1,'p_rel','lexPar.py',469),
  ('rel -> SAME','rel',1,'p_rel','lexPar.py',470),
  ('rel -> DIFFERENT','rel',1,'p_rel','lexPar.py',471),
  ('log -> OR','log',1,'p_log','lexPar.py',478),
  ('log -> AND','log',1,'p_log','lexPar.py',479),
  ('var_cte -> ID pushid','var_cte',2,'p_var_cte','lexPar.py',485),
  ('var_cte -> CTE_I pushcte','var_cte',2,'p_var_cte','lexPar.py',486),
  ('var_cte -> CTE_F pushcte','var_cte',2,'p_var_cte','lexPar.py',487),
  ('var_cte -> CTE_S pushcte','var_cte',2,'p_var_cte','lexPar.py',488),
  ('var_cte -> TRUE pushcte','var_cte',2,'p_var_cte','lexPar.py',489),
  ('var_cte -> FALSE pushcte','var_cte',2,'p_var_cte','lexPar.py',490),
  ('var_cte -> asigvector','var_cte',1,'p_var_cte','lexPar.py',491),
  ('findvec -> FIND pushop LPAREN ID LBRACE ex RBRACE RPAREN SEMICOLON','findvec',9,'p_findvec','lexPar.py',495),
  ('sorti -> SORT pushop LPAREN ID LBRACE RBRACE RPAREN SEMICOLON','sorti',8,'p_sorti','lexPar.py',500),
  ('asigvector -> ID pushid LBRACE ex RBRACE','asigvector',5,'p_asigvector','lexPar.py',506),
  ('fcall -> ID existfunc LPAREN startera fcall1 RPAREN','fcall',6,'p_fcall','lexPar.py',511),
  ('fcall -> ID existfunc LPAREN startera RPAREN','fcall',5,'p_fcall','lexPar.py',512),
  ('fcallvoid -> ID existfunc LPAREN startera fcall1 RPAREN SEMICOLON','fcallvoid',7,'p_fcallvoid','lexPar.py',523),
  ('fcallvoid -> ID existfunc LPAREN startera RPAREN SEMICOLON','fcallvoid',6,'p_fcallvoid','lexPar.py',524),
  ('existfunc -> <empty>','existfunc',0,'p_existfunc','lexPar.py',533),
  ('startera -> <empty>','startera',0,'p_startera','lexPar.py',542),
  ('fcall1 -> expres generateparam','fcall1',2,'p_fcall1','lexPar.py',547),
  ('fcall1 -> expres generateparam COMA fcall1','fcall1',4,'p_fcall1','lexPar.py',548),
  ('generateparam -> <empty>','generateparam',0,'p_generateparam','lexPar.py',557),
  ('empty -> <empty>','empty',0,'p_empty','lexPar.py',565),
  ('pushcte -> <empty>','pushcte',0,'p_pushcte','lexPar.py',576),
  ('pushid -> <empty>','pushid',0,'p_pushid','lexPar.py',580),
  ('pushop -> <empty>','pushop',0,'p_pushop','lexPar.py',584),
  ('popop -> <empty>','popop',0,'p_popop','lexPar.py',588),
  ('resolverasignacion -> <empty>','resolverasignacion',0,'p_resolverasignacion','lexPar.py',592),
  ('resasignvec -> <empty>','resasignvec',0,'p_resasignvec','lexPar.py',604),
  ('resfact -> <empty>','resfact',0,'p_resfact','lexPar.py',617),
  ('resterm -> <empty>','resterm',0,'p_resterm','lexPar.py',621),
  ('resrel -> <empty>','resrel',0,'p_resrel','lexPar.py',625),
  ('resif -> <empty>','resif',0,'p_resif','lexPar.py',629),
  ('reselse -> <empty>','reselse',0,'p_reselse','lexPar.py',633),
  ('finif -> <empty>','finif',0,'p_finif','lexPar.py',637),
  ('while1 -> <empty>','while1',0,'p_while1','lexPar.py',641),
  ('while2 -> <empty>','while2',0,'p_while2','lexPar.py',645),
  ('while3 -> <empty>','while3',0,'p_while3','lexPar.py',649),
]
