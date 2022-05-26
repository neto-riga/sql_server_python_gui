# %%
from sqlalchemy import create_engine
import pandas as pd
import PySimpleGUI as sg
import os
# %%
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-EKPLE5V'
DATABASE_NAME = 'AGENCIA'

DATABASE_CONNECTION = f"mssql://@{SERVER_NAME}/{DATABASE_NAME}?driver={DRIVER_NAME}"
engine = create_engine(DATABASE_CONNECTION)
conn = engine.connect()

# %%
layout = [
    [sg.Button('Inserción'), sg.Button('Visualización'),
    sg.Button('Actualización'), sg.Button('Eliminación')],
    [sg.Button('Cerrar')]
]

v_principal = sg.Window('Menu Principal', layout)
while True:
    event, values = v_principal.read()
    if event == 'Cerrar' or event == sg.WINDOW_CLOSED:
        break
    elif event == 'Inserción':
        layout2 = [
            [sg.Text('Seleccione la tabla a la cual añadirá datos')],
            [sg.Button('CLIENTE'), sg.Button('CARRO'), sg.Button('COMPRA'),
            sg.Button('MECANICO'), sg.Button('REPARACION')],
            [sg.Button('Regresar')]
        ]
        v_menu_insercion = sg.Window('Menu Inserción', layout2)
        while True:
            event2, values2 = v_menu_insercion.read()
            if event2 == 'Regresar' or event2 == sg.WINDOW_CLOSED:
                break
            elif event2 == 'CLIENTE':
                layout_cliente = [
                    [sg.Text('Ingrese los valores que desee añadir', font=(sg.DEFAULT_FONT, 15))],
                    [sg.Text('Nombre completo', size=(20, 1)), sg.Input(key='-NOMBRE-')],
                    [sg.Text('RFC', size=(20, 1)), sg.Input(key='-RFC-')],
                    [sg.Text('Direccion', size=(20, 1)), sg.Input(key='-DIR-')],
                    [sg.Text('Teléfono', size=(20, 1)), sg.Input(key='-TEL-')],
                    [sg.Button('Ingresar'), sg.Button('Cancelar')]
                ]
                v_datos_cliente = sg.Window('Inserción Cliente', layout_cliente)
                while True:
                    event_insercion, values_insercion = v_datos_cliente.read()
                    if event_insercion == 'Cancelar' or event_insercion == sg.WINDOW_CLOSED:
                        break
                    elif event_insercion == 'Ingresar': 
                        for key, val in values_insercion.items():
                            print(f"{key} {val}")
                        ### HACER CONSULTA AQUÍ
                        sg.popup_auto_close("Añadido con éxito")
                v_datos_cliente.close()
            elif event2  == 'CARRO':
                layout_carro = [
                    [sg.Text('Ingrese los valores que desee añadir', font=(sg.DEFAULT_FONT, 15))],
                    [sg.Text('Matrícula', size=(20, 1)), sg.Input(key='-MATRICULA-')],
                    [sg.Text('Modelo', size=(20, 1)), sg.Input(key='-MODELO-')],
                    [sg.Text('Color', size=(20, 1)), sg.Input(key='-COLOR-')],
                    [sg.Text('Precio', size=(20, 1)), sg.Input(key='-PRECIO-')],
                    [sg.Text('Marca', size=(20, 1)), sg.Input(key='-MARCA-')],
                    [sg.Button('Ingresar'), sg.Button('Cancelar')]
                ]
                v_datos_carro = sg.Window('Inserción Carro', layout_carro)
                while True:
                    event_insercion, values_insercion = v_datos_carro.read()
                    if event_insercion == 'Cancelar' or event_insercion == sg.WINDOW_CLOSED:
                        break
                    elif event_insercion == 'Ingresar': 
                        ### HACER CONSULTA AQUÍ
                        sg.popup_auto_close("Añadido con éxito")
                v_datos_carro.close()
            elif event2 == 'COMPRA':
                rfc_cliente = pd.read_sql_query('''SELECT RFC FROM CLIENTE ORDER BY RFC''', conn)
                mat_carro = pd.read_sql_query("""SELECT matricula FROM CARRO ORDER BY matricula""", conn)

                layout_compra = [
                    [sg.Text('Ingrese los valores que desee añadir', font=(sg.DEFAULT_FONT, 15))],
                    [sg.Text('Fechas en formato (aaaa-mm-dd)')],
                    [sg.Text("Fecha de Compra", size=(20, 1)), sg.Input(key='-FECHA_COMPRA-')],
                    [sg.Text('Forma de Pago', size=(20, 1)), sg.Input(key='-PAGO-')],
                    [sg.Text('RFC Cliente', size=(20, 1)),
                    sg.Listbox(rfc_cliente.values.tolist(), key='-RFC_CLIENTE-', size=(15, 2))],
                    [sg.Text('Matrícula del carro', size=(20, 1)), 
                    sg.Listbox(mat_carro.values.tolist(), key='-MATRICULA_CARRO-', size=(15, 2))],
                    [sg.Button('Ingresar'), sg.Button('Cancelar')]
                ]
                v_datos_compra = sg.Window('Inserción Compra', layout_compra)
                while True:
                    event_insercion, values_insercion = v_datos_compra.read()
                    if event_insercion == 'Cancelar' or event_insercion == sg.WINDOW_CLOSED:
                        break
                    elif event_insercion == 'Ingresar':
                        for llave, val in values_insercion.items():
                            print(f"{llave}  {val}")
                        ### HACER CONSULTA AQUÍ
                        sg.popup_auto_close("Añadido con éxito")
                v_datos_compra.close()
            elif event2 == 'MECANICO':
                layout_mecanico = [
                    [sg.Text('Ingrese los valores que desee añadir', font=(sg.DEFAULT_FONT, 15))],
                    [sg.Text('Nombre completo', size=(20, 1)), sg.Input(key='-NOMBRE-')],
                    [sg.Text('RFC', size=(20, 1)), sg.Input(key='-RFC-')],
                    [sg.Text('Turno', size=(20, 1)), sg.Input(key='-TURNO-')],
                    [sg.Text('Teléfono', size=(20, 1)), sg.Input(key='-TEL-')],
                    [sg.Button('Ingresar'), sg.Button('Cancelar')]
                ]
                v_datos_mecanico = sg.Window('Inserción Mecánico', layout_mecanico)
                while True:
                    event_insercion, values_insercion = v_datos_mecanico.read()
                    if event_insercion == 'Cancelar' or event_insercion == sg.WINDOW_CLOSED:
                        break
                    elif event_insercion == 'Ingresar': 
                        ### HACER CONSULTA AQUÍ
                        sg.popup_auto_close("Añadido con éxito")
                v_datos_mecanico.close()
            elif event2 == 'REPARACION':
                rfc_cliente = pd.read_sql_query('''SELECT RFC FROM CLIENTE ORDER BY RFC''', conn)
                rfc_mecanico = pd.read_sql_query('''SELECT RFC FROM MECANICO ORDER BY RFC''', conn)
                mat_carro = pd.read_sql_query("""SELECT matricula FROM CARRO ORDER BY matricula""", conn)

                layout_reparacion = [
                    [sg.Text('Ingrese los valores que desee añadir', font=(sg.DEFAULT_FONT, 15))],
                    [sg.Text('Fechas en formato (aaaa-mm-dd)')],
                    [sg.Text("Fecha de ingreso", size=(20, 1)), sg.Input(key='-FECHA_INGRESO-')],
                    [sg.Text("Fecha de entrega", size=(20, 1)), sg.Input(key='-FECHA_ENTREGA-')],
                    [sg.Text('Costo', size=(20, 1)), sg.Input(key='-COSTO-')],
                    [sg.Text('RFC cliente', size=(20, 1)),
                    sg.Listbox(rfc_cliente.values.tolist(), key='-RFC_CLIENTE-', size=(15, 2))],
                    [sg.Text('RFC mecánico', size=(20, 1)),
                    sg.Listbox(rfc_mecanico.values.tolist(), key='-RFC_MECANICO-', size=(15, 2))],
                    [sg.Text('Matrícula del carro', size=(20, 1)), 
                    sg.Listbox(mat_carro.values.tolist(), key='-MATRICULA_CARRO-', size=(15, 2))],
                    [sg.Button('Ingresar'), sg.Button('Cancelar')]
                ]
                v_datos_reparacion = sg.Window('Inserción Compra', layout_reparacion)
                while True:
                    event_insercion, values_insercion = v_datos_reparacion.read()
                    if event_insercion == 'Cancelar' or event_insercion == sg.WINDOW_CLOSED:
                        break
                    elif event_insercion == 'Ingresar':
                        for llave, val in values_insercion.items():
                            print(f"{llave}  {val}")
                        ### HACER CONSULTA AQUÍ
                        sg.popup_auto_close("Añadido con éxito")
                v_datos_reparacion.close()
        v_menu_insercion.close()
    elif event == 'Visualización':
        layout_visualizacion = [
            [sg.Text('Seleccione la tabla a la cual visualizará')],
            [sg.Button('CLIENTE'), sg.Button('CARRO'), sg.Button('COMPRA'),
            sg.Button('MECANICO'), sg.Button('REPARACION')],
            [sg.Button('Regresar')]
        ]
        v_visualizacion = sg.Window("Visualización de Datos", layout_visualizacion)
        while True:
            event_visual, values_visual = v_visualizacion.read()
            if event_visual in ('Regresar', sg.WIN_CLOSED):
                break
            elif event_visual in ['CLIENTE', 'CARRO', 'COMPRA', 'MECANICO', 'REPARACION']:
                query = pd.read_sql_query(f'''SELECT * FROM {event_visual}''', conn)
                values = query.values.tolist()
                headings = query.columns.to_list()
                layout_tablas = [
                    [sg.Table(values = values, headings=headings)],
                    [sg.Button("Regresar")]
                ]
                v_tablas = sg.Window(f"Tabla de {event_visual}", layout_tablas)
                while True:
                    event_tabla, vlaues_tabla = v_tablas.read()
                    if event_tabla in ("Regresar", sg.WIN_CLOSED):
                        break
                v_tablas.close()
        v_visualizacion.close()
    elif event == 'Actualización':
        layout_act = [
            [sg.Text('Seleccione la tabla a la cual se actualizarán valores')],
            [sg.Button('CLIENTE'), sg.Button('CARRO'), sg.Button('COMPRA'),
            sg.Button('MECANICO'), sg.Button('REPARACION')],
            [sg.Button('Regresar')]
        ]
        v_act = sg.Window("Actualización de datos", layout_act)
        while True:
            event_act, values_act = v_act.read()
            if event_act in ("Regresar", sg.WINDOW_CLOSED):
                break
            elif event_act in ['CLIENTE', 'CARRO', 'COMPRA', 'MECANICO', 'REPARACION']:
                q = pd.read_sql_query(f"""SELECT TOP 1 * FROM {event_act}""", conn)
                columnas = q.columns.to_list()
                layout_col = [
                    [sg.Text("Seleccione el valor a cambiar")],
                    [sg.Listbox(columnas, key='-VALOR-'), sg.Button("Seleccionar")],
                    [sg.Button('Regresar')]
                ]
                v_col = sg.Window("Selecciona la columna", layout_col)
                while True:
                    event_col, values_col = v_col.read()
                    if event_col in ("Regresar", sg.WINDOW_CLOSED):
                        break
                    elif event_col == "Seleccionar" and values_col["-VALOR-"][0] in columnas:
                        q_pk = pd.read_sql_query(f"""
                            SELECT column_name as PRIMARYKEYCOLUMN
                            FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS TC 

                            INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS KU
                                ON TC.CONSTRAINT_TYPE = 'PRIMARY KEY' 
                                AND TC.CONSTRAINT_NAME = KU.CONSTRAINT_NAME 
                                AND KU.table_name='{event_act}'

                            ORDER BY 
                                KU.TABLE_NAME
                                ,KU.ORDINAL_POSITION
                            ;
                        """, conn)
                        q2 = pd.read_sql_query(f"""SELECT {values_col['-VALOR-'][0]} FROM {event_act}""", conn)
                        if q_pk.values.tolist()[0][0] == values_col['-VALOR-'][0]:
                            q3 = q2.copy()
                        else:
                            q3 = pd.read_sql_query(f"""SELECT {q_pk.values.tolist()[0][0]} FROM {event_act}""", conn)
                        vals = q2.values[:,0].tolist()
                        val_pk = q3.values[:,0].tolist()
                        print(tuple(zip(val_pk, vals)))
                        layout_cambio = [
                            [sg.Text("Realice el cambio deseado", font=(sg.DEFAULT_FONT, 15))],
                            [sg.Text(f"Se muestra la clave {q_pk.values.tolist()[0][0]} junto con los valores a cambiar de {values_col['-VALOR-'][0]}")],
                            [sg.Listbox(tuple(zip(val_pk, vals)), size=(60, 3))],
                            [sg.Text("Ingrese el nuevo valor"), sg.Input(key='-VAL-')],
                            [sg.Button("Aceptar"), sg.Button("Regresar")]
                        ]
                        v_cambio = sg.Window("Inserción de datos", layout_cambio)
                        while True:
                            event_cambio, values_cambio = v_cambio.read()
                            if event_cambio in ("Regresar", sg.WINDOW_CLOSED):
                                break
                        v_cambio.close()
                v_col.close()
        v_act.close()
    elif event == 'Eliminación':
        layout_elim = [
            [sg.Text('Seleccione la tabla a la cual se eliminarán valores')],
            [sg.Button('CLIENTE'), sg.Button('CARRO'), sg.Button('COMPRA'),
            sg.Button('MECANICO'), sg.Button('REPARACION')],
            [sg.Button('Regresar')]
        ]
        v_elim = sg.Window("Eliminación de datos", layout_elim)
        while True:
            event_elim, values_elim = v_elim.read()
            if event_tabla in ("Regresar", sg.WIN_CLOSED):
                break

        v_elim.close()
v_principal.close()