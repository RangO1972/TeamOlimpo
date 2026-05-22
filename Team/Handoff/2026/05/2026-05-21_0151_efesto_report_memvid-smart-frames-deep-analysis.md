---
data: '2026-05-21'
timestamp: '2026-05-21T01:51:44'
agent: efesto
invocation: 19
type: report
status: completed
priority: high
title: Memvid Smart Frames — Deep Analysis
task_id: T-043
output_refs: Team/Fucina/memvid-smartframes-analysis.md
---

## Memvid Smart Frames — Analisi Completa

Repository: `/home/stra/TeamOlimpo/Team/Fucina/repos/memvid/`
Report salvato in: `/home/stra/TeamOlimpo/Team/Fucina/memvid-smartframes-analysis.md`

### Perimetro analisi
- **MV2_SPEC.md** — specifica formato file (versione 2.1)
- **source Rust**: 170+ file analizzati in `src/`
- **Cargo.toml**: feature flags, dipendenze

### Risultati chiave

| Aspetto | Conclusione |
|---------|-------------|
| **Smart Frame** | Struct `Frame` in `types/frame.rs`: payload compresso (Zstd), URI mv2://, chunk manifest per documenti grandi, temporal anchor, stato enrichment |
| **Formato .mv2** | Single-file elegante: Header(4K) + WAL(1-64MB) + Data Segments + Indici (Tantivy, HNSW, time) + TOC |
| **Chunking** | 2 livelli: naive (1200 char a confini frase) + strutturale (preserva tabelle con header propagation, code block, heading). Default strutturale automatico |
| **WAL** | Circolare embedded, BLAKE3 checksum, checkpoint a 75% o 1000 op. Crescita dinamica per doubling |
| **Crash safety** | WAL replay + AtomicWriteFile staging lock — doppia garanzia |
| **Compressione adattiva** | **Non presente**. Solo Zstd uniforme, nessuna gerarchia hot/warm/cold. I Tier (Free/Dev/Enterprise) controllano solo capacità |
| **Search** | Multi-engine: Tantivy BM25, HNSW vettoriale (384d cosine), sketch pre-filter (simhash). Adaptive retrieval con 5 strategie (combined default) |
| **Temporal** | Time index + temporal track: menzioni temporali risolte in timestamp (anche frasi relative come "next friday") |
| **Encryption** | Capsule .mv2e: AES-256-GCM + Argon2id KDF |
| **Memory Cards** | Triple SPO (entità-attributo-valore) per memoria strutturata, con schema validation |

### Deviazioni spec/codice
- Spec dice CRC32, codice usa BLAKE3
- Spec menziona encoding Lz4, codice ha solo Plain/Zstd

### Output
Report completo salvato in `Team/Fucina/memvid-smartframes-analysis.md`
