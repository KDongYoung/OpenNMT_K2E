# OpenNMT_K2E
Open NMT - Korean to English translation

---------------------------------------------------------------------------------------------------
- MECAB + sentencepiece 실행하여 txt파일 변환

!python mecab_sentencepiece.py

- preprocess

!python preprocess.py

- train

!python train.py -save_model data/model/model -world_size 1 -gpu_rank 0

- translate

!python translate.py -model data/model/model.pt -output data/prediction/pred.txt -replace_unk -verbose -beam_size 1 -gpu 0

- BLEU

!perl tools/multi-bleu.perl data/tgt-test-token.txt < data/prediction/pred.txt

- GUI
gui2.py


This work is based on [\[OpenNMT\]](https://github.com/OpenNMT/OpenNMT-py)
