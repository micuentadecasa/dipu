# App de Tests - Oposición Diputación de Albacete

Aplicación estática para estudiar el examen de **Diseñador/a de Aplicaciones (Grupo C1, Subescala Técnica)**.

La versión actual está preparada para alojarse gratis en **GitHub Pages**: no necesita Flask, SQLite, backend ni API keys. Las preguntas se cargan desde `frontend/src/questions.js`, generado a partir de `seed_data.py`.

## how to run locally
If you want to test the exact production build that GitHub Pages will use:                                                                            
                                                                                                                                                       
 ```bash                                                                                                                                               
   cd /Users/luis/projects/dipu/frontend                                                                                                               
   npm run build                                                                                                                                       
   npm run preview      

 ```                                                                                                                                                   
                                                                                                                                                       
 Then open the preview URL shown, usually:                                                                                                             
                                                                                                                                                       
 ```text                                                                                                                                               
   http://localhost:4173                                                                                                                               
 ```                            


 ## How to host it on GitHub Pages                                                                                                                        
                                                                                                                                                       
 1. Push this project to GitHub.                                                                                                                       
 2. Go to your repository on GitHub.                                                                                                                   
 3. Open:                                                                                                                                              
                                                                                                                                                       
 ```text                                                                                                                                               
   Settings → Pages                                                                                                                                    
 ```                                                                                                                                                   
                                                                                                                                                       
 4. Under Build and deployment, set:                                                                                                                   
                                                                                                                                                       
 ```text                                                                                                                                               
   Source: GitHub Actions                                                                                                                              
 ```      
                                                                                                                                              
                                                                                                                                                       
 5. Push to the main branch.                                                                                                                           
 6. GitHub will run the workflow in:                                                                                                                   
                                                                                                                                                       
 ```text                                                                                                                                               
   .github/workflows/deploy.yml                                                                                                                        
 ```                                                                                                                                                   
                                                                                                                                                       
 7. When it finishes, your app will be available at something like:                                                                                    
                                                                                                                                                       
 ```text                                                                                                                                               
   https://YOUR_USERNAME.github.io/YOUR_REPOSITORY_NAME/                                                                                               
 ```                                                                                                                                                   
                                                                                                                                                       
 You can check the deployment progress under the repository’s Actions tab.      

## Qué hace

- Al entrar crea una ronda de **30 preguntas aleatorias**.
- Puedes responder pregunta por pregunta.
- La corrección es inmediata:
  - respuesta correcta: verde;
  - respuesta incorrecta: rojo y la correcta aparece en verde.
- Abajo hay un botón para **mostrar/ocultar las respuestas correctas**, útil para estudiar al principio.
- Botón de **Nueva ronda de 30** para practicar otra selección aleatoria.

## Desarrollo local

```bash
cd frontend
npm install
npm run dev
```

Abre la URL que muestre Vite, normalmente `http://localhost:5173`.

## Compilar

```bash
cd frontend
npm run build
```

La web lista para publicar queda en `frontend/dist/`.

## Publicar gratis en GitHub Pages

### Opción recomendada: GitHub Actions

1. Sube el proyecto a un repositorio de GitHub.
2. Crea el archivo `.github/workflows/deploy.yml` con este contenido:

```yaml
name: Deploy GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
          cache-dependency-path: frontend/package-lock.json
      - run: npm ci
        working-directory: frontend
      - run: npm run build
        working-directory: frontend
      - uses: actions/upload-pages-artifact@v3
        with:
          path: frontend/dist

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

3. En GitHub ve a **Settings → Pages**.
4. En **Build and deployment**, selecciona **Source: GitHub Actions**.
5. Haz push a `main`.
6. Cuando termine la acción, la app estará en una URL como:

```text
https://TU_USUARIO.github.io/NOMBRE_DEL_REPO/
```

### Opción manual rápida

También puedes ejecutar:

```bash
cd frontend
npm run build
```

y subir el contenido de `frontend/dist/` a la rama/configuración que uses para Pages.

## Archivos importantes

| Archivo | Función |
| --- | --- |
| `frontend/src/App.jsx` | App de test estática |
| `frontend/src/App.css` | UI nueva |
| `frontend/src/questions.js` | Banco de preguntas usado por GitHub Pages |
| `seed_data.py` | Fuente original de preguntas |
| `temario.md` | Temario oficial |

## Nota sobre el backend anterior

Los archivos `app.py`, `db.py`, `generator.py`, `templates/` y `static/` pertenecen a la versión Flask anterior. GitHub Pages no ejecuta Python ni SQLite, por eso la app publicada usa únicamente React + datos estáticos.
