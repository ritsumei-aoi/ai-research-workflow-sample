# 1.58-bit 行列の行列式分布

n 次正方行列で、値が {-1, 0, 1} のいずれかである行列（1.58-bit 行列）について、行列式の分布と極値を計算的に調べるプロジェクト。

## 概要

### 研究テーマ

- **行列式分布**: 全 3^(n²) 個の n×n ternary 行列について、行列式の値の分布を計算
- **極値問題**: det_max(n) = max{|det(A)| : A ∈ {-1,0,1}^(n×n)} を求める
- **漸近的性質**: det_max(n) の n に関する増大度の考察

### 背景

- log₂(3) ≈ 1.58 なので、各成分は約 1.58 ビットの情報量を持つ
- ±1 行列の最大行列式は Hadamard 行列と関連（Hadamard 予想）
- {-1, 0, 1} 行列は ±1 行列の一般化であり、0 を許すことで異なる構造が現れる

## ディレクトリ構成

```
├── data/
│   ├── det_results/       # Schema 1: n ごとの行列式計算結果
│   └── analysis/          # Schema 2: n 横断の分析結果
├── src/ternary_det/       # コアライブラリ
├── tests/                 # テストコード
├── experiments/           # 実験スクリプト
├── docs/
│   ├── theory/            # 理論資料（証明・解析）
│   ├── drafts/            # 論文草稿
│   └── reviews/           # レビュー管理
├── handover/              # セッション引き継ぎ・ワークフロー
├── scripts/               # ユーティリティ
└── log/                   # セッションログ
```

## クイックスタート

```bash
pip install -e .
pip install -r requirements.txt
pytest tests/ -v
```

## JSON スキーマ

- [Schema 1: 行列式計算結果](docs/json_schema_det_results.md)
- [Schema 2: 分析結果](docs/json_schema_analysis.md)

## ワークフロー

- [handover/README.md](handover/README.md) — 引き継ぎ情報索引
- [handover/workflow_method_b.md](handover/workflow_method_b.md) — AI エージェントワークフロー

## ライセンス

MIT License
