# Sesion Practica "React"

## Descripcion:

Mostramos a nuestros compañeros el uso basico de React explicando que es, que son los componentes en react y por que recomendamos que sea utilizado a comparacion de otras librerias que pueden hacer casi lo mismo.

[Presentacion utilizada](React.pdf)

## Actividad Realizada

### Antes de empezar

1. Usaremos un editor de codigo web llamado [**codeSandBox**](https://codesandbox.io/s/xenodochial-voice-15p1ln?file=/src/App.js) donde ya tiene instalado React para ahorrar el tiempo de instalacion.  

    Si gustan instalarlo en otro momento, vean el siguiente [**tutorial**](https://victorroblesweb.es/2019/09/18/como-instalar-react-desde-cero-2019/).  

<br>

  
2. Utilizaremos la siguiente plantilla de html y css para modificarlo e implementarle las funcionalidades de React. Como se puede observar, parte de HTML se usara en componentes.  
   

    HTML

    ```html
        <body>
            <div class="Main-container">
                <div class="container-login">
                    <div class="wrap-login">

                        <div class="login-pic">
                            <img src="img.png" alt="IMG">
                        </div>

                        
                        <!--------Inicio-Login----------------->
                        <form class="login-form">
                            <span class="login-form-title">Login</span>

                            <div class="wrap-input">
                                <input type="text" class="input" name="email" placeholder="Email" required>
                                <span class="focus-input"></span>
                                <span class="symbol-input">
                                    <i class="fa fa-envelope" aria-hidden="true"></i>
                                </span>
                            </div>
                            <div class="wrap-input">
                                <input type="password" class="input" name="pass" placeholder="Password" required>
                                <span class="focus-input"></span>
                                <span class="symbol-input">
                                    <i class="fa fa-lock" aria-hidden="true"></i>
                                </span>
                            </div>
                            <!---------/login------->

                            
                            <!---------LoginBtn------->
                            <div class="login-form-btn-container">
                                <button class="login-form-btn">Login</button>
                            </div>

                            <div class="text-center p-t-1">
                                <span class="txt1">Forgot</span>
                                <a href="#" class="txt2"> Username / Password ?</a>
                            </div>

                            <div class="text-center p-t-2">
                                <a href="#" class="txt2">Create Your Account <i class="fa fa-long-arrow-right " aria-hidden="true"></i></a>
                            </div>
                        <!---------/LoginBtn------->

                        </form>
                    </div>
                </div>
            </div>
        </body>
    ```

<br>


3. Ahora vamos a crear una carpeta llamada "**componentes**" que se encontrara dentro de la carpeta src.

![imagen de componentes](imagenes/componentes.png)

Además crearemos otra carpeta dentro de src que se llamará "imagenes", nos servirá para almacenar la imagen a mostrar.  
Nuestra carpeta src deberá verse similar a esto.

![imagen de carpeta imagen](imagenes/carpeta_imagenes.png)

<br>

4. Ahora vamos a crear nuestro primer componente, para esto necesitamos crear un archivo dentro de la carpeta "componentes", este archivo se llamara '**Login.js**'

<br>

5. Dentro de nuestro nuevo archivo, escribiremos lo siguiente:

```javascript

import React from 'react';

const Login = () => {

    return (



    )
}

export default Login;
```

<br>

6. Vamos a trasladar el codigo correspondiente al inicio de sesion y lo colocaremos dentro de los parentesis del return del componente que acabamos de crear. El resultado quedara algo similar a esto.

```javascript

import React from 'react';

const Login = () => {

    return (

        <form class="login-form">
            <span class="login-form-title">Login</span>

             <div class="wrap-input">
                <input type="text" class="input" name="email" placeholder="Email" required />
                <span class="focus-input"></span>
                <span class="symbol-input">
                    <i class="fa fa-envelope" aria-hidden="true"></i>
                </span>
            </div>
                <div class="wrap-input">
                    <input type="password" class="input" name="pass" placeholder="Password" required />
                    <span class="focus-input"></span>
                    <span class="symbol-input">
                        <i class="fa fa-lock" aria-hidden="true"></i>
                </span>
            </div>
        </form>

    )
}

export default Login;
```

<br>

7. Listo!, ya tenemos nuestro primer componente, ahora vamos a crear el componente de los botones de inicio de sesion, para esto vamos a realizar el mismo procedimiento.
Primero creamos un nuevo archivo llamado '**LoginBtn.js**' dentro de la carpeta componentes.

<br>

8. Posteriormente, escribimos lo siguiente:

```javascript

import React from 'react';


const Button = () => {

    return (
        

        
    )

}

export default Button;
```

<br>

9. Luego, agregamos el codigo HTML que corresponde al boton de inicio de sesion y lo colocamos dentro del return. El codigo de este componente quedará de la siguiente manera:


```javascript
import React from 'react';

const Button = () => {

    return (
        <div class="login-form-btn-container">
            <button class="login-form-btn">Login</button>

            <div class="text-center">
                <span class="txt1">Forgot</span>
                    <a href="" class="txt2"> Username / Password ?</a>
                </div>

                <div class="text-center ">
                    <a href="" class="txt3">Create Your Account <i class="fa fa-long-arrow-center " aria-hidden="true"></i></a>
                </div>
        </div>

    )

}

export default Button;
```

<br>


10. Para finalizar, haremos el ultimo componente el cual sera la imagen que se va a mostrar. Este componente es mas corto y para esto necesitamos crear un archivo llamado 'Image.js' y escribiremos el siguiente codigo. Mas aparte la imagen que se les dara en breves en el chat. por defecto su nombre es "logo_uady.png", por favor coloquenlo en la carpeta imagenes.

```javascript

import React from 'react';
import logo_uady from './src/imagenes/logo_uady.png'

const Image = () => {

    return (

        <img src= {logo_uady} className='imagen' />
    )

}
export default Image;
```


<br>


<h2>Modificando el Index.js</h2>
<br>

11. Ahora, si queremos que nuestros componentes se vean en nuestra pagina web, debemos crear un **index.js** e importar todo lo necesario, esto quiere decir importar React, ReactDOM, el CSS correspondiente y los componentes que acabamos de crear.

```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

import Login from './componentes/Login'
import Image from './componentes/Image';
import LoginBtn from './componentes/LoginBtn'
```

<br>

12. Ahora, vamos a crear una constante a la que le asignaremos el método render de ReactDOM, esto es para que se puedan renderizar o "imprimir por pantalla" todos los componentes que hemos creado.

```javascript

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(

  <>
  <Login />
  <Button />
  <Image />
  </>
    
);
```

<br>


<h2>El index.js queda de la siguiente manera... </h2>
<br>

```javascript

import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.js';

import Login from './components/Login'
import Image from './components/Image';
import LoginBtn from './components/LoginBtn'

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(

  <>
  <Login />
  <Button />
  <Image />
  </>
    
);

```


<h2>Implementamos el CSS </h2>
<br>

13. Implementamos el archivo CSS copiando el codigo en el archivo styles.css

```css
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700&display=swap');

    *{
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}
body, html{
  height: 100%;
  font-family: 'Poppins',sans-serif;
  font-weight: 400;
  background-color: white;
}

:root {
  width: 100%;
  float: right;
  position: relative;
  padding: 2rem
}

.imagen{
  width: 40%;
  position: relative;

}

.Main-container{
  width: 100%;
  margin: 0 auto;
}
.container-login{
  width: 80%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding: 15px;
  background: #9053c7;
  background: linear-gradient(-135deg, #c850c0, #4158d0);
}
.wrap-login{
  width: 960px;
  background: #fff;
  border-radius: 10px;
  overflow: hidden;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  padding: 177px 130px 33px 95px;
}
.login-pic{
  width: 316px;
}
.login-pic img{
  max-width: 100%;
}
.login-form{
  width: 50%;
  position: relative;
  float: right;
  margin: 1rem;
}


.login-form-title{
  font-family: 'poppins', sans-serif;
  font-size: 24px;
  color: #333333;
  line-height: 1.2;
  text-align: center;
  font-weight: 700;
  width: 100%;
  display: block;
  padding-bottom: 54px;
}
.wrap-input{
  position: relative;
  width: 100%;
  z-index: 1;
  margin-bottom: 10px;
}
.input{
  font-family: 'Poppins' , sans-serif;
  font-size: 15px;
  font-weight: 500;
  line-height: 1.5;
  color: #666666;
  outline: none;
  border: none;
  display: block;
  width: 100%;
  background: #e6e6e6;
  height: 50px;
  border-radius: 25px;
  padding: 0 30px 0 68px;
}
.focus-input{
  display: block;
  position: absolute;
  border-radius: 25px;
  bottom: 0;
  left: 0;
  z-index: -1;
  width: 100%;
  height: 100%;
  box-shadow: 0px 0px 0px 0px;
  color: rgba(87, 184,70, 0.8);
}
.input:focus + .focus-input{
  animation:  anim-shadow 0.5s ease-in-out forwards;
}
@-webkit-keyframes anim-shadow{
  to {
      box-shadow:  0px 0px 70px 25px ;
      opacity: 0;
  }
}
@keyframes anim-shadow{
  to {
      box-shadow:  0px 0px 70px 25px ;
      opacity: 0;
  }
}

.symbol-input{
  font-size: 15px;
  display: flex;
  align-items: center;
  position: absolute;
  border-radius: 25px;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  padding-left: 35px;
  pointer-events: none;
  color: #666666;
  transition: all 0.4s
}
.input:focus + .focus-input + .symbol-input{
  color: #57b846;
  padding-left: 28px;
}

.login-form-btn-container{
  width: 50%;
  float: right;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding-top: 20px;
}
.login-form-btn{
  font-family:'poppins',sans-serif ;
  font-size: 15px;
  line-height: 1.5;
  color: #fff;
  background: #57b846;
  text-transform: uppercase;
  width: 100%;
  height: 50px;
  border-radius: 25px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 25px ;
  transition: all 0.4s;
  border: none;

}
.login-form-btn:hover{
  background: #333333;
}
.text-center{
  text-align: center;
}
.txt1{
  font-family: 'poppins';
  font-size: 13px;
  line-height: 1.5;
  color: #666666;
}
.txt2{
  font-family: 'poppins';
  font-size: 13px;
  line-height: 1.5;
  color: #666666;
  padding: 1px;
}

.txt3{
  font-family: 'poppins';
  font-size: 13px;
  line-height: 1.5;
  color: #666666;
  padding: 20px;
}


a{
  font-family: 'poppins', sans-serif;
  font-size: 14px;
  line-height: 1.7;
  color: #666666;
  margin: 0px;
  transition: all 0.4s;
  text-decoration: none;
  font-weight: 400;
}
a:focus{
  outline: none !important;
}
a:hover{
  color: #57b846;
}
button{
  outline: none !important;
  border: none;
  background: transparent;
}
button:hover{
  cursor: pointer;
}

/* Responsive */
@media (max-width: 992px){

.wrap-login{
  padding: 177px 90px 33px 85px;
}

.login-pic{
  width: 35%;
}
.login-form{
  width: 50%;
}

}


@media (max-width: 768px){
  .wrap-login{
      padding: 100px 80px 33px 80px;
  }
  
  .login-pic{
  display: none;
  }
  .login-form{
      width: 100%;
  } 
}


@media (max-width: 576px){
  .wrap-login{
      padding: 100px 15px 33px 15px;
  }
}

    
```

Ahora podran ver la pagina simulada para registrarte. todo esto usando componentes.