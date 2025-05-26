# 小問3

雛形となる HTML テンプレート に、変数の値を埋め込んで出力する、 `render_html(tmpl: str, params: Dict[str, str]) -> str` という関数の作成を依頼されました。

- 第1引数 `tmpl` は HTML テンプレートの文字列が渡されます。
- 第2引数`params`は HTML テンプレート上に展開する値が格納されており、型は `Dict[str, str]` です。
- HTML テンプレートには 英小文字のみからなる変数の値を展開させることができ、例えば `price` という値を埋め込みたい場合は `<%price%>` と記述し、`paramｓ['price']` の値で置き換えます。
- HTML テンプレートで展開するよう指定された値は、params に必ず存在すると考えて良いです。
- `render_html` 関数での値の展開機能は、HTML 内の通常のテキストを出力するための利用を目的としています。
  - 通常のテキストとは `<p>このぶぶん</p>` のことです。
  - 半角スペースの出力を考慮する必要はありません。
  - 戻り値として返された内容をウェブブラウザで表示したときに `params` に格納された文字列が、そのままウェブブラウザ上に表示されている必要があります。
  - HTML タグの出力や HTML の属性の出力、JavaScript の作成を行うことはできません。
      - つまり `<このぶぶん>` や `<tag param="このぶぶん">`、`<script>このぶぶん</script>` のような用途を考慮する必要はありません。

この関数を記述するのに、XSS(Cross Site Scripting) の脆弱性が混入しないように、一部の文字に対してエスケープ処理を行う必要があると考えました。

## [3-1]

以下に `render_html` の実装を示します。エスケープ処理として不足している文字が1文字以上あります。その文字を以下から選択してください。

1. `#`
2. `!`
3. `&`
4. `'`
5. `"`

## 関数（Python3.x）

```Python
import re
from typing import Dict

def render_html(tmpl: str, params: Dict[str, str]) -> str:
    def repl(matchobj):
        name = matchobj.group(0)[2:-2]
        value = params[name]
        value = value.replace('<', '&lt;')
        value = value.replace('>', '&gt;')
        return value
    return re.sub(r'<%[a-z]+%>', repl, tmpl)
```

## [3-2]

不足している文字をエスケープする処理を追加するのに適切な場所として、何行目の直後が良いか答えてください。行番号の数え方は、先頭行（ `import re` の行）を1行目として数えてください。
