function getreport(){
    var engmarks=document.getElementById('english').value;
    var hinmarks=document.getElementById('hindi').value;
    var mathmarks=document.getElementById('maths').value;
    var phymarks=document.getElementById('physics').value;
    var chemarks=document.getElementById('chemistry').value;
  var totalmarks=engmarks+hinmarks+mathmarks+phymarks+chemarks;
   var percent=(totalmarks/5)*100;
document.getElementById('name').value=document.getElementById('t1').value;
document.getElementById('roll').value=document.getElementById('t2').value;
document.getElementById('total').value=totalmarks;
document.getElementById('percent').value=percent;
}