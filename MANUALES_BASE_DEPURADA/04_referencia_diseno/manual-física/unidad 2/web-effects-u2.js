// ============================================
// EFECTOS WEB - UNIDAD 2: TERMODINÁMICA
// Criatura: Llama de fuego animada
// ============================================

let particles = [];
let mouseX = window.innerWidth / 2;
let mouseY = window.innerHeight / 2;
let canvas, ctx;
let creatureX, creatureY;
let flameParticles = [];
let time = 0;

function initWebEffects() {
    canvas = document.createElement('canvas');
    canvas.id = 'particles-canvas';
    canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:9999;pointer-events:none;';
    document.body.appendChild(canvas);
    ctx = canvas.getContext('2d');

    creatureX = window.innerWidth / 2;
    creatureY = window.innerHeight / 2;

    resizeCanvas();
    initParticles();
    addNavigation();
    addDarkBg();
    animate();

    window.addEventListener('resize', () => { resizeCanvas(); initParticles(); });
    document.addEventListener('mousemove', (e) => { mouseX = e.clientX; mouseY = e.clientY; });
    document.addEventListener('touchmove', (e) => {
        if (e.touches.length > 0) { mouseX = e.touches[0].clientX; mouseY = e.touches[0].clientY; }
    });
}

function addDarkBg() { const bg = document.createElement('div'); bg.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:linear-gradient(135deg,#1a0a0a 0%,#3d1a00 50%,#1a0a2e 100%);z-index:-1;'; document.body.insertBefore(bg, document.body.firstChild) }

function addNavigation() {
    if (document.querySelector('.web-nav-bar')) return;
    const nav = document.createElement('nav');
    nav.className = 'web-nav-bar';
    nav.innerHTML = `<div class="web-nav-content"><a href="../index-web.html" class="web-nav-logo">ALBATROS <span>FÍSICA</span></a><div class="web-nav-links"><a href="../index-web.html">Inicio</a><a href="../unidad 1/index.html">U1</a><a href="../unidad 2/index.html" style="background:#FF6F00;color:#fff;">U2</a><a href="../unidad 3/index.html">U3</a><a href="../unidad 4/index.html">U4</a><a href="../ANEXOS/index.html">Anexos</a></div></div>`;
    const style = document.createElement('style');
    style.textContent = `.web-nav-bar{position:fixed;top:0;left:0;right:0;z-index:10000;background:rgba(255,111,0,0.95);backdrop-filter:blur(15px);padding:10px 20px}.web-nav-content{max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center}.web-nav-logo{font-family:Montserrat,sans-serif;font-weight:900;font-size:1rem;color:#fff;text-decoration:none}.web-nav-logo span{color:#FFF3E0}.web-nav-links{display:flex;gap:5px}.web-nav-links a{color:#FFF3E0;text-decoration:none;font-family:Montserrat,sans-serif;font-size:.7rem;font-weight:600;padding:5px 10px;border-radius:12px;background:rgba(255,255,255,.15);transition:.3s}.web-nav-links a:hover{background:#E65100}body{padding-top:50px}.page{max-width:900px;margin:0 auto;background:rgba(255,255,255,0.95);border-radius:12px;box-shadow:0 10px 40px rgba(0,0,0,0.3)}@media print{#particles-canvas,.web-nav-bar{display:none!important}body{padding-top:0}.page{max-width:none;box-shadow:none}}`;
    document.head.appendChild(style);
    document.body.insertBefore(nav, document.body.firstChild);
}

function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }

function createParticle() {
    return {
        x: Math.random() * canvas.width, y: Math.random() * canvas.height,
        size: Math.random() * 2.5 + 0.5, speedX: (Math.random() - 0.5) * 0.3, speedY: (Math.random() - 0.5) * 0.3 - 0.3,
        opacity: Math.random() * 0.4 + 0.1, hue: Math.random() * 40 + 15 // Naranja-rojo
    };
}

function initParticles() {
    particles = [];
    const num = Math.min(Math.floor((canvas.width * canvas.height) / 15000), 80);
    for (let i = 0; i < num; i++) particles.push(createParticle());
}

function createFlameParticle(x, y) {
    return {
        x: x + (Math.random() - 0.5) * 15,
        y: y,
        vx: (Math.random() - 0.5) * 2,
        vy: -Math.random() * 4 - 2,
        size: Math.random() * 10 + 5,
        life: 1,
        hue: Math.random() * 40 + 10
    };
}

function updateParticles() {
    particles.forEach(p => {
        p.x += p.speedX; p.y += p.speedY;
        if (p.x < 0) p.x = canvas.width; if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height; if (p.y > canvas.height) p.y = 0;
    });
}

function drawParticles() {
    particles.forEach(p => {
        ctx.beginPath(); ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fillStyle = `hsla(${p.hue}, 100%, 50%, ${p.opacity})`; ctx.fill();
    });
}

function drawCreature() {
    time += 0.08;
    const dx = mouseX - creatureX, dy = mouseY - creatureY;
    creatureX += dx * 0.07; creatureY += dy * 0.07;

    // Crear partículas de fuego
    if (Math.random() > 0.5) {
        flameParticles.push(createFlameParticle(creatureX, creatureY + 15));
    }

    // Actualizar y dibujar partículas de fuego
    flameParticles = flameParticles.filter(fp => {
        fp.x += fp.vx;
        fp.y += fp.vy;
        fp.vy *= 0.98;
        fp.life -= 0.02;
        fp.size *= 0.97;

        if (fp.life > 0) {
            ctx.beginPath();
            ctx.arc(fp.x, fp.y, fp.size, 0, Math.PI * 2);
            const gradient = ctx.createRadialGradient(fp.x, fp.y, 0, fp.x, fp.y, fp.size);
            gradient.addColorStop(0, `hsla(50, 100%, 70%, ${fp.life})`);
            gradient.addColorStop(0.5, `hsla(${fp.hue}, 100%, 50%, ${fp.life * 0.7})`);
            gradient.addColorStop(1, `hsla(0, 100%, 30%, 0)`);
            ctx.fillStyle = gradient;
            ctx.fill();
            return true;
        }
        return false;
    });

    // Núcleo de la llama
    const flameHeight = 40 + Math.sin(time * 3) * 8;
    const flameWidth = 25 + Math.sin(time * 2) * 5;

    // Llama exterior (roja)
    ctx.beginPath();
    ctx.moveTo(creatureX, creatureY - flameHeight);
    ctx.bezierCurveTo(
        creatureX + flameWidth, creatureY - flameHeight * 0.3,
        creatureX + flameWidth * 0.8, creatureY + 10,
        creatureX, creatureY + 20
    );
    ctx.bezierCurveTo(
        creatureX - flameWidth * 0.8, creatureY + 10,
        creatureX - flameWidth, creatureY - flameHeight * 0.3,
        creatureX, creatureY - flameHeight
    );
    const gradOuter = ctx.createLinearGradient(creatureX, creatureY + 20, creatureX, creatureY - flameHeight);
    gradOuter.addColorStop(0, 'rgba(255, 100, 0, 0.9)');
    gradOuter.addColorStop(0.5, 'rgba(255, 50, 0, 0.7)');
    gradOuter.addColorStop(1, 'rgba(200, 0, 0, 0.3)');
    ctx.fillStyle = gradOuter;
    ctx.fill();

    // Llama media (naranja)
    ctx.beginPath();
    ctx.moveTo(creatureX, creatureY - flameHeight * 0.7);
    ctx.bezierCurveTo(
        creatureX + flameWidth * 0.6, creatureY - flameHeight * 0.2,
        creatureX + flameWidth * 0.5, creatureY + 5,
        creatureX, creatureY + 15
    );
    ctx.bezierCurveTo(
        creatureX - flameWidth * 0.5, creatureY + 5,
        creatureX - flameWidth * 0.6, creatureY - flameHeight * 0.2,
        creatureX, creatureY - flameHeight * 0.7
    );
    const gradMid = ctx.createLinearGradient(creatureX, creatureY + 15, creatureX, creatureY - flameHeight * 0.7);
    gradMid.addColorStop(0, 'rgba(255, 200, 0, 0.9)');
    gradMid.addColorStop(1, 'rgba(255, 100, 0, 0.5)');
    ctx.fillStyle = gradMid;
    ctx.fill();

    // Núcleo (amarillo/blanco)
    ctx.beginPath();
    ctx.moveTo(creatureX, creatureY - flameHeight * 0.4);
    ctx.bezierCurveTo(
        creatureX + flameWidth * 0.3, creatureY - flameHeight * 0.1,
        creatureX + flameWidth * 0.2, creatureY + 5,
        creatureX, creatureY + 10
    );
    ctx.bezierCurveTo(
        creatureX - flameWidth * 0.2, creatureY + 5,
        creatureX - flameWidth * 0.3, creatureY - flameHeight * 0.1,
        creatureX, creatureY - flameHeight * 0.4
    );
    const gradCore = ctx.createLinearGradient(creatureX, creatureY + 10, creatureX, creatureY - flameHeight * 0.4);
    gradCore.addColorStop(0, 'rgba(255, 255, 200, 1)');
    gradCore.addColorStop(1, 'rgba(255, 255, 0, 0.6)');
    ctx.fillStyle = gradCore;
    ctx.fill();

    // Resplandor
    ctx.beginPath();
    ctx.arc(creatureX, creatureY, 50, 0, Math.PI * 2);
    const glowGrad = ctx.createRadialGradient(creatureX, creatureY, 0, creatureX, creatureY, 50);
    glowGrad.addColorStop(0, 'rgba(255, 150, 0, 0.3)');
    glowGrad.addColorStop(1, 'rgba(255, 100, 0, 0)');
    ctx.fillStyle = glowGrad;
    ctx.fill();
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    updateParticles(); drawParticles(); drawCreature();
    requestAnimationFrame(animate);
}

if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initWebEffects);
else initWebEffects();
