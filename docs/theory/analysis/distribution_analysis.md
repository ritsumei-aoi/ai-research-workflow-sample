# Ternary Matrix Determinant Distribution Analysis (n=1–4)

本ドキュメントでは，n=1,2,3,4 の三値行列（要素が -1, 0, 1）に対する行列式の全列挙分布と，計算統計情報をまとめます．

## 概要
- 各 n について，`experiments/compute_and_save_det.py` で全列挙し，`data/det_results/det_{n}.json` に保存
- 実行環境: Python, MacBook Pro (Apple M1)
- 実行時間: n=1: 0.0000s, n=2: 0.0001s, n=3: 0.0303s, n=4: 83.5259s

## n=1
- 総数: 3
- 分布: -1: 1, 0: 1, 1: 1
- det_max: 1, det_min: -1

## n=2
- 総数: 81
- 分布: -2: 4, -1: 20, 0: 33, 1: 20, 2: 4
- det_max: 2, det_min: -2

## n=3
- 総数: 19683
- 分布: -4: 240, -3: 288, -2: 1896, -1: 3480, 0: 7875, 1: 3480, 2: 1896, 3: 288, 4: 240
- det_max: 4, det_min: -4

## n=4
- 総数: 43,046,721
- 分布（抜粋）: det=0: 15,099,201, det=±16: 384, det=±12: 6144, det=±10: 18432, det=±8: 162816, det=±6: 423936, det=±4: 1,648,704, det=±2: 4,824,192, det=±1: 5,170,368
- det_max: 16, det_min: -16

詳細分布は data/det_results/det_4.json を参照してください．

---

## 実行時間まとめ
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
