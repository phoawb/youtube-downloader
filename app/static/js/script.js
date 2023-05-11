function showLoadingAnimation() {
  document.getElementById('loading-animation').style.display = 'block';
}

function handleInput() {
  const input = document.getElementById('video_url');
  if (!input || !input.validity.valid) {
    console.log('input was not valid');
    return;
  }
  showLoadingAnimation();
}

function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName('tabcontent');
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = 'none';
  }
  tablinks = document.getElementsByClassName('tablinks');
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(' active', '');
  }
  document.getElementById(tabName).style.display = 'table-row';
  evt.currentTarget.className += ' active';
}

// Default to showing the first tab on page load
document.getElementById("{{ streams[0]['itag'] }}").style.display = 'table-row';
document.getElementsByClassName;

/* var form = document.getElementById('form');
form.addEventListener('submit', handleInput); */

/* var input = document.getElementById('video_url');
input.addEventListener('keyup', handleInput); */
