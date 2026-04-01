# モジュールimportに関する注意事項

本プロジェクトでは、以下の点に注意してモジュールimportを行ってください。

- すべてのモジュールは `src/` ディレクトリ以下に配置します。
- サンプルコードや実験用スクリプトは `experiments/` ディレクトリ以下に配置します。
- すべてのコードは「レポジトリルート」から端末で実行することを前提とします。
- そのため、`experiments/` 以下のスクリプトから `src/` 以下のモジュールをimportする場合は、以下のようにパスを明示的に指定してください：

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
```

- この指定により、`src/` 以下のモジュールを正しくimportできます。
- 他のディレクトリ構成や実行方法を採用する場合は、同様にパスの指定を調整してください。
