"""
blocklist.py

Este archivo solo contiene la lista de bloqueo de los tokens JWT. Será importado por
la aplicación y el recurso de cierre de sesión para que los tokens puedan agregarse a la lista de bloqueo cuando el
usuario cierra sesión.
"""

BLOCKLIST = set()