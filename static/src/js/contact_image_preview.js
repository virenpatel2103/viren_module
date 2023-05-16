console.log("-----------------------------------------------------------loaded")
var input = document.getElementById('user_img');
console.log("this is input-------------------------------", input)
if(input) {
  input.addEventListener('change', function () {
    getUploadImageUrl(this);
  });
}

function getUploadImageUrl(input) {

  if (input.files && input.files[0]) {
    var reader = new FileReader();
    console.log("this is reader-------------------------------", reader)
    reader.onload = function (e) {
      document.getElementById('user_img').setAttribute('src', e.target.result);
    };

    reader.readAsDataURL(input.files[0]);
  }
}