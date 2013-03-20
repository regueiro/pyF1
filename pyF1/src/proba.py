#!/usr/bin/env python
from ldtp import *
from ldtputils import *

try:
    logMsg = 'See season calendar'
    log (logMsg, 'teststart')
    launchapp ('main.py')
    if waittillguiexist ('*pyF1') == 0:
        raise LdtpExecutionError ('pyF1 window does not exist')
    
    #Na fiestra inicial
    click ('*pyF1', 'btnView results')
    
    #Na fiestra de consulta de resultados
    comboselect ('cboSeason', 'Temporada 2010')
    click ('*pyF1', 'btnApply')
    comboselect ('cboDriver / Team / GP / Calendar', 'Season Calendar')
    click ('*pyF1', 'btnApply')
    
    #Saimos
    selectmenuitem ('*pyF1', 'mnuFile;mnuQuit')
    
except LdtpExecutionError, msg:
    log (msg, 'cause')
    log (logMsg, 'fail')
    log (logMsg, 'testend')
    raise LdtpExecutionError (logMsg)

