# 小問2

## [2-1]

商品ID（任意の整数）をもとに、一致する商品の説明文を返す`get_description(params)`という関数の作成を依頼されました。

- 与えられた商品IDと一致する説明文が存在する場合はその説明文を返し、存在しない場合は空の文字列を返します。
- 引数`params`はブラウザから送られてきたパラメータがそのまま渡されます。
- ユーザーが指定した商品IDは`params['id']`で取り出すことができます。
- 商品の説明文は所定のディレクトリに商品IDそのままのファイル名で格納されており、それを読み込む必要があります。

このとき、以下の関数内の`#### CODE ####`に入る最も適切なコードを、選択肢の中から選んでください。

## 関数（Python3.x）

```Python
def get_description(params):
	desc_path = 'data/descriptions'
	id = params['id']
	#### CODE ####
	description = ''
	if os.path.isfile(path):
		f = open(path, 'r')
		description = f.read()
		f.close()
	return description
```

## 選択肢

1. `path = desc_path + '/' + id`
2. `path = os.path.join(desc_path, id)`
3. `path = os.path.join(desc_path, '/', id)`
4. `path = os.path.join(desc_path, os.path.basename(id))`
5. `path = os.path.join(desc_path, os.path.abspath(id))`
6. `path = os.path.join(desc_path, os.path.relpath(id))`
