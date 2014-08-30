
  function allusers()
  {

    $.ajax({
          url : "/surveys/ajaxalldeptusers",
          type : "POST",
          dataType: "json",
          data : {
             csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
             dept: $('#dept').val(),
             Surey_ID:$('#Surey_ID').val(),

             
          },

          success : function(json) {
           //$('#result').append( 'Server Response: ' + json.server_response);
           $('#box').html(json.message),
           console.log('my message' + json)
          },
          error : function(xhr,errmsg,err) {
          alert(xhr.status + ": " + xhr.responseText);
          }
          
        });
          
  }

