htmx.onLoad((event) => {
  htmx.findAll('.flash').forEach((element) => {
    console.log(element)
    element.classList.remove('hidden');

    setTimeout(() => {
      element.classList.add('hidden');
      // setTimeout(() => {
      //   htmx.find('[data-toast-container]').removeChild(element);
      // }, 2000);
    }, 5000);
  })
});

