// Creating the function for copying the text
function CopyFunction()
{
  // Getting the text field
  var copyText = document.getElementById("sum-btn");

  // Select the text field
  copyText.select();
  copyText.setSelectionRange(0, 99999);

  // Copy the text inside the text field
  document.execCommand("copy");

  // Alert the copied text
  alert("Copied the text: " + copyText.value); 
}
