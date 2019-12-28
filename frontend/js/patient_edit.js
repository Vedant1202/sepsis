function showf()
{
  var v=document.getElementById('user_input').value;
  var inputContainer=document.getElementById('inut');
  for(var i=0;i<v;i++)
  {
    var newForm = document.createElement("input");
        newForm.setAttribute("type", "text");
        newForm.setAttribute("class", "uk-input rounded");

        inputContainer.appendChild(newForm).style.margin="10px 0 0 0";
        inputContainer.appendChild(document.createElement("br"));
  }



  var input=document.getElementById('inut2');
  for(var y=0;y<v;y++)
  {
    var fewForm=document.createElement("input");
        fewForm.setAttribute("type", "file");
        fewForm.setAttribute("class", "d.none");
        input.appendChild(fewForm).style.margin="10px 0 10px 0";
        input.appendChild(document.createElement("br"));
  }
}
