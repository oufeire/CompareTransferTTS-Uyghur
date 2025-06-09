# Config

This section describes the main configuration files used for training three Uyghur TTS models (M0, M1, M2), including preprocessing parameters, training hyperparameters, and model architecture. All models are based on the FastSpeech 2 framework with modifications to accommodate low-resource scenarios and cross-lingual transfer learning.

# Model Variants

M0: No pretraining; all parameters are randomly initialized.
M1: Pretrained on LJSpeech (English).
M2: Pretrained on CSS10-Russian (Russian).

Except for the pretrained model loading, all other configurations are identical across M0–M2 to ensure fair experimental comparison.

# Configuration Structure

The system is configured through three main YAML files:

# 1. preprocess.yaml – Preprocessing Configuration

- Audio is sampled at 22050 Hz. mel_fmax is set to 8000 to support HiFi-GAN vocoder.
- Pitch and energy features are extracted at the phoneme level and normalized, which improves prosody naturalness in synthesized speech.
- language_id is added as a feature to support multilingual pretraining scenarios.
- Lexicon sources:
  - Uyghur: Generated via custom G2P system and manually verified.
  - Russian: Based on a normalized version of the CSS10 lexicon.
- All languages share a unified phoneme inventory. Russian phonemes are standardized accordingly.
- To avoid leaking personal identifiers, lexicon paths use a generic placeholder: {username}/FastSpeech2/lexicon/....

# 2. train.yaml – Training Configuration

- Optimizer: Adam with batch size of 16.
- Learning rate scheduler: 3-stage annealing at 300k, 400k, and 500k steps with a decay rate of 0.3.
- Training steps: 300,000 in total.
- Checkpoints saved every 10,000 steps; validation and synthesis run every 1,000 steps.

# 3. model.yaml – Model Architecture

- Transformer encoder: 4 layers; decoder: 6 layers.
- Each layer has 2 attention heads and 256 hidden units.
- Pitch and energy use linear quantization, suitable for normalized inputs.
- The model is set to single-speaker mode (multi_speaker: false).
- Vocoder: HiFi-GAN with speaker: "universal" to support non-LJSpeech datasets.

# Additional Notes

- All datasets (Uyghur, Russian, English) were preprocessed and lexicon-built independently to ensure consistent phoneme-level inputs.
- During inference, a shared decoding configuration is used: fixed speaker_id, and pitch/energy/duration scales are all set to 1.0, ensuring fair model comparison.

