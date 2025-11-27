# FastAPI Curso

Este proyecto es un ejemplo básico de una aplicación FastAPI gestionada con `uv`.

## Requisitos previos

Necesitas tener instalado `uv` para gestionar las dependencias y el entorno virtual.

### Instalación de uv

Puedes instalar `uv` ejecutando el siguiente comando en tu terminal (macOS/Linux):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Para Windows:

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Inicialización y Ejecución

1.  **Clonar el repositorio** (si aplica) o navegar a la carpeta del proyecto.

2.  **Instalar dependencias**:
    Si ya existe un archivo `pyproject.toml` o `uv.lock`, `uv` creará el entorno virtual automáticamente al ejecutar cualquier comando.

3.  **Ejecutar el servidor de desarrollo**:
    Para levantar la aplicación utilizando `uvicorn` dentro del entorno gestionado por `uv`, ejecuta:

    ```bash
    uv run uvicorn main:app --reload
    ```

    Esto iniciará el servidor en `http://127.0.0.1:8000`. El flag `--reload` permite que el servidor se reinicie automáticamente al detectar cambios en el código.

## Gestión de Paquetes

Para añadir una nueva librería al proyecto, utiliza el comando `uv add`. Por ejemplo, para añadir `requests`:

```bash
uv add requests
```

Esto actualizará automáticamente tu archivo `pyproject.toml` y el archivo de bloqueo `uv.lock`.