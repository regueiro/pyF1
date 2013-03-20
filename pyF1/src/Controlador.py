#!/usr/bin/python2.5
# -*- coding: utf-8
import gtk
from model import Facade


Facade.establecer_directorio_bd("db")


class ConsultarResultados:
    
    def __init__(self):
        self.actualizar_datos()
        self.__listview_gp_parrilla = gtk.ListStore(int, str)
        self.__listview_gp_carrera = gtk.ListStore(int, str)
        self.__listview_temporada_pilotos = gtk.ListStore(int, str, int)
        self.__listview_temporada_equipos = gtk.ListStore(int, str, int)
        self.__listview_carreras_temporada = gtk.ListStore(str,str,str)

    def actualizar_datos(self):
        self.__temporadas = Facade.obtener_lista_temporadas()
        self.__temporadas.sort()
        self.__numero_temporadas = -1
        self.__lista_temps = []
        for t in self.__temporadas:
            self.__lista_temps.append(Facade.obtener_temporada(t))
            self.__numero_temporadas = self.__numero_temporadas + 1
        self.__lista_temps.sort(key=lambda nombre: nombre.obtener_datos()["nombre"])
        self.set_temporada_activa(self.__numero_temporadas)
        self.__gp_activo = -1
    
    def set_temporada_activa(self, indice):
        if indice >= 0:
            self.__temporada_activa = self.__lista_temps[indice]
        else:
            self.__temporada_activa = None
    
    def set_gp_activo(self, indice):
        self.__gp_activo = indice
    
    
    
    def rellenar_combobox_lista_temporadas(self, combobox):
        liststore = gtk.ListStore(str)
        
        for t in self.__lista_temps:
            liststore.append([t.obtener_datos()["nombre"]])
        
        combobox.set_model(liststore)
        combobox.set_active(self.__numero_temporadas)
    
    
    
    def rellenar_combobox_resultados_selector(self, combobox):
        liststore = gtk.ListStore(str)
        
        liststore.append([_("Drivers' Championship")])
        liststore.append([_("Teams' Championship")])
        liststore.append([_("Race Results")])
        liststore.append([_("Season Calendar")])
        
        combobox.set_model(liststore)
        if self.__temporada_activa != None:
            combobox.set_active(0)
            combobox.set_sensitive(True)
    
    
    
    def rellenar_combobox_resultados_grandes_premios(self, combobox):
        liststore = gtk.ListStore(str)
        if self.__temporada_activa != None:
            gps = self.__temporada_activa.obtener_lista_GPs()
        else:
            gps = []
        for g in gps:
            liststore.append([g.obtener_datos()["nombre"]])
        
        combobox.set_model(liststore)
        combobox.set_active(0)
    
    
    
    def rellenar_etiqueta_datos_mostrados(self, etiqueta, mostrar):
        if self.__temporada_activa != None:
            if self.__gp_activo >= 0:
                etiqueta.set_text(self.__temporada_activa.obtener_datos()["nombre"] + ": "
                                  + self.__temporada_activa.obtener_lista_GPs()[self.__gp_activo].obtener_datos()["nombre"])
            elif mostrar == "pilotos":
                etiqueta.set_text(self.__temporada_activa.obtener_datos()["nombre"]
                                  + _(": Drivers' Championship results"))
            elif mostrar == "equipos":
                etiqueta.set_text(self.__temporada_activa.obtener_datos()["nombre"]
                                  + _(": Teams' Championship results"))
            elif mostrar == "carreras":
                etiqueta.set_text(self.__temporada_activa.obtener_datos()["nombre"]
                                  + _(": Race calendar"))
        else:
            etiqueta.set_text(_("There aren't any seasons stored in the database yet"))
    
    
    
    def crear_listview_gp_parrilla(self, list):
        modelo = list.get_model()
        if not modelo:
            list.set_model(self.__listview_gp_parrilla)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Position"), render, text=0)
            list.append_column(col)
            
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Driver"), render, text=1)
            list.append_column(col)
            
            #set the selection option so that only one row can be selected
            sel = list.get_selection()
            sel.set_mode(gtk.SELECTION_SINGLE)
    
    
    
    def crear_listview_gp_carrera(self, list):
        modelo = list.get_model()
        if not modelo:
            list.set_model(self.__listview_gp_carrera)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Position"), render, text=0)
            list.append_column(col)
            
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Driver"), render, text=1)
            list.append_column(col)
            
            #set the selection option so that only one row can be selected
            sel = list.get_selection()
            sel.set_mode(gtk.SELECTION_SINGLE)
    
    
    
    def crear_listview_temporada_pilotos(self, list):
        modelo = list.get_model()
        if not modelo:
            list.set_model(self.__listview_temporada_pilotos)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Position"), render, text=0)
            list.append_column(col)
            
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Driver"), render, text=1)
            list.append_column(col)
            
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Points"), render, text=2)
            list.append_column(col)
            
            #set the selection option so that only one row can be selected
            sel = list.get_selection()
            sel.set_mode(gtk.SELECTION_SINGLE)
    
    def crear_listview_temporada_equipos(self, list):
        modelo = list.get_model()
        if not modelo:
            list.set_model(self.__listview_temporada_equipos)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Position"), render, text=0)
            list.append_column(col)
            
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Team"), render, text=1)
            list.append_column(col)
            
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Points"), render, text=2)
            list.append_column(col)
            
            #set the selection option so that only one row can be selected
            sel = list.get_selection()
            sel.set_mode(gtk.SELECTION_SINGLE)

    def crear_listview_carreras_temporada(self, list):
        modelo = list.get_model()
        if not modelo:
            list.set_model(self.__listview_carreras_temporada)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Race"), render, text=0)
            list.append_column(col)

            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Starting Date"), render, text=1)
            list.append_column(col)

            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Ending Date"), render, text=2)
            list.append_column(col)

            #set the selection option so that only one row can be selected
            sel = list.get_selection()
            sel.set_mode(gtk.SELECTION_SINGLE)

    def rellenar_listview_gp_parrilla(self, list, tempgp):
        try:
            gp = self.__temporada_activa.obtener_lista_GPs()[tempgp]
        except:
            gp = None
            
        self.__listview_gp_parrilla.clear()
        
        if gp != None:
            if gp.ha_comenzado():
                pilotos = gp.obtener_parrilla()
                i = 1
                for p in pilotos:
                    self.__listview_gp_parrilla.append([i, p.obtener_datos()["nombre"]])
                    i = i + 1
        list.set_model(self.__listview_gp_parrilla)
    
    
    
    def rellenar_listview_gp_carrera(self, list, tempgp):
        try:
            gp = self.__temporada_activa.obtener_lista_GPs()[tempgp]
        except:
            gp = None

        self.__listview_gp_carrera.clear()

        if gp != None:
            if gp.ha_finalizado():
                pilotos = gp.obtener_resultado()
                i = 1
                for p in pilotos:
                    self.__listview_gp_carrera.append([i, p.obtener_datos()["nombre"]])
                    i = i + 1
        list.set_model(self.__listview_gp_carrera)
    
    
    
    def rellenar_listview_temporada_pilotos(self, list):
        if self.__temporada_activa != None:
            pilotos = self.__temporada_activa.obtener_lista_pilotos()
        else:
            pilotos = []
        self.__listview_temporada_pilotos.clear()
        
        lista = []
        for p in pilotos:
            lista.append((self.__temporada_activa.puntos_piloto(p), p.obtener_datos()["nombre"]))
        lista.sort(key=lambda puntos: -puntos[0])
        
        i = 0
        for p in lista:
            self.__listview_temporada_pilotos.append([i + 1, lista[i][1], lista[i][0]])
            i = i + 1
        list.set_model(self.__listview_temporada_pilotos)
    
    
    
    def rellenar_listview_temporada_equipos(self, list):
        if self.__temporada_activa != None:
            equipos = self.__temporada_activa.obtener_lista_equipos()
        else:
            equipos = []
        self.__listview_temporada_equipos.clear()
        
        lista = []
        for e in equipos:
            lista.append((self.__temporada_activa.puntos_equipo(e), e.obtener_datos()["nombre"]))
        lista.sort(key=lambda puntos: -puntos[0])
        
        i = 0
        for p in lista:
            self.__listview_temporada_equipos.append([i + 1, lista[i][1], lista[i][0]])
            i = i + 1
        list.set_model(self.__listview_temporada_equipos)

    def rellenar_listview_carreras_temporada(self, list):
        gps = self.__temporada_activa.obtener_lista_GPs()

        self.__listview_carreras_temporada.clear()
        gps.sort(key=lambda fecha: fecha.obtener_datos()["inicio"])
        for g in gps:
            self.__listview_carreras_temporada.append([g.obtener_datos()["nombre"],g.obtener_datos()["inicio"].strftime("%x"),g.obtener_datos()["fin"].strftime("%x")])

        list.set_model(self.__listview_carreras_temporada)

class IntroducirResultados:
    
    def __init__(self):
        self.__listview_gp_parrilla = gtk.ListStore(int, str)
        self.__listview_gp_carrera = gtk.ListStore(int, str)
        self.__tabla = None
        self.__editando = ""

    def hay_gps_por_editar(self):
        valido = False
        for t in self.__lista_gps_validos_temp:
            if len(t) > 0:
                valido = True
        return valido

    def actualizar_datos(self):
        self.__temporadas = Facade.obtener_lista_temporadas()
        self.__temporadas.sort()
        self.__lista_temps = []
        self.__lista_temp_validas = []
        self.__lista_gps_validos_temp = []
        temporada_valida = False
        pos_temp = 0
        for t in self.__temporadas:
            self.__lista_gps_validos_temp.append({})
            pos_general = 0
            pos_gp = 0
            temporada = Facade.obtener_temporada(t)
            self.__lista_temps.append(temporada)
            gps_temporada = temporada.obtener_lista_GPs()
            for gp in gps_temporada:
                if ((not gp.ha_comenzado()) or (not gp.ha_finalizado())):
                    temporada_valida = True
                    self.__lista_gps_validos_temp[pos_temp][pos_gp] = pos_general
                    pos_gp = pos_gp + 1
                    

                pos_general = pos_general + 1
            if temporada_valida:
                self.__lista_temp_validas.append(pos_temp)
            temporada_valida = False
            pos_temp = pos_temp + 1
            
        self.set_temporada_activa(pos_temp-1)
        self.__gp_activo = -1
        self.__listview_gp_parrilla = gtk.ListStore(int, str)
        self.__listview_gp_carrera = gtk.ListStore(int, str)
    
    def crear_listview_gp_parrilla(self, list):
        list.set_model(self.__listview_gp_parrilla)
        render = gtk.CellRendererText()
        col = gtk.TreeViewColumn(_("Position"), render, text=0)
        list.append_column(col)
        render = gtk.CellRendererText()
        col = gtk.TreeViewColumn(_("Driver"), render, text=1)
        list.append_column(col)
        
        #set the selection option so that only one row can be selected
        sel = list.get_selection()
        sel.set_mode(gtk.SELECTION_SINGLE)
    
    
    
    def crear_listview_gp_carrera(self, list):
        list.set_model(self.__listview_gp_carrera)
        render = gtk.CellRendererText()
        col = gtk.TreeViewColumn(_("Position"), render, text=0)
        list.append_column(col)
        
        render = gtk.CellRendererText()
        col = gtk.TreeViewColumn(_("Driver"), render, text=1)
        list.append_column(col)
        
        #set the selection option so that only one row can be selected
        sel = list.get_selection()
        sel.set_mode(gtk.SELECTION_SINGLE)
    
    
    
    def set_temporada_activa(self, indice):
        self.__temporada_activa = indice
    
    def get_temporada_activa(self):
        return self.__lista_temps[self.__lista_temp_validas[self.__temporada_activa]]
    
    def __obtener_gp_activo(self):
        return self.get_temporada_activa().obtener_lista_GPs()[self.__lista_gps_validos_temp[self.__lista_temp_validas[self.__temporada_activa]][self.__gp_activo]]
    
    def __obtener_gp_valido(self, indice):
        return self.get_temporada_activa().obtener_lista_GPs()[self.__lista_gps_validos_temp[indice]]
        
    def set_gp_activo(self, indice):
        self.__gp_activo = indice
        gp = self.__obtener_gp_activo()
        if gp.ha_comenzado():
            self.__editando = "carrera"
        else:
            self.__editando = "clasificacion"
    
    
    def rellenar_combobox_lista_temporadas(self, combobox):
        liststore = gtk.ListStore(str)
        for t in self.__lista_temp_validas:
            liststore.append([self.__lista_temps[t].obtener_datos()["nombre"]])
        combobox.set_model(liststore)
        combobox.set_active(len(self.__lista_temp_validas)-1)
        self.set_temporada_activa(len(self.__lista_temp_validas)-1)
    
    
    
    def rellenar_combobox_grandes_premios(self, combobox):
        liststore = gtk.ListStore(str)
        gps = self.get_temporada_activa().obtener_lista_GPs()
        for gp in gps:
            if gp.ha_comenzado() == False or gp.ha_finalizado() == False:
                liststore.append([gp.obtener_datos()["nombre"]])
        combobox.set_model(liststore)
        combobox.set_active(0)
        self.set_gp_activo(0)
    
    
    
    def rellenar_lista_pilotos(self, scrolledwindow):
        if self.__tabla:
            self.__tabla.destroy()
        if self.__editando == "clasificacion":
            pilotos = self.get_temporada_activa().obtener_lista_pilotos()
        else:
            pilotos = self.__obtener_gp_activo().obtener_parrilla()
        numero_participantes = len(pilotos)

        self.__tabla = ""
        self.__tabla = gtk.Table(numero_participantes + 1, 2, False)
        scrolledwindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scrolledwindow.add_with_viewport(self.__tabla)
        widget_posicion = []
        self.__widget_piloto = []
        etiqueta_posicion = gtk.Label(_("Position"))
        etiqueta_piloto = gtk.Label(_("Driver"))
        self.__tabla.attach(etiqueta_posicion, 0, 1, 0, 1, False, False, 100, 10)
        self.__tabla.attach(etiqueta_piloto, 1, 2, 0, 1, False, False, -1, 10)
        etiqueta_piloto.show()
        etiqueta_posicion.show()
        for i in range(0, numero_participantes):
            widget_posicion.append(gtk.Label(str(i + 1) + "º"))
            self.__tabla.attach(widget_posicion[i], 0, 1, i + 1, i + 2, False, False, 100)
            widget_posicion[i].show()
        self.__pilotos_disponibles = []
        for p in pilotos:
            self.__pilotos_disponibles.append(p.obtener_datos()["nombre"])
        
        self.__pilotos_disponibles.sort()
        
        for i in range(0, numero_participantes):
            self.__widget_piloto.append([gtk.combo_box_new_text(), "--", 0])
            self.__widget_piloto[i][0].append_text("--")
            for p in self.__pilotos_disponibles:
                self.__widget_piloto[i][0].append_text(p)
            
            self.__tabla.attach(self.__widget_piloto[i][0], 1, 2, i + 1, i + 2, gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL, 10)
            self.__widget_piloto[i][0].set_active(0)
            self.__widget_piloto[i][0].show()
            self.__widget_piloto[i][2] = self.__widget_piloto[i][0].connect('changed', self.on_checkbox_pilotos_changed)
            self.__widget_piloto[i][0].connect('focus', self.on_widget_piloto_focus, scrolledwindow, i)
            
        self.__tabla.show()
    
    
    
    def rellenar_lista_pilotos_c(self, scrolledwindow):
        if self.__tabla_c:
            self.__tabla_c.destroy()
        
        numero_participantes = self.__temporada_activa.obtener_datos()["n_pilotos_gp"]
        self.__tabla_c = gtk.Table(numero_participantes + 1, 2, False)
        scrolledwindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scrolledwindow.add_with_viewport(self.__tabla_c)
        widget_posicion = []
        self.__widget_piloto = []
        etiqueta_posicion = gtk.Label(_("Position"))
        etiqueta_piloto = gtk.Label(_("Driver"))
        self.__tabla_c.attach(etiqueta_posicion, 0, 1, 0, 1, False, False, 100, 10)
        self.__tabla_c.attach(etiqueta_piloto, 1, 2, 0, 1, False, False)
        etiqueta_piloto.show()
        etiqueta_posicion.show()
        for i in range(0, numero_participantes):
            widget_posicion.append(gtk.Label(str(i + 1) + "º"))
            self.__tabla_c.attach(widget_posicion[i], 0, 1, i + 1, i + 2, False, False, 100)
            widget_posicion[i].show()
        
        pilotos = self.__temporada_activa.obtener_lista_pilotos()
        self.__pilotos_disponibles = []
        for p in pilotos:
            self.__pilotos_disponibles.append(p.obtener_datos()["nombre"])
        
        self.__pilotos_disponibles.sort()
        
        for i in range(0, numero_participantes):
            self.__widget_piloto.append([gtk.combo_box_new_text(), "--", 0])
            self.__widget_piloto[i][0].append_text("--")
            for p in self.__pilotos_disponibles:
                self.__widget_piloto[i][0].append_text(p)
            
            self.__tabla_c.attach(self.__widget_piloto[i][0], 1, 2, i + 1, i + 2)
            self.__widget_piloto[i][0].show()
            self.__widget_piloto[i][0].set_active(0)
            self.__widget_piloto[i][2] = self.__widget_piloto[i][0].connect('changed', self.on_checkbox_pilotos_changed)
            self.__widget_piloto[i][0].connect('focus', self.on_widget_piloto_focus, scrolledwindow, i)

        self.__tabla_c.show()

    
    
    
    def on_widget_piloto_focus(self, widget, data, scrolledwindow, posicion):
        vadjustment = gtk.Adjustment(posicion, posicion * widget.size_request()[1], posicion + 2, posicion + 3, posicion + 4, posicion + 5)
        adj = scrolledwindow.get_vadjustment()
        scrolledwindow.set_vadjustment(vadjustment)
    
    
    
    def on_checkbox_pilotos_changed(self, widget):
        for i in self.__widget_piloto:
            i[0].handler_block(i[2]) #bloqueamos la señal changed para evitar llamadas recursivas
        
        wid_act = []
        piloto_selec = widget.get_active_text() # guadamos el piloto que se ha seleccionado
        for i in self.__widget_piloto: # buscamos el widget que ha cambiado en nuestra lista
            if i[0] == widget:
                wid_act = i
                piloto_anterior = i[1] # guardamos el piloto que tenia antes de cambiar
        
        if piloto_selec != "--" and piloto_selec != None: # Si se ha seleccionado un piloto y no --, lo quitamos de la lista de disponibles
            for p in self.__pilotos_disponibles:
                if p == piloto_selec:
                    self.__pilotos_disponibles.remove(p)
        if piloto_anterior != "--": # Si tenia un piloto seleccionado antes de cambiar, lo añadimos a la lista de disponibles
            self.__pilotos_disponibles.append(piloto_anterior)
            self.__pilotos_disponibles.sort()
        
        wid_act[1] = piloto_selec # Actualizamos el campo piloto_seleccionado de la lista de widgets para el widget que cambio
        
        for i in self.__widget_piloto: # para cada widget
            posicion = 0
            activo = i[0].get_active_text() # guardamos el texto activo
            if i[0] != widget: # si no es el widget que ha cambiado
                if activo != "--": # si tenia un piloto activo, lo añadimos a la lista de disponibles
                    self.__pilotos_disponibles.append(activo)
                    self.__pilotos_disponibles.sort()
                
                modelo = i[0].get_model() # buscamos el modelo
                modelo.clear() # lo vaciamos
                i[0].append_text("--") # añadimos la seleccion vacía
                if "--" == activo: # si estaba activo --, lo activamos
                    i[0].set_active(0)
                for p in self.__pilotos_disponibles: # añadimos todos los pilotos disponibles
                    posicion = posicion + 1
                    i[0].append_text(p)
                    if p == activo: # y activamos el que ya estaba
                        i[0].set_active(posicion)
                if activo != "--": # si habíamos añadido un piloto a la lista por estar activo en el combobox, lo eliminamos para que no se añada al resto de widgets
                    self.__pilotos_disponibles.remove(activo)
        for i in self.__widget_piloto: # reconectamos las señales
            i[0].handler_unblock(i[2])
    
    
    
    def comprobar_checkboxes_pilotos(self):
        minimo = 5
        finalizado = False
        correcto = True
        continuar = False
        gp = self.__obtener_gp_activo()
        if gp.ha_comenzado():
            numero_participantes = len(gp.obtener_parrilla())
        else:
            numero_participantes = self.get_temporada_activa().obtener_datos()["n_pilotos_gp"]
        
        for w in self.__widget_piloto:
            numero_participantes = numero_participantes -1
            if not finalizado:
                if w[0].get_active_text() == "--":
                    finalizado = True
                else:
                    minimo = minimo - 1
            elif w[0].get_active_text() != "--":
                correcto = False

        if numero_participantes == 0:
            finalizado = True

        continuar = finalizado and correcto and minimo <= 0
        return continuar
    
    
    
    def guardar_resultados(self, numero_vueltas, ventana_correcto):
        pilotos = self.get_temporada_activa().obtener_lista_pilotos()
        pilotos_ordenados = []
        for w in self.__widget_piloto:
            nombre_piloto = w[0].get_active_text()
            for p in pilotos:
                if p.obtener_datos()["nombre"] == nombre_piloto:
                    pilotos_ordenados.append(p)
        if self.__editando == "clasificacion":
            self.__obtener_gp_activo().establecer_parrilla(pilotos_ordenados)
        elif self.__editando == "carrera":
            self.__obtener_gp_activo().establecer_resultado(pilotos_ordenados, numero_vueltas)
        
        Facade.almacenar_temporada(self.get_temporada_activa())
        ventana_correcto.run()
    
    
    
    def tipo_activo(self):
        return self.__editando
    
    
    
    def definir_maximo_vueltas(self, widget):
        
        numero_vueltas = self.__obtener_gp_activo().obtener_datos()["n_vueltas_gp"]
        adjustment = gtk.Adjustment(numero_vueltas, 0, numero_vueltas, 1, 10, 0)
        widget.set_adjustment(adjustment)
        widget.set_value(numero_vueltas)


class MantenimientoTemporada:

    def __init__(self):
        self.actualizar_datos()
        
        self.__listview_temporadas = gtk.ListStore(str)
        self.__listview_equipos = gtk.ListStore(str)
        self.__listview_pilotos = gtk.ListStore(str)
        self.__listview_gps = gtk.ListStore(str)
        self.__listview_reglas = gtk.ListStore(str, int)
        self.__fecha_inicio = None
        self.__fecha_fin = None
        self.__num_reglas = 0
        self.__reglas = []
        self.__reglas_temporada_sin_guardar = []

    def actualizar_datos(self):
        temp = Facade.obtener_lista_temporadas()

        self.__temporadas = []
        self.__equipos = []
        self.__pilotos = []
        self.__gps = []
        self.__reglas = []
        self.__reglas_temporada_sin_guardar = []
        if temp != []:
            for t in temp:
                temporada = Facade.obtener_temporada(t)
                self.__temporadas.append(temporada)
            self.__temporadas.sort(key=lambda nombre: nombre.obtener_datos()["nombre"])
        self.__temporada_seleccionada = ""
        self.__fecha_inicio = None
        self.__fecha_fin = None

    def crear_listview_temporadas(self, list):
        modelo = list.get_model()
        if not modelo:
            list.set_model(self.__listview_temporadas)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Season Name"), render, text=0)
            list.append_column(col)

            #set the selection option so that only one row can be selected
            sel = list.get_selection()
            sel.set_mode(gtk.SELECTION_SINGLE)

    def rellenar_listview_temporadas(self, list):
        self.__listview_temporadas.clear()

        for t in self.__temporadas:
            self.__listview_temporadas.append([t.obtener_datos()["nombre"]])
        list.set_model(self.__listview_temporadas)

    def crear_listview_equipos(self, list):
        modelo = list.get_model()
        if not modelo:
            list.set_model(self.__listview_equipos)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Team"), render, text=0)
            list.append_column(col)

            #set the selection option so that only one row can be selected
            sel = list.get_selection()
            sel.set_mode(gtk.SELECTION_SINGLE)

    def rellenar_listview_equipos(self, list):
        self.__listview_equipos.clear()

        for t in self.__equipos:
            self.__listview_equipos.append([t.obtener_datos()["nombre"]])
        list.set_model(self.__listview_equipos)

    def crear_listview_pilotos(self, list):
        modelo = list.get_model()
        if not modelo:
            list.set_model(self.__listview_pilotos)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Driver"), render, text=0)
            list.append_column(col)

            #set the selection option so that only one row can be selected
            sel = list.get_selection()
            sel.set_mode(gtk.SELECTION_SINGLE)

    def rellenar_listview_pilotos(self, list):
        self.__listview_pilotos.clear()

        for t in self.__pilotos:
            self.__listview_pilotos.append([t.obtener_datos()["nombre"]])
        list.set_model(self.__listview_pilotos)

    def crear_listview_gps(self, list):
        modelo = list.get_model()
        if not modelo:
            list.set_model(self.__listview_gps)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Grand Prix"), render, text=0)
            list.append_column(col)

            #set the selection option so that only one row can be selected
            sel = list.get_selection()
            sel.set_mode(gtk.SELECTION_SINGLE)

    def rellenar_listview_gps(self, list):
        self.__listview_gps.clear()

        for g in self.__gps:
            self.__listview_gps.append([g.obtener_datos()["nombre"]])
        list.set_model(self.__listview_gps)

    def crear_listview_reglas(self, list):
        modelo = list.get_model()
        if not modelo:
            list.set_model(self.__listview_reglas)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Position"), render, text=0)
            list.append_column(col)
            render = gtk.CellRendererText()
            render.connect('edited', self.__regla_editada_callback, self.__listview_reglas, list)
            render.set_property('editable', True)
            col = gtk.TreeViewColumn(_("Points"), render, text=1)
            list.append_column(col)

        #set the selection option so that only one row can be selected
        sel = list.get_selection()
        sel.set_mode(gtk.SELECTION_SINGLE)

        temporada = self.__obtener_temporada()
        self.__reglas = []
        if temporada:
            puntos = temporada.obtener_datos()["tabla_puntos"]
            if puntos:
                for r in temporada.obtener_datos()["tabla_puntos"]:
                    self.__reglas.append(r)
        elif self.__reglas_temporada_sin_guardar != []:
            self.__reglas = self.__reglas_temporada_sin_guardar

    def rellenar_listview_reglas(self, list):
        
                
        self.__listview_reglas.clear()
        x = 1
        for r in self.__reglas:
            self.__listview_reglas.append([x, r])
            x = x + 1
        list.set_model(self.__listview_reglas)

    def __regla_editada_callback(self, celda, path, nuevo_texto, model, list):
        iter = model.get_iter(path)
        try:
            puntos = int(nuevo_texto)
            if puntos <0:
                puntos = 0
        except:
            puntos = 0
        value = model.get_value(iter, 1)
        if value != puntos:
            model.set_value(iter, 1, puntos)
    
            self.__borrar_regla(value)
            self.__reglas.append(puntos)
            self.__reglas.sort()
            self.__reglas.reverse()

            self.rellenar_listview_reglas(list)
        elif puntos == 0:
            self.rellenar_listview_reglas(list)

    def obtener_seleccionado(self, list):
        sel = list.get_selection()
        (tree, iter) = sel.get_selected()
        if iter != None:
            item = tree.get_value(iter, 0)
            self.__temporada_seleccionada = item
            return item

    def __obtener_temporada(self):
        for t in self.__temporadas:
            if t.obtener_datos()["nombre"] == self.__temporada_seleccionada:
                return t
            
    def validar_nombre_corto(self, nombre_corto):
        return self.__temporadas[0].validar_nombre_corto(nombre_corto)

    def rellenar_datos(self, nombre, nombre_corto, inicio, fin, pilotos_gp, pilotos_parrilla):
        temporada = self.__obtener_temporada()

        nombre.set_text(temporada.obtener_datos()["nombre"])
        nombre_corto.set_text(temporada.obtener_datos()["nombre_corto"])
        fecha_inicio = temporada.obtener_datos()["inicio"]
        if fecha_inicio:
            inicio.set_label(fecha_inicio.strftime("%x"))
        fecha_fin = temporada.obtener_datos()["fin"]
        if fecha_fin:
            fin.set_label(fecha_fin.strftime("%x"))
        pil_gp = temporada.obtener_datos()["n_pilotos_gp"]
        adjustment_gp = gtk.Adjustment(pil_gp, 0, 100, 1, 10, 0)
        pilotos_gp.set_adjustment(adjustment_gp)
        pilotos_gp.set_value(pil_gp)
        pil_parrilla = temporada.obtener_datos()["n_pilotos_parrilla"]
        adjustment_parrilla = gtk.Adjustment(pil_parrilla, 0, 100, 1, 10, 0)
        pilotos_parrilla.set_adjustment(adjustment_parrilla)
        pilotos_parrilla.set_value(pil_parrilla)

        self.__equipos = []
        for e in temporada.obtener_lista_equipos():
            self.__equipos.append(e)
        self.__equipos.sort(key=lambda nombre: nombre.obtener_datos()["nombre"])
        self.__gps = []
        for e in temporada.obtener_lista_GPs():
            self.__gps.append(e)
        self.__gps.sort(key=lambda nombre: nombre.obtener_datos()["inicio"].strftime("%x"))
        self.__pilotos = []
        for e in temporada.obtener_lista_pilotos():
            self.__pilotos.append(e)
        self.__pilotos.sort(key=lambda nombre: nombre.obtener_datos()["nombre"])



    def actualizar_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def actualizar_fecha_fin(self, fecha_fin):
        self.__fecha_fin = fecha_fin

    def borrar_temporada(self):
        temporada = self.__obtener_temporada()
        Facade.eliminar_temporada(temporada)
        self.actualizar_datos()

    def guardar_temporada(self, nombre, nombre_corto, pilotos_gp, pilotos_parrilla):
        temporada_a_actualizar = None
        for t in self.__temporadas:
            if t.obtener_datos()["nombre_corto"] == nombre_corto:
                temporada_a_actualizar = t

        if temporada_a_actualizar != None:
            datos = {}
            if temporada_a_actualizar.obtener_datos()["nombre"] != nombre:
                datos["nombre"] = nombre
            if temporada_a_actualizar.obtener_datos()["nombre_corto"] != nombre_corto:
                datos["nombre_corto"] = nombre_corto
            if (self.__fecha_inicio != None) and (temporada_a_actualizar.obtener_datos()["inicio"] != self.__fecha_inicio):
                datos["inicio"] = self.__fecha_inicio
            if (self.__fecha_fin != None) and (temporada_a_actualizar.obtener_datos()["fin"] != self.__fecha_fin):
                datos["fin"] = self.__fecha_fin
            if temporada_a_actualizar.obtener_datos()["n_pilotos_gp"] != pilotos_gp:
                datos["n_pilotos_gp"] = pilotos_gp
            if temporada_a_actualizar.obtener_datos()["n_pilotos_parrilla"] != pilotos_parrilla:
                datos["n_pilotos_parrilla"] = pilotos_parrilla

            try:
                temporada_a_actualizar.establecer_datos(datos)
                Facade.almacenar_temporada(temporada_a_actualizar)
                self.actualizar_datos()
                return True
            except:
                return False
        else:
            temporada_nueva = Facade.nueva_temporada(nombre, nombre_corto)
            datos = {}
            datos["inicio"] = self.__fecha_inicio
            datos["fin"] = self.__fecha_fin
            datos["n_pilotos_gp"] = pilotos_gp
            datos["n_pilotos_parrilla"] = pilotos_parrilla
            if self.__reglas_temporada_sin_guardar != []:
                datos["tabla_puntos"] = self.__reglas_temporada_sin_guardar
            temporada_nueva.establecer_datos(datos)
            Facade.almacenar_temporada(temporada_nueva)
            self.actualizar_datos()
            return True

    def anadir_fila_reglas(self, list):
        self.__listview_reglas.append(["", 0])
        list.set_model(self.__listview_reglas)
 
        iter = self.__listview_reglas.get_iter_first()


        while self.__listview_reglas.iter_next(iter) != None:
            iter = self.__listview_reglas.iter_next(iter)

        columna = list.get_column(1)
        list.set_cursor(self.__listview_reglas.get_path(iter), columna, True)

    def borrar_fila_reglas(self, list):
        True

        selection = list.get_selection()
        model, iter, = selection.get_selected()
        if iter:
            pos = model.get_value(iter, 1)
        
            path = model.get_path(iter)
            model.remove(iter)
            selection.select_path(path)


            if not selection.path_is_selected(path):
                row = path[0]-1
                if row >= 0:
                    selection.select_path((row,))

            self.__borrar_regla(pos)
            self.__listview_reglas.clear()
            self.rellenar_listview_reglas(list)

    def __borrar_regla(self, puntos):
        for r in self.__reglas:
            if r == puntos:
                self.__reglas.remove(r)
                return True

    def guardar_reglas(self):
        datos = {"tabla_puntos" : self.__reglas}
        temporada = self.__obtener_temporada()
        if temporada:
            try:
                temporada.establecer_datos(datos)
                Facade.almacenar_temporada(temporada)
                return True
            except:
                return False
        else:
            self.__reglas_temporada_sin_guardar = self.__reglas
            return True
        

class MantenimientoGPs:

    def __init__(self):
        self.actualizar_datos()
        self.set_temporada_activa(self.__numero_temporadas)
        self.__listview_gps = gtk.ListStore(str)


        self.__fecha_inicio = None
        self.__fecha_fin = None
        self.__temporada_vacia = True

    def actualizar_datos(self):
        temp = Facade.obtener_lista_temporadas()
        self.__temporadas = []
        self.__numero_temporadas = -1
        self.__gps = []
        for t in temp:
            temporada = Facade.obtener_temporada(t)
            self.__temporadas.append(temporada)
            self.__numero_temporadas = self.__numero_temporadas + 1

        self.__temporadas.sort(key=lambda nombre: nombre.obtener_datos()["nombre"])
        self.__temporada_seleccionada = ""
        
        self.__gp_activo = -1

    def set_temporada_activa(self, indice):
        if indice >= 0:
            self.__temporada_activa = self.__temporadas[indice]
        else:
            self.__temporada_activa = None
        

    def set_gp_activo(self,gp):
        self.__gp_activo = gp

    def rellenar_combobox_lista_temporadas(self, combobox):
        liststore = gtk.ListStore(str)

        for t in self.__temporadas:
            liststore.append([t.obtener_datos()["nombre"]])

        combobox.set_model(liststore)
        combobox.set_active(self.__numero_temporadas)

    def crear_listview_gps(self, list):
        modelo = list.get_model()
        if not modelo:
            list.set_model(self.__listview_gps)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Grand Prix"), render, text=0)
            list.append_column(col)

            #set the selection option so that only one row can be selected
            sel = list.get_selection()
            sel.set_mode(gtk.SELECTION_SINGLE)

    def rellenar_listview_gps(self, list):
        self.__listview_gps.clear()
        self.__gps = self.__temporada_activa.obtener_lista_GPs()

        for g in self.__gps:
            self.__listview_gps.append([g.obtener_datos()["nombre"]])
        list.set_model(self.__listview_gps)
        if len(self.__gps) == 0:
            self.__temporada_vacia = True
        else:
            self.__temporada_vacia = False

    def get_temporada_vacia(self):
        return self.__temporada_vacia
    def rellenar_temporada(self, temporada):
        temporada.set_text(self.__temporada_activa.obtener_datos()["nombre"])
        
    def rellenar_datos(self, temporada, gp, circuito, inicio, fin, vueltas, estado):
        temporada.set_text(self.__temporada_activa.obtener_datos()["nombre"])
        gp.set_text(self.__gp_activo.obtener_datos()["nombre"])
        circuito.set_text(self.__gp_activo.obtener_datos()["lugar"])
        self.__fecha_inicio = self.__gp_activo.obtener_datos()["inicio"]
        inicio.set_label(self.__fecha_inicio.strftime("%x"))
        self.__fecha_fin = self.__gp_activo.obtener_datos()["fin"]
        fin.set_label(self.__fecha_fin.strftime("%x"))
        numero_vueltas = self.__gp_activo.obtener_datos()["n_vueltas_gp"]
        adjustment = gtk.Adjustment(numero_vueltas, 0, 100, 1, 10, 0)
        vueltas.set_adjustment(adjustment)
        vueltas.set_value(numero_vueltas)

        
        if self.__gp_activo.ha_finalizado():
            estado.set_text(_("Finished"))
        elif self.__gp_activo.ha_comenzado():
            estado.set_text(_("Started"))

    def obtener_seleccionado(self, list):
        sel = list.get_selection()
        (tree, iter) = sel.get_selected()
        if iter != None:
            item = tree.get_value(iter, 0)
            self.__obtener_gp_activo(item)
            return item

        
    def __obtener_gp_activo(self, gp):
        for g in self.__gps:
            if g.obtener_datos()["nombre"] == str(gp):
                self.__gp_activo = g
    
    def guardar_gp(self, nombre, circuito, vueltas):
        gp = self.__gp_activo
        if gp != None:
            datos = {}
            if gp.obtener_datos()["nombre"] != nombre:
                datos["nombre"] = nombre
            if gp.obtener_datos()["lugar"] != circuito:
                datos["lugar"] = circuito
            if (self.__fecha_inicio != None) and (gp.obtener_datos()["inicio"] != self.__fecha_inicio):
                datos["inicio"] = self.__fecha_inicio
            if (self.__fecha_fin != None) and (gp.obtener_datos()["fin"] != self.__fecha_fin):
                datos["fin"] = self.__fecha_fin
            if gp.obtener_datos()["n_vueltas_gp"] != vueltas:
                datos["n_vueltas_gp"] = vueltas

            try:
                if datos != {}:
                    gp.establecer_datos(datos)
                    Facade.almacenar_temporada(self.__temporada_activa)
                self.actualizar_datos()
                return (True,False)
            except:
                return (False,False)
        else:
            try:
                gp_nuevo = Facade.nuevo_GP(nombre, circuito,self.__fecha_inicio,self.__fecha_fin,vueltas)
                self.__temporada_activa.anadir_GP(gp_nuevo)
                Facade.almacenar_temporada(self.__temporada_activa)
                self.actualizar_datos()
                return (True,True)
            except:
                return (False,True)


    def actualizar_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def actualizar_fecha_fin(self, fecha_fin):
        self.__fecha_fin = fecha_fin


    def borrar_gp(self):
        gp = self.__gp_activo
        self.__temporada_activa.eliminar_GP(gp)
        Facade.almacenar_temporada(self.__temporada_activa)
        self.actualizar_datos()


class MantenimientoPilotos:

    def __init__(self):
        self.actualizar_datos()
        self.set_temporada_activa(self.__numero_temporadas)
        self.__listview_pilotos = gtk.ListStore(str)
        self.__listview_equipos = gtk.ListStore(str,str)

        self.__equipos_del_piloto = []
        self.__fecha_nacimiento = None
        self.__foto = None
        self.__temporada_vacia = True

    def actualizar_datos(self):
        temp = Facade.obtener_lista_temporadas()
        self.__temporadas = []
        self.__numero_temporadas = -1
        self.__pilotos = []
        for t in temp:
            temporada = Facade.obtener_temporada(t)
            self.__temporadas.append(temporada)
            self.__numero_temporadas = self.__numero_temporadas + 1

        self.__temporadas.sort(key=lambda nombre: nombre.obtener_datos()["nombre"])
        self.__temporada_seleccionada = ""
        
        self.__piloto_activo = -1

    def set_temporada_activa(self, indice):
        if indice >= 0:
            self.__temporada_activa = self.__temporadas[indice]
        else:
            self.__temporada_activa = None

    def rellenar_combobox_lista_temporadas(self, combobox):
        liststore = gtk.ListStore(str)

        for t in self.__temporadas:
            liststore.append([t.obtener_datos()["nombre"]])

        combobox.set_model(liststore)
        combobox.set_active(self.__numero_temporadas)

    def rellenar_datos(self, nombre, nacimiento, foto):
        nombre.set_text(self.__piloto_activo.obtener_datos()["nombre"])
        fecha_nac = self.__piloto_activo.obtener_datos()["nacimiento"]
        if fecha_nac:
            nacimiento.set_label(fecha_nac.strftime("%x"))
            self.__fecha_nacimiento = fecha_nac
        else:
            nacimiento.set_label(_("Select a date"))
        foto_piloto = self.__piloto_activo.obtener_datos()["foto"]
        if foto_piloto:
            foto.set_from_file(foto_piloto)
        else:
            foto.set_from_stock(gtk.STOCK_MISSING_IMAGE,gtk.ICON_SIZE_DIALOG)
        self.__get_equipos_del_piloto()
       


    def obtener_seleccionado(self, list):
        sel = list.get_selection()
        (tree, iter) = sel.get_selected()
        if iter != None:
            item = tree.get_value(iter, 0)
            self.__obtener_piloto_activo(item)
            return item

    def __obtener_piloto_activo(self, piloto):
        for p in self.__pilotos:
            if p.obtener_datos()["nombre"] == piloto:
                self.__piloto_activo = p

    def guardar_piloto(self, nombre):
        piloto = self.__piloto_activo
        if piloto != None:
            datos = {}
            if piloto.obtener_datos()["nombre"] != nombre:
                datos["nombre"] = nombre
            if self.__foto != None and piloto.obtener_datos()["foto"] != self.__foto:
                    datos["foto"] = self.__foto
            if (self.__fecha_nacimiento != None) and (piloto.obtener_datos()["nacimiento"] != self.__fecha_nacimiento):
                datos["nacimiento"] = self.__fecha_nacimiento

            try:
                piloto.establecer_datos(datos)
                Facade.almacenar_temporada(self.__temporada_activa)
                self.actualizar_datos()
                return True
            except:
                return False
        else:
            try:
                piloto_nuevo = Facade.nuevo_piloto(nombre)
                datos = {}
                if self.__foto != None:
                    datos["foto"] = self.__foto
                if self.__fecha_nacimiento != None:
                    datos["nacimiento"] = self.__fecha_nacimiento
                if len(datos)>0:
                    piloto_nuevo.establecer_datos(datos)
                self.__temporada_activa.anadir_piloto(piloto_nuevo)
                Facade.almacenar_temporada(self.__temporada_activa)
                self.actualizar_datos()
                return True
            except:
                return False


    def actualizar_fecha_nacimiento(self, fecha):
        self.__fecha_nacimiento = fecha

    def actualizar_foto(self,foto):
        self.__foto = foto
        
    def borrar_piloto(self):
        piloto = self.__piloto_activo
        self.__temporada_activa.eliminar_piloto(piloto)
        Facade.almacenar_temporada(self.__temporada_activa)
        self.actualizar_datos()

    def crear_listview_pilotos(self, list):
        modelo = list.get_model()
        if not modelo:
            list.set_model(self.__listview_pilotos)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Name"), render, text=0)
            list.append_column(col)

            #set the selection option so that only one row can be selected
            sel = list.get_selection()
            sel.set_mode(gtk.SELECTION_SINGLE)

    def rellenar_listview_pilotos(self, list):
        self.__listview_pilotos.clear()
        self.__pilotos = self.__temporada_activa.obtener_lista_pilotos()

        for p in self.__pilotos:
            self.__listview_pilotos.append([p.obtener_datos()["nombre"]])
        list.set_model(self.__listview_pilotos)
        if len(self.__pilotos) == 0:
            self.__temporada_vacia = True
        else:
            self.__temporada_vacia = False


    def crear_listview_equipos(self, list):
        modelo = list.get_model()
        if not modelo:
            list.set_model(self.__listview_equipos)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Name"), render, text=0)
            list.append_column(col)
            render = gtk.CellRendererText()
            col = gtk.TreeViewColumn(_("Signing Date"), render, text=1)
            list.append_column(col)

            #set the selection option so that only one row can be selected
            sel = list.get_selection()
            sel.set_mode(gtk.SELECTION_SINGLE)

    def rellenar_listview_equipos(self, list):
        self.__listview_equipos.clear()
        self.__get_equipos_del_piloto()
        for e in self.__equipos_del_piloto:
            self.__listview_equipos.append([e[1].obtener_datos()["nombre"],e[0].strftime("%x")])
        list.set_model(self.__listview_equipos)

    def get_temporada_vacia(self):
        return self.__temporada_vacia

    def set_piloto_activo(self,piloto):
        self.__piloto_activo = piloto

    def __get_equipos_del_piloto(self):
        self.__equipos_del_piloto = []
        if self.__piloto_activo != None:
            for e in self.__piloto_activo.obtener_datos()["equipos"]:
                self.__equipos_del_piloto.append(e)
        self.__equipos_del_piloto.sort()
