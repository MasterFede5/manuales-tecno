// ============================================
// EFECTOS WEB - UNIDAD 1: MECÁNICA DE FLUIDOS
// Criatura: Burbuja/Gota de agua animada
// ============================================

let particles = [];
let mouseX = window.innerWidth / 2;
let mouseY = window.innerHeight / 2;
let canvas, ctx;
let creatureX, creatureY;
let bubbles = [];
let time = 0;

function initWebEffects() {
    canvas = document.createElement('canvas');
    canvas.id = 'particles-canvas';
    canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:9999;pointer-events:none;';
    document.body.appendChild(canvas);
    ctx = canvas.getContext('2d');

    creatureX = window.innerWidth / 2;
    creatureY = window.innerHeight / 2;

    // Crear burbujas que siguen la gota principal
    for (let i = 0; i < 8; i++) {
        bubbles.push({
            offsetX: (Math.random() - 0.5) * 40,
            offsetY: (Math.random() - 0.5) * 40,
            size: Math.random() * 8 + 4,
            phase: Math.random() * Math.PI * 2
        });
    }

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

function addDarkBg() { const bg = document.createElement('div'); bg.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:linear-gradient(135deg,#0a0a1a 0%,#01579B 50%,#0a1a2e 100%);z-index:-1;'; document.body.insertBefore(bg, document.body.firstChild) }

function addNavigation() {
    if (document.querySelector('.web-nav-bar')) return;
    const nav = document.createElement('nav');
    nav.className = 'web-nav-bar';
    nav.innerHTML = `
        <div class="web-nav-content">
            <a href="../index-web.html" class="web-nav-logo">ALBATROS <span>FÍSICA</span></a>
            <div class="web-nav-links">
                <a href="../index-web.html">Inicio</a>
                <a href="../unidad 1/index.html" style="background:#0277BD;color:#fff;">U1</a>
                <a href="../unidad 2/index.html">U2</a>
                <a href="../unidad 3/index.html">U3</a>
                <a href="../unidad 4/index.html">U4</a>
                <a href="../ANEXOS/index.html">Anexos</a>
            </div>
        </div>
    `;
    const style = document.createElement('style');
    style.textContent = `
        .web-nav-bar { position:fixed;top:0;left:0;right:0;z-index:10000;background:rgba(2,119,189,0.95);backdrop-filter:blur(15px);padding:10px 20px; }
        .web-nav-content { max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center; }
        .web-nav-logo { font-family:'Montserrat',sans-serif;font-weight:900;font-size:1rem;color:#fff;text-decoration:none; }
        .web-nav-logo span { color:#E1F5FE; }
        .web-nav-links { display:flex;gap:5px; }
        .web-nav-links a { color:#E1F5FE;text-decoration:none;font-family:'Montserrat',sans-serif;font-size:0.7rem;font-weight:600;padding:5px 10px;border-radius:12px;background:rgba(255,255,255,0.1);transition:.3s; }
        .web-nav-links a:hover { background:#01579B;transform:translateY(-2px); }
        @media (max-width:768px) { .web-nav-links { display:none; } }
        body { padding-top:50px; }
        .page { max-width:900px;margin:0 auto;background:rgba(255,255,255,0.95);border-radius:12px;box-shadow:0 10px 40px rgba(0,0,0,0.3); }
        @media print { #particles-canvas,.web-nav-bar { display:none!important; } body { padding-top:0; } .page { max-width:none;box-shadow:none; } }
    `;
    document.head.appendChild(style);
    document.body.insertBefore(nav, document.body.firstChild);
}

function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }

function createParticle() {
    return {
        x: Math.random() * canvas.width, y: Math.random() * canvas.height,
        size: Math.random() * 3 + 1, speedX: (Math.random() - 0.5) * 0.3, speedY: (Math.random() - 0.5) * 0.3 - 0.2,
        opacity: Math.random() * 0.4 + 0.1, hue: Math.random() * 30 + 190 // Azul agua
    };
}

function initParticles() {
    particles = [];
    const num = Math.min(Math.floor((canvas.width * canvas.height) / 15000), 80);
    for (let i = 0; i < num; i++) particles.push(createParticle());
}

function updateParticles() {
    particles.forEach(p => {
        p.x += p.speedX; p.y += p.speedY;
        const dx = mouseX - p.x, dy = mouseY - p.y, dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 150) { p.x += dx * 0.002; p.y += dy * 0.002; }
        if (p.x < 0) p.x = canvas.width; if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height; if (p.y > canvas.height) p.y = 0;
    });
}

function drawParticles() {
    particles.forEach(p => {
        ctx.beginPath(); ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fillStyle = `hsla(${p.hue}, 80%, 60%, ${p.opacity})`; ctx.fill();
    });
}

function drawCreature() {
    time += 0.05;
    const dx = mouseX - creatureX, dy = mouseY - creatureY;
    creatureX += dx * 0.06; creatureY += dy * 0.06;

    // Gota principal con efecto de agua
    const wobble = Math.sin(time * 2) * 3;
    const size = 25 + Math.sin(time) * 3;

    // Gradiente de agua
    const gradient = ctx.createRadialGradient(creatureX - 5, creatureY - 8, 0, creatureX, creatureY, size);
    gradient.addColorStop(0, 'rgba(255, 255, 255, 0.9)');
    gradient.addColorStop(0.3, 'rgba(100, 200, 255, 0.8)');
    gradient.addColorStop(0.7, 'rgba(2, 119, 189, 0.7)');
    gradient.addColorStop(1, 'rgba(1, 87, 155, 0.6)');

    // Dibujar gota principal
    ctx.beginPath();
    ctx.moveTo(creatureX, creatureY - size);
    ctx.bezierCurveTo(
        creatureX + size + wobble, creatureY - size / 2,
        creatureX + size, creatureY + size / 2,
        creatureX, creatureY + size
    );
    ctx.bezierCurveTo(
        creatureX - size, creatureY + size / 2,
        creatureX - size - wobble, creatureY - size / 2,
        creatureX, creatureY - size
    );
    ctx.fillStyle = gradient;
    ctx.fill();

    // Brillo
    ctx.beginPath();
    ctx.ellipse(creatureX - 8, creatureY - 10, 6, 4, -0.5, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
    ctx.fill();

    // Burbujas flotantes
    bubbles.forEach((b, i) => {
        const bx = creatureX + b.offsetX + Math.sin(time + b.phase) * 10;
        const by = creatureY + b.offsetY + Math.cos(time * 0.8 + b.phase) * 8;
        ctx.beginPath();
        ctx.arc(bx, by, b.size + Math.sin(time * 2 + b.phase) * 2, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(100, 200, 255, 0.4)';
        ctx.fill();
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
        ctx.lineWidth = 1;
        ctx.stroke();
    });

    // Ondas de agua
    for (let i = 0; i < 3; i++) {
        const waveSize = 35 + i * 15 + Math.sin(time - i * 0.5) * 5;
        ctx.beginPath();
        ctx.arc(creatureX, creatureY, waveSize, 0, Math.PI * 2);
        ctx.strokeStyle = `rgba(2, 119, 189, ${0.3 - i * 0.1})`;
        ctx.lineWidth = 2;
        ctx.stroke();
    }
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    updateParticles(); drawParticles(); drawCreature();
    requestAnimationFrame(animate);
}

if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initWebEffects);
else initWebEffects();
