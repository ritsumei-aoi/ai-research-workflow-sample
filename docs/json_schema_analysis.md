# JSON Schema: 分析結果 (Schema 2)

## 概要

複数の n にわたる行列式計算結果の集約分析を保存するスキーマ。

## ファイル配置

```
data/analysis/
├── analysis_1_to_3.json
├── analysis_1_to_6.json
└── ...
```

## ファイル命名規則

```
analysis_{n_min}_to_{n_max}.json
```

## スキーマ定義

```json
{
  "schema_version": "1.0",
  "n_range": [1, 6],
  "det_max_sequence": {
    "1": 1,
    "2": 2,
    "3": 4,
    "4": 12,
    "5": 32,
    "6": 100
  },
  "det_max_growth": {
    "ratios": {"2": 2.0, "3": 2.0, "4": 3.0, "5": 2.67, "6": 3.125},
    "log_ratios": {"2": 1.0, "3": 1.0, "4": 1.585, "5": 1.415, "6": 1.644}
  },
  "zero_fraction": {
    "1": 0.333,
    "2": 0.407,
    "3": 0.555,
    "4": 0.685
  },
  "conjectures": [
    {
      "id": "C1",
      "statement": "det_max(n) grows as c^n for some constant c ≈ 2.5",
      "evidence": "Numerical fit for n ≤ 6",
      "status": "unverified"
    }
  ],
  "metadata": {
    "analyzed_at": "2026-04-01T00:00:00Z",
    "source_files": ["det_1.json", "det_2.json", "det_3.json"]
  }
}
```

### フィールド説明

| フィールド | 型 | 必須 | 説明 |
|-----------|---|------|------|
| `schema_version` | string | ✅ | スキーマバージョン |
| `n_range` | [int, int] | ✅ | 分析対象の n の範囲 |
| `det_max_sequence` | object | ✅ | {n: det_max(n)} |
| `det_max_growth` | object | ✅ | 隣接比・対数比 |
| `zero_fraction` | object | ✅ | det=0 の割合 |
| `conjectures` | array | — | 予想リスト |
| `metadata` | object | ✅ | 分析メタ情報 |
