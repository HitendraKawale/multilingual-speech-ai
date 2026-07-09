# Week 1 — Audio Foundations (start here)

This is Week 1. Goal: understand
how sound becomes model input, and lock down the ML primitives you've used without studying.

**Rule (from the plan):** type the code yourself. The skeletons here have TODOs — AI can
*explain*, but you write it. End each day with the "explain it in 60s" test.

---

## Step 0 — Setup (10 min, once)
```bash
cd learning/week1-audio
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
Grab a short audio clip to work with — record ~10s of yourself (any phone voice-memo,
export as .wav/.m4a) and drop it in this folder as `sample.wav`. You'll reuse it all week.

---

## Day 1 — Waveform (your first run)
- **Do:** open `day1_waveform.py`, fill the TODOs, run it: `python day1_waveform.py`
- **Learn:** waveform, **sampling rate** (why 16 kHz for speech), bit depth, mono vs stereo.
- **Explain in 60s:** what does the y-axis of a waveform represent? What does the sampling rate change?

## Day 2 — Spectrogram + mel spectrogram
- **Do:** duplicate Day 1 into `day2_spectrogram.py`; compute and plot a spectrogram, then a **mel spectrogram** (`librosa.feature.melspectrogram`).
- **Learn:** Fourier transform (intuition only), why we look at frequencies over time, why "mel" (perceptual scale).
- **Explain in 60s:** what is a mel spectrogram and why do speech models use it instead of the raw waveform?

## Day 3 — HF Audio Course
- Work through **Unit 1** (audio data) + skim **Unit 2**: huggingface.co/learn/audio-course
- Note anything new in `LEARNINGS.md`.

## Day 4 — ML primitives refresher (own what you've used)
- **Do:** in `day4_embeddings.py`, embed 5 short sentences (sentence-transformers) and compute
  cosine similarity between them with numpy — by hand, not a library helper.
- **Learn:** what an embedding is, vector space, cosine similarity; train/val/test; over/underfitting.
- **Explain in 60s:** what is an embedding, and why does cosine similarity measure "closeness in meaning"?

## Day 5 — Transformers, high level
- **Read:** Jay Alammar, "The Illustrated Transformer."
- **Explain in 60s (out loud, recorded):** tokens → embeddings → attention → output. What does attention *do*?
- **Checkpoint:** you can explain mel spectrogram, embedding, and attention each in 60s. If not, revisit.

---

## Keep a log
Write in `LEARNINGS.md` every session: what you did, what broke, what clicked. It becomes
interview gold ("tell me about something you learned recently").

> Next week (Week 2) you'll install Whisper and do **Sprint 0** — transcribe your 5 languages,
> compute WER by hand. This folder is where that lives too.
