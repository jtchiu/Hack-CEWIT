$(document).ready(function(){
  $("ul.dropdown-menu input[type=checkbox]").each(function(){
    $(this).change(function(){
      var line = "";
      $("ul.dropdown-menu input[type=checkbox]").each(function(){
        if($(this).is(":checked")){
          var ingredient = this.attributes[3].value;
          line += ingredient + ";";
        }
      });
      $("input.form-control").val(line);
    });
  });
});


$(document).on('submit', '#search-bar-form', function(){
    var search_bar_form = $('#search-bar-form');

    var ingredients =search_bar_form[0].value

    var json = {ingredients : ingredients};
    $.ajax({
      url: search_bar_form.attr('action'),
        type: 'POST',
        data: JSON.stringify(json),
        // contentType: "application/json; charset=utf-8",
        // dataType:"json",
        success: function(response){
          search_bar_form.val('');
        },
        error: function(error){
          console.log(error);
          alert(error)
        },
        complete: function(data){

        }
    });
    return false;
});

$(document).on('click', '#search-bar-form-submit', function(){
  $('#search-bar-form').submit()
});
