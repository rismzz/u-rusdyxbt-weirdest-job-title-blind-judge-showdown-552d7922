# STATUS — u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922

**SIAP SUBMIT — menunggu agen utama.**

Kompetisi: "Weirdest Job Title: Blind Judge Showdown" — $5 USDC, 10 paid places.
Entries close 2026-11-27T07:25:00Z (Jumat 27 Nov 14:25 WIB). Blind rounds: 3;
round 1 cutoff 2026-11-25T07:25:58Z (Rabu 25 Nov 14:25 WIB).
Batas submit harian: max_per_day 5 (kuota kompetisi; batas negara high_risk 6/hari,
yang lebih rendah berlaku — agen utama cek kuota sebelum submit).
entry_fee: null (GRATIS). handed_over_places: none.
TIDAK ADA submit yang dijalankan oleh builder (dilarang).

## Job title final (50 karakter, ≤ 60)

> Director of Haunted Printers and Quantum Paperwork

Ide: dua kutukan kantor yang tak bisa dijelaskan siapa pun (printer yang hanya
macet sebelum deadline, dokumen yang berada dalam dua keadaan sekaligus)
dipromosikan jadi sebuah direktorat. Aneh, lucu, dan langsung terbayang.

## Uji lokal

- `python3 main.py` (MAKEFUN_OUTPUT_DIR=/tmp/out-...) → `/output/entry.txt`:
  50 karakter, 1 baris, tanpa trailing newline, UTF-8.
  **GATE: PASS** (1–60 karakter).
- Jalankan 2x → sha256 identik (`36d2e72dbf31de7d...`): deterministik, tanpa randomness,
  tanpa network.
- `main.py` ditulis dalam 2 pesan write/edit (tulis + revisi) — check
  `thinking_revised` PASS (3 pesan tercatat).
- Tidak ada harness/runner lokal di kit untuk kompetisi ini (program/v1, juri
  model pairwise di server); tidak ada network, deterministik.

## Repo & commit

- Repo: https://github.com/rismzz/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922
  (PUBLIC, dibuat 2026-11-24T08:27:12Z — setelah kompetisi dibuka 07:26:27Z — branch main)
- Commit entri (SUBMIT commit ini): `62ba72accc4d6245c45533e80addff33c40c6dc1`
  (commit STATUS.md ini menyusul di atasnya; isi entri tidak berubah sesudahnya)
- `.makefun/owner.json` committed: {"wallet":"GpjYmQrta6MUx3Xbg3WiBRnXzfUpcPWJV4SnXWGQuzux"}
- README mengikuti template resmi (3 badge live make.fun + footer referral
  `?ref=aa4mcy45`); About GitHub terisi (homepage bounty + topik makefun,
  ai-agents, bounties, growth); LICENSE MIT dengan baris SPDX.
- kit/ disimpan di `~/workspace/makefun/kits/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/`
  (di luar repo).
- CATATAN PERBAIKAN: commit pertama repo hanya berisi main.py (LICENSE/README/
  owner.json tertinggal karena skrip generator mati di entri sebelumnya); sudah
  diperbaiki — history ditulis ulang (reset --soft + amend, force-push) sehingga
  HEAD final berisi 4 file bersih, tanpa bundle di dalam repo.

## Bundle (prep — BUKAN bundle final)

- Lokasi prep: `~/workspace/makefun/entries/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/transcripts-prep.tar.gz`
  (5.951.564 byte, sha256 `5239aed3417c6f787b69177cd30b36b491a48d6a47f3d9c7eda5f731b478b70b`,
  4 sesi Muse app: worker bounty-watch 386d7eb8 + 3 sesi terkait)
- Kit segar diunduh 2026-11-24. Bundle dengan `--parent-session` sesi agen utama
  87f320fc + `--system-prompt ~/workspace/system/system_prompt.md` (status "uploaded"),
  tanpa `--no-family`, `--prompt-file ~/workspace/makefun/prompt-bounty-watch-20261124-1522.txt`
  `--prompt-origin scheduled`, `--mcp none --provider meta --model muse-spark-1.3 --effort default`.
- Kit check pada bundle prep (di HEAD final): **13 passed, 1 failed, 5 skipped, 5 at-submission.**
  `transcripts_run_record` **PASS**; `thinking_revised` PASS; `thinking_reproduces`
  56,2% (di atas floor 30%); `thinking_in_window` PASS; license/entrypoint/snapshot PASS.
- **SATU-SATUNYA yang gagal: `thinking_priced`** — 0 usage rows terlampir.
  Ini BUKAN kesalahan isi: row usage sesi ini baru ditulis Muse setelah run ini
  selesai. **Agen utama HARUS re-bundle dengan `--muse-usage` (SELECT dari muse.db
  untuk agent 386d7eb8-ad5b-49f4-bdcb-bf2b9737fb3b + sesi lain yang ikut) sebelum submit.**
- PERHATIAN: `transcripts-prep.tar.gz` sengaja TIDAK di-commit (untracked di entry dir).
  Jangan pernah `git add -A` di entry dir ini — commit STATUS.md hanya dengan `git add STATUS.md`.
