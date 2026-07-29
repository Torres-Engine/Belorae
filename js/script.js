/**
 * BELORAE CONFEITARIA SAUDÁVEL - Script
 *
 * Os botões "Fazer Pedido", "Ver Cardápio" e "Consultar pelo WhatsApp", e os
 * ícones flutuantes de WhatsApp/Instagram, são todos <a> simples com href
 * direto, sem precisar de JS. Não existe menu mobile com toggle: o nav some
 * via CSS (display:none) no mobile mais estreito.
 *
 * O que precisa de JS hoje:
 * - Barra fina de progresso de rolagem no topo da página.
 * - Botão flutuante "voltar ao topo" (aparece só depois de rolar a página).
 */

var barraProgresso = document.getElementById('scroll-progress');
var botaoTopo = document.getElementById('back-to-top');

function atualizarNaRolagem() {
  var alturaRolavel = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var progresso = alturaRolavel > 0 ? (window.scrollY / alturaRolavel) * 100 : 0;

  if (barraProgresso) {
    barraProgresso.style.width = progresso + '%';
  }

  if (botaoTopo) {
    if (window.scrollY > window.innerHeight) {
      botaoTopo.classList.add('visivel');
    } else {
      botaoTopo.classList.remove('visivel');
    }
  }
}

if (botaoTopo) {
  botaoTopo.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

document.addEventListener('scroll', atualizarNaRolagem, { passive: true });
window.addEventListener('resize', atualizarNaRolagem);
atualizarNaRolagem();
