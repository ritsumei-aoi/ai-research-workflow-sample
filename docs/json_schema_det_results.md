# JSON Schema: 行列式計算結果 (Schema 1)

## 概要

n×n ternary 行列 ({-1, 0, 1} 行列) の行列式計算結果を保存するスキーマ。

## ファイル配置

```
data/det_results/
├── det_1.json
├── det_2.json
├── det_3.json
└── ...
```

## ファイル命名規則

```
det_{n}.json
```

- `n`: 行列サイズ（正整数）

## スキーマ定義

```json
{
  "schema_version": "1.0",
  "matrix_size": 3,
  "entry_set": [-1, 0, 1],
  "computation_type": "exhaustive",
  "total_matrices": 19683,
  "distribution": {
    "0": 10935,
    "1": 2916,
    "-1": 2916,
    "2": 729,
    "-2": 729,
    "3": 324,
    "-3": 324,
    "4": 54,
    "-4": 54,
    "5": 0,
    "-5": 0
  },
  "det_max": 4,
  "det_min": -4,
  "extremal_matrices": {
    "max": [
      {
        "matrix": [[1, 1, 0], [0, 1, 1], [1, 0, 1]],
        "det": 4
      }
    ],
    "min": [
      {
        "matrix": [[1, 1, 0], [0, 1, 1], [1, 0, -1]],
        "det": -4
      }
    ]
  },
  "metadata": {
    "computed_at": "2026-04-01T00:00:00Z",
    "computation_time_sec": 0.5,
    "random_seed": null,
    "sample_size": null
  }
}
```

### フィールド説明

| フィールド | 型 | 必須 | 説明 |
|-----------|---|------|------|
| `schema_version` | string | ✅ | スキーマバージョン |
| `matrix_size` | integer | ✅ | 行列サイズ n |
| `entry_set` | array | ✅ | 行列成分の値集合 |
| `computation_type` | string | ✅ | `"exhaustive"` or `"sampling"` |
| `total_matrices` | integer | ✅ | 行列の総数（exhaustive: 3^(n²), sampling: sample_size） |
| `distribution` | object | ✅ | {行列式値(文字列): 出現回数} |
| `det_max` | integer | ✅ | 最大行列式値 |
| `det_min` | integer | ✅ | 最小行列式値 |
| `extremal_matrices` | object | ✅ | 最大・最小行列式を達成する行列のリスト |
| `metadata` | object | ✅ | 計算メタ情報 |

### computation_type

| 値 | 説明 |
|---|---|
| `"exhaustive"` | 全 3^(n²) 行列を網羅（n ≤ 4 推奨） |
| `"sampling"` | ランダムサンプリング（n ≥ 5）。`metadata.sample_size` と `metadata.random_seed` が必須 |

### 行列の表現

行列は行優先 (row-major) のリストのリストとして表現する：
```json
[[1, 0, -1], [0, 1, 1], [-1, 0, 1]]
```
→ 1行目 [1, 0, -1], 2行目 [0, 1, 1], 3行目 [-1, 0, 1]
