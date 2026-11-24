from flask import Flask, render_template

#Criação do app Flask
app=Flask(__name__)

#Rota para a página princial
#esse arroba é um decorato
@app.route('/')
def home():
    return "(<h1>Bem vindo a minha suuuupeeerr pagina!</h1>)"

#Rota para a página sobre!
@app.route('/sobre')
def sobre():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Sobre | Leonardo Zambelli</title>

    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root {
            --background: #070910;
            --gold: #e7bc76;
            --purple: #9b87f5;
            --white: #f5f5f7;
            --muted: #9699aa;
            --border: rgba(255,255,255,0.09);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background: var(--background);
            color: var(--white);
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
            min-height: 100vh;
        }

        ::selection {
            background: var(--gold);
            color: #070910;
        }

        #universe {
            position: fixed;
            inset: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -3;
        }

        .nebula {
            position: fixed;
            width: 650px;
            height: 650px;
            border-radius: 50%;
            filter: blur(150px);
            opacity: 0.12;
            pointer-events: none;
            z-index: -2;
            animation: nebulaMove 18s infinite alternate ease-in-out;
        }

        .nebula-one {
            background: #6741d9;
            top: -250px;
            right: -150px;
        }

        .nebula-two {
            background: #c28b42;
            bottom: -300px;
            left: -200px;
            animation-delay: -9s;
        }

        @keyframes nebulaMove {
            to {
                transform: translate(100px, 80px) scale(1.3);
            }
        }

        #progress {
            position: fixed;
            top: 0;
            left: 0;
            height: 3px;
            width: 0;
            background: linear-gradient(90deg, var(--purple), var(--gold));
            z-index: 100;
        }

        nav {
            max-width: 1250px;
            margin: auto;
            padding: 30px 6%;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .logo {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 24px;
            font-weight: 700;
            letter-spacing: -2px;
        }

        .logo span {
            color: var(--gold);
        }

        .nav-link {
            color: var(--muted);
            text-decoration: none;
            font-size: 13px;
            transition: 0.3s;
        }

        .nav-link:hover {
            color: var(--gold);
        }

        .hero {
            min-height: 85vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 70px 24px 100px;
            position: relative;
        }

        .avatar-container {
            width: 190px;
            height: 190px;
            position: relative;
            display: grid;
            place-items: center;
            margin-bottom: 45px;
            animation: entrance 1.2s both;
        }

        .avatar {
            width: 142px;
            height: 142px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid var(--background);
            box-shadow: 0 0 50px rgba(231,188,118,0.15);
        }

        .orbit {
            position: absolute;
            inset: 0;
            border: 1px solid rgba(231,188,118,0.25);
            border-radius: 50%;
            animation: rotate 12s linear infinite;
        }

        .orbit::before {
            content: '';
            position: absolute;
            top: -4px;
            left: 50%;
            width: 8px;
            height: 8px;
            background: var(--gold);
            border-radius: 50%;
            box-shadow: 0 0 20px var(--gold);
        }

        .orbit-second {
            inset: -14px;
            border: 1px dashed rgba(155,135,245,0.25);
            animation-direction: reverse;
            animation-duration: 25s;
        }

        .orbit-second::before {
            background: var(--purple);
            box-shadow: 0 0 15px var(--purple);
        }

        @keyframes rotate {
            to { transform: rotate(360deg); }
        }

        .eyebrow {
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 5px;
            color: var(--gold);
            margin-bottom: 22px;
            animation: entrance 1s 0.2s both;
        }

        h1 {
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(48px, 9vw, 112px);
            line-height: 0.98;
            letter-spacing: -0.07em;
            font-weight: 700;
            animation: entrance 1s 0.4s both;
        }

        .gradient-text {
            background: linear-gradient(
                110deg,
                #ffffff,
                #e7bc76,
                #9b87f5,
                #ffffff
            );
            background-size: 300%;
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            animation: gradientFlow 8s linear infinite;
        }

        @keyframes gradientFlow {
            to { background-position: 300% center; }
        }

        .typing-container {
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(16px, 3vw, 24px);
            color: var(--muted);
            margin-top: 30px;
            min-height: 35px;
            animation: entrance 1s 0.6s both;
        }

        #typing {
            color: var(--gold);
        }

        .cursor {
            display: inline-block;
            width: 2px;
            height: 23px;
            background: var(--gold);
            vertical-align: middle;
            animation: blink 0.8s infinite;
        }

        @keyframes blink {
            50% { opacity: 0; }
        }

        .hero-description {
            max-width: 600px;
            color: var(--muted);
            font-size: 15px;
            line-height: 1.9;
            margin: 25px auto 35px;
            animation: entrance 1s 0.8s both;
        }

        .buttons {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            animation: entrance 1s 1s both;
        }

        .button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            padding: 16px 28px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 13px;
            font-weight: 600;
            transition: 0.35s;
        }

        .button-primary {
            background: var(--gold);
            color: #101010;
        }

        .button-primary:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 40px rgba(231,188,118,0.25);
        }

        .button-secondary {
            color: var(--white);
            border: 1px solid var(--border);
            background: rgba(255,255,255,0.025);
        }

        .button-secondary:hover {
            border-color: var(--gold);
            transform: translateY(-5px);
        }

        .button svg {
            width: 18px;
            height: 18px;
        }

        .scroll-indicator {
            position: absolute;
            bottom: 20px;
            color: var(--muted);
            font-size: 10px;
            letter-spacing: 4px;
            text-transform: uppercase;
        }

        .scroll-line {
            width: 1px;
            height: 45px;
            background: linear-gradient(var(--gold), transparent);
            margin: 15px auto 0;
            animation: scrollPulse 2s infinite;
        }

        @keyframes scrollPulse {
            50% { transform: scaleY(0.5); opacity: 0.4; }
        }

        @keyframes entrance {
            from {
                opacity: 0;
                transform: translateY(35px);
                filter: blur(8px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
                filter: blur(0);
            }
        }

        .container {
            max-width: 1150px;
            margin: auto;
            padding: 100px 25px;
        }

        .section-label {
            color: var(--gold);
            font-size: 11px;
            letter-spacing: 4px;
            text-transform: uppercase;
            margin-bottom: 20px;
        }

        h2 {
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(35px, 5vw, 62px);
            letter-spacing: -3px;
            line-height: 1.1;
            margin-bottom: 25px;
        }

        .section-description {
            max-width: 700px;
            font-size: 16px;
            line-height: 1.9;
            color: var(--muted);
            margin-bottom: 50px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }

        .card {
            position: relative;
            overflow: hidden;
            background: linear-gradient(
                145deg,
                rgba(255,255,255,0.045),
                rgba(255,255,255,0.01)
            );
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 35px 28px;
            min-height: 300px;
            backdrop-filter: blur(15px);
            transition: border-color 0.4s, box-shadow 0.4s;
        }

        .card::before {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(
                350px circle at var(--x, 50%) var(--y, 50%),
                rgba(231,188,118,0.10),
                transparent 65%
            );
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.4s;
        }

        .card:hover::before {
            opacity: 1;
        }

        .card:hover {
            border-color: rgba(231,188,118,0.4);
            box-shadow: 0 15px 60px rgba(0,0,0,0.3);
        }

        .card-number {
            font-family: 'Space Grotesk', sans-serif;
            color: var(--muted);
            font-size: 11px;
            letter-spacing: 3px;
        }

        .card-icon {
            font-size: 42px;
            color: var(--gold);
            margin: 30px 0 20px;
            font-family: 'Space Grotesk', sans-serif;
        }

        .card h3 {
            font-size: 22px;
            margin-bottom: 15px;
            font-family: 'Space Grotesk', sans-serif;
        }

        .card p {
            color: var(--muted);
            font-size: 14px;
            line-height: 1.8;
        }

        .manifesto {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 80px;
            align-items: center;
        }

        .manifesto p {
            color: var(--muted);
            font-size: 15px;
            line-height: 1.9;
            margin-bottom: 20px;
        }

        .cosmic-art {
            min-height: 350px;
            display: grid;
            place-items: center;
            position: relative;
        }

        .cosmic-art svg {
            width: 100%;
            max-width: 380px;
            overflow: visible;
        }

        .constellation {
            animation: constellationFloat 6s ease-in-out infinite;
            transform-origin: center;
        }

        @keyframes constellationFloat {
            50% { transform: translateY(-12px); }
        }

        .celestial-ring {
            transform-origin: 180px 180px;
            animation: rotate 35s linear infinite;
        }

        .star-point {
            animation: starGlow 3s ease-in-out infinite alternate;
        }

        @keyframes starGlow {
            from { opacity: 0.35; }
            to { opacity: 1; }
        }

        .zodiac {
            position: absolute;
            bottom: 0;
            color: var(--gold);
            letter-spacing: 5px;
            font-size: 10px;
            text-transform: uppercase;
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }

        .skill {
            border: 1px solid var(--border);
            border-radius: 50px;
            padding: 12px 22px;
            color: var(--muted);
            font-size: 13px;
            background: rgba(255,255,255,0.025);
            transition: 0.35s;
        }

        .skill:hover {
            color: var(--gold);
            border-color: var(--gold);
            transform: translateY(-4px);
        }

        .github-panel {
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 45px;
            background: rgba(255,255,255,0.025);
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin: 35px 0;
        }

        .stat {
            border-left: 1px solid rgba(231,188,118,0.3);
            padding: 15px 25px;
        }

        .stat-value {
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(30px, 5vw, 55px);
            color: var(--gold);
            font-weight: 600;
        }

        .stat-label {
            color: var(--muted);
            font-size: 12px;
            margin-top: 8px;
        }

        #github-status {
            font-size: 11px;
            color: var(--muted);
            margin-bottom: 25px;
        }

        .quote-section {
            text-align: center;
            padding: 100px 25px;
            max-width: 900px;
            margin: auto;
        }

        .quote-symbol {
            font-family: Georgia, serif;
            font-size: 100px;
            color: var(--gold);
            line-height: 0.8;
            opacity: 0.6;
        }

        .quote-section blockquote {
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(25px, 4vw, 43px);
            font-weight: 300;
            line-height: 1.5;
            letter-spacing: -1px;
            margin: 20px 0;
        }

        .quote-section small {
            color: var(--muted);
            letter-spacing: 3px;
            text-transform: uppercase;
            font-size: 10px;
        }

        .separator {
            max-width: 1100px;
            height: 1px;
            margin: auto;
            background: linear-gradient(
                90deg,
                transparent,
                rgba(231,188,118,0.3),
                transparent
            );
        }

        .js-ready .reveal {
            opacity: 0;
            transform: translateY(45px);
            transition: opacity 0.9s, transform 0.9s;
        }

        .js-ready .reveal.visible {
            opacity: 1;
            transform: translateY(0);
        }

        footer {
            text-align: center;
            padding: 60px 25px 35px;
        }

        .footer-logo {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 38px;
            font-weight: 700;
            letter-spacing: -3px;
            color: var(--gold);
            margin-bottom: 20px;
        }

        footer p {
            color: var(--muted);
            font-size: 12px;
            line-height: 2;
        }

        .footer-detail {
            font-size: 10px;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-top: 25px;
        }

        @media (max-width: 800px) {
            .cards {
                grid-template-columns: 1fr;
            }

            .manifesto {
                grid-template-columns: 1fr;
                gap: 30px;
            }

            .container {
                padding: 65px 24px;
            }

            .github-panel {
                padding: 28px 20px;
            }

            .stat {
                padding: 10px 12px;
            }

            .stats {
                gap: 5px;
            }

            .hero {
                min-height: 90vh;
            }

            h2 {
                letter-spacing: -2px;
            }
        }

        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                animation: none !important;
                transition: none !important;
                scroll-behavior: auto !important;
            }

            .js-ready .reveal {
                opacity: 1;
                transform: none;
            }
        }
    </style>
</head>

<body>

    <div id="progress"></div>

    <canvas id="universe" aria-hidden="true"></canvas>

    <div class="nebula nebula-one"></div>
    <div class="nebula nebula-two"></div>

    <nav>
        <div class="logo">LZ<span>.</span></div>

        <a href="https://github.com/leonardoszambelli"
           target="_blank"
           rel="noopener noreferrer"
           class="nav-link">
            GITHUB &#8599;
        </a>
    </nav>

    <main>

        <section class="hero">

            <div class="avatar-container">
                <div class="orbit"></div>
                <div class="orbit orbit-second"></div>

                <img
                    class="avatar"
                    src="https://github.com/leonardoszambelli.png"
                    alt="Leonardo Zambelli"
                >
            </div>

            <div class="eyebrow">
                Mente humana &bull; Tecnologia &bull; Conhecimento
            </div>

            <h1>
                Leonardo<br>
                <span class="gradient-text">Zambelli.</span>
            </h1>

            <div class="typing-container">
                <span id="typing">Psicólogo.</span><span class="cursor"></span>
            </div>

            <p class="hero-description">
                Entre a complexidade da mente humana e a precisão dos
                algoritmos, encontro diferentes formas de compreender
                o mundo, explorar possibilidades e construir conhecimento.
            </p>

            <div class="buttons">

                <a class="button button-primary"
                   href="https://github.com/leonardoszambelli"
                   target="_blank"
                   rel="noopener noreferrer">

                    <svg viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 0C5.37 0 0 5.37 0 12c0 5.3
                        3.44 9.8 8.21 11.39.6.11.82-.26.82-.58
                        0-.29-.01-1.04-.02-2.04-3.34.73-4.04-1.61
                        -4.04-1.61-.55-1.39-1.33-1.76-1.33-1.76
                        -1.09-.74.08-.73.08-.73 1.2.08 1.84
                        1.23 1.84 1.23 1.07 1.83 2.81 1.3
                        3.49.99.11-.78.42-1.3.76-1.6-2.67
                        -.3-5.47-1.33-5.47-5.93 0-1.31.47
                        -2.38 1.23-3.22-.12-.3-.53-1.52.12
                        -3.17 0 0 1.01-.32 3.3 1.23A11.5
                        11.5 0 0112 5.8c1.02 0 2.04.14
                        3 .4 2.29-1.55 3.3-1.23 3.3-1.23
                        .65 1.65.24 2.87.12 3.17.76.84
                        1.23 1.91 1.23 3.22 0 4.61-2.81
                        5.62-5.49 5.92.43.37.82 1.1.82
                        2.22 0 1.6-.01 2.89-.01 3.28
                        0 .32.22.69.83.57C20.57 21.8
                        24 17.3 24 12 24 5.37 18.63 0 12 0z"/>
                    </svg>

                    Explorar GitHub
                </a>

                <a class="button button-secondary" href="#sobre">
                    Conheça minha história &#8595;
                </a>

            </div>

            <div class="scroll-indicator">
                Explore
                <div class="scroll-line"></div>
            </div>

        </section>

        <div class="separator"></div>

        <section class="container" id="sobre">

            <div class="reveal">
                <div class="section-label">01 / Identidade</div>

                <h2>
                    Diferentes universos.<br>
                    <span class="gradient-text">Uma mesma curiosidade.</span>
                </h2>

                <p class="section-description">
                    Meu nome é Leonardo dos Santos Zambelli.
                    Sou bancário, psicólogo e estudante de programação.
                    Minha trajetória reúne três áreas aparentemente
                    distintas, mas profundamente conectadas pela
                    capacidade de interpretar informações, compreender
                    comportamentos e solucionar problemas.
                </p>
            </div>

            <div class="cards">

                <article class="card reveal">
                    <div class="card-number">01 / PSIQUE</div>
                    <div class="card-icon">&#936;</div>

                    <h3>Psicologia</h3>

                    <p>
                        Interesse pela psicanálise freudiana clássica,
                        pelo inconsciente, pelos processos psíquicos
                        e pelas forças que influenciam o comportamento
                        humano para além da consciência.
                    </p>
                </article>

                <article class="card reveal">
                    <div class="card-number">02 / LÓGICA</div>
                    <div class="card-icon">&lt;/&gt;</div>

                    <h3>Tecnologia</h3>

                    <p>
                        Atualmente aprofundando meus conhecimentos
                        em Python, lógica de programação e
                        desenvolvimento web. Uma jornada de aprendizado
                        orientada pela curiosidade e pela experimentação.
                    </p>
                </article>

                <article class="card reveal">
                    <div class="card-number">03 / ESTRATÉGIA</div>
                    <div class="card-icon">&#9671;</div>

                    <h3>Mercado financeiro</h3>

                    <p>
                        Minha atuação no setor bancário conecta
                        raciocínio analítico, tomada de decisão,
                        responsabilidade e compreensão das relações
                        humanas no universo financeiro.
                    </p>
                </article>

            </div>

        </section>

        <div class="separator"></div>

        <section class="container manifesto">

            <div class="reveal">

                <div class="section-label">02 / Perspectiva</div>

                <h2>
                    O universo<br>
                    <span class="gradient-text">dentro de nós.</span>
                </h2>

                <p>
                    A astronomia nos convida a olhar para além dos
                    limites do mundo conhecido. A psicologia nos
                    convida a realizar uma jornada semelhante,
                    mas em direção ao nosso próprio interior.
                </p>

                <p>
                    Entre estrelas, símbolos, pensamentos e códigos,
                    existe uma busca comum: compreender aquilo
                    que ainda não conhecemos.
                </p>

                <p>
                    A simbologia de Leão inspira a identidade
                    visual deste espaço, representando criatividade,
                    expressão, coragem e individualidade.
                </p>

            </div>

            <div class="cosmic-art reveal">

                <svg viewBox="0 0 360 360" aria-hidden="true">

                    <defs>
                        <radialGradient id="sunGradient">
                            <stop offset="0%" stop-color="#e7bc76"
                                  stop-opacity="0.18"/>
                            <stop offset="100%" stop-color="#e7bc76"
                                  stop-opacity="0"/>
                        </radialGradient>

                        <filter id="glow">
                            <feGaussianBlur stdDeviation="3"
                                            result="blur"/>
                            <feMerge>
                                <feMergeNode in="blur"/>
                                <feMergeNode in="SourceGraphic"/>
                            </feMerge>
                        </filter>
                    </defs>

                    <circle cx="180" cy="180" r="175"
                            fill="url(#sunGradient)"/>

                    <circle cx="180" cy="180" r="150"
                            fill="none"
                            stroke="#e7bc76"
                            stroke-opacity="0.15"/>

                    <circle cx="180" cy="180" r="130"
                            fill="none"
                            stroke="#e7bc76"
                            stroke-opacity="0.2"
                            stroke-dasharray="2 8"/>

                    <circle cx="180" cy="180" r="105"
                            fill="none"
                            stroke="#9b87f5"
                            stroke-opacity="0.2"/>

                    <g class="celestial-ring">
                        <ellipse cx="180" cy="180"
                                 rx="165" ry="70"
                                 fill="none"
                                 stroke="#9b87f5"
                                 stroke-opacity="0.35"
                                 transform="rotate(-35 180 180)"/>

                        <circle cx="345" cy="180" r="3"
                                fill="#e7bc76"
                                filter="url(#glow)"/>
                    </g>

                    <g class="constellation">

                        <path
                            d="M65 220 L130 195 L205 215
                               L230 145 L200 95 L250 55
                               L290 85 M130 195 L230 145"
                            fill="none"
                            stroke="#e7bc76"
                            stroke-opacity="0.65"
                            stroke-width="1.2"
                        />

                        <g fill="#e7bc76" filter="url(#glow)">
                            <circle class="star-point"
                                    cx="65" cy="220" r="3"/>
                            <circle cx="130" cy="195" r="4"/>
                            <circle class="star-point"
                                    cx="205" cy="215" r="5"/>
                            <circle cx="230" cy="145" r="3"/>
                            <circle class="star-point"
                                    cx="200" cy="95" r="3"/>
                            <circle cx="250" cy="55" r="4"/>
                            <circle cx="290" cy="85" r="3"/>
                        </g>

                        <text x="180" y="310"
                              text-anchor="middle"
                              font-size="38"
                              fill="#e7bc76"
                              opacity="0.8">
                            &#9804;
                        </text>

                    </g>

                </svg>

                <div class="zodiac">
                    Leo &bull; Elemento fogo
                </div>

            </div>

        </section>

        <div class="separator"></div>

        <section class="container reveal">

            <div class="section-label">03 / Conhecimento</div>

            <h2>
                Aprendizado <span class="gradient-text">contínuo.</span>
            </h2>

            <p class="section-description">
                Áreas de conhecimento, interesses e tecnologias
                que fazem parte da minha trajetória de desenvolvimento.
            </p>

            <div class="skills">
                <span class="skill">Python</span>
                <span class="skill">Flask</span>
                <span class="skill">HTML5</span>
                <span class="skill">CSS3</span>
                <span class="skill">JavaScript</span>
                <span class="skill">Git & GitHub</span>
                <span class="skill">Lógica de programação</span>
                <span class="skill">Psicologia</span>
                <span class="skill">Psicanálise freudiana</span>
                <span class="skill">Comportamento humano</span>
                <span class="skill">Mercado financeiro</span>
                <span class="skill">Astronomia</span>
                <span class="skill">Astrologia</span>
            </div>

        </section>

        <section class="container reveal">

            <div class="section-label">04 / Open Source</div>

            <h2>
                Construindo o <span class="gradient-text">futuro.</span>
            </h2>

            <div class="github-panel">

                <h3>Meu universo no GitHub</h3>

                <p class="section-description"
                   style="margin: 15px 0 0;">
                    Projetos, experimentos e registros da minha
                    evolução no universo da programação.
                </p>

                <div class="stats">

                    <div class="stat">
                        <div class="stat-value" id="repos">&mdash;</div>
                        <div class="stat-label">Repositórios</div>
                    </div>

                    <div class="stat">
                        <div class="stat-value" id="followers">&mdash;</div>
                        <div class="stat-label">Seguidores</div>
                    </div>

                    <div class="stat">
                        <div class="stat-value" id="following">&mdash;</div>
                        <div class="stat-label">Seguindo</div>
                    </div>

                </div>

                <p id="github-status" aria-live="polite">
                    Consultando dados públicos do GitHub...
                </p>

                <a class="button button-primary"
                   href="https://github.com/leonardoszambelli?tab=repositories"
                   target="_blank"
                   rel="noopener noreferrer">
                    Ver meus projetos &#8599;
                </a>

            </div>

        </section>

        <div class="separator"></div>

        <section class="quote-section reveal">

            <div class="quote-symbol">&ldquo;</div>

            <blockquote>
                Compreender a mente é explorar o desconhecido.
                Programar é transformar o desconhecido
                em possibilidades.
            </blockquote>

            <small>Uma reflexão sobre conhecimento</small>

        </section>

    </main>

    <div class="separator"></div>

    <footer>

        <div class="footer-logo">LZ.</div>

        <p>
            Leonardo dos Santos Zambelli
        </p>

        <p>
            Psicologia &bull; Tecnologia &bull; Mercado Financeiro
        </p>

        <p class="footer-detail">
            Desenvolvido com Python & Flask
        </p>

        <p style="margin-top: 25px;">
            &copy; <span id="year"></span> Leonardo Zambelli
        </p>

    </footer>

    <script>

        const reducedMotion = window.matchMedia(
            '(prefers-reduced-motion: reduce)'
        ).matches;

        // ANO AUTOMÁTICO

        document.getElementById('year').textContent =
            new Date().getFullYear();


        // EFEITO DE DIGITAÇÃO

        const phrases = [
            'Psicólogo.',
            'Bancário.',
            'Estudante de Python.',
            'Entusiasta da psicanálise.',
            'Explorador do conhecimento.'
        ];

        let phraseIndex = 0;
        let charIndex = 0;
        let deleting = false;

        const typing = document.getElementById('typing');

        function typeEffect() {

            const phrase = phrases[phraseIndex];

            charIndex += deleting ? -1 : 1;

            typing.textContent = phrase.substring(0, charIndex);

            let delay = deleting ? 35 : 85;

            if (!deleting && charIndex === phrase.length) {
                deleting = true;
                delay = 1900;
            }

            else if (deleting && charIndex === 0) {
                deleting = false;
                phraseIndex = (phraseIndex + 1) % phrases.length;
                delay = 350;
            }

            setTimeout(typeEffect, delay);
        }

        if (!reducedMotion) {
            typing.textContent = '';
            typeEffect();
        }


        // ANIMAÇÕES DURANTE A ROLAGEM

        if ('IntersectionObserver' in window && !reducedMotion) {

            document.body.classList.add('js-ready');

            const observer = new IntersectionObserver(
                entries => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('visible');
                            observer.unobserve(entry.target);
                        }
                    });
                },
                { threshold: 0.08 }
            );

            document.querySelectorAll('.reveal').forEach(
                element => observer.observe(element)
            );
        }


        // BARRA DE PROGRESSO

        function updateProgress() {

            const height =
                document.documentElement.scrollHeight -
                window.innerHeight;

            const progress = height > 0
                ? window.scrollY / height * 100
                : 0;

            document.getElementById('progress').style.width =
                progress + '%';
        }

        window.addEventListener('scroll', updateProgress, {
            passive: true
        });

        window.addEventListener('resize', updateProgress);

        updateProgress();


        // ILUMINAÇÃO INTERATIVA DOS CARDS

        document.querySelectorAll('.card').forEach(card => {

            card.addEventListener('pointermove', event => {

                const rect = card.getBoundingClientRect();

                card.style.setProperty(
                    '--x',
                    (event.clientX - rect.left) + 'px'
                );

                card.style.setProperty(
                    '--y',
                    (event.clientY - rect.top) + 'px'
                );

            });

        });


        // UNIVERSO ANIMADO COM CANVAS

        const canvas = document.getElementById('universe');
        const ctx = canvas.getContext('2d');

        let width;
        let height;
        let stars = [];
        let meteors = [];
        let frame = 0;

        const mouse = {
            x: 0,
            y: 0
        };

        function resizeUniverse() {

            const dpr = Math.min(window.devicePixelRatio || 1, 2);

            width = window.innerWidth;
            height = window.innerHeight;

            canvas.width = width * dpr;
            canvas.height = height * dpr;

            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

            const total = Math.min(
                200,
                Math.floor(width * height / 6500)
            );

            stars = Array.from({ length: total }, () => ({
                x: Math.random() * width,
                y: Math.random() * height,
                radius: Math.random() * 1.5 + 0.2,
                opacity: Math.random() * 0.7 + 0.15,
                phase: Math.random() * Math.PI * 2,
                speed: Math.random() * 0.025 + 0.005,
                depth: Math.random() * 12,
                gold: Math.random() > 0.85
            }));

            meteors = [];

            if (reducedMotion) {
                drawUniverse();
            }
        }

        window.addEventListener('pointermove', event => {

            mouse.x = (event.clientX / window.innerWidth - 0.5);
            mouse.y = (event.clientY / window.innerHeight - 0.5);

        }, { passive: true });

        function createMeteor() {

            meteors.push({
                x: Math.random() * width,
                y: -30,
                vx: -5 - Math.random() * 3,
                vy: 4 + Math.random() * 3,
                life: 1
            });
        }

        function drawUniverse() {

            ctx.clearRect(0, 0, width, height);

            frame++;

            stars.forEach(star => {

                const opacity = reducedMotion
                    ? star.opacity
                    : star.opacity *
                      (0.65 + Math.sin(
                          frame * star.speed + star.phase
                      ) * 0.35);

                const x = star.x + mouse.x * star.depth;
                const y = star.y + mouse.y * star.depth;

                ctx.beginPath();

                ctx.arc(x, y, star.radius, 0, Math.PI * 2);

                ctx.fillStyle = star.gold
                    ? 'rgba(231,188,118,' + opacity + ')'
                    : 'rgba(210,215,255,' + opacity + ')';

                ctx.fill();

            });

            if (!reducedMotion) {

                if (Math.random() < 0.004) {
                    createMeteor();
                }

                meteors.forEach(meteor => {

                    const gradient = ctx.createLinearGradient(
                        meteor.x,
                        meteor.y,
                        meteor.x - meteor.vx * 15,
                        meteor.y - meteor.vy * 15
                    );

                    gradient.addColorStop(
                        0,
                        'rgba(231,188,118,' + meteor.life + ')'
                    );

                    gradient.addColorStop(
                        1,
                        'rgba(231,188,118,0)'
                    );

                    ctx.beginPath();

                    ctx.moveTo(meteor.x, meteor.y);

                    ctx.lineTo(
                        meteor.x - meteor.vx * 15,
                        meteor.y - meteor.vy * 15
                    );

                    ctx.strokeStyle = gradient;
                    ctx.lineWidth = 1.5;
                    ctx.stroke();

                    meteor.x += meteor.vx;
                    meteor.y += meteor.vy;
                    meteor.life -= 0.008;

                });

                meteors = meteors.filter(
                    meteor => meteor.life > 0
                );

                requestAnimationFrame(drawUniverse);
            }
        }

        if (ctx) {

            window.addEventListener('resize', resizeUniverse);

            resizeUniverse();

            if (!reducedMotion) {
                drawUniverse();
            }
        }


        // CONTADORES ANIMADOS

        function animateCounter(element, target) {

            if (reducedMotion) {
                element.textContent = target;
                return;
            }

            const duration = 1500;
            const start = performance.now();

            function update(now) {

                const progress = Math.min(
                    (now - start) / duration,
                    1
                );

                const easing = 1 - Math.pow(1 - progress, 3);

                element.textContent = Math.floor(
                    target * easing
                ).toLocaleString('pt-BR');

                if (progress < 1) {
                    requestAnimationFrame(update);
                }
            }

            requestAnimationFrame(update);
        }


        // INTEGRAÇÃO COM A API PÚBLICA DO GITHUB
        // Não exige token nem instalação de bibliotecas Python.

        async function loadGitHub() {

            const status = document.getElementById('github-status');

            try {

                const response = await fetch(
                    'https://api.github.com/users/leonardoszambelli'
                );

                if (!response.ok) {
                    throw new Error('GitHub indisponível');
                }

                const data = await response.json();

                animateCounter(
                    document.getElementById('repos'),
                    data.public_repos
                );

                animateCounter(
                    document.getElementById('followers'),
                    data.followers
                );

                animateCounter(
                    document.getElementById('following'),
                    data.following
                );

                status.textContent =
                    'Dados atualizados diretamente pela API do GitHub.';

                status.style.color = '#8dbba1';

            } catch (error) {

                status.textContent =
                    'Dados temporariamente indisponíveis. ' +
                    'Visite meu perfil para consultar os projetos.';

            }
        }

        loadGitHub();

    </script>

</body>
</html>
"""

#rota com variaveis na URL 
@app.route('/ola/<nome>')
def saudacao(nome):
    return f"<h1> Seja bem vindo </h1> {nome}"



if __name__ == '__main__':
    app.run(debug=True)