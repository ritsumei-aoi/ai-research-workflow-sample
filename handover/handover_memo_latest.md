# Handover Memo (Latest Session)

**このファイルは最新セッションの情報のみを含みます。過去のセッションは `handover_memo_archived.md` を参照してください。**

***

## Current Status (最新状況)

**最終更新**: 2026-04-01
**実施方式**: Method B
**セッションブランチ**: main
**現在の進行状況**: Step 1--4 の実装が進行中。Step 1--3 は完了（n=1..3 の結果を data/det_results に保存）。Step 4（extremal）の基本実装を追加。

***

## Implementation Roadmap (実装ロードマップ)

- [x] **Step 1**: コアライブラリの実装（matrix_gen, det_compute, distribution）
- [x] **Step 2**: JSON スキーマの定義と I/O 実装（schema_io）
- [x] **Step 3**: n=1,2,3 の網羅的計算と結果保存
- [x] **Step 4**: 極値探索アルゴリズムの実装（extremal）
- [ ] **Step 5**: n=4,5 の計算（サンプリング含む）
- [ ] **Step 6**: det_max(n) の性質の理論的考察
- [ ] **Step 7**: 理論文書・論文草稿の作成

***

## Implementation Guidelines (実装ガイドライン)

- 行列式は整数として厳密計算（浮動小数点は使用しない）
- n ≤ 4 では全数探索、n ≥ 5 ではランダムサンプリングを併用
- JSON スキーマにはバージョン番号 `schema_version` を含める
- 結果の再現性のため、乱数シードを記録する

***

## Future Work (将来の作業)

- {-1, 0, 1} 行列から {-1, 1} 行列（Hadamard 型）への特殊化
- 対称行列・反対称行列への制限
- 特性多項式の分布
- n が大きい場合の漸近公式との比較

***

## 🔄 次回セッションへの引き継ぎ

### 短期目標

1. Step 5: n=4,5 の計算（サンプリング実行済み、n=4 exhaustive は未実施）
2. Step 6: det_max(n) の性質の理論的考察（次セッションの課題）

### 注意事項

- n=4 の全数探索（43,046,721 行列）は時間とディスクを消費するため、実施前に許可が必要です。
- data/det_results に n=1..3 の exhaustive 結果と n=4/n=5 のサンプリング結果が保存済み。
