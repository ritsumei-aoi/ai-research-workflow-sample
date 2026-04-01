Created: today
Category:

## I1. src以下のモジュールimportのためのコード設定について

このプロジェクトでは，コードはレポジトリルートから実行することを想定します．そのため，
experiments などにあるコードは以下を指定することにします：
```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
```
これを指定するという注意事項を handover 以下に新規にファイルを作成して記載してください．現在の experiments にあるものはこちらで対応ずみです．つまり，記載する必要な情報は以下ですが，他にあればそちらの判断で加えてください：

- モジュールは`src` 以下に作っている
- サンプルコードは `experiments` 以下に作ることを基本とする
- 各コードはレポジトリルートから端末で実行することを想定する．これらより，各コードはモジュールimport のためのpathの指定を行う必要がある（上で提示したコード）

---

## I2. n=1,2,3,4 の検証に伴う統計情報の作成

n=4までを全て求めました． data 以下にデータが格納されているので，それを踏まえて
`docs/theory/analysis/distribution_analysis.md` を作成してください．
これは `docs/theory/README.md` で作成予定とされているものです．
現時点の data で作成した情報を元に作成してください．
ちなみに，現環境では以下の実行時間になったので，それも記載しておいてください．

```
% python ./experiments/compute_and_save_det.py
Computing n=1...
Saved data/det_results/det_1.json (time=0.0000s)
Computing n=2...
Saved data/det_results/det_2.json (time=0.0001s)
Computing n=3...
Saved data/det_results/det_3.json (time=0.0303s)
Computing n=4...
Saved data/det_results/det_4.json (time=83.5259s)
```
