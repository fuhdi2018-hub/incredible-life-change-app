"""Phase 1 TTS evaluation: YarnGPT Yoruba speech test.

Saves a Yoruba sentence spoken by speaker "abayomi" to yarngpt_test.wav.

Notes (eval-only workarounds, NOT app code):
- yarngpt 0.2.0's bundled WavTokenizer checkpoint URL is stale (returns
  "Entry not found"), so this script fetches the current file
  (wavtokenizer_large_speech_320_v2.ckpt) into yarngpt's expected path first.
- torch>=2.6 defaults torch.load to weights_only=True, which the old
  outetts loader doesn't pass; we patch the default back for this
  trusted Hugging Face file only.
"""
import os

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_DISABLE_XET"] = "1"  # xet CAS breaks on this connection; use plain HTTP

import torch

_orig_load = torch.load


def _patched_load(*args, **kwargs):
    kwargs.setdefault("weights_only", False)
    return _orig_load(*args, **kwargs)


torch.load = _patched_load

import shutil
from huggingface_hub import hf_hub_download

MODEL_PATH = os.path.expanduser(
    "~/.yarngpt/models/wavtokenizer_large_speech_320_24k.ckpt"
)


def ensure_ckpt():
    if os.path.exists(MODEL_PATH) and os.path.getsize(MODEL_PATH) > 1_000_000:
        print("Checkpoint present, skipping download.")
        return
    print("Downloading checkpoint (~1.75GB, resumable) ...")
    last_err = None
    for attempt in range(1, 6):
        try:
            cached = hf_hub_download(
                repo_id="novateur/WavTokenizer-large-speech-75token",
                filename="wavtokenizer_large_speech_320_v2.ckpt",
            )
            break
        except Exception as e:
            last_err = e
            print(f"Attempt {attempt}/5 failed, retrying: {type(e).__name__}")
    else:
        raise last_err
    shutil.copyfile(cached, MODEL_PATH)
    print("Checkpoint download complete.")


ensure_ckpt()

from yarngpt import generate_speech
import torchaudio

TEXT = "Jésù wá gẹ́gẹ́ bí alátúnṣe ńlá. Ìtara ilé rẹ ti jẹ mí run."

print("Generating Yoruba speech with speaker 'abayomi' ...")
audio = generate_speech(TEXT, speaker="abayomi", language="yoruba")

torchaudio.save("yarngpt_test.wav", audio, sample_rate=24000)
print("Saved yarngpt_test.wav — have a listen.")
