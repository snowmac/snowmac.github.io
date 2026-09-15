(function () {
  function typeInto(el) {
    var text = el.getAttribute('data-text') || '';
    var cursor = document.createElement('span');
    cursor.className = 'cursor';
    el.textContent = '';
    el.appendChild(cursor);

    var i = 0;
    function step() {
      if (i < text.length) {
        cursor.insertAdjacentText('beforebegin', text.charAt(i));
        i++;
        setTimeout(step, 28);
      }
    }
    step();
  }

  document.addEventListener('DOMContentLoaded', function () {
    var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var targets = document.querySelectorAll('.typewriter-text');
    targets.forEach(function (el) {
      if (reduceMotion) {
        el.textContent = el.getAttribute('data-text') || '';
      } else {
        typeInto(el);
      }
    });
  });
})();
