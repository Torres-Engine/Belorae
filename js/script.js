/**
 * BELORAE CONFEITARIA SAUDÁVEL - Script
 * Reconstruído conforme SPEC.md seção 3 (RF-01) e seção 6.6
 * Responsabilidades:
 * - Montar link de WhatsApp com mensagem pré-escrita e exata
 * - Aplicar link em todos os 3 botões de pedido
 */

// ===== CONFIGURAÇÃO =====
const NUMERO_WHATSAPP = "5541996123682"; // Formato: país + DDD + número, só dígitos
const MENSAGEM = "Olá! Vi o site da Belorae e quero fazer um pedido.";

// ===== FUNÇÕES =====

/**
 * Monta URL de WhatsApp com número e mensagem
 * Segue formato: https://wa.me/NUMERO?text=MENSAGEM_CODIFICADA
 */
function obterLinkWhatsApp() {
  const mensagemCodificada = encodeURIComponent(MENSAGEM);
  return `https://wa.me/${NUMERO_WHATSAPP}?text=${mensagemCodificada}`;
}

/**
 * Aplica clique nos botões de pedido para abrir WhatsApp
 * IDs: btn-header, btn-hero-primary, btn-cta-final
 */
function vincularBotoesWhatsApp() {
  const linkWhatsApp = obterLinkWhatsApp();
  const idsBoties = ["btn-header", "btn-hero-primary", "btn-cta-final"];

  idsBoties.forEach((id) => {
    const botao = document.getElementById(id);
    if (botao) {
      botao.addEventListener("click", (e) => {
        e.preventDefault();
        window.open(linkWhatsApp, "_blank");
      });
    }
  });
}

// ===== INICIALIZAÇÃO =====
document.addEventListener("DOMContentLoaded", () => {
  vincularBotoesWhatsApp();
});

