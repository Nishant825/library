$(document).ready(function () {
    var errorOccurred = {{ error_occurred}};
    if (errorOccurred){
      $(".user-input").addClass("form_error");
    } 
});