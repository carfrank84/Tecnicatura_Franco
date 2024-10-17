# CLASE 01 MIÉRCOLES 14 DE AGOSTO DEL 2024 - Portafolio 1
## USO DE GITHUB Parte 1

GitHub es una plataforma que nos permite guardar repositorios de Git que podemos usar como servidores remotos y ejecutar algunos comandos de forma visual e interactiva (sin necesidad de la consola de comandos).

Luego de crear nuestra cuenta, podemos crear o importar repositorios, crear organizaciones y proyectos de trabajo, descubrir repositorios de otras personas, contribuir a esos proyectos, dar estrellas y muchas otras cosas.

### COMANDOS

- **Import repository**, **New repository**, **New organization**: significa que es como tu empresa.
- **New project**: significa que es como un grupo de repositorios que puedes tener dentro de una empresa.
- **New gist**: es un pedazo de código que puedes compartir.

#### New repository
Ponemos el nombre: `class-git`, descripción: "Haremos un blog increíble", hay muchas licencias para publicar el código: NO lo hacemos ahora.

#### Create repository
Lo ponemos en **privado** o en **público**.

El `README.md` es el archivo que veremos por defecto al entrar a un repositorio. Es una muy buena práctica configurarlo para describir el proyecto,

### CLASE 02 MIÉRCOLES 21 DE AGOSTO DEL 2024 - Portafolio 2 ###

## Vamos a cargar la llave SSH pública en GitHub

Para copiar la llave pública debes ir al archivo `.ssh` y allí encontrarás el archivo `.pub`. Lo puedes abrir con un editor de texto y luego copiar el contenido que está dentro.

### Copiar la llave pública

1. Ir a GitHub, ir a **Settings**.
2. Ir a **SSH and GPG keys**.
3. Crear una nueva: **New SSH key**, poner nombre y pegar la SSH pública. Con esto está listo.

Aconsejo que la SSH tenga el nombre del ordenador en el que estás trabajando. Esto se debe hacer con cada PC nueva o dispositivo nuevo que tengamos para acceder a nuestra cuenta de GitHub.

### Comandos Git

- `git branch`: Vemos en qué rama estamos.
- `git checkout master`: Nos posicionamos en la rama `master`.
- `git branch -M main`: Cambiamos el nombre de la rama `master` a `main`.
- `git remote add origin git@github.com:nombreUsuario/class-git.git`: Agregamos el repositorio remoto, este es un ejemplo.
- `git remote -v`: Verificamos si ya está conectado.
- `git merge segunda`: Mergeamos lo que tenemos en la rama `segunda` en `main`.
- `git commit -am "Uso de GitHub parte 20"`: Hacemos el commit de hoy.
- `git push origin main`: Pasamos todo lo hecho a GitHub. Revisar en el repositorio en GitHub.

### Cambio de nombre de la rama master a main

Suele suceder que en el repositorio de GitHub se hayan creado dos ramas: la rama `master` y la rama `main`. Se debe:

1. Ir al repositorio en **Settings**.
2. Cambiar la rama principal de `master` a `main`.
3. Luego de eso, ya podemos borrar la rama `master`.

### CLASE 03 MIÉRCOLES 28 DE AGOSTO DEL 2024 - Portafolio 3 ###

## Cambios en GitHub: de master a main

El escritor argentino Julio Cortázar afirma que las palabras tienen color y peso. Por otro lado, los sinónimos existen por definición, pero no expresan lo mismo. Feo no es lo mismo que desagradable, ni aromático es lo mismo que oloroso.

Por lo anterior, podemos afirmar que los sinónimos no expresan lo mismo, no tienen el mismo "color" ni el mismo "peso".

Sí, esta lectura es parte de la enseñanza profesional de **Git & GitHub**.

Desde el 1 de octubre de 2020, GitHub cambió el nombre de la rama principal: ya no es "master" —como aprenderás aquí— sino **main**.

Este cambio fue derivado de una profunda reflexión ocasionada por el movimiento **#BlackLivesMatter**.

La industria de la tecnología lleva muchos años usando términos como **master**, **slave**, **blacklist** o **whitelist** y esperamos que pronto puedan ir desapareciendo.

Y sí, las palabras importan.

Por lo que de aquí en adelante, cada vez que me escuches mencionar "master", debes saber que hago referencia a "main".

### ¿Cuándo sigue siendo master y cuándo sigue siendo main? ###

Cuando se crea un repositorio desde **git bash** en nuestro ordenador a través de `git init`, sigue siendo el estándar como **master**. ¿Qué hacer con esto? Debes cambiar el nombre de la rama master a main con el comando:

git branch -M main


### CLASE 04 MIÉRCOLES 4 DE SEPTIEMBRE DEL 2024 - Portafolio 4 ###

### Tu primer push ###

La creación de las SSH es necesaria solo una vez por cada computadora. Aquí conocerás cómo conectar a GitHub usando SSH.

Luego de crear nuestras llaves SSH, podemos entregarle la llave pública a GitHub para comunicarnos de forma segura y sin necesidad de escribir nuestro usuario y contraseña todo el tiempo.

Para esto debes entrar a la **Configuración de Llaves SSH** en GitHub, crear una nueva llave con el nombre que desees y el contenido de la llave pública de tu computadora.

Ahora podemos actualizar la URL que guardamos en nuestro repositorio remoto, solo que, en vez de guardar la URL con HTTPS, vamos a usar la URL con SSH:

git remote set-url origin url-ssh-del-repositorio-en-github

### CLASE 05 MIÉRCOLES 11 DE SEPTIEMBRE DEL 2024 - Portafolio 5 ###

### Git tag y versiones en GitHub ###

En Git, las etiquetas o **Git tags** tienen un papel importante al asignar versiones a los commits más significativos de un proyecto. Aprender a utilizar el comando `git tag`, entender los diferentes tipos de etiquetas, cómo crearlas, eliminarlas y compartirlas, es esencial para un flujo de trabajo eficiente.

### Creación de etiquetas en Git

git tag


### CLASE 06 MIÉRCOLES 18 DE SEPTIEMBRE DEL 2024 - Portafolio 6 ###

## Error con los tags
### Investigación: ¿Qué pasa si por error cargamos un tag dos veces?

**¿Cómo solucionarías este problema o error?**

La respuesta debe ser enviada antes de las **23 horas** por cada grupo. Deben enviar comandos y todos los pasos que harían frente a este conflicto. (tarea enviada al profesor ariel mediante correo electronico) 
# CLASE 07 MIÉRCOLES 25 DE SEPTIEMBRE DEL 2024 - Portafolio 7

## Error con los tags

### Investigación: 
Si un tag es imposible generarlo dos veces, ¿cómo es que existe el error de dos tags con el mismo nombre?

### ¿Cómo se origina este problema o error?

La respuesta debe ser enviada antes de las 23 horas por cada grupo. Deben enviar comandos y todos los pasos que harían frente a este conflicto.

# CLASE 08 MIÉRCOLES 2 DE OCTUBRE DEL 2024 - Portafolio 8

## Manejo de ramas en GitHub

Si no te funciona el comando gitk es posible no lo tengas instalado por defecto. Para instalar gitk debemos ejecutar los siguientes comandos:


  sudo apt-get update
  sudo apt-get install gitk
  Repasa: ¿Qué es Git?
Las ramas nos permiten hacer cambios a nuestros archivos sin modificar la versión principal (main). Puedes trabajar con ramas que nunca envías a GitHub, así como pueden haber ramas importantes en GitHub que nunca usas en el repositorio local. Lo crucial es que aprendas a manejarlas para trabajar profesionalmente.

Si, estando en otra rama, modificamos los archivos y hacemos commit, tanto el historial(git log) como los archivos serán afectados. La ventaja que tiene usar ramas es que las modificaciones solo afectarán a esa rama en particular. Si luego de “guardar” los archivos(usando commit) nos movemos a otra rama (git checkout otraRama) veremos como las modificaciones de la rama pasada no aparecen en la otraRama.



### CLASE 09 MIÉRCOLES 9 DE OCTUBRE DEL 2024 - Portafolio 9

## Tarea para antes de las 23 horas

Investigar cómo se puede clonar un repo con el HTTPS del mismo, es decir, siendo ustedes los dueños del repositorio, y desde la nube quieren traer este repo a nuestro ordenador. Nos pedirá **Username** y **password**: ¿qué se debe hacer para lograr hacer cambios y así utilizar `pull`, `push`, y todo lo necesario para trabajar? Como referencia les digo que solo usuario y contraseña no serán suficientes, esto cambió desde el año 2021 y ahora hay algo más para poder hacer esto y tener así acceso total.

## Configurar múltiples colaboradores en un repositorio de GitHub ###

Por defecto, cualquier persona puede clonar o descargar tu proyecto desde GitHub, pero no pueden crear commits ni ramas. Esto quiere decir que pueden copiar tu proyecto, pero no colaborar con él. Si este es público, de otra manera, si es privado, es necesario que realmente estés haciendo una invitación; sino, no lo van a poder ver. Existen varias formas de solucionar esto para poder aceptar contribuciones. Una de ellas es añadir a cada persona de nuestro equipo como colaborador de nuestro repositorio.

### Cómo agregar colaboradores en GitHub ###

Solo debemos entrar a la configuración de colaboradores de nuestro proyecto. Se encuentra en:

`Repositorio > Settings > Collaborators`

Ahí, debemos añadir el email o username de los nuevos colaboradores.

### Modificar un mensaje de commit erróneo

Si, como colaborador, agregaste erróneamente el mensaje del commit, lo puedes cambiar de la siguiente manera:


### Hacer un commit con el nuevo mensaje que queremos ###
git commit --amend # Corregimos el mensaje
git pull origin main # Traer el repositorio remoto
git push --set-upstream origin main # Ejecutar el cambio, el error arreglado

# CLASE 10 MIÉRCOLES 16 DE OCTUBRE DEL 2024 - Portafolio 10

## Flujo de trabajo profesional

### Haciendo merge de ramas de desarrollo a main

Para poder desarrollar software de manera óptima y ordenada, necesitamos tener un flujo de trabajo profesional, que nos permita trabajar en conjunto sin interrumpir el trabajo de otros desarrolladores.

Una buena práctica de flujo de trabajo sería la siguiente:

1. Crear ramas
2. Asignar una rama a cada programador
3. El programador baja el repositorio con `git pull origin master`
4. El programador cambia de rama
5. El programador trabaja en esa rama y hace commits
6. El programador sube su trabajo con `git push origin #nombre_rama`
7. El encargado de organizar el proyecto baja, revisa y unifica todos los cambios
