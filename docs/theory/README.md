# docs/theory/ — 理論資料

1.58-bit 行列（{-1, 0, 1} 行列）の行列式に関する理論的文書をまとめるディレクトリ。

## ディレクトリ構成

```
docs/theory/
├── README.md              # 本ファイル
├── proofs/                # 形式的証明
├── analysis/              # 計算的解析・探索結果
└── derivations/           # 個別の数学的導出ノート
```

## 予定ファイル

### proofs/ — 形式的証明

| ファイル | 内容 |
|---|---|
| `proof_det_max_small_n.md` | n ≤ 4 の det_max(n) の証明（網羅的探索による） |

### analysis/ — 計算的解析

| ファイル | 内容 |
|---|---|
| `distribution_analysis.md` | 行列式分布の統計的性質の解析 |

### derivations/ — 導出ノート

| ファイル | 内容 |
|---|---|
| `hadamard_bound.md` | Hadamard 上界の ternary 行列版の導出 |

## 関連ファイル

- `docs/drafts/`: LaTeX 文書（論文草稿）
- `docs/json_schema_det_results.md`: 行列式計算結果の JSON スキーマ
- `docs/json_schema_analysis.md`: 分析結果の JSON スキーマ
- `handover/`: 引き継ぎ・ワークフロー文書
