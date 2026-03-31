import sqlite3

def crear_tabla_usuarios():
    # Creamos el archivo de la base de datos
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    
    # Creamos la tabla con la columna para contar los créditos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            nombre TEXT,
            es_real BOOLEAN DEFAULT 0,
            puntos_confianza FLOAT DEFAULT 0.0,
            creditos_usados INTEGER DEFAULT 0
        )
    ''')
    
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_tabla_usuarios()
