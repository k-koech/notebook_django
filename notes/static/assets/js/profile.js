//   ==========SUBSCRIBE==============
function subscribe()
{
    $(document).ready(function()
    {
       
        $.ajax({
            method:'POST',
            url:'subscribe',
        data:{
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            }, 

            success: function(response) 
            {
                console.log(response)
                             
                if(response.success=="subscribed")
                {
                    swal({
                        title: "Success!",
                        text: "Subscribed successfully!",
                        icon: "success",
                        timer: 5000
                      });

                }
                else if(response.success=="unsubscribed")
                {
                    swal({
                        title: "Success!",
                        text: "Unsubscribed successfully!",
                        icon: "success",
                        timer: 5000
                      });
                }
            },

            error: function (error) {
                alert('Error');
            }

        });
        
        // });
    });
}