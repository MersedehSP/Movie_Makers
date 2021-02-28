
$( document ).ready(function() {
    console.log( "ready!" );
    $("#budget-phrase, #budget-selection, #duration-phrase, #duration-selection, #duration-submit-btn, #budget-submit-btn, #results, #next-movie-search" ).hide();

});

 //Activate only the Budget related elements
$("#prediction-submit-btn").on('click',function(e){
    console.log('key is pressed')
    $("#starting-phrase, #prediction-submit-btn").hide();
    $("#budget-phrase, #budget-selection, #budget-submit-btn").show();
})

//Activate only the Duration  related elements
$("#budget-submit-btn").on('click',function(e){
    console.log('Submit Budget is pressed')
    $("#budget-phrase, #budget-selection, #budget-submit-btn").hide();
    $("#duration-phrase, #duration-submit-btn, #duration-selection").show();
})

// Retrieve the results a
$("#duration-submit-btn").on('click',function(e){
    console.log('Button is pressed to retrieve results')
// Here ajax call need to be made to fetch json data and the below line will be deleted
    $("#duration-phrase, #duration-submit-btn, #duration-selection").hide();
    $("#results, #next-movie-search").show();
   
})

// Get back to the beginning
$("#next-movie-search").on('click',function(e){
    console.log('Continue  is pressed')
    $("#results,#next-movie-search").hide();
    $("#prediction-submit-btn, #starting-phrase").show();

   
})

function submitForm() {
  
    var frm = $('form[name="movie-details"');
    frm.submit(); // Submit the form
    frm.reset();  // Reset all form data
    return false; // Prevent page refresh
 }




