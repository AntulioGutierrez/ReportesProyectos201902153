var updateBtns = document.getElementsByClassName('actualizar-carrito')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productoId = this.dataset.iddelarticulo
        var accion = this.dataset.accion
        //console.log('idproducto: ', productoId, 'hacer: ', accion)
        //console.log('el que esta aqui es: ', usuario)
        if (usuario === 'AnonymousUser'){
            agregarElementoAlCookie(productoId, accion)
        }
        else{
            actualizarOrdenUsuario(productoId, accion)
        }
        
    })
}

function actualizarOrdenUsuario(productoId, accion){
    console.log('ingreso usuario  enviando datos .....')

    var url = '/actualizarItem/'
    fetch(url,{
        method:'POST', 
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'iddelarticulo': productoId, 'hacer': accion})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('mensaje', data)
        location.reload(true);//investigar como quitar esto y que actualize los datos de del carrito sin recargar la pagina
    })
}

function agregarElementoAlCookie(productoId, accion){
    console.log('NO HAY USUARIO LOGUEADO')
    
    if (accion == 'agregar'){
        if (carrito[productoId] == undefined){
            carrito[productoId] = {'quantity':1}
        }else{
            carrito[productoId]['quantity'] += 1
        }
    }

    if (accion == 'quitar'){
        carrito[productoId]['quantity'] -= 1

        if (carrito[productoId]['quantity'] <= 0){
            console.log('Producto Eliminado')
            delete carrito[productoId]
        }
    }
    console.log('Carrito:', carrito)
    document.cookie = 'carrito=' + JSON.stringify(carrito) + ";domain=;path=/"
    location.reload()
}