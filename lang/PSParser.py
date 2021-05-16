from sly import Parser
from lang.PSLexer import PSLexer

import lang.PSFunctions as psf

class PSParser(Parser):

  tokens = PSLexer.tokens

  precedence = (
    ('left' ,PRINT ,SAVE  ,SELECT, FROM, PLOT),  # FUNCTIONS
    ('left' ,LOAD  ,MEAN  ,MEDIAN, STD , CUT ),  # FUNCTIONS
    ('left' ,PLUS  ,MINUS ,),                    # OPERATIONS
    ('left' ,TIMES ,DIVIDE,),                    # HIGH PRIORITY OPERATIONS
    ('right',UMINUS,),                           # UNARY OPERATORS
  )

  def __init__(self):
    self.ids = {}

  @_('PRINT expr')
  def statement(self, p):
    return print(p.expr)

  @_('SAVE ID STRING')
  def statement(self, p):
    psf.save(p.ID, p.STRING)

  @_('ID ASSIGN expr')
  def statement(self, p):
    self.ids[p.ID] = p.expr

  @_('expr')
  def statement(self, p):
    pass

  @_('expr PLUS expr')
  def expr(self, p):
    return p.expr0 + p.expr1

  @_('expr MINUS expr')
  def expr(self, p):
    return p.expr0 - p.expr1

  @_('expr TIMES expr')
  def expr(self, p):
    return p.expr0 * p.expr1

  @_('expr DIVIDE expr')
  def expr(self, p):
    return p.expr0 / p.expr1

  @_('MINUS expr %prec UMINUS')
  def expr(self, p):
    return -p.expr

  @_('LPAREN expr RPAREN')
  def expr(self, p):
    return p.expr

  @_('FLOAT')
  def expr(self, p):
    return float(p.FLOAT)

  @_('INTEGER')
  def expr(self, p):
    return int(p.INTEGER)

  @_('STRING')
  def expr(self, p):
    return str(p.STRING)

  @_('ID')
  def expr(self, p):
    try:
      return self.ids[p.ID]
    except LookupError:
      print(f'Undefined name {p.ID!r}')

  @_('COLUMNS ID')
  def expr(self, p):
    return psf.columns(self.ids[p.ID])

  @_('select')
  def expr(self, p):
    return p.select

  @_('SELECT STRING STRING FROM expr')
  def select(self, p):
    return (psf.select_from(p.STRING0, p.STRING1, p.expr))

  @_('SELECT STRING FROM expr')
  def select(self, p):
    return (psf.select_from(p.STRING, None, p.expr))

  @_('SELECT FROM expr')
  def select(self, p):
    return (psf.select_from(None, None, p.expr))

  @_('LOAD STRING')
  def expr(self, p):
    return psf.load(p.STRING)
  
  @_('CUT INTEGER INTEGER ID')
  def expr(self, p):
    return psf.cut(p.INTEGER0, p.INTEGER1, self.ids[p.ID])

  @_('CUT INTEGER INTEGER ID INTEGER')
  def expr(self, p):
    return psf.cut(p.INTEGER0, p.INTEGER1, self.ids[p.ID], p.INTEGER2)

  @_('PLOT ID STRING')
  def expr(self, p):
    psf.plot(self.ids[p.ID], p.STRING)
    return 0

  @_('MEAN expr')
  def expr(self, p):
    return psf.mean(p.expr)

  @_('MEDIAN expr')
  def expr(self, p):
    return psf.median(p.expr)

  @_('STD expr')
  def expr(self, p):
    return psf.std(p.expr)