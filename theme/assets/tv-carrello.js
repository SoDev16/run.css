/* Compte à rebours de réservation du tiroir panier.
   Le tiroir est reconstruit à chaque modification du panier : on observe donc
   le document plutôt que de s'accrocher à un élément qui disparaîtra. */
(() => {
  let restant = null, minuterie = null;

  function demarrer(el) {
    if (minuterie) return;
    const depart = el.textContent.trim().split(':');
    restant = (Number(depart[0]) || 10) * 60 + (Number(depart[1]) || 0);
    minuterie = setInterval(() => {
      if (restant <= 0) return;
      restant--;
      document.querySelectorAll('[data-tv-conto]').forEach((n) => {
        n.textContent =
          String(Math.floor(restant / 60)).padStart(2, '0') + ':' + String(restant % 60).padStart(2, '0');
      });
    }, 1000);
  }

  function verifier() {
    const el = document.querySelector('[data-tv-conto]');
    if (!el) return;
    if (restant !== null) {
      el.textContent =
        String(Math.floor(restant / 60)).padStart(2, '0') + ':' + String(restant % 60).padStart(2, '0');
    } else {
      demarrer(el);
    }
  }

  document.addEventListener('DOMContentLoaded', verifier);
  new MutationObserver(verifier).observe(document.documentElement, { childList: true, subtree: true });
})();
