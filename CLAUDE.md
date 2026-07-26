# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal **learning** repository, not a product. The owner is working through a multi-week
curriculum on speech/audio AI (audio foundations → Whisper/ASR). Everything lives under `learning/`.

## Who this is for, and how to help

The owner is a polyglot with a recent MSc in AI, job-hunting for a first speech-AI role on a 2-3
month horizon. ML theory is fresh and doesn't need explaining; audio/DSP and production
engineering habits are both new. So skip what an embedding or a training loop is, and don't skip
what a mel scale, a formant, or a frame hop is — or the practical tooling a degree doesn't cover.
With no prior industry role to point at, this repo has to carry the evidence, so depth that
survives an interview question beats breadth that doesn't.

`learning/week1-audio/README.md` states the working agreement:

> **Rule (from the plan):** type the code yourself. The skeletons here have TODOs — AI can
> *explain*, but you write it.

This applies to the **curriculum exercises**, and it is not a ban on writing code. For a TODO in a
day-N script, explain the concept and name the relevant API, then let the owner type it —
generating it skips the entire point. For anything that isn't the lesson (tooling, config,
debugging, scaffolding, plotting boilerplate) or when asked for code directly, just write it.

Files with unfinished TODOs and rough first-draft code are expected. Don't tidy them unprompted.

## Layout and flow

- `learning/week1-audio/README.md` — the Week 1 day-by-day plan (Day 1 waveform → Day 5
  transformers). Read this first to know where the user is in the curriculum; recent commits tell
  you which day is in progress.
- `learning/week1-audio/LEARNINGS.md` — the session log the user is meant to fill in per day.
  Prompt them toward it rather than writing entries for them.
- `learning/notes/` — conceptual notes (linguistics, speech production, human-vs-AI pipeline),
  written by the user in their own words.
- Day-N scripts live either at the `week1-audio/` root (`day1_waveform.py`) or in a per-day
  subdirectory (`day2/`). Both patterns are in use.

## Running things

Single venv for all of Week 1, Python 3.14 (Homebrew):

```bash
cd learning/week1-audio
source .venv/bin/activate
pip install -r requirements.txt
python day1_waveform.py
```

There is no build, no linter, and no test suite. Scripts are run directly and are verified by
looking at the matplotlib window they open.

## Gotchas

- **Audio paths are bare relative strings** (`"sample.wav"`, `"my_voice.wav"`), so a script only
  works from the directory that holds its audio. `sample.wav` sits in `week1-audio/`, but
  `my_voice.wav` sits in `learning/` — the `day2/` scripts were run from `learning/` with the venv
  activated from elsewhere. If a script fails to find its file, check the cwd before changing code.
- **All audio is gitignored** (`*.wav`, `*.mp3`, `*.m4a`, `*.flac`), so recordings never appear in
  `git ls-files`. A missing `.wav` in git does not mean it's missing on disk.
- **`requirements.txt` is behind the code.** `day2/save_voicewav.py` needs `sounddevice` and
  `soundfile`; both are installed in the venv but only `soundfile` is listed. `sounddevice` also
  needs macOS microphone permission for the terminal app to record.
- Week 2 will add `openai-whisper` and `jiwer` for the WER sprint; the same folder is intended to
  host it.
