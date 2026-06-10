// ============================================
// EFECTOS WEB - UNIDAD 3: ELECTROMAGNETISMO
// Criatura: Rayo globular / Esfera de plasma
// ============================================

let particles = [];
let mouseX = window.innerWidth / 2;
let mouseY = window.innerHeight / 2;
let canvas, ctx;
let creatureX, creatureY;
let lightningBolts = [];
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

function addDarkBg() { const bg = document.createElement('div'); bg.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:linear-gradient(135deg,#0a0a1a 0%,#2a0a3a 50%,#1a0a2e 100%);z-index:-1;'; document.body.insertBefore(bg, document.body.firstChild) }

function addNavigation() {
    if (document.querySelector('.web-nav-bar')) return;
    const nav = document.createElement('nav');
    nav.className = 'web-nav-bar';
    nav.innerHTML = `<div class="web-nav-content"><a href="../index-web.html" class="web-nav-logo">ALBATROS <span>FÍSICA</span></a><div class="web-nav-links"><a href="../index-web.html">Inicio</a><a href="../unidad 1/index.html">U1</a><a href="../unidad 2/index.html">U2</a><a href="../unidad 3/index.html" style="background:#9C27B0;color:#fff;">U3</a><a href="../unidad 4/index.html">U4</a><a href="../ANEXOS/index.html">Anexos</a></div></div>`;
    const style = document.createElement('style');
    style.textContent = `.web-nav-bar{position:fixed;top:0;left:0;right:0;z-index:10000;background:rgba(156,39,176,0.95);backdrop-filter:blur(15px);padding:10px 20px}.web-nav-content{max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center}.web-nav-logo{font-family:Montserrat,sans-serif;font-weight:900;font-size:1rem;color:#fff;text-decoration:none}.web-nav-logo span{color:#E1BEE7}.web-nav-links{display:flex;gap:5px}.web-nav-links a{color:#E1BEE7;text-decoration:none;font-family:Montserrat,sans-serif;font-size:.7rem;font-weight:600;padding:5px 10px;border-radius:12px;background:rgba(255,255,255,.1);transition:.3s}.web-nav-links a:hover{background:#7B1FA2}body{padding-top:50px}.page{max-width:900px;margin:0 auto;background:rgba(255,255,255,0.95);border-radius:12px;box-shadow:0 10px 40px rgba(0,0,0,0.3)}@media print{#particles-canvas,.web-nav-bar{display:none!important}body{padding-top:0}.page{max-width:none;box-shadow:none}}`;
    document.head.appendChild(style);
    document.body.insertBefore(nav, document.body.firstChild);
}

function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }

function createParticle() {
    return {
        x: Math.random() * canvas.width, y: Math.random() * canvas.height,
        size: Math.random() * 2 + 1, speedX: (Math.random() - 0.5) * 0.4, speedY: (Math.random() - 0.5) * 0.4,
        opacity: Math.random() * 0.5 + 0.2, hue: Math.random() * 60 + 260 // Púrpura-azul
    };
}

function initParticles() {
    particles = [];
    const num = Math.min(Math.floor((canvas.width * canvas.height) / 12000), 100);
    for (let i = 0; i < num; i++) particles.push(createParticle());
}

function generateLightningPath(startX, startY, endAngle, length) {
    const path = [{ x: startX, y: startY }];
    let currentX = startX, currentY = startY;
    const segments = Math.floor(length / 8);

    for (let i = 0; i < segments; i++) {
        const progress = i / segments;
        const angleVariation = (Math.random() - 0.5) * 0.8;
        const segmentLength = 8 + Math.random() * 5;

        currentX += Math.cos(endAngle + angleVariation) * segmentLength;
        currentY += Math.sin(endAngle + angleVariation) * segmentLength;
        path.push({ x: currentX, y: currentY });
    }
    return path;
}

function updateParticles() {
    particles.forEach(p => {
        p.x += p.speedX; p.y += p.speedY;
        // Atracción eléctrica hacia el cursor
        const dx = mouseX - p.x, dy = mouseY - p.y, dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 200 && dist > 50) {
            p.x += dx * 0.003; p.y += dy * 0.003;
        }
        if (p.x < 0) p.x = canvas.width; if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height; if (p.y > canvas.height) p.y = 0;
    });
}

function drawParticles() {
    particles.forEach(p => {
        ctx.beginPath(); ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fillStyle = `hsla(${p.hue}, 100%, 70%, ${p.opacity})`; ctx.fill();
    });

    // Conexiones eléctricas
    particles.forEach((p1, i) => {
        particles.slice(i + 1).forEach(p2 => {
            const dx = p1.x - p2.x, dy = p1.y - p2.y, dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 80) {
                ctx.beginPath(); ctx.moveTo(p1.x, p1.y); ctx.lineTo(p2.x, p2.y);
                ctx.strokeStyle = `rgba(200, 100, 255, ${0.15 * (1 - dist / 80)})`; ctx.lineWidth = 1; ctx.stroke();
            }
        });
    });
}

function drawCreature() {
    time += 0.1;
    const dx = mouseX - creatureX, dy = mouseY - creatureY;
    creatureX += dx * 0.08; creatureY += dy * 0.08;

    const speed = Math.sqrt(dx * dx + dy * dy);
    const sphereRadius = 30 + Math.sin(time) * 3;

    // Generar rayos desde la esfera
    if (Math.random() > 0.7) {
        const angle = Math.random() * Math.PI * 2;
        const length = 30 + Math.random() * 40 + speed * 0.5;
        lightningBolts.push({
            path: generateLightningPath(creatureX, creatureY, angle, length),
            life: 1,
            width: Math.random() * 2 + 1
        });
    }

    // Resplandor exterior
    ctx.beginPath();
    ctx.arc(creatureX, creatureY, sphereRadius + 25, 0, Math.PI * 2);
    const outerGlow = ctx.createRadialGradient(creatureX, creatureY, sphereRadius, creatureX, creatureY, sphereRadius + 25);
    outerGlow.addColorStop(0, 'rgba(150, 100, 255, 0.4)');
    outerGlow.addColorStop(1, 'rgba(150, 100, 255, 0)');
    ctx.fillStyle = outerGlow;
    ctx.fill();

    // Dibujar rayos
    lightningBolts = lightningBolts.filter(bolt => {
        if (bolt.path.length < 2) return false;

        ctx.beginPath();
        ctx.moveTo(bolt.path[0].x, bolt.path[0].y);
        bolt.path.forEach(pt => ctx.lineTo(pt.x, pt.y));

        // Rayo brillante
        ctx.strokeStyle = `rgba(200, 150, 255, ${bolt.life})`;
        ctx.lineWidth = bolt.width * 2;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        ctx.stroke();

        // Núcleo blanco
        ctx.strokeStyle = `rgba(255, 255, 255, ${bolt.life * 0.8})`;
        ctx.lineWidth = bolt.width;
        ctx.stroke();

        bolt.life -= 0.08;
        return bolt.life > 0;
    });

    // Esfera de plasma
    const gradient = ctx.createRadialGradient(creatureX - 8, creatureY - 8, 0, creatureX, creatureY, sphereRadius);
    gradient.addColorStop(0, 'rgba(255, 255, 255, 0.95)');
    gradient.addColorStop(0.3, 'rgba(200, 150, 255, 0.9)');
    gradient.addColorStop(0.6, 'rgba(150, 50, 200, 0.8)');
    gradient.addColorStop(1, 'rgba(100, 0, 150, 0.6)');

    ctx.beginPath();
    ctx.arc(creatureX, creatureY, sphereRadius, 0, Math.PI * 2);
    ctx.fillStyle = gradient;
    ctx.fill();

    // Anillos de energía
    for (let i = 0; i < 3; i++) {
        const ringRadius = sphereRadius + 10 + i * 8 + Math.sin(time * 2 + i) * 3;
        ctx.beginPath();
        ctx.arc(creatureX, creatureY, ringRadius, 0, Math.PI * 2);
        ctx.strokeStyle = `rgba(200, 150, 255, ${0.4 - i * 0.1})`;
        ctx.lineWidth = 2;
        ctx.stroke();
    }

    // Destellos internos
    for (let i = 0; i < 5; i++) {
        const angle = (time * 0.5 + i * Math.PI * 2 / 5);
        const sparkX = creatureX + Math.cos(angle) * sphereRadius * 0.6;
        const sparkY = creatureY + Math.sin(angle) * sphereRadius * 0.6;
        ctx.beginPath();
        ctx.arc(sparkX, sparkY, 3 + Math.random() * 2, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
        ctx.fill();
    }
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    updateParticles(); drawParticles(); drawCreature();
    requestAnimationFrame(animate);
}

if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initWebEffects);
else initWebEffects();
