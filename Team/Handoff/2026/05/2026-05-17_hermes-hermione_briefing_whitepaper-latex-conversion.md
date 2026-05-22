---
date: 2026-05-17
mittente: Hermes
destinatario: Hermione
tipo: briefing
stato: completato
priorita: alta
titolo: "Conversione whitepaper.md → LaTeX + TikZ per arXiv"
quality_score: ""
verifica_esterna: false
riferimenti:
  - "Team Olimpo Whitepaper: /home/stra/teamolimpo-paper/paper/whitepaper.md"
  - "Repo: /home/stra/teamolimpo-paper/"
  - "Template Overleaf arXiv: https://www.overleaf.com/latex/templates/arxiv-template/"

teamolimpo-paper/
├── paper/
│   ├── whitepaper.md       # 🇬🇧 originale
│   ├── whitepaper.tex      # 🇬🇧 da CREARE — LaTeX con TikZ nativo
│   ├── whitepaper-it.md    # 🇮🇹 (lasciare invariato)
│   └── references.bib      # da CREARE — 21 riferimenti in BibTeX
├── docs/
├── assets/
│   └── images/
├── README.md
└── LICENSE
```

## Sezioni Bianco — Cosa NON Fare

1. **NON tradurre alla lettera**: Le sezioni in .md vanno trasposte in LaTeX, non copiate brutalmente. Adatta la formattazione.
2. **NON inserire frontmatter YAML**: Rimuovilo completamente. Il LaTeX non lo usa.
3. **NON usare `enumerate`/`itemize` per tutto**: Le liste semplici sì, ma per strutture dati usa tabelle o descrizioni.
4. **NON hardcodare path**: I path TikZ vanno risolti con `\includegraphics{}` se servono immagini, ma qui usiamo **TikZ puro** — nessun file esterno.
5. **NON esagerare con la grafica**: I diagrammi TikZ devono essere **compatti** (max 1 pagina ciascuno). Se escono troppo grandi, usa `\resizebox` o `\scalebox`.
6. **NON spostare i diagrammi in appendice**: Ogni diagramma va nella sezione corrispondente (proprio come nell'originale).
7. **NON modificare il contenuto testuale**: Le parole, le frasi, l'abstract, le definizioni — uguali identiche. Cambia solo la formattazione.

## Formato Output

### File 1: `paper/whitepaper.tex`

**Struttura LaTeX:**

```latex
\documentclass[12pt,a4paper]{article}

% --- Pacchetti essenziali ---
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\geometry{margin=1in}
\usepackage{setspace}
\onehalfspacing
\usepackage[backend=bibtex,style=numeric, sorting=none]{biblatex}
\addbibresource{references.bib}

\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning,fit,backgrounds,calc,decorations.pathreplacing}
\usepackage{tabularx}
\usepackage{booktabs}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{float}

% --- Stile TikZ condiviso ---
\tikzstyle{box} = [rectangle, draw, text centered, minimum height=1.2em, rounded corners]
\tikzstyle{arrow} = [thick,->,>=stealth]

% Metadata
\title{Team Olimpo: An Agent Qualification Framework for Production-Ready Multi-Agent Systems}
\author{Team Olimpo}
\date{\texttt{github.com/RangO1972/teamolimpo-paper}}
\hypersetup{
  pdfauthor={Team Olimpo},
  pdftitle={Team Olimpo: An Agent Qualification Framework...},
}

\begin{document}
\maketitle

--- QUI TUTTO IL CONTENUTO DEL PAPER ---

\printbibliography
\end{document}
```

**Regole per le sezioni:**
- Use `\section{}` per sezioni principali (1-12)
- Use `\subsection{}` per sotto-sezioni (es. 3.1, 3.2)
- Use `\subsubsection{}` per sotto-sotto-sezioni (es. 5.1, 5.2)
- Use `\textbf{}` per enfasi (non `\textit`)
- Use `\emph{}` per enfasi in corsivo quando serve contrasto
- Use `\texttt{}` per termini tecnici/path/nomi file
- Use `\begin{quote}` per citazioni e box evidenziati

**Tabelle:**
```latex
\begin{table}[H]
\centering
\caption{Agent Roles and Risk Classification}
\label{tab:agent-roles}
\begin{tabularx}{\textwidth}{lXcl}
\toprule
Agent & Role & Model & Risk Class \\
\midrule
Hermes & Pure orchestrator & big-pickle & High \\
...
\bottomrule
\end{tabularx}
\end{table}
```

**Code blocks:**
```latex
\begin{lstlisting}[frame=single,language=Python]
# code here
\end{lstlisting}
```

**Box evidenziati (per note e warning):**
```latex
\begin{quote}
\textbf{Key insight:} ...text...
\end{quote}
```

### File 2: `paper/references.bib`

Tutti i 21 riferimenti in formato BibTeX `@misc{...}`:

```bibtex
@misc{autogpt,
  author = {Significant Gravitas},
  title = {{AutoGPT}},
  year = {2023},
  howpublished = {\url{https://github.com/Significant-Gravitas/AutoGPT}}
}
```

Mappa ogni `[N]` del .md a un `\cite{key}` nel testo. 21 entry.

---

## Diagrammi TikZ — Template e Specifiche

### Diagramma 1 — System Architecture (Sezione 3.1)

Flowchart architetturale: da includere come figura singola, stile pulito.

```latex
\begin{figure}[H]
\centering
\resizebox{\textwidth}{!}{%
\begin{tikzpicture}[
  node distance=0.8cm and 2cm,
  box/.style={rectangle, draw, rounded corners, minimum width=2.8cm, minimum height=1.0cm, align=center, font=\small\bfseries},
  group/.style={rectangle, draw, dashed, rounded corners, fill=gray!5, inner sep=0.3cm, label={[font=\small\itshape]above:#1}},
  arrow/.style={thick,->,>=stealth}
]

% --- Top: User ---
\node[box, fill=gray!20] (user) {User};

% --- Orchestration Layer ---
\node[box, fill=blue!20, below=1.5cm of user] (hermes) {Hermes\\\small(Orchestrator)\\\small\textit{big-pickle}};

\node[group, fit={(hermes)}, label=above:Orchestration Layer] (orch) {};

% --- Research ---
\node[box, fill=green!20, below left=1.5cm and -0.5cm of hermes] (proteo) {Proteo\\\small Senior Researcher};
\node[box, fill=green!20, below=0.3cm of proteo] (metis) {Metis\\\small Strategist};
\node[box, fill=green!20, below=0.3cm of metis] (pythagoras) {Pythàgoras\\\small Web Researcher};
\node[group, fit={(proteo)(metis)(pythagoras)}, label=above:Research \& Analysis] (research) {};

% ... continue for all groups ...
% Quality & Audit → Design → Content → Development
% 13 agenti totali

% --- Arrows from Hermes to all agents ---
\foreach \agent in {proteo, metis, pythagoras, atena, calliope, efesto, clio, dike, hermione, euterpe, demetra, eunomia}
  \draw[arrow] (hermes.south) -- ++(0,-0.2) -| (\agent.north);

% --- Special arrows ---
\draw[arrow, dashed] (atena.south) -- ++(0,-0.3) -| (hermes.east);
\draw[arrow, dashed] (metis.east) -- ++(0.5,0) |- (user.east);

\end{tikzpicture}%
}
\caption{Team Olimpo System Architecture}
\label{fig:architecture}
\end{figure}
```

**Nota**: Il template sopra è parziale. Completa con TUTTI i 13 agenti e TUTTI i gruppi, seguendo esattamente il diagramma Mermaid originale nella sezione 3.1 del whitepaper. I gruppi da creare:
- **Research \& Analysis**: Proteo, Metis, Pythàgoras
- **Design \& Construction**: Atena, Calliope
- **Development \& Tools**: Efesto
- **Quality \& Audit**: Clio, Dike
- **Content Production**: Hermione, Euterpe, Demetra, Eunomia

### Diagramma 2 — Handoff Sequence (Sezione 4.2)

Sequence diagram con `tikzpicture`.

Alternative tikz: usa il pattern `\draw[arrow]` con coordinate o usa `pgf-umlsd` se disponibile (ma meglio tikz puro per affidabilità).

```latex
\begin{figure}[H]
\centering
\begin{tikzpicture}[
  line/.style={thick},
  arrow/.style={thick,->,>=stealth},
  dashedline/.style={thick,dashed},
  box/.style={rectangle, draw, rounded corners, minimum width=2cm, minimum height=0.6cm, align=center, font=\small\bfseries}
]

% Lifelines (vertical lines for participants)
\node[box, fill=gray!20] (user) at (0,0) {User};
\draw[line] (user.south) -- ++(0,-12);

\node[box, fill=blue!20] (hermes) at (4,0) {Hermes};
\draw[line] (hermes.south) -- ++(0,-12);

\node[box, fill=green!20] (agent) at (8,0) {Worker};
\draw[line] (agent.south) -- ++(0,-12);

\node[box, fill=orange!20] (quality) at (12,0) {Quality Gate};
\draw[line] (quality.south) -- ++(0,-12);

% Messages
\draw[arrow] (user.south) -- node[above,sloped]{\small Task request} (hermes.north);
% timestamps down
\draw[arrow] (0,-1.5) -- node[above]{Task decomposition} (4,-1.5);
\draw[arrow] (4,-2.5) -- node[above]{Handoff file (delegation)} (8,-2.5);
\node[font=\tiny, below right] at (4,-2.5) {Library/Handoff/YYYY/MM/...};
\draw[arrow] (8,-4) -- node[above]{Execute task} (8,-5);
\draw[arrow] (8,-5.5) -- node[above]{Handoff file (result)} (4,-5.5);
\draw[arrow] (4,-6.5) -- node[above]{Send for verification} (12,-6.5);
\draw[arrow] (12,-7.5) -- node[above]{Verification result} (4,-7.5);

% Quality check condition
\node[font=\small] at (12,-9) {Quality passed?};

\draw[arrow] (4,-9.5) -- node[above]{Quality OK} (0,-9.5);
\draw[dashedline] (12,-9) -- (12,-9.5) -- (8,-9.5);
\node[font=\small, below] at (8,-9.5) {Or revision loop back to agent};

\end{tikzpicture}
\caption{Handoff Communication Flow}
\label{fig:handoff}
\end{figure}
```

**Nota**: Il template sopra è parziale. Completa con tutti i passaggi dal diagramma Mermaid originale (sezione 4.2), seguendo esattamente la sequenza: User→Hermes, Hermes decomposes, Hermes→Agent handoff, Agent executes, Agent→Hermes result, Hermes→Quality gate, Quality→Hermes result, decision (pass/revision), Hermes→User final output.

### Diagramma 3 — AQF 5 Fasi (Sezione 5.2)

Flowchart sinistra→destra con box e feedback loop.

```latex
\begin{figure}[H]
\centering
\begin{tikzpicture}[
  node distance=1.5cm and 1cm,
  box/.style={rectangle, draw, rounded corners, minimum width=2.5cm, minimum height=1.8cm, align=center, font=\small\bfseries, text width=2.3cm},
  arrow/.style={thick,->,>=stealth},
  dashedarrow/.style={thick,dashed,->,>=stealth}
]

\node[box, fill=blue!30] (adq) {ADQ\\\small Agent Design\\Qualification\\\tiny Review prompt,\\identity, boundaries};
\node[box, fill=blue!40, right=of adq] (aeq) {AEQ\\\small Agent Environment\\Qualification\\\tiny Verify tools,\\permissions, env.};
\node[box, fill=blue!50, right=of aeq] (aoq) {AOQ\\\small Agent Operational\\Qualification\\\tiny Test on happy path,\\edge cases, failures};
\node[box, fill=blue!60, right=of aoq] (apq) {APQ\\\small Agent Performance\\Qualification\\\tiny Verify consistent\\output on production};
\node[box, fill=yellow!40, right=of apq] (acm) {ACM\\\small Agent Continuous\\Monitoring\\\tiny Track deviation,\\quality trends, drift};

\draw[arrow] (adq) -- node[above]{\footnotesize Design approved} (aeq);
\draw[arrow] (aeq) -- node[above]{\footnotesize Env. ready} (aoq);
\draw[arrow] (aoq) -- node[above]{\footnotesize Tests passed} (apq);
\draw[arrow] (apq) -- node[above]{\footnotesize Perf. verified} (acm);
\draw[dashedarrow] (acm) .. controls +(0,-1.5) and +(0,-1.5) .. node[below]{\footnotesize Drift detected → redesign} (adq);

\end{tikzpicture}
\caption{AQF — The Five Qualification Phases}
\label{fig:aqf}
\end{figure}
```

### Diagramma 4 — Agent Factory Pipeline (Sezione 6.1)

Flowchart top-down con 6 fasi, AQF gate come blocco centrale.

```latex
\begin{figure}[H]
\centering
\begin{tikzpicture}[
  node distance=1cm and 1.5cm,
  box/.style={rectangle, draw, rounded corners, minimum width=3cm, minimum height=0.8cm, align=center, font=\small},
  phase/.style={rectangle, draw, rounded corners, minimum width=3.5cm, minimum height=0.8cm, align=center, font=\small\bfseries},
  aqf/.style={rectangle, draw, rounded corners, fill=yellow!30, minimum width=3cm, minimum height=1.2cm, align=center, font=\small\bfseries},
  arrow/.style={thick,->,>=stealth}
]

\node[phase] (p1) {Phase 1: Domain Identification};
\node[phase, below=of p1] (p2) {Phase 2: Domain Analysis};
\node[box, right=1cm of p2, font=\tiny, text width=3cm] (p2desc) {Proteo — skills, tools,\\methodologies, risks};
\node[phase, below=of p2] (p3) {Phase 3: Evaluation};
\node[phase, below=of p3] (p4) {Phase 4: Construction};
\node[box, right=1cm of p4, font=\tiny, text width=3cm] (p4desc) {Atena — agent identity,\\prompt, boundaries};
\node[aqf, below=of p4] (aqfg) {AQF Gates\\ADQ→AEQ→AOQ→APQ→ACM};
\node[phase, below=of aqfg] (p6) {Phase 6: Deployment};

\draw[arrow] (p1) -- (p2);
\draw[arrow] (p2) -- (p3);
\draw[arrow] (p3) -- (p4);
\draw[arrow] (p4) -- (aqfg);
\draw[arrow] (aqfg) -- (p6);

% Optional loop back
\draw[arrow, dashed] (p6.south) -- ++(0,-0.5) -| (p1.east);

\end{tikzpicture}
\caption{Agent Factory Pipeline}
\label{fig:factory}
\end{figure}
```

**Nota**: Il template sopra è semplificato. Completa con tutti i dettagli dal diagramma Mermaid originale (sezione 6.1): includi i box descrittivi laterali per ogni fase, il ruolo di Calliope (optional), e il feedback loop come nell'originale.

---

## Criteri di Accettazione

Prima di dichiarare completato, verifica:

1. [ ] **Tutte le 12 sezioni presenti** — abstract → conclusioni (stesso ordine, stesso titolo)
2. [ ] **Tutto il testo preservato** — nessuna frase omessa, nessun paragrafo saltato
3. [ ] **Tutte le tabelle trasposte** — stessi dati, stesse intestazioni
4. [ ] **Tutti i 4 diagrammi presenti** — in TikZ nativo, nella sezione corretta
5. [ ] **Tutte le references trasformate** — 21 entry in BibTeX, match con `\cite{}` nel testo
6. [ ] **Frontmatter YAML rimosso** — non deve apparire nel .tex
7. [ ] **Compilabile su Overleaf** — usa solo pacchetti standard, niente pacchetti oscuri
8. [ ] **Nessun file esterno** — zero immagini, zero .sty, zero .cls aggiuntivi
9. [ ] **Nessun path assoluto** — tutto relativo alla cartella `paper/`
10. [ ] **Linguaggio invariato** — stessi testi, stessa formattazione semantica

## Output Atteso

Scrivi i file in `/home/stra/teamolimpo-paper/paper/`:

- `whitepaper.tex` — file LaTeX completo, compilabile su Overleaf
- `references.bib` — 21 riferimenti in BibTeX

Dopo aver finito, fammi sapere. Clio farà una verifica indipendente.
