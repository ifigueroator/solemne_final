
  $(document).ready(function () {
      $("form[name='validaFormulario']")
          .validate({
              errorElement: 'span',
              errorPlacement: function (error, element) {
                  error.addClass('invalid-feedback');
                  element.closest('.col-sm-12').append(error);
                  element.closest('.col-md-6').append(error);
                  element.closest('.col-md-2').append(error);
                  
              },
              highlight: function (element, errorClass, validClass) {
                  $(element).addClass('is-invalid');
              },
              unhighlight: function (element, errorClass, validClass) {
                  $(element).removeClass('is-invalid');
              },
              rules: {
                  txtNombre: {
                      required: true,
                      normalizer: function (value) {
                          return $.trim(value);
                      },
                  },
                  txtUsuario: {
                    required: true,
                    normalizer: function (value) {
                        return $.trim(value);
                    },
                },

                txtUsuarioi: {
                    required: true,
                    normalizer: function (value) {
                        return $.trim(value);
                    },
                },
                txtPass: {
                      required: true,
                      minlength: 8,
                    
                  },

                  txtPassR: {
                    required: true,
                   
                    equalTo:"#txtPass"
                  
                },

                  txtCorreo: {
                    required: true,
                    email: true,
                  
                },


                  txtTelefono:{
                    required: true,
                  
            matches   : "^(\\d|\\s)+$",
            minlength : 10,
            maxlength : 20
                  },
                  txtObs: {
                      required: true,
                      normalizer: function (value) {
                          return $.trim(value);
                      },
                  },
                  genero: {
                      required: true
                  },
                  comunas: {
                      required: true
                  },
              },
              messages: {
                  txtNombre: {
                  required:'Favor ingrese su nombre y apellido'},  

                  txtCorreo: {
                  required: 'El correo debe tener el siguiente formato Ejemplo: correo@correo.cl'},
            
                  txtTelefono: {
                  required:  'El campo Telefono debe tener 9 digitos'},

                  txtObs: {
                  required:'Favor ingrese sus comentarios.'},  
                                   
                  txtUsuario: {
                  required:'Favor ingrese un usuario'},

                 txtPass: {
                 required:'Debe ingresar una contraseña no menor a 8 digitos',
                 min: 'Debe ser mínimo 8'},  
                                                             
                 txtPassR: {
                 required:'La Contraseña no es igual a la ingresada',
                 equalTo:'Debe ser igual a la contraseña ingresada'},                                                            }, 
               
                  
          
                 
          })

  });




   