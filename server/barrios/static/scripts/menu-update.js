window.addEventListener('htmx:pushedIntoHistory', (event) => {
  setAnchorClass();
})

window.addEventListener('load', (event) => {
  setAnchorClass();
})

function setAnchorClass() {
  const pathname = window.location.pathname;
  const targetAnchor = document.querySelector(`a[href='${pathname}']`);

  otherAnchors = Array.from(document.querySelectorAll('.current-page'));

  for (anchor of otherAnchors) {
    if(Array.from(anchor.classList).includes('current-page')) {
      anchor.classList.remove('current-page');
    }
  }

  if (targetAnchor) {
    targetAnchor.classList.add('current-page');
  }
}
