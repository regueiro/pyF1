#!/usr/bin/python
# -*- coding: utf-8
import datetime
import gettext

import Controlador
import gtk
import gtk.glade



class PyF1:

    # Definiciones para toda la interfaz
    def on_window_destroy(self, widget, data=None):
        gtk.main_quit()
    
    def on_archivo_salir_activate(self,widget):
        gtk.main_quit()

    def on_ayuda_acerca_activate(self,widget):
        self.__ventana_about.run()

    def on_ventana_about_response(self,widget,response):
        self.__ventana_about.hide()

    def on_resultados_ver_activate(self,widget):
        self.__mostrar_pagina_consultar_resultados()
        self.__paginas.set_current_page(1)

    def on_resultados_editar_activate(self,widget):
        self.__ctrl_introducir_resultados.actualizar_datos()
        if self.__ctrl_introducir_resultados.hay_gps_por_editar():
            self.__mostrar_pagina_introducir_resultados()
            self.__paginas.set_current_page(2)
        else:
            self.__ventana_introducir_resultados_dialogo_no_hay_gps.run()

    def on_editar_temporada_activate(self,widget):
        self.__mostrar_pagina_mantenimiento_temporadas()
        self.__paginas.set_current_page(3)

    def on_editar_equipo_activate(self,widget):
        self.__mostrar_pagina_mantenimiento_equipos()
        self.__paginas.set_current_page(6)

    def on_editar_piloto_activate(self,widget):
        self.__mostrar_pagina_mantenimiento_pilotos()
        self.__paginas.set_current_page(5)

    def on_editar_gp_activate(self,widget):
        self.__mostrar_pagina_mantenimiento_gps()
        self.__paginas.set_current_page(4)




    # Definiciones para la pagina principal
    def on_pagina_principal_boton_consultar_resultados_clicked(self, widget):
        self.__mostrar_pagina_consultar_resultados()
        self.__paginas.set_current_page(1)
    
    def on_pagina_principal_boton_introducir_resultados_clicked(self, widget):
        self.__ctrl_introducir_resultados.actualizar_datos()
        if self.__ctrl_introducir_resultados.hay_gps_por_editar():
            self.__mostrar_pagina_introducir_resultados()
            self.__paginas.set_current_page(2)
        else:
            self.__ventana_introducir_resultados_dialogo_no_hay_gps.run()

    def on_pagina_principal_boton_mantenimiento_temporada_clicked(self, widget):
        self.__mostrar_pagina_mantenimiento_temporadas()
        self.__paginas.set_current_page(3)
    
    def on_pagina_principal_boton_mantenimiento_gp_clicked(self, widget):
        self.__mostrar_pagina_mantenimiento_gps()
        self.__paginas.set_current_page(4)

    def on_pagina_principal_boton_mantenimiento_equipo_clicked(self, widget):
        self.__mostrar_pagina_mantenimiento_equipos()
        self.__paginas.set_current_page(6)

    def on_pagina_principal_boton_mantenimiento_piloto_clicked(self, widget):
        self.__mostrar_pagina_mantenimiento_pilotos()
        self.__paginas.set_current_page(5)



    # Definiciones para la pagina de consultar resultados
    def __mostrar_pagina_consultar_resultados(self):
        self.__ctrl_consultar_resultados.actualizar_datos()
        self.__ctrl_consultar_resultados.rellenar_combobox_lista_temporadas(self.__p_consultar_resultados_combobox_temporada)
        self.__ctrl_consultar_resultados.rellenar_combobox_resultados_selector(self.__p_consultar_resultados_combobox_selector)
        self.__ctrl_consultar_resultados.rellenar_combobox_resultados_grandes_premios(self.__p_consultar_resultados_combobox_gps)
        
        self.__ctrl_consultar_resultados.crear_listview_temporada_equipos(self.__p_consultar_resultados_lista_equipos)
        self.__ctrl_consultar_resultados.crear_listview_temporada_pilotos(self.__p_consultar_resultados_lista_pilotos)
        self.__ctrl_consultar_resultados.crear_listview_gp_parrilla(self.__p_consultar_resultados_lista_gp_parrilla)
        self.__ctrl_consultar_resultados.crear_listview_gp_carrera(self.__p_consultar_resultados_lista_gp_carrera)
        self.__ctrl_consultar_resultados.crear_listview_carreras_temporada(self.__p_consultar_resultados_lista_carreras_temporada)

        self.__ctrl_consultar_resultados.rellenar_listview_temporada_equipos(self.__p_consultar_resultados_lista_equipos)
        self.__ctrl_consultar_resultados.rellenar_listview_temporada_pilotos(self.__p_consultar_resultados_lista_pilotos)
        self.__ctrl_consultar_resultados.rellenar_etiqueta_datos_mostrados(self.__p_consultar_resultados_etiqueta_datos_mostrados, 0)


    
    def on_consultar_resultados_boton_volver_clicked(self, widget):
        self.__paginas.set_current_page(0)
    
    def on_consultar_resultados_combobox_selector_changed(self, widget):
        if self.__p_consultar_resultados_combobox_selector.get_active() == 2:
            self.__p_consultar_resultados_combobox_gps.set_sensitive(True)
        else:
            self.__p_consultar_resultados_combobox_gps.set_sensitive(False)
    
    def on_consultar_resultados_combobox_temporada_changed(self, widget):
        self.__ctrl_consultar_resultados.set_temporada_activa(widget.get_active())
        self.__ctrl_consultar_resultados.rellenar_combobox_resultados_grandes_premios(self.__p_consultar_resultados_combobox_gps)
    
    def __consultar_resultados_cambiar_pagina(self, seleccion):
        if seleccion == 0:
            self.__ctrl_consultar_resultados.set_gp_activo(-1)
            self.__ctrl_consultar_resultados.rellenar_etiqueta_datos_mostrados(self.__p_consultar_resultados_etiqueta_datos_mostrados, "pilotos")
            self.__ctrl_consultar_resultados.rellenar_listview_temporada_pilotos(self.__p_consultar_resultados_lista_pilotos)
            self.__p_consultar_resultados_notebook.set_current_page(0)
        elif seleccion == 1:
            self.__ctrl_consultar_resultados.set_gp_activo(-1)
            self.__ctrl_consultar_resultados.rellenar_etiqueta_datos_mostrados(self.__p_consultar_resultados_etiqueta_datos_mostrados, "equipos")
            self.__ctrl_consultar_resultados.rellenar_listview_temporada_equipos(self.__p_consultar_resultados_lista_equipos)
            self.__p_consultar_resultados_notebook.set_current_page(1)
        elif seleccion == 2:
            gp = self.__p_consultar_resultados_combobox_gps.get_active()
            self.__ctrl_consultar_resultados.set_gp_activo(gp)
            self.__ctrl_consultar_resultados.rellenar_etiqueta_datos_mostrados(self.__p_consultar_resultados_etiqueta_datos_mostrados, -1)
            self.__ctrl_consultar_resultados.rellenar_listview_gp_parrilla(self.__p_consultar_resultados_lista_gp_parrilla, gp)
            self.__ctrl_consultar_resultados.rellenar_listview_gp_carrera(self.__p_consultar_resultados_lista_gp_carrera, gp)
            self.__p_consultar_resultados_notebook.set_current_page(2)
        else:
            self.__ctrl_consultar_resultados.rellenar_etiqueta_datos_mostrados(self.__p_consultar_resultados_etiqueta_datos_mostrados, "carreras")
            self.__ctrl_consultar_resultados.rellenar_listview_carreras_temporada(self.__p_consultar_resultados_lista_carreras_temporada)
            self.__p_consultar_resultados_notebook.set_current_page(3)
            
    
    
    def on_consultar_resultados_boton_mostrar_clicked(self, widget):
        seleccion = self.__p_consultar_resultados_combobox_selector.get_active()
        self.__consultar_resultados_cambiar_pagina(seleccion)

    # Definiciones para la pagina de introducir resultados
    
    def on_introducir_resultados_combobox_temporada_changed(self, widget):
        self.__ctrl_introducir_resultados.set_temporada_activa(widget.get_active())
        self.__ctrl_introducir_resultados.rellenar_combobox_grandes_premios(self.__p_introducir_resultados_combobox_gp)

    def __mostrar_pagina_introducir_resultados(self):
        self.__ctrl_introducir_resultados.rellenar_combobox_lista_temporadas(self.__p_introducir_resultados_combobox_temporada)

    def on_introducir_resultados_boton_aceptar_clicked(self, widget):
        self.__ctrl_introducir_resultados.set_gp_activo(self.__p_introducir_resultados_combobox_gp.get_active())

        if self.__ctrl_introducir_resultados.tipo_activo() == "clasificacion":
            self.__p_introducir_resultados_tabs.set_current_page(0)
            self.__p_introducir_resultados_scrolledwindow_clasificacion.set_sensitive(True)
            self.__p_introducir_resultados_scrolledwindow_carrera.set_sensitive(False)
            self.__ctrl_introducir_resultados.rellenar_lista_pilotos(self.__p_introducir_resultados_scrolledwindow_clasificacion)
        else:
            self.__p_introducir_resultados_tabs.set_current_page(1)
            self.__p_introducir_resultados_scrolledwindow_clasificacion.set_sensitive(False)
            self.__p_introducir_resultados_scrolledwindow_carrera.set_sensitive(True)
            self.__ctrl_introducir_resultados.rellenar_lista_pilotos(self.__p_introducir_resultados_scrolledwindow_carrera)
            self.__ctrl_introducir_resultados.definir_maximo_vueltas(self.__p_introducir_resultados_spinbutton_numero_vueltas)
        
        self.__p_introducir_resultados_tabs.show()
        self.__p_introducir_resultados_boton_guardar.set_sensitive(True)
    
    
    
    def on_introducir_resultados_boton_guardar_clicked(self, widget):
        if self.__ctrl_introducir_resultados.comprobar_checkboxes_pilotos():
            self.__ventana_introducir_resultados_dialogo_guardar_confirmar_datos.run()
        else:
            self.__ventana_introducir_resultados_dialogo_guardar_incorrecto.run()
   
    def on_ventana_introducir_resultados_dialogo_guardar_confirmar_datos_response(self, widget, response):
        if response == gtk.RESPONSE_YES:
            widget.hide()
            self.__p_introducir_resultados_scrolledwindow_clasificacion.set_sensitive(False)
            self.__p_introducir_resultados_scrolledwindow_carrera.set_sensitive(False)
            if self.__ctrl_introducir_resultados.tipo_activo() == "clasificacion":
                self.__ctrl_introducir_resultados.guardar_resultados(0, self.__ventana_introducir_resultados_dialogo_guardar_correcto)
                self.__paginas.set_current_page(0)
            else:
                self.__ctrl_introducir_resultados.guardar_resultados(self.__p_introducir_resultados_spinbutton_numero_vueltas.get_value(), self.__ventana_introducir_resultados_dialogo_guardar_correcto)
                self.__paginas.set_current_page(0)
        else:
            widget.hide()

    
    def on_introducir_resultados_boton_volver_clicked(self, widget):
        self.__paginas.set_current_page(0)
    
    def on_ventana_introducir_resultados_dialogo_no_hay_gps_response(self, widget, response):
        widget.hide()

    def on_ventana_introducir_resultados_dialogo_guardar_incorrecto_response(self, widget, response):
        widget.hide()

    def on_ventana_introducir_resultados_dialogo_guardar_correcto_response(self, widget, response):
        widget.hide()



    
    # Definiciones para la pagina de modificar temporada
    
    def on_mantenimiento_temporadas_boton_atras_clicked(self, widget):
        self.__paginas.set_current_page(0)

    def __mostrar_pagina_mantenimiento_temporadas(self):
        self.__ctrl_mantenimiento_temporada.crear_listview_temporadas(self.__p_mantenimiento_temporadas_lista_temporadas)
        self.__ctrl_mantenimiento_temporada.rellenar_listview_temporadas(self.__p_mantenimiento_temporadas_lista_temporadas)

    def on_mantenimiento_temporadas_boton_anadir_clicked(self, widget):
        self.__seleccionado_t = None
        adjustment_gp = gtk.Adjustment(0, 0, 100, 1, 10, 0)
        self.__p_modificar_temporada_spinbutton_num_pilotos_GP.set_adjustment(adjustment_gp)
        self.__p_modificar_temporada_spinbutton_num_pilotos_GP.set_value(0)
        adjustment_parrilla = gtk.Adjustment(0, 0, 100, 1, 10, 0)
        self.__p_modificar_temporada_spinbutton_num_pilotos_parrilla.set_adjustment(adjustment_parrilla)
        self.__p_modificar_temporada_spinbutton_num_pilotos_parrilla.set_value(0)
        self.__p_mantenimiento_temporadas_paginador.set_current_page(1)
        self.__ctrl_mantenimiento_temporada.actualizar_datos()

    def on_mantenimiento_temporadas_boton_borrar_clicked(self, widget):
        self.__seleccionado_t = self.__ctrl_mantenimiento_temporada.obtener_seleccionado(self.__p_mantenimiento_temporadas_lista_temporadas)
        if self.__seleccionado_t:
            self.__ventana_modificar_temporada_dialogo_borrar_temporada.run()

    def __comprobar_datos_temporada(self):
        if not self.__p_modificar_temporada_entrada_nombre.get_text():
            return False
        elif not self.__p_modificar_temporada_entrada_nombre_corto.get_text():
            return False
        elif not self.__ctrl_mantenimiento_temporada.validar_nombre_corto(self.__p_modificar_temporada_entrada_nombre_corto.get_text()):
            return False
        elif self.__p_modificar_temporada_boton_fecha_inicio.get_label() == _("Select a date"):
            return False
        elif self.__p_modificar_temporada_boton_fecha_fin.get_label() == _("Select a date"):
            return False
        elif self.__p_modificar_temporada_spinbutton_num_pilotos_GP.get_value() == 0:
            return False
        elif self.__p_modificar_temporada_spinbutton_num_pilotos_parrilla.get_value() == 0:
            return False
        else:
            return True

    def on_modificar_temporada_boton_guardar_clicked(self, widget):
        if self.__comprobar_datos_temporada():
            self.__ventana_modificar_temporada_dialogo_guardar_datos_confirmar.run()
        else:
            self.__ventana_modificar_temporada_dialogo_guardar_datos_incorrecto.run()

    def on_mantenimiento_temporadas_boton_editar_clicked(self, widget):
        self.__seleccionado_t = self.__ctrl_mantenimiento_temporada.obtener_seleccionado(self.__p_mantenimiento_temporadas_lista_temporadas)
        if self.__seleccionado_t:
            self.__ctrl_mantenimiento_temporada.rellenar_datos(self.__p_modificar_temporada_entrada_nombre,
                                                               self.__p_modificar_temporada_entrada_nombre_corto,
                                                               self.__p_modificar_temporada_boton_fecha_inicio,
                                                               self.__p_modificar_temporada_boton_fecha_fin,
                                                               self.__p_modificar_temporada_spinbutton_num_pilotos_GP,
                                                               self.__p_modificar_temporada_spinbutton_num_pilotos_parrilla)
            self.__p_mantenimiento_temporadas_paginador.set_current_page(1)

    def on_modificar_temporada_boton_cancelar_clicked(self, widget):
        self.__ventana_modificar_temporada_dialogo_cancelar.run()

    def on_modificar_temporada_boton_limpiar_clicked(self, widget):
        if self.__seleccionado_t == None:
            self.__p_modificar_temporada_entrada_nombre.set_text("")
            self.__p_modificar_temporada_entrada_nombre_corto.set_text("")
            self.__p_modificar_temporada_boton_fecha_inicio.set_label(_("Select a date"))
            self.__p_modificar_temporada_boton_fecha_fin.set_label(_("Select a date"))
            self.__p_modificar_temporada_spinbutton_num_pilotos_GP.set_value(0)
            self.__p_modificar_temporada_spinbutton_num_pilotos_parrilla.set_value(0)
        else:
            self.__seleccionado_t = self.__ctrl_mantenimiento_temporada.obtener_seleccionado(self.__p_mantenimiento_temporadas_lista_temporadas)
            if self.__seleccionado_t:
                self.__ctrl_mantenimiento_temporada.rellenar_datos(self.__p_modificar_temporada_entrada_nombre,
                                                                   self.__p_modificar_temporada_entrada_nombre_corto,
                                                                   self.__p_modificar_temporada_boton_fecha_inicio,
                                                                   self.__p_modificar_temporada_boton_fecha_fin,
                                                                   self.__p_modificar_temporada_spinbutton_num_pilotos_GP,
                                                                   self.__p_modificar_temporada_spinbutton_num_pilotos_parrilla)

    def on_modificar_temporada_boton_fecha_inicio_clicked(self, widget):
        self.__ventana_modificar_temporada_dialogo_fecha_inicio.show()

    def on_ventana_modificar_temporada_dialogo_fecha_inicio_boton_aceptar_clicked(self, widget):
        (year, month, day) = self.__ventana_modificar_temporada_dialogo_fecha_inicio_calendario.get_date()
        fecha = datetime.date(year, month+1, day)
        self.__ventana_modificar_temporada_dialogo_fecha_inicio.hide()

        self.__p_modificar_temporada_boton_fecha_inicio.set_label(fecha.strftime("%x"))
        self.__ctrl_mantenimiento_temporada.actualizar_fecha_inicio(fecha)

    def on_ventana_modificar_temporada_dialogo_fecha_inicio_boton_cancelar_clicked(self, widget):
        self.__ventana_modificar_temporada_dialogo_fecha_inicio.hide()


    def on_ventana_modificar_temporada_dialogo_fecha_inicio_delete_event(self, widget, data):
        self.__ventana_modificar_temporada_dialogo_fecha_inicio.hide()
        return True

    def on_modificar_temporada_boton_fecha_fin_clicked(self, widget):
        self.__ventana_modificar_temporada_dialogo_fecha_fin.show()


    def on_ventana_modificar_temporada_dialogo_fecha_fin_boton_aceptar_clicked(self, widget):
        (year, month, day) = self.__ventana_modificar_temporada_dialogo_fecha_fin_calendario.get_date()
        fecha = datetime.date(year, month+1, day)
        self.__ventana_modificar_temporada_dialogo_fecha_fin.hide()

        self.__p_modificar_temporada_boton_fecha_fin.set_label(fecha.strftime("%x"))
        self.__ctrl_mantenimiento_temporada.actualizar_fecha_fin(fecha)


    def on_ventana_modificar_temporada_dialogo_fecha_fin_boton_cancelar_clicked(self, widget):
        self.__ventana_modificar_temporada_dialogo_fecha_fin.hide()

    def on_ventana_modificar_temporada_dialogo_fecha_fin_delete_event(self, widget, data):
        self.__ventana_modificar_temporada_dialogo_fecha_fin.hide()
        return True

    def on_ventana_modificar_temporada_dialogo_cancelar_response(self, widget, response):
        if response == gtk.RESPONSE_YES:
            self.__p_mantenimiento_temporadas_paginador.set_current_page(0)
            self.__p_modificar_temporada_entrada_nombre.set_text("")
            self.__p_modificar_temporada_entrada_nombre_corto.set_text("")
            self.__p_modificar_temporada_boton_fecha_inicio.set_label(_("Select a date"))
            self.__p_modificar_temporada_boton_fecha_fin.set_label(_("Select a date"))
            self.__p_modificar_temporada_spinbutton_num_pilotos_GP.set_value(0)
            self.__p_modificar_temporada_spinbutton_num_pilotos_parrilla.set_value(0)
            self.__ctrl_mantenimiento_temporada.actualizar_datos()
            widget.hide()
        else:
            widget.hide()

    def on_ventana_modificar_temporada_dialogo_guardar_datos_confirmar_response(self, widget, response):
        if response == gtk.RESPONSE_YES:
            guardado = self.__ctrl_mantenimiento_temporada.guardar_temporada(self.__p_modificar_temporada_entrada_nombre.get_text(),
                                                                             self.__p_modificar_temporada_entrada_nombre_corto.get_text(),
                                                                             self.__p_modificar_temporada_spinbutton_num_pilotos_GP.get_value(),
                                                                             self.__p_modificar_temporada_spinbutton_num_pilotos_parrilla.get_value())
            widget.hide()
            if guardado:
                self.__ctrl_mantenimiento_temporada.actualizar_datos()
                self.__ctrl_mantenimiento_temporada.rellenar_listview_temporadas(self.__p_mantenimiento_temporadas_lista_temporadas)
                self.__ventana_modificar_temporada_dialogo_guardardo.run()
                self.__p_mantenimiento_temporadas_paginador.set_current_page(0)
            else:
                self.__ventana_modificar_temporada_dialogo_guardar_datos_temporada_comenzada.run()
        else:
            widget.hide()

    def on_ventana_modificar_temporada_dialogo_guardar_datos_temporada_comenzada_response(self, widget, response):
        widget.hide()

    def on_ventana_modificar_temporada_dialogo_guardado_response(self, widget, response):
        widget.hide()

    def on_ventana_modificar_temporada_dialogo_guardar_datos_incorrecto_response(self, widget, response):
        widget.hide()

    def on_ventana_modificar_temporada_dialogo_borrar_temporada_response(self, widget, response):
        if response == gtk.RESPONSE_YES:
            self.__ctrl_mantenimiento_temporada.borrar_temporada()
            self.__ctrl_mantenimiento_temporada.actualizar_datos()
            self.__ctrl_mantenimiento_temporada.rellenar_listview_temporadas(self.__p_mantenimiento_temporadas_lista_temporadas)
            
            widget.hide()
        else:
            widget.hide()

    def on_modificar_temporada_boton_reglas_puntuacion_clicked(self, widget):
        self.__mostrar_pagina_lista_reglas_temporada()
        self.__p_mantenimiento_temporadas_paginador.set_current_page(5)

    def on_modificar_temporada_boton_lista_GPs_clicked(self, widget):
        self.__mostrar_pagina_lista_gps_temporada()
        self.__p_mantenimiento_temporadas_paginador.set_current_page(3)

    def on_modificar_temporada_boton_lista_equipos_clicked(self, widget):
        self.__mostrar_pagina_lista_equipos_temporada()
        self.__p_mantenimiento_temporadas_paginador.set_current_page(2)

    def on_modificar_temporada_boton_lista_pilotos_clicked(self, widget):
        self.__mostrar_pagina_lista_pilotos_temporada()
        self.__p_mantenimiento_temporadas_paginador.set_current_page(4)


    def __mostrar_pagina_lista_gps_temporada(self):
        self.__ctrl_mantenimiento_temporada.crear_listview_gps(self.__p_modificar_temporada_lista_de_gps_lista_gps)
        self.__ctrl_mantenimiento_temporada.rellenar_listview_gps(self.__p_modificar_temporada_lista_de_gps_lista_gps)

    def __mostrar_pagina_lista_reglas_temporada(self):
        self.__ctrl_mantenimiento_temporada.crear_listview_reglas(self.__p_modificar_temporada_reglas_de_puntuacion_lista_reglas)
        self.__ctrl_mantenimiento_temporada.rellenar_listview_reglas(self.__p_modificar_temporada_reglas_de_puntuacion_lista_reglas)

    def __mostrar_pagina_lista_equipos_temporada(self):
        self.__ctrl_mantenimiento_temporada.crear_listview_equipos(self.__p_modificar_temporada_lista_de_equipos_lista_equipos)
        self.__ctrl_mantenimiento_temporada.rellenar_listview_equipos(self.__p_modificar_temporada_lista_de_equipos_lista_equipos)

    def __mostrar_pagina_lista_pilotos_temporada(self):
        self.__ctrl_mantenimiento_temporada.crear_listview_pilotos(self.__p_modificar_temporada_lista_de_pilotos_lista_pilotos)
        self.__ctrl_mantenimiento_temporada.rellenar_listview_pilotos(self.__p_modificar_temporada_lista_de_pilotos_lista_pilotos)


    def on_modificar_temporada_lista_de_equipos_boton_atras_clicked(self, widget):
        self.__p_mantenimiento_temporadas_paginador.set_current_page(1)

    def on_modificar_temporada_lista_de_gps_boton_atras_clicked(self, widget):
        self.__p_mantenimiento_temporadas_paginador.set_current_page(1)

    def on_modificar_temporada_lista_de_pilotos_boton_atras_clicked(self, widget):
        self.__p_mantenimiento_temporadas_paginador.set_current_page(1)

    def on_modificar_temporada_reglas_de_puntuacion_boton_guardar_clicked(self, widget):
        self.__ventana_modificar_temporada_reglas_puntuacion_dialogo_guardar_confirmar.run()

    def on_modificar_temporada_reglas_de_puntuacion_boton_editar_clicked(self, widget):
        path, focus_column = self.__p_modificar_temporada_reglas_de_puntuacion_lista_reglas.get_cursor()
        columna = self.__p_modificar_temporada_reglas_de_puntuacion_lista_reglas.get_column(1)
        if path:
            self.__p_modificar_temporada_reglas_de_puntuacion_lista_reglas.set_cursor(path, columna, True)

    def on_modificar_temporada_reglas_de_puntuacion_boton_anadir_clicked(self, widget):
        self.__ctrl_mantenimiento_temporada.anadir_fila_reglas(self.__p_modificar_temporada_reglas_de_puntuacion_lista_reglas)

    def on_modificar_temporada_reglas_de_puntuacion_boton_borrar_clicked(self, widget):
        self.__ctrl_mantenimiento_temporada.borrar_fila_reglas(self.__p_modificar_temporada_reglas_de_puntuacion_lista_reglas)


    def on_modificar_temporada_reglas_de_puntuacion_boton_cancelar_clicked(self, widget):
        self.__ventana_modificar_temporada_reglas_puntuacion_dialogo_cancelar.run()

    def on_ventana_modificar_temporada_reglas_puntuacion_dialogo_guardar_confirmar_response(self, widget, response):
        if response == gtk.RESPONSE_YES:
            guardado = self.__ctrl_mantenimiento_temporada.guardar_reglas()
            widget.hide()
            if guardado:
                self.__ventana_modificar_temporada_reglas_puntuacion_dialogo_guardado.run()
                self.__p_mantenimiento_temporadas_paginador.set_current_page(1)
            else:
                self.__ventana_modificar_temporada_reglas_puntuacion_dialogo_temporada_comenzada.run()
        else:
            widget.hide()

    def on_ventana_modificar_temporada_reglas_puntuacion_dialogo_borrar_response(self, widget, response):
        if response == gtk.RESPONSE_YES:
            #borrar
            widget.hide()
        else:
            widget.hide()

    def on_ventana_modificar_temporada_reglas_puntuacion_dialogo_cancelar_response(self, widget, response):
        if response == gtk.RESPONSE_YES:
            widget.hide()
            self.__p_mantenimiento_temporadas_paginador.set_current_page(1)
        else:
            widget.hide()

    def on_ventana_modificar_temporada_reglas_puntuacion_dialogo_guardado_response(self, widget, response):
        widget.hide()

    def on_ventana_modificar_temporada_reglas_puntuacion_dialogo_temporada_comenzada_response(self,widget,response):
        widget.hide()




    # Definiciones para la pagina de mantenimiento GPS
    def __mostrar_pagina_mantenimiento_gps(self):
        self.__ctrl_mantenimiento_gps.actualizar_datos()
        self.__ctrl_mantenimiento_gps.rellenar_combobox_lista_temporadas(self.__p_mantenimiento_gps_combobox_temporada)
        self.__p_mantenimiento_gps_boton_borrar.set_sensitive(False)
        self.__p_mantenimiento_gps_boton_editar.set_sensitive(False)
        self.__p_mantenimiento_gps_boton_anadir.set_sensitive(False)
        self.__ctrl_mantenimiento_gps.crear_listview_gps(self.__p_mantenimiento_gps_lista)

    def on_mantenimiento_gps_boton_aplicar_clicked(self, widget):
        self.__ctrl_mantenimiento_gps.set_temporada_activa(self.__p_mantenimiento_gps_combobox_temporada.get_active())
        self.__ctrl_mantenimiento_gps.rellenar_listview_gps(self.__p_mantenimiento_gps_lista)
        self.__p_mantenimiento_gps_boton_anadir.set_sensitive(True)
        if not self.__ctrl_mantenimiento_gps.get_temporada_vacia():
            self.__p_mantenimiento_gps_boton_borrar.set_sensitive(True)
            self.__p_mantenimiento_gps_boton_editar.set_sensitive(True)
        else:
            self.__p_mantenimiento_gps_boton_borrar.set_sensitive(False)
            self.__p_mantenimiento_gps_boton_editar.set_sensitive(False)


    def on_mantenimiento_gps_boton_anadir_clicked(self, widget):
        self.__ctrl_mantenimiento_gps.set_gp_activo(None)
        self.__seleccionado = None

        self.__p_modificar_gp_entrada_nombre_gp.set_text("")
        self.__p_modificar_gp_entrada_circuito.set_text("")
        self.__p_modificar_gp_boton_fecha_inicio.set_label(_("Select a date"))
        self.__p_modificar_gp_boton_fecha_fin.set_label(_("Select a date"))

        adjustment_vueltas = gtk.Adjustment(0, 0, 100, 1, 10, 0)
        self.__p_modificar_gp_spinbutton_num_vueltas.set_adjustment(adjustment_vueltas)
        self.__p_modificar_gp_spinbutton_num_vueltas.set_value(0)
        self.__ctrl_mantenimiento_gps.rellenar_temporada(self.__p_modificar_gp_etiqueta_nombre_temporada)
        self.__p_modificar_gp_etiqueta_estado_actual.set_text(_("Not Started"))
        self.__p_mantenimiento_gps_paginador.set_current_page(1)

    def on_mantenimiento_gps_boton_borrar_clicked(self, widget):
        self.__seleccionado = self.__ctrl_mantenimiento_gps.obtener_seleccionado(self.__p_mantenimiento_gps_lista)
        if self.__seleccionado:
            self.__ventana_mantenimiento_gp_dialogo_borrar.run()

    def on_mantenimiento_gps_boton_editar_clicked(self, widget):
        self.__seleccionado = self.__ctrl_mantenimiento_gps.obtener_seleccionado(self.__p_mantenimiento_gps_lista)
        self.__p_modificar_gp_etiqueta_estado_actual.set_text(_("Not Started"))
        if self.__seleccionado:
            self.__ctrl_mantenimiento_gps.rellenar_datos(self.__p_modificar_gp_etiqueta_nombre_temporada,
                                                         self.__p_modificar_gp_entrada_nombre_gp,
                                                         self.__p_modificar_gp_entrada_circuito,
                                                         self.__p_modificar_gp_boton_fecha_inicio,
                                                         self.__p_modificar_gp_boton_fecha_fin,
                                                         self.__p_modificar_gp_spinbutton_num_vueltas,
                                                         self.__p_modificar_gp_etiqueta_estado_actual)
        self.__p_mantenimiento_gps_paginador.set_current_page(1)

    def on_mantenimiento_gps_boton_atras_clicked(self, widget):
        self.__paginas.set_current_page(0)

    def on_modificar_gp_boton_fecha_inicio_clicked(self, widget):
        self.__ventana_modificar_gp_dialogo_fecha_inicio.show()

    def on_ventana_modificar_gp_dialogo_fecha_inicio_boton_aceptar_clicked(self, widget):
        (year, month, day) = self.__ventana_modificar_gp_dialogo_fecha_inicio_calendario.get_date()
        fecha = datetime.date(year, month+1, day)
        self.__ventana_modificar_gp_dialogo_fecha_inicio.hide()
        self.__p_modificar_gp_boton_fecha_inicio.set_label(fecha.strftime("%x"))
        self.__ctrl_mantenimiento_gps.actualizar_fecha_inicio(fecha)

    def on_ventana_modificar_gp_dialogo_fecha_inicio_boton_cancelar_clicked(self, widget):
        self.__ventana_modificar_gp_dialogo_fecha_inicio.hide()

    def on_ventana_modificar_gp_dialogo_fecha_inicio_delete_event(self, widget, data):
        self.__ventana_modificar_gp_dialogo_fecha_inicio.hide()
        return True

    def on_modificar_gp_boton_fecha_fin_clicked(self, widget):
        self.__ventana_modificar_gp_dialogo_fecha_fin.show()

    def on_ventana_modificar_gp_dialogo_fecha_fin_boton_aceptar_clicked(self, widget):
        (year, month, day) = self.__ventana_modificar_gp_dialogo_fecha_fin_calendario.get_date()
        fecha = datetime.date(year, month+1, day)
        self.__ventana_modificar_gp_dialogo_fecha_fin.hide()
        self.__p_modificar_gp_boton_fecha_fin.set_label(fecha.strftime("%x"))
        self.__ctrl_mantenimiento_gps.actualizar_fecha_fin(fecha)

    def on_ventana_modificar_gp_dialogo_fecha_fin_boton_cancelar_clicked(self, widget):
        self.__ventana_modificar_gp_dialogo_fecha_fin.hide()

    def on_ventana_modificar_gp_dialogo_fecha_fin_delete_event(self, widget, data):
        self.__ventana_modificar_gp_dialogo_fecha_fin.hide()
        return True

    def __comprobar_datos_gp(self):
        if not self.__p_modificar_gp_entrada_nombre_gp.get_text():
            return False
        elif not self.__p_modificar_gp_entrada_circuito.get_text():
            return False
        elif self.__p_modificar_gp_boton_fecha_inicio.get_label() == _("Select a date"):
            return False
        elif self.__p_modificar_gp_boton_fecha_fin.get_label() == _("Select a date"):
            return False
        elif self.__p_modificar_gp_spinbutton_num_vueltas.get_value() == 0:
            return False
        else:
            return True

    def on_modificar_gp_boton_guardar_clicked(self, widget):
        if self.__comprobar_datos_gp():
            self.__ventana_modificar_gp_dialogo_guardar_datos_confirmar.run()
        else:
            self.__ventana_modificar_gp_dialogo_guardar_datos_incorrecto.run()

    def on_modificar_gp_boton_cancelar_clicked(self, widget):
        self.__ventana_modificar_gp_dialogo_cancelar.run()

    def on_modificar_gp_boton_limpiar_clicked(self, widget):
        if self.__seleccionado == None:
            self.__p_modificar_gp_entrada_nombre_gp.set_text("")
            self.__p_modificar_gp_entrada_circuito.set_text("")
            self.__p_modificar_gp_boton_fecha_inicio.set_label(_("Select a date"))
            self.__p_modificar_gp_boton_fecha_fin.set_label(_("Select a date"))
            self.__p_modificar_gp_spinbutton_num_vueltas.set_value(0)
            self.__p_modificar_gp_etiqueta_estado_actual.set_text(_("Not Started"))
        else:
            self.__seleccionado = self.__ctrl_mantenimiento_gps.obtener_seleccionado(self.__p_mantenimiento_gps_lista)
            if self.__seleccionado:
                self.__ctrl_mantenimiento_gps.rellenar_datos(self.__p_modificar_gp_etiqueta_nombre_temporada,
                                                         self.__p_modificar_gp_entrada_nombre_gp,
                                                         self.__p_modificar_gp_entrada_circuito,
                                                         self.__p_modificar_gp_boton_fecha_inicio,
                                                         self.__p_modificar_gp_boton_fecha_fin,
                                                         self.__p_modificar_gp_spinbutton_num_vueltas,
                                                         self.__p_modificar_gp_etiqueta_estado_actual)

    def on_ventana_modificar_gp_dialogo_guardar_datos_confirmar_response(self, widget, response):
        if response == gtk.RESPONSE_YES:
            guardado, nuevo = self.__ctrl_mantenimiento_gps.guardar_gp(self.__p_modificar_gp_entrada_nombre_gp.get_text(),
                                                                self.__p_modificar_gp_entrada_circuito.get_text(),
                                                                self.__p_modificar_gp_spinbutton_num_vueltas.get_value())
            widget.hide()
            if guardado:
                self.__ctrl_mantenimiento_gps.rellenar_listview_gps(self.__p_mantenimiento_gps_lista)
                self.__ventana_modificar_gp_dialogo_guardado.run()
                self.__p_mantenimiento_gps_paginador.set_current_page(0)
            elif not guardado and nuevo:
                self.__ventana_modificar_gp_dialogo_guardar_datos_reglas_temporada.run()
            elif not guardado and not nuevo:
                self.__ventana_modificar_gp_dialogo_guardar_datos_gp_comenzado.run()
            
        else:
            widget.hide()

    def on_ventana_modificar_gp_dialogo_guardar_datos_reglas_temporada_response(self,widget,response):
        widget.hide()
        
    def on_ventana_modificar_gp_dialogo_guardar_datos_gp_comenzado_response(self, widget, response):
        widget.hide()

    def on_ventana_modificar_gp_dialogo_guardado_response(self, widget, response):
        widget.hide()

    def on_ventana_modificar_gp_dialogo_guardar_datos_incorrecto_response(self, widget, response):
        widget.hide()

    def on_ventana_mantenimiento_gp_dialogo_borrar_response(self,widget,response):
        if response == gtk.RESPONSE_YES:
            self.__ctrl_mantenimiento_gps.borrar_gp()
            self.__ctrl_mantenimiento_gps.rellenar_listview_gps(self.__p_mantenimiento_gps_lista)

            widget.hide()
        else:
            widget.hide()

    def on_ventana_modificar_gp_dialogo_cancelar_response(self,widget,response):
        if response == gtk.RESPONSE_YES:
            self.__p_mantenimiento_gps_paginador.set_current_page(0)
            widget.hide()
        else:
            widget.hide()

    # Definiciones para la pagina de mantenimiento pilotos
    def __mostrar_pagina_mantenimiento_pilotos(self):
        self.__ctrl_mantenimiento_pilotos.actualizar_datos()
        self.__ctrl_mantenimiento_pilotos.rellenar_combobox_lista_temporadas(self.__p_mantenimiento_pilotos_combobox_temporada)
        self.__p_mantenimiento_pilotos_boton_borrar.set_sensitive(False)
        self.__p_mantenimiento_pilotos_boton_editar.set_sensitive(False)
        self.__p_mantenimiento_pilotos_boton_anadir.set_sensitive(False)

        self.__ctrl_mantenimiento_pilotos.crear_listview_pilotos(self.__p_mantenimiento_pilotos_lista_pilotos)

    def on_mantenimiento_pilotos_boton_aplicar_clicked(self, widget):
        self.__ctrl_mantenimiento_pilotos.set_temporada_activa(self.__p_mantenimiento_pilotos_combobox_temporada.get_active())
        self.__ctrl_mantenimiento_pilotos.rellenar_listview_pilotos(self.__p_mantenimiento_pilotos_lista_pilotos)
        self.__p_mantenimiento_pilotos_boton_anadir.set_sensitive(True)
        if not self.__ctrl_mantenimiento_pilotos.get_temporada_vacia():
            self.__p_mantenimiento_pilotos_boton_borrar.set_sensitive(True)
            self.__p_mantenimiento_pilotos_boton_editar.set_sensitive(True)
        else:
            self.__p_mantenimiento_pilotos_boton_borrar.set_sensitive(False)
            self.__p_mantenimiento_pilotos_boton_editar.set_sensitive(False)


    def on_mantenimiento_pilotos_boton_anadir_clicked(self, widget):
        self.__ctrl_mantenimiento_pilotos.set_piloto_activo(None)
        self.__seleccionado_p = None
        self.__limpiar_ventana_modificar_piloto()
        self.__p_mantenimiento_pilotos_paginador.set_current_page(1)

    def on_mantenimiento_pilotos_boton_borrar_clicked(self, widget):
        self.__seleccionado_p = self.__ctrl_mantenimiento_pilotos.obtener_seleccionado(self.__p_mantenimiento_pilotos_lista_pilotos)
        if self.__seleccionado_p:
            self.__ventana_mantenimiento_piloto_dialogo_borrar.run()

    def on_mantenimiento_pilotos_boton_editar_clicked(self, widget):
        self.__seleccionado_p = self.__ctrl_mantenimiento_pilotos.obtener_seleccionado(self.__p_mantenimiento_pilotos_lista_pilotos)
        if self.__seleccionado_p:
            self.__ctrl_mantenimiento_pilotos.rellenar_datos(self.__p_modificar_piloto_entrada_nombre_piloto,
                                                         self.__p_modificar_piloto_boton_fecha_nacimiento,
                                                         self.__p_modificar_piloto_imagen_foto_piloto)
            self.__ctrl_mantenimiento_pilotos.crear_listview_equipos(self.__p_modificar_piloto_lista_equipos)
            self.__ctrl_mantenimiento_pilotos.rellenar_listview_equipos(self.__p_modificar_piloto_lista_equipos)

            self.__p_mantenimiento_pilotos_paginador.set_current_page(1)

    def on_mantenimiento_pilotos_boton_atras_clicked(self, widget):
        self.__paginas.set_current_page(0)

    def __comprobar_datos_piloto(self):
        if not self.__p_modificar_piloto_entrada_nombre_piloto.get_text():
            return False
        elif self.__p_modificar_piloto_boton_fecha_nacimiento.get_label() == _("Select a date"):
            return False
        else:
            return True

    def on_modificar_piloto_boton_fecha_nacimiento_clicked(self,widget):
        self.__ventana_modificar_piloto_dialogo_fecha_nacimiento.show()

    def on_modificar_piloto_boton_cambiar_foto_piloto_clicked(self,widget):
        self.__ventana_modificar_piloto_dialogo_foto.show()

    def on_modificar_piloto_boton_cancelar_clicked(self, widget):
        self.__ventana_modificar_piloto_dialogo_cancelar.run()
    
    def on_modificar_piloto_boton_guardar_clicked(self,widget):
        if self.__comprobar_datos_piloto():
           self.__ventana_modificar_piloto_dialogo_guardar_datos_confirmar.run()
        else:
            self.__ventana_modificar_piloto_dialogo_guardar_datos_incorrecto.run()

    def on_modificar_piloto_boton_limpiar_clicked(self,widget):
        if self.__seleccionado_p == None:
            self.__limpiar_ventana_modificar_piloto()
        else:
            self.__seleccionado_p = self.__ctrl_mantenimiento_pilotos.obtener_seleccionado(self.__p_mantenimiento_pilotos_lista_pilotos)
            if self.__seleccionado_p:
                self.__ctrl_mantenimiento_pilotos.rellenar_datos(self.__p_modificar_piloto_entrada_nombre_piloto,
                                                         self.__p_modificar_piloto_boton_fecha_nacimiento,
                                                         self.__p_modificar_piloto_imagen_foto_piloto)
            self.__ctrl_mantenimiento_pilotos.crear_listview_equipos(self.__p_modificar_piloto_lista_equipos)
            self.__ctrl_mantenimiento_pilotos.rellenar_listview_equipos(self.__p_modificar_piloto_lista_equipos)

    def on_ventana_modificar_piloto_dialogo_fecha_nacimiento_boton_aceptar_clicked(self, widget):
        (year, month, day) = self.__ventana_modificar_piloto_dialogo_fecha_nacimiento_calendario.get_date()
        fecha = datetime.date(year, month+1, day)
        self.__ventana_modificar_piloto_dialogo_fecha_nacimiento.hide()

        self.__p_modificar_piloto_boton_fecha_nacimiento.set_label(fecha.strftime("%x"))
        self.__ctrl_mantenimiento_pilotos.actualizar_fecha_nacimiento(fecha)

    def on_ventana_modificar_piloto_dialogo_fecha_nacimiento_boton_cancelar_clicked(self, widget):
        self.__ventana_modificar_piloto_dialogo_fecha_nacimiento.hide()

    def on_ventana_modificar_piloto_dialogo_fecha_nacimiento_delete_event(self, widget, data):
        self.__ventana_modificar_piloto_dialogo_fecha_nacimiento.hide()
        return True

    def on_ventana_modificar_piloto_dialogo_guardar_datos_confirmar_response(self, widget, response):
        if response == gtk.RESPONSE_YES:
            guardado = self.__ctrl_mantenimiento_pilotos.guardar_piloto(self.__p_modificar_piloto_entrada_nombre_piloto.get_text())
            widget.hide()
            if guardado:
                self.__ctrl_mantenimiento_pilotos.actualizar_datos()
                self.__ctrl_mantenimiento_pilotos.rellenar_listview_pilotos(self.__p_mantenimiento_pilotos_lista_pilotos)
                self.__ventana_modificar_piloto_dialogo_guardado.run()
                if not self.__ctrl_mantenimiento_pilotos.get_temporada_vacia():
                    self.__p_mantenimiento_pilotos_boton_borrar.set_sensitive(True)
                    self.__p_mantenimiento_pilotos_boton_editar.set_sensitive(True)
                else:
                    self.__p_mantenimiento_pilotos_boton_borrar.set_sensitive(False)
                    self.__p_mantenimiento_pilotos_boton_editar.set_sensitive(False)
                self.__p_mantenimiento_pilotos_boton_borrar.set_sensitive(True)
                self.__p_mantenimiento_pilotos_boton_editar.set_sensitive(True)
                self.__p_mantenimiento_pilotos_paginador.set_current_page(0)
                self.__limpiar_ventana_modificar_piloto()

        else:
            widget.hide()

    def on_ventana_modificar_piloto_dialogo_guardado_response(self, widget, response):
        widget.hide()

    def on_ventana_modificar_piloto_dialogo_guardar_datos_incorrecto_response(self, widget, response):
        widget.hide()

    def on_ventana_mantenimiento_piloto_dialogo_borrar_response(self,widget,response):
        if response == gtk.RESPONSE_YES:
            self.__ctrl_mantenimiento_pilotos.borrar_piloto()
            self.__ctrl_mantenimiento_pilotos.actualizar_datos()
            self.__ctrl_mantenimiento_pilotos.rellenar_listview_pilotos(self.__p_mantenimiento_pilotos_lista_pilotos)
            self.__limpiar_ventana_modificar_piloto()
            if not self.__ctrl_mantenimiento_pilotos.get_temporada_vacia():
                self.__p_mantenimiento_pilotos_boton_borrar.set_sensitive(True)
                self.__p_mantenimiento_pilotos_boton_editar.set_sensitive(True)
            else:
                self.__p_mantenimiento_pilotos_boton_borrar.set_sensitive(False)
                self.__p_mantenimiento_pilotos_boton_editar.set_sensitive(False)

            widget.hide()
        else:
            widget.hide()

    def on_ventana_modificar_piloto_dialogo_cancelar_response(self,widget,response):
        if response == gtk.RESPONSE_YES:
            self.__limpiar_ventana_modificar_piloto()
            self.__p_mantenimiento_pilotos_paginador.set_current_page(0)
            widget.hide()
        else:
            widget.hide()

    def __limpiar_ventana_modificar_piloto(self):
        self.__ctrl_mantenimiento_pilotos.set_piloto_activo(None)
        self.__p_modificar_piloto_entrada_nombre_piloto.set_text("")
        self.__p_modificar_piloto_boton_fecha_nacimiento.set_label(_("Select a date"))
        self.__p_modificar_piloto_imagen_foto_piloto.set_from_stock(gtk.STOCK_MISSING_IMAGE,gtk.ICON_SIZE_DIALOG)
        self.__ctrl_mantenimiento_pilotos.crear_listview_equipos(self.__p_modificar_piloto_lista_equipos)
        self.__ctrl_mantenimiento_pilotos.rellenar_listview_equipos(self.__p_modificar_piloto_lista_equipos)
        self.__seleccionado_p = None

    def __anadir_filtos_dialogo_foto(self,dialogo):
        filter = gtk.FileFilter()
        filter.set_name(_("All files"))
        filter.add_pattern("*")
        dialogo.add_filter(filter)

        filter = gtk.FileFilter()
        filter.set_name(_("Images"))
        filter.add_mime_type("image/png")
        filter.add_mime_type("image/jpeg")
        filter.add_mime_type("image/gif")
        filter.add_pattern("*.png")
        filter.add_pattern("*.jpg")
        filter.add_pattern("*.gif")
        filter.add_pattern("*.tif")
        filter.add_pattern("*.xpm")
        dialogo.add_filter(filter)

    def on_ventana_modificar_piloto_dialogo_foto_boton_abrir_clicked(self,widget):
        foto = self.__ventana_modificar_piloto_dialogo_foto.get_filename()
        self.__ctrl_mantenimiento_pilotos.actualizar_foto(foto)
        self.__ventana_modificar_piloto_dialogo_foto.hide()
        self.__p_modificar_piloto_imagen_foto_piloto.set_from_file(foto)
    def on_ventana_modificar_piloto_dialogo_foto_boton_cancelar_clicked(self,widget):
        self.__ventana_modificar_piloto_dialogo_foto.hide()

    def on_ventana_modificar_piloto_dialogo_foto_delete_event(self,widget,data):
        self.__ventana_modificar_piloto_dialogo_foto.hide()
        return True

    # Definiciones para la pagina de mantenimiento equipos
    def __mostrar_pagina_mantenimiento_equipos(self):
        False

    def on_mantenimiento_equipos_boton_aplicar_clicked(self, widget):
        False

    def on_mantenimiento_equipos_boton_anadir_clicked(self, widget):
        self.__p_mantenimiento_equipos_paginador.set_current_page(1)

    def on_mantenimiento_equipos_boton_borrar_clicked(self, widget):
        self.__ventana_mantenimiento_equipo_dialogo_borrar.run()

    def on_mantenimiento_equipos_boton_editar_clicked(self, widget):
        self.__p_mantenimiento_equipos_paginador.set_current_page(1)

    def on_mantenimiento_equipos_boton_atras_clicked(self, widget):
        self.__paginas.set_current_page(0)

    def on_modificar_equipo_boton_fecha_inicio_clicked(self,widget):
        self.__ventana_modificar_equipo_dialogo_fecha_inicio.show()

    def on_modificar_equipo_boton_fecha_fin_clicked(self,widget):
        self.__ventana_modificar_equipo_dialogo_fecha_fin.show()

    def on_modificar_equipo_boton_cambiar_foto_equipo_clicked(self,widget):
        self.__ventana_modificar_equipo_dialogo_foto.show()

    def on_modificar_equipo_boton_cancelar_clicked(self, widget):
        self.__ventana_modificar_equipo_dialogo_cancelar.run()

    def on_modificar_equipo_boton_guardar_clicked(self,widget):
        self.__ventana_modificar_equipo_dialogo_guardar_datos_confirmar.run()

    def on_modificar_equipo_boton_limpiar_clicked(self,widget):
        False

    def on_ventana_modificar_equipo_dialogo_fecha_inicio_boton_aceptar_clicked(self, widget):
        self.__ventana_modificar_equipo_dialogo_fecha_inicio.hide()

    def on_ventana_modificar_equipo_dialogo_fecha_fin_boton_aceptar_clicked(self, widget):
        self.__ventana_modificar_equipo_dialogo_fecha_fin.hide()

    def on_ventana_modificar_equipo_dialogo_fecha_inicio_boton_cancelar_clicked(self, widget):
        self.__ventana_modificar_equipo_dialogo_fecha_inicio.hide()

    def on_ventana_modificar_equipo_dialogo_fecha_fin_boton_cancelar_clicked(self, widget):
        self.__ventana_modificar_equipo_dialogo_fecha_fin.hide()

    def on_ventana_modificar_equipo_dialogo_fecha_inicio_delete_event(self, widget, data):
        self.__ventana_modificar_equipo_dialogo_fecha_inicio.hide()
        return True

    def on_ventana_modificar_equipo_dialogo_fecha_fin_delete_event(self, widget, data):
        self.__ventana_modificar_equipo_dialogo_fecha_fin.hide()
        return True

    def on_ventana_modificar_equipo_dialogo_guardar_datos_confirmar_response(self, widget, response):
        if response == gtk.RESPONSE_YES:
            widget.hide()
            self.__p_mantenimiento_equipos_paginador.set_current_page(0)
        else:
            widget.hide()

    def on_ventana_modificar_equipo_dialogo_guardado_response(self, widget, response):
        widget.hide()

    def on_ventana_modificar_equipo_dialogo_guardar_datos_incorrecto_response(self, widget, response):
        widget.hide()

    def on_ventana_mantenimiento_equipo_dialogo_borrar_response(self,widget,response):
        widget.hide()

    def on_ventana_modificar_equipo_dialogo_cancelar_response(self,widget,response):
        if response == gtk.RESPONSE_YES:
            self.__p_mantenimiento_equipos_paginador.set_current_page(0)
            widget.hide()
        else:
            widget.hide()

    def on_ventana_modificar_equipo_dialogo_foto_boton_abrir_clicked(self,widget):
        self.__ventana_modificar_equipo_dialogo_foto.hide()
        
    def on_ventana_modificar_equipo_dialogo_foto_boton_cancelar_clicked(self,widget):
        self.__ventana_modificar_equipo_dialogo_foto.hide()

    def on_ventana_modificar_equipo_dialogo_foto_delete_event(self,widget,data):
        self.__ventana_modificar_equipo_dialogo_foto.hide()
        return True

    def on_modificar_equipo_boton_ver_pilotos_clicked(self,widget):
        self.__ventana_modificar_equipo_lista_pilotos.show()

    def on_modificar_equipo_boton_ver_temporadas_clicked(self,widget):
        self.__ventana_modificar_equipo_lista_temporadas.show()

    def on_ventana_modificar_equipo_lista_pilotos_boton_atras_clicked(self, widget):
        self.__ventana_modificar_equipo_lista_pilotos.hide()

    def on_ventana_modificar_equipo_lista_temporadas_boton_atras_clicked(self, widget):
        self.__ventana_modificar_equipo_lista_temporadas.hide()

    def on_ventana_modificar_equipo_lista_pilotos_delete_event(self, widget, data):
        self.__ventana_modificar_equipo_lista_pilotos.hide()
        return True

    def on_ventana_modificar_equipo_lista_temporadas_delete_event(self, widget, data):
        self.__ventana_modificar_equipo_lista_temporadas.hide()
        return True

    def on_modificar_equipo_boton_cambiar_escudo_clicked(self,widget):
        self.__ventana_modificar_equipo_dialogo_foto.show()
        
    def __init__(self):
        self.__ctrl_consultar_resultados = Controlador.ConsultarResultados()
        self.__ctrl_introducir_resultados = Controlador.IntroducirResultados()
        self.__ctrl_mantenimiento_temporada = Controlador.MantenimientoTemporada()
        self.__ctrl_mantenimiento_gps = Controlador.MantenimientoGPs()
        self.__ctrl_mantenimiento_pilotos = Controlador.MantenimientoPilotos()
        
        self.__builder = gtk.glade.XML("glade/interfaz.glade")
        
        self.ventana_principal = self.__builder.get_widget("ventana_principal")
        self.__ventana_about = self.__builder.get_widget("ventana_about")
        self.__ventana_introducir_resultados_dialogo_guardar_incorrecto = self.__builder.get_widget("ventana_introducir_resultados_dialogo_guardar_incorrecto")
        self.__ventana_introducir_resultados_dialogo_guardar_correcto = self.__builder.get_widget("ventana_introducir_resultados_dialogo_guardar_correcto")
        self.__ventana_introducir_resultados_dialogo_guardar_confirmar_datos = self.__builder.get_widget("ventana_introducir_resultados_dialogo_guardar_confirmar_datos")
        self.__ventana_introducir_resultados_dialogo_no_hay_gps = self.__builder.get_widget("ventana_introducir_resultados_dialogo_no_hay_gps")
        self.__ventana_modificar_temporada_dialogo_fecha_inicio = self.__builder.get_widget("ventana_modificar_temporada_dialogo_fecha_inicio")
        self.__ventana_modificar_temporada_dialogo_fecha_inicio_calendario = self.__builder.get_widget("ventana_modificar_temporada_dialogo_fecha_inicio_calendario")
        self.__ventana_modificar_temporada_dialogo_fecha_fin = self.__builder.get_widget("ventana_modificar_temporada_dialogo_fecha_fin")
        self.__ventana_modificar_temporada_dialogo_fecha_fin_calendario = self.__builder.get_widget("ventana_modificar_temporada_dialogo_fecha_fin_calendario")
        self.__ventana_modificar_temporada_dialogo_cancelar = self.__builder.get_widget("ventana_modificar_temporada_dialogo_cancelar")
        self.__ventana_modificar_temporada_dialogo_borrar_temporada = self.__builder.get_widget("ventana_modificar_temporada_dialogo_borrar_temporada")
        self.__ventana_modificar_temporada_dialogo_guardar_datos_incorrecto = self.__builder.get_widget("ventana_modificar_temporada_dialogo_guardar_datos_incorrecto")
        self.__ventana_modificar_temporada_dialogo_guardar_datos_confirmar = self.__builder.get_widget("ventana_modificar_temporada_dialogo_guardar_datos_confirmar")
        self.__ventana_modificar_temporada_dialogo_guardardo = self.__builder.get_widget("ventana_modificar_temporada_dialogo_guardado")
        self.__ventana_modificar_temporada_dialogo_guardar_datos_temporada_comenzada = self.__builder.get_widget("ventana_modificar_temporada_dialogo_guardar_datos_temporada_comenzada")

        self.__ventana_modificar_temporada_lista_equipos_dialogo_guardar_confirmar = self.__builder.get_widget("ventana_modificar_temporada_lista_equipos_dialogo_guardar_confirmar")
        self.__ventana_modificar_temporada_lista_equipos_dialogo_cancelar = self.__builder.get_widget("ventana_modificar_temporada_lista_equipos_dialogo_cancelar")
        self.__ventana_modificar_temporada_lista_equipos_dialogo_borrar = self.__builder.get_widget("ventana_modificar_temporada_lista_equipos_dialogo_borrar")
        self.__ventana_modificar_temporada_lista_equipos_dialogo_guardado = self.__builder.get_widget("ventana_modificar_temporada_lista_equipos_dialogo_guardado")

        self.__ventana_modificar_temporada_lista_gps_dialogo_guardar_confirmar = self.__builder.get_widget("ventana_modificar_temporada_lista_gps_dialogo_guardar_confirmar")
        self.__ventana_modificar_temporada_lista_gps_dialogo_cancelar = self.__builder.get_widget("ventana_modificar_temporada_lista_gps_dialogo_cancelar")
        self.__ventana_modificar_temporada_lista_gps_dialogo_borrar = self.__builder.get_widget("ventana_modificar_temporada_lista_gps_dialogo_borrar")
        self.__ventana_modificar_temporada_lista_gps_dialogo_guardado = self.__builder.get_widget("ventana_modificar_temporada_lista_gps_dialogo_guardado")

        self.__ventana_modificar_temporada_lista_pilotos_dialogo_guardar_confirmar = self.__builder.get_widget("ventana_modificar_temporada_lista_pilotos_dialogo_guardar_confirmar")
        self.__ventana_modificar_temporada_lista_pilotos_dialogo_cancelar = self.__builder.get_widget("ventana_modificar_temporada_lista_pilotos_dialogo_cancelar")
        self.__ventana_modificar_temporada_lista_pilotos_dialogo_borrar = self.__builder.get_widget("ventana_modificar_temporada_lista_pilotos_dialogo_borrar")
        self.__ventana_modificar_temporada_lista_pilotos_dialogo_guardado = self.__builder.get_widget("ventana_modificar_temporada_lista_pilotos_dialogo_guardado")

        self.__ventana_modificar_temporada_reglas_puntuacion_dialogo_guardar_confirmar = self.__builder.get_widget("ventana_modificar_temporada_reglas_puntuacion_dialogo_guardar_confirmar")
        self.__ventana_modificar_temporada_reglas_puntuacion_dialogo_cancelar = self.__builder.get_widget("ventana_modificar_temporada_reglas_puntuacion_dialogo_cancelar")
        self.__ventana_modificar_temporada_reglas_puntuacion_dialogo_borrar = self.__builder.get_widget("ventana_modificar_temporada_reglas_puntuacion_dialogo_borrar")
        self.__ventana_modificar_temporada_reglas_puntuacion_dialogo_guardado = self.__builder.get_widget("ventana_modificar_temporada_reglas_puntuacion_dialogo_guardado")
        self.__ventana_modificar_temporada_reglas_puntuacion_dialogo_temporada_comenzada = self.__builder.get_widget("ventana_modificar_temporada_reglas_puntuacion_dialogo_temporada_comenzada")

        self.__ventana_modificar_temporada_lista_equipos_dialogo_equipos_disponibles_anadir_temporada = self.__builder.get_widget("ventana_modificar_temporada_lista_equipos_dialogo_equipos_disponibles_anadir_temporada")
        self.__ventana_modificar_temporada_lista_equipos_dialogo_equipos_disponibles_anadir_temporada_lista = self.__builder.get_widget("ventana_modificar_temporada_lista_equipos_dialogo_equipos_disponibles_anadir_temporada_lista")

        self.__ventana_modificar_gp_dialogo_fecha_inicio = self.__builder.get_widget("ventana_modificar_gp_dialogo_fecha_inicio")
        self.__ventana_modificar_gp_dialogo_fecha_fin = self.__builder.get_widget("ventana_modificar_gp_dialogo_fecha_fin")
        self.__ventana_modificar_gp_dialogo_fecha_inicio = self.__builder.get_widget("ventana_modificar_gp_dialogo_fecha_inicio")
        self.__ventana_modificar_gp_dialogo_fecha_inicio_calendario = self.__builder.get_widget("ventana_modificar_gp_dialogo_fecha_inicio_calendario")
        self.__ventana_modificar_gp_dialogo_fecha_fin = self.__builder.get_widget("ventana_modificar_gp_dialogo_fecha_fin")
        self.__ventana_modificar_gp_dialogo_fecha_fin_calendario = self.__builder.get_widget("ventana_modificar_gp_dialogo_fecha_fin_calendario")
        self.__ventana_modificar_gp_dialogo_guardar_datos_confirmar = self.__builder.get_widget("ventana_modificar_gp_dialogo_guardar_datos_confirmar")
        self.__ventana_modificar_gp_dialogo_cancelar = self.__builder.get_widget("ventana_modificar_gp_dialogo_cancelar")
        self.__ventana_modificar_gp_dialogo_guardado = self.__builder.get_widget("ventana_modificar_gp_dialogo_guardado")
        self.__ventana_modificar_gp_dialogo_guardar_datos_incorrecto = self.__builder.get_widget("ventana_modificar_gp_dialogo_guardar_datos_incorrecto")
        self.__ventana_modificar_gp_dialogo_guardar_datos_gp_comenzado = self.__builder.get_widget("ventana_modificar_gp_dialogo_guardar_datos_gp_comenzado")
        self.__ventana_modificar_gp_dialogo_guardar_datos_reglas_temporada = self.__builder.get_widget("ventana_modificar_gp_dialogo_guardar_datos_reglas_temporada")
        self.__ventana_mantenimiento_gp_dialogo_borrar = self.__builder.get_widget("ventana_mantenimiento_gp_dialogo_borrar")

        self.__ventana_modificar_piloto_dialogo_cancelar = self.__builder.get_widget("ventana_modificar_piloto_dialogo_cancelar")
        self.__ventana_modificar_piloto_dialogo_guardado = self.__builder.get_widget("ventana_modificar_piloto_dialogo_guardado")
        self.__ventana_modificar_piloto_dialogo_guardar_datos_incorrecto = self.__builder.get_widget("ventana_modificar_piloto_dialogo_guardar_datos_incorrecto")
        self.__ventana_modificar_piloto_dialogo_guardar_datos_confirmar = self.__builder.get_widget("ventana_modificar_piloto_dialogo_guardar_datos_confirmar")
        self.__ventana_modificar_piloto_dialogo_fecha_nacimiento = self.__builder.get_widget("ventana_modificar_piloto_dialogo_fecha_nacimiento")
        self.__ventana_mantenimiento_piloto_dialogo_borrar = self.__builder.get_widget("ventana_mantenimiento_piloto_dialogo_borrar")
        self.__ventana_modificar_piloto_dialogo_foto = self.__builder.get_widget("ventana_modificar_piloto_dialogo_foto")
        self.__ventana_modificar_piloto_dialogo_fecha_nacimiento_calendario  = self.__builder.get_widget("ventana_modificar_piloto_dialogo_fecha_nacimiento_calendario")
        self.__anadir_filtos_dialogo_foto(self.__ventana_modificar_piloto_dialogo_foto)
        
        self.__ventana_modificar_equipo_dialogo_cancelar = self.__builder.get_widget("ventana_modificar_equipo_dialogo_cancelar")
        self.__ventana_modificar_equipo_dialogo_guardado = self.__builder.get_widget("ventana_modificar_equipo_dialogo_guardado")
        self.__ventana_modificar_equipo_dialogo_guardar_datos_incorrecto = self.__builder.get_widget("ventana_modificar_equipo_dialogo_guardar_datos_incorrecto")
        self.__ventana_modificar_equipo_dialogo_guardar_datos_confirmar = self.__builder.get_widget("ventana_modificar_equipo_dialogo_guardar_datos_confirmar")
        self.__ventana_modificar_equipo_dialogo_fecha_inicio = self.__builder.get_widget("ventana_modificar_equipo_dialogo_fecha_inicio")
        self.__ventana_modificar_equipo_dialogo_fecha_fin = self.__builder.get_widget("ventana_modificar_equipo_dialogo_fecha_fin")
        self.__ventana_mantenimiento_equipo_dialogo_borrar = self.__builder.get_widget("ventana_mantenimiento_equipo_dialogo_borrar")
        self.__ventana_modificar_equipo_dialogo_foto = self.__builder.get_widget("ventana_modificar_equipo_dialogo_foto")
        self.__anadir_filtos_dialogo_foto(self.__ventana_modificar_equipo_dialogo_foto)
        self.__ventana_modificar_equipo_lista_temporadas = self.__builder.get_widget("ventana_modificar_equipo_lista_temporadas")
        self.__ventana_modificar_equipo_lista_pilotos = self.__builder.get_widget("ventana_modificar_equipo_lista_pilotos")

        self.__paginas = self.__builder.get_widget("paginador")
        
        self.__p_consultar_resultados_combobox_temporada = self.__builder.get_widget("consultar_resultados_combobox_temporada")
        self.__p_consultar_resultados_combobox_selector = self.__builder.get_widget("consultar_resultados_combobox_selector")
        self.__p_consultar_resultados_combobox_gps = self.__builder.get_widget("consultar_resultados_combobox_gps")
        self.__p_consultar_resultados_notebook = self.__builder.get_widget("consultar_resultados_tabs")
        self.__p_consultar_resultados_lista_pilotos = self.__builder.get_widget("consultar_resultados_lista_pilotos")
        self.__p_consultar_resultados_lista_equipos = self.__builder.get_widget("consultar_resultados_lista_equipos")
        self.__p_consultar_resultados_lista_gp_parrilla = self.__builder.get_widget("consultar_resultados_lista_gp_parrilla")
        self.__p_consultar_resultados_lista_gp_carrera = self.__builder.get_widget("consultar_resultados_lista_gp_carrera")
        self.__p_consultar_resultados_etiqueta_datos_mostrados = self.__builder.get_widget("consultar_resultados_etiqueta_datos_mostrados")
        self.__p_consultar_resultados_lista_carreras_temporada = self.__builder.get_widget("consultar_resultados_lista_carreras_temporada")
        
        self.__p_introducir_resultados_combobox_temporada = self.__builder.get_widget("introducir_resultados_combobox_temporada")
        self.__p_introducir_resultados_combobox_gp = self.__builder.get_widget("introducir_resultados_combobox_gp")
        self.__p_introducir_resultados_scrolledwindow_clasificacion = self.__builder.get_widget("introducir_resultados_scrolledwindow_clasificacion")
        self.__p_introducir_resultados_scrolledwindow_carrera = self.__builder.get_widget("introducir_resultados_scrolledwindow_carrera")
        self.__p_introducir_resultados_tabs = self.__builder.get_widget("introducir_resultados_tabs")
        self.__p_introducir_resultados_tab_clasificacion = self.__builder.get_widget("introducir_resultados_tab_clasificacion")
        self.__p_introducir_resultados_tab_carrera = self.__builder.get_widget("introducir_resultados_tab_carrera")
        self.__p_introducir_resultados_boton_guardar = self.__builder.get_widget("introducir_resultados_boton_guardar")
        self.__p_introducir_resultados_spinbutton_numero_vueltas = self.__builder.get_widget("introducir_resultados_spinbutton_numero_vueltas")

        self.__p_mantenimiento_temporadas_paginador = self.__builder.get_widget("pagina_temporadas")
        self.__p_mantenimiento_temporadas_lista_temporadas = self.__builder.get_widget("mantenimiento_temporadas_lista_temporadas")
        self.__p_modificar_temporada_entrada_nombre = self.__builder.get_widget("modificar_temporada_entrada_nombre")
        self.__p_modificar_temporada_entrada_nombre_corto = self.__builder.get_widget("modificar_temporada_entrada_nombre_corto")
        self.__p_modificar_temporada_boton_fecha_inicio = self.__builder.get_widget("modificar_temporada_boton_fecha_inicio")
        self.__p_modificar_temporada_boton_fecha_fin = self.__builder.get_widget("modificar_temporada_boton_fecha_fin")
        self.__p_modificar_temporada_spinbutton_num_pilotos_GP = self.__builder.get_widget("modificar_temporada_spinbutton_num_pilotos_GP")
        self.__p_modificar_temporada_spinbutton_num_pilotos_parrilla = self.__builder.get_widget("modificar_temporada_spinbutton_num_pilotos_parrilla")
        self.__p_modificar_temporada_lista_de_equipos_lista_equipos = self.__builder.get_widget("modificar_temporada_lista_de_equipos_lista_equipos")
        self.__p_modificar_temporada_lista_de_gps_lista_gps = self.__builder.get_widget("modificar_temporada_lista_de_gps_lista_gps")
        self.__p_modificar_temporada_lista_de_pilotos_lista_pilotos = self.__builder.get_widget("modificar_temporada_lista_de_pilotos_lista_pilotos")
        self.__p_modificar_temporada_reglas_de_puntuacion_lista_reglas = self.__builder.get_widget("modificar_temporada_reglas_de_puntuacion_lista_reglas")


        self.__p_mantenimiento_gps_paginador = self.__builder.get_widget("pagina_gps")
        self.__p_mantenimiento_gps_combobox_temporada = self.__builder.get_widget("mantenimiento_gps_combobox_temporada")
        self.__p_mantenimiento_gps_lista = self.__builder.get_widget("mantenimiento_gps_lista")
        self.__p_mantenimiento_gps_boton_anadir = self.__builder.get_widget("mantenimiento_gps_boton_anadir")
        self.__p_mantenimiento_gps_boton_borrar = self.__builder.get_widget("mantenimiento_gps_boton_borrar")
        self.__p_mantenimiento_gps_boton_editar = self.__builder.get_widget("mantenimiento_gps_boton_editar")
        self.__p_mantenimiento_gps_boton_atras = self.__builder.get_widget("mantenimiento_gps_boton_atras")
        self.__p_modificar_gp_etiqueta_nombre_temporada = self.__builder.get_widget("modificar_gp_etiqueta_nombre_temporada")
        self.__p_modificar_gp_entrada_nombre_gp = self.__builder.get_widget("modificar_gp_entrada_nombre_gp")
        self.__p_modificar_gp_entrada_circuito = self.__builder.get_widget("modificar_gp_entrada_circuito")
        self.__p_modificar_gp_boton_fecha_inicio = self.__builder.get_widget("modificar_gp_boton_fecha_inicio")
        self.__p_modificar_gp_boton_fecha_fin = self.__builder.get_widget("modificar_gp_boton_fecha_fin")
        self.__p_modificar_gp_spinbutton_num_vueltas = self.__builder.get_widget("modificar_gp_spinbutton_num_vueltas")
        self.__p_modificar_gp_etiqueta_estado_actual = self.__builder.get_widget("modificar_gp_etiqueta_estado_actual")
        self.__p_modificar_gp_boton_guardar = self.__builder.get_widget("modificar_gp_boton_guardar")
        self.__p_modificar_gp_boton_limpiar = self.__builder.get_widget("modificar_gp_boton_limpiar")
        self.__p_modificar_gp_boton_cancelar = self.__builder.get_widget("modificar_gp_boton_cancelar")

        self.__p_mantenimiento_pilotos_paginador = self.__builder.get_widget("pagina_pilotos")
        self.__p_mantenimiento_pilotos_combobox_temporada = self.__builder.get_widget("mantenimiento_pilotos_combobox_temporada")
        self.__p_mantenimiento_pilotos_boton_aplicar = self.__builder.get_widget("mantenimiento_pilotos_boton_aplicar")
        self.__p_mantenimiento_pilotos_lista_pilotos = self.__builder.get_widget("mantenimiento_pilotos_lista_pilotos")
        self.__p_mantenimiento_pilotos_boton_anadir = self.__builder.get_widget("mantenimiento_pilotos_boton_anadir")
        self.__p_mantenimiento_pilotos_boton_borrar = self.__builder.get_widget("mantenimiento_pilotos_boton_borrar")
        self.__p_mantenimiento_pilotos_boton_editar = self.__builder.get_widget("mantenimiento_pilotos_boton_editar")
        self.__p_mantenimiento_pilotos_boton_atras = self.__builder.get_widget("mantenimiento_pilotos_boton_atras")
        self.__p_modificar_piloto_entrada_nombre_piloto = self.__builder.get_widget("modificar_piloto_entrada_nombre_piloto")
        self.__p_modificar_piloto_boton_fecha_nacimiento = self.__builder.get_widget("modificar_piloto_boton_fecha_nacimiento")
        self.__p_modificar_piloto_boton_cambiar_foto_piloto = self.__builder.get_widget("modificar_piloto_boton_cambiar_foto_piloto")
        self.__p_modificar_piloto_imagen_foto_piloto = self.__builder.get_widget("modificar_piloto_imagen_foto_piloto")
        self.__p_modificar_piloto_lista_equipos = self.__builder.get_widget("modificar_piloto_lista_equipos")
        self.__p_modificar_piloto_boton_cambiar_de_equipo = self.__builder.get_widget("modificar_piloto_boton_cambiar_de_equipo")
        self.__p_modificar_piloto_boton_guardar = self.__builder.get_widget("modificar_piloto_boton_guardar")
        self.__p_modificar_piloto_boton_limpiar = self.__builder.get_widget("modificar_piloto_boton_limpiar")
        self.__p_modificar_piloto_boton_cancelar = self.__builder.get_widget("modificar_piloto_boton_cancelar")

        self.__p_mantenimiento_equipos_paginador = self.__builder.get_widget("pagina_equipos")
        self.__p_mantenimiento_equipos_combobox_temporada = self.__builder.get_widget("mantenimiento_equipos_combobox_temporada")
        self.__p_mantenimiento_equipos_boton_aplicar = self.__builder.get_widget("mantenimiento_equipos_boton_aplicar")
        self.__p_mantenimiento_equipos_lista_equipos = self.__builder.get_widget("mantenimiento_equipos_lista_equipos")
        self.__p_mantenimiento_equipos_boton_anadir = self.__builder.get_widget("mantenimiento_equipos_boton_anadir")
        self.__p_mantenimiento_equipos_boton_borrar = self.__builder.get_widget("mantenimiento_equipos_boton_borrar")
        self.__p_mantenimiento_equipos_boton_editar = self.__builder.get_widget("mantenimiento_equipos_boton_editar")
        self.__p_mantenimiento_equipos_boton_atras = self.__builder.get_widget("mantenimiento_equipos_boton_atras")
        self.__p_modificar_equipo_entrada_nombre_equipo = self.__builder.get_widget("modificar_equipo_entrada_nombre_equipo")
        self.__p_modificar_equipo_boton_fecha_nacimiento = self.__builder.get_widget("modificar_equipo_boton_fecha_nacimiento")
        self.__p_modificar_equipo_boton_cambiar_foto_equipo = self.__builder.get_widget("modificar_equipo_boton_cambiar_foto_equipo")
        self.__p_modificar_equipo_imagen_foto_equipo = self.__builder.get_widget("modificar_equipo_imagen_foto_equipo")
        self.__p_modificar_equipo_lista_equipos = self.__builder.get_widget("modificar_equipo_lista_equipos")
        self.__p_modificar_equipo_boton_cambiar_de_equipo = self.__builder.get_widget("modificar_equipo_boton_cambiar_de_equipo")
        self.__p_modificar_equipo_boton_guardar = self.__builder.get_widget("modificar_equipo_boton_guardar")
        self.__p_modificar_equipo_boton_limpiar = self.__builder.get_widget("modificar_equipo_boton_limpiar")
        self.__p_modificar_equipo_boton_cancelar = self.__builder.get_widget("modificar_equipo_boton_cancelar")



        self.__builder.signal_autoconnect(self)
        
        if (self.ventana_principal):
            self.ventana_principal.connect("destroy", gtk.main_quit)




if __name__ == "__main__":
    APP = "pyF1"
    DIR = "./locale" #/usr/local/share/locale" #/usr/share/locale"
    gettext.textdomain(APP)
    gettext.bindtextdomain(APP, DIR)
    gtk.glade.textdomain(APP)
    gtk.glade.bindtextdomain(APP, DIR)
    gettext.install(APP, DIR, True)
    _ = gettext.gettext
    
    app = PyF1()
    app.ventana_principal.show()
    gtk.main()
