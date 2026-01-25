// ============================================
// EFECTOS WEB COMPARTIDOS - ALBATROS FÍSICA
// Araña esquelética de partículas
// ============================================

// Variables globales
let particles = [];
let mouseX = window.innerWidth / 2;
let mouseY = window.innerHeight / 2;
let canvas, ctx;
let spiderX, spiderY, spiderAngle = 0;
let legPhase = 0;

// Puntos de la araña (esqueleto)
const spiderBody = {
    head: { x: 0, y: -15 },
    thorax: { x: 0, y: 0 },
    abdomen: { x: 0, y: 25 }
};

// 8 patas - puntos de articulación
const legConfigs = [
    // Patas izquierdas (4)
    { base: -8, angle: -30, len1: 25, len2: 30 },
    { base: -6, angle: -60, len1: 22, len2: 28 },
    { base: -6, angle: -120, len1: 22, len2: 28 },
    { base: -8, angle: -150, len1: 25, len2: 30 },
    // Patas derechas (4)
    { base: 8, angle: 30, len1: 25, len2: 30 },
    { base: 6, angle: 60, len1: 22, len2: 28 },
    { base: 6, angle: 120, len1: 22, len2: 28 },
    { base: 8, angle: 150, len1: 25, len2: 30 }
];

// ============================================
// INICIALIZACIÓN
// ============================================
function initWebEffects() {
    canvas = document.createElement('canvas');
    canvas.id = 'particles-canvas';
    canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:9999;pointer-events:none;';
    document.body.appendChild(canvas);
    ctx = canvas.getContext('2d');

    spiderX = window.innerWidth / 2;
    spiderY = window.innerHeight / 2;

    resizeCanvas();
    initParticles();
    addNavigation();
    animate();

    window.addEventListener('resize', () => {
        resizeCanvas();
        initParticles();
    });

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    document.addEventListener('touchmove', (e) => {
        if (e.touches.length > 0) {
            mouseX = e.touches[0].clientX;
            mouseY = e.touches[0].clientY;
        }
    });
}

// ============================================
// NAVEGACIÓN FIJA
// ============================================
function addNavigation() {
    // Verificar si ya existe navegación
    if (document.querySelector('.web-nav-bar')) return;

    const nav = document.createElement('nav');
    nav.className = 'web-nav-bar';
    nav.innerHTML = `
        <div class="web-nav-content">
            <a href="../index-web.html" class="web-nav-logo">ALBATROS <span>FÍSICA</span></a>
            <div class="web-nav-links">
                <a href="../index-web.html">Inicio</a>
                <a href="../unidad 1/index.html">Unidad 1</a>
                <a href="../unidad 2/index.html">Unidad 2</a>
                <a href="../unidad 3/index.html">Unidad 3</a>
                <a href="../unidad 4/index.html">Unidad 4</a>
                <a href="../ANEXOS/index.html">Anexos</a>
            </div>
        </div>
    `;

    // Estilos inline para la navegación
    const style = document.createElement('style');
    style.textContent = `
        .web-nav-bar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 10000;
            background: rgba(11, 31, 58, 0.95);
            backdrop-filter: blur(15px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding: 10px 20px;
        }
        .web-nav-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .web-nav-logo {
            font-family: 'Montserrat', sans-serif;
            font-weight: 900;
            font-size: 1.1rem;
            color: #fff;
            text-decoration: none;
            letter-spacing: 2px;
        }
        .web-nav-logo span { color: #FF6F00; }
        .web-nav-links {
            display: flex;
            gap: 6px;
        }
        .web-nav-links a {
            color: #E0E6ED;
            text-decoration: none;
            font-family: 'Montserrat', sans-serif;
            font-size: 0.7rem;
            font-weight: 600;
            padding: 6px 12px;
            border-radius: 15px;
            transition: all 0.3s ease;
            background: rgba(255, 255, 255, 0.05);
        }
        .web-nav-links a:hover {
            background: #FF6F00;
            color: #fff;
            transform: translateY(-2px);
        }
        @media (max-width: 768px) {
            .web-nav-links { display: none; }
        }
    `;
    document.head.appendChild(style);
    document.body.insertBefore(nav, document.body.firstChild);
}

// ============================================
// PARTÍCULAS
// ============================================
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

function createParticle() {
    return {
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        size: Math.random() * 2.5 + 0.5,
        speedX: (Math.random() - 0.5) * 0.4,
        speedY: (Math.random() - 0.5) * 0.4,
        opacity: Math.random() * 0.4 + 0.1,
        hue: Math.random() * 50 + 20
    };
}

function initParticles() {
    particles = [];
    const numParticles = Math.floor((canvas.width * canvas.height) / 15000);
    for (let i = 0; i < Math.min(numParticles, 80); i++) {
        particles.push(createParticle());
    }
}

function updateParticles() {
    particles.forEach(p => {
        p.x += p.speedX;
        p.y += p.speedY;

        const dx = mouseX - p.x;
        const dy = mouseY - p.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 150) {
            p.x += dx * 0.002;
            p.y += dy * 0.002;
        }

        if (p.x < 0) p.x = canvas.width;
        if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height;
        if (p.y > canvas.height) p.y = 0;
    });
}

function drawParticles() {
    particles.forEach(p => {
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fillStyle = `hsla(${p.hue}, 100%, 60%, ${p.opacity})`;
        ctx.fill();
    });

    // Conexiones tipo telaraña
    particles.forEach((p1, i) => {
        particles.slice(i + 1).forEach(p2 => {
            const dx = p1.x - p2.x;
            const dy = p1.y - p2.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 100) {
                ctx.beginPath();
                ctx.moveTo(p1.x, p1.y);
                ctx.lineTo(p2.x, p2.y);
                ctx.strokeStyle = `rgba(255, 111, 0, ${0.06 * (1 - dist / 100)})`;
                ctx.lineWidth = 0.5;
                ctx.stroke();
            }
        });
    });
}

// ============================================
// ARAÑA ESQUELÉTICA DE PARTÍCULAS
// ============================================
function updateSpider() {
    const dx = mouseX - spiderX;
    const dy = mouseY - spiderY;

    // Movimiento suave
    spiderX += dx * 0.05;
    spiderY += dy * 0.05;

    // Rotación hacia el cursor
    const targetAngle = Math.atan2(dy, dx) + Math.PI / 2;
    let angleDiff = targetAngle - spiderAngle;
    while (angleDiff > Math.PI) angleDiff -= Math.PI * 2;
    while (angleDiff < -Math.PI) angleDiff += Math.PI * 2;
    spiderAngle += angleDiff * 0.08;

    // Fase de animación de patas
    const speed = Math.sqrt(dx * dx + dy * dy);
    legPhase += speed * 0.01;
}

function drawSpider() {
    ctx.save();
    ctx.translate(spiderX, spiderY);
    ctx.rotate(spiderAngle);

    // Dibujar patas (8 patas esqueléticas)
    legConfigs.forEach((leg, i) => {
        const phase = legPhase + (i * Math.PI / 4);
        const wobble = Math.sin(phase) * 8;

        // Punto base en el tórax
        const baseX = leg.base;
        const baseY = 0;

        // Primer segmento (coxa-femur)
        const angle1 = (leg.angle * Math.PI / 180) + Math.sin(phase) * 0.15;
        const joint1X = baseX + Math.cos(angle1) * leg.len1;
        const joint1Y = baseY + Math.sin(angle1) * leg.len1;

        // Segundo segmento (tibia-tarso) - más angular
        const angle2 = angle1 + (leg.angle > 0 ? 0.8 : -0.8) + Math.cos(phase) * 0.1;
        const endX = joint1X + Math.cos(angle2) * leg.len2;
        const endY = joint1Y + Math.sin(angle2) * leg.len2;

        // Dibujar segmentos de la pata como líneas
        ctx.beginPath();
        ctx.moveTo(baseX, baseY);
        ctx.lineTo(joint1X, joint1Y);
        ctx.lineTo(endX, endY);
        ctx.strokeStyle = 'rgba(255, 100, 0, 0.8)';
        ctx.lineWidth = 2;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        ctx.stroke();

        // Puntos/partículas en las articulaciones
        [{ x: baseX, y: baseY }, { x: joint1X, y: joint1Y }, { x: endX, y: endY }].forEach((pt, j) => {
            ctx.beginPath();
            ctx.arc(pt.x, pt.y, j === 2 ? 2 : 3, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(255, 150, 0, 0.9)';
            ctx.fill();
        });
    });

    // Cuerpo esquelético (líneas conectando puntos)
    // Abdomen
    ctx.beginPath();
    ctx.ellipse(0, 20, 8, 12, 0, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(255, 100, 0, 0.7)';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Tórax
    ctx.beginPath();
    ctx.ellipse(0, 0, 6, 8, 0, 0, Math.PI * 2);
    ctx.stroke();

    // Cabeza
    ctx.beginPath();
    ctx.ellipse(0, -12, 5, 6, 0, 0, Math.PI * 2);
    ctx.stroke();

    // Conexiones del cuerpo
    ctx.beginPath();
    ctx.moveTo(0, 8);
    ctx.lineTo(0, -6);
    ctx.stroke();

    // Ojos (8 puntos brillantes)
    const eyePositions = [
        { x: -3, y: -14, r: 2 },
        { x: 3, y: -14, r: 2 },
        { x: -5, y: -12, r: 1.5 },
        { x: 5, y: -12, r: 1.5 },
        { x: -2, y: -16, r: 1 },
        { x: 2, y: -16, r: 1 },
        { x: -1, y: -17, r: 0.8 },
        { x: 1, y: -17, r: 0.8 }
    ];

    eyePositions.forEach(eye => {
        ctx.beginPath();
        ctx.arc(eye.x, eye.y, eye.r, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(255, 50, 50, 0.9)';
        ctx.fill();
        // Brillo
        ctx.beginPath();
        ctx.arc(eye.x + 0.3, eye.y - 0.3, eye.r * 0.4, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(255, 200, 200, 0.8)';
        ctx.fill();
    });

    // Quelíceros (colmillos)
    ctx.beginPath();
    ctx.moveTo(-2, -8);
    ctx.quadraticCurveTo(-4, -4, -3, 0);
    ctx.moveTo(2, -8);
    ctx.quadraticCurveTo(4, -4, 3, 0);
    ctx.strokeStyle = 'rgba(255, 80, 0, 0.8)';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    ctx.restore();
}

// ============================================
// ANIMACIÓN PRINCIPAL
// ============================================
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    updateParticles();
    drawParticles();

    updateSpider();
    drawSpider();

    requestAnimationFrame(animate);
}

// Auto-inicializar
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initWebEffects);
} else {
    initWebEffects();
}
