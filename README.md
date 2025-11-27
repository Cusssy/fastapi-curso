## Inicialización del Proyecto con `uv`

`uv` es un instalador y gestor de paquetes de Python extremadamente rápido, escrito en Rust. Se utiliza para gestionar dependencias y entornos virtuales de manera eficiente.

### 1. Instalación de `uv`

#### macOS y Linux
Para instalar `uv` en sistemas basados en Unix, puedes usar el siguiente comando en tu terminal:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows
En Windows, puedes instalarlo usando PowerShell:

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Alternativamente, si ya tienes `pip` instalado, puedes instalar `uv` como un paquete de Python (aunque se recomienda el script de instalación independiente):

```bash
pip install uv
```

### 2. Inicializar un nuevo proyecto

Una vez instalado, puedes inicializar un nuevo entorno virtual y estructura de proyecto.

1.  **Crear un entorno virtual:**
    `uv` puede crear un entorno virtual (`.venv`) mucho más rápido que las herramientas tradicionales.

    ```bash
    uv venv
    ```

2.  **Activar el entorno virtual:**

    *   **macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```
    *   **Windows:**
        ```powershell
        .venv\Scripts\activate
        ```

3.  **Instalar dependencias:**
    Para instalar paquetes, utiliza `uv pip install`. Por ejemplo, para instalar FastAPI y Uvicorn:

    ```bash
    uv pip install fastapi uvicorn
    ```

4.  **Generar archivo de requisitos (opcional):**
    Si necesitas generar un archivo `requirements.txt` basado en tu entorno actual:

    ```bash
    uv pip freeze > requirements.txt
    ```

5.  **Instalar desde requirements.txt:**
    Si ya tienes un archivo de requisitos:

    ```bash
    uv pip install -r requirements.txt
    ```