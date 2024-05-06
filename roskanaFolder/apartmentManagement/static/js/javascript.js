const hoverObj =document.querySelectorAll('.viewShow');
const showObj =document.querySelectorAll('.viewRoom');

function toggleDropdown() {
    var dropdownContent = document.getElementById("myDropdown");
    dropdownContent.classList.toggle("show");
}
  

window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown_content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
}


hoverObj.forEach((viewShow,index)=>{
    viewShow.addEventListener('mouseover',()=>{
        showObj.forEach(viewRoom=>{
            viewRoom.style.display = 'none';
        });
        showObj[index].style.display='flex';
    });
    viewShow.addEventListener('mouseout',()=>{
        showObj.forEach(viewRoom=>{
            
        });
        showObj[index].style.display='none';
    });
});



