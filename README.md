# CompareTransferTTS-Uyghur
A Uyghur text-to-speech (TTS) model trained with transfer learning from English and Russian using the FastSpeech 2 architecture.

## 🔗 Resources

- **Uyghur Speech Data** (30 minutes, female speaker) for fine-tuning:  
  [Multilingual LibriSpeech - OpenSLR 22](http://www.openslr.org/22/)

- **LJSpeech (English) Dataset** for pretraining:  
  [LJSpeech Dataset by Keith Ito](https://keithito.com/LJ-Speech-Dataset/)

- **CSS10-Russian Dataset** for pretraining:  
  [CSS10 GitHub Repository](https://github.com/bootphon/CSS10)

- **Montreal Forced Aligner (MFA)**:  
  [Montreal Forced Aligner GitHub](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner)

- **FastSpeech 2 Implementation** used in this study:  
  [ming024/FastSpeech2 GitHub](https://github.com/ming024/FastSpeech2)


 
 
# Instructions

You can reproduce our Uyghur TTS experiments using the steps below.  
   
Please refer to the links and config files provided in this repository for more details.

---

## Steps

1. **Activate your environment.**  
   We recommend using Python/3.8.16-GCCcore-11.2.0 and following the installation instructions from the Montreal Forced Aligner (MFA). 


2. **Prepare the phoneme set.**  
   For Uyghur, we used a Uyghur New Script phoneme inventory derived from the Uyghur romanization scheme.  
   Please ensure that the phoneme symbols used in `text/symbols.py` match the dictionary and `.lab` files.
3. **Validate the English and Russian audio files.**  
   ```bash
   mfa validate /path/to/your/audio_and_lab_files/ /path/to/your/dictionary/
   ```

4. **Train the English and Russian acoustic models:**  
   ```bash
   mfa train /path/to/your/audio_and_lab_files/ /path/to/your/dictionary/ /output/path
   ```

5. **Align the English and Russian datasets:**  
   ```bash
   mfa align /path/to/your/audio_and_lab_files/ /path/to/your/dictionary/ /output/path
   ```
After alignment, we recommend checking the English and Russian `.lab` label files for fine-grained IPA symbols.  
If such phonetic forms are present, please normalize them to their base phonemes to ensure consistency with the phoneme inventory defined in the lexicon.

Examples:
- Length mark `[ː]`: `tː → t`
- Dental diacritic `[̪]`: `d̪ → d`
- Palatalization mark `[ʲ]`: `tʲ → t`
6. **Preprocess data for each language:**  
   ```bash
   python3 preprocess.py config/your_language/preprocess.yaml
   ```

7. **Train the source models (English/Russian):**  
   ```bash
   python3 train.py -p config/your_language/preprocess.yaml -m config/your_language/model.yaml
   ```

8. **Validate the Uyghur audio files:**  
   ```bash
   mfa validate /path/to/uyghur/audio_and_lab/ /path/to/uyghur/dictionary/
   ```

9. **Train the Uyghur acoustic model for MFA:**
    
   The Uyghur pronunciation dictionary (G2P-generated and manually corrected) is provided as `lexicon_uy`.  
   ```bash
   mfa train /path/to/uyghur/audio_and_lab/ /path/to/uyghur/dictionary/ /output/path
   ```
11. **Align the Uyghur audio files:**  
   ```bash
   mfa align /path/to/uyghur/audio_and_lab/ /path/to/uyghur/dictionary/ /output/path
   ```

11. **Preprocess Uyghur data:**  
   ```bash
   python3 preprocess.py config/uyghur/preprocess.yaml
   ```

12. **Fine-tune from the pretrained model (e.g., English):**  
   ```bash
   python3 train.py -p config/uyghur/preprocess.yaml -m config/uyghur/model.yaml --restore_step 200000
   ```

13. **Synthesize Uyghur audio:**  
   ```bash
   python3 synthesize.py --text "ha ras gezit botkisi aqamsәn ya?" --restore_step 300000 --speaker_id 0
   ```


