
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '5ABB8A4C7D2D864520E381848D2EB6B4'
    
_lr_action_items = {',':([6,7,9,10,11,14,],[-4,-5,12,-6,-8,-7,]),'{':([13,],[16,]),'RETURN':([16,18,19,21,23,],[17,-11,17,-12,-13,]),'$end':([1,3,15,22,],[-1,0,-2,-9,]),'(':([5,6,],[7,-4,]),';':([6,20,],[-4,23,]),'IDENT':([0,2,4,7,8,12,17,],[4,6,-3,4,6,4,6,]),'}':([16,18,19,21,23,],[-10,-11,22,-12,-13,]),')':([6,7,9,10,11,14,],[-4,-5,13,-6,-8,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'func_decl':([0,],[1,]),'type':([0,7,12,],[2,8,8,]),'ident':([2,8,17,],[5,11,20,]),'statements':([16,],[19,]),'statement':([16,19,],[18,21,]),'block':([13,],[15,]),'program':([0,],[3,]),'func_args':([7,],[9,]),'func_arg_decl':([7,12,],[10,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> func_decl','program',1,'p_program','parser.py',12),
  ('func_decl -> type ident ( func_args ) block','func_decl',6,'p_function_declaration','parser.py',17),
  ('type -> IDENT','type',1,'p_type','parser.py',22),
  ('ident -> IDENT','ident',1,'p_ident','parser.py',27),
  ('func_args -> <empty>','func_args',0,'p_func_args','parser.py',31),
  ('func_args -> func_arg_decl','func_args',1,'p_func_args','parser.py',32),
  ('func_args -> func_args , func_arg_decl','func_args',3,'p_func_args','parser.py',33),
  ('func_arg_decl -> type ident','func_arg_decl',2,'p_func_arg_decl','parser.py',43),
  ('block -> { statements }','block',3,'p_block','parser.py',47),
  ('statements -> <empty>','statements',0,'p_statements','parser.py',50),
  ('statements -> statement','statements',1,'p_statements','parser.py',51),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',52),
  ('statement -> RETURN ident ;','statement',3,'p_return_statement','parser.py',55),
  ('return -> RETURN','return',1,'p_return','parser.py',58),
]
