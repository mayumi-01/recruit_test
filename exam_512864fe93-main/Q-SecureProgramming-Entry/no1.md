# 小問1

## [1-1]

商品名（任意の文字列）をもとに、一致する商品リストを返す`get_items(c, params)`という関数の作成を依頼されました。
​
- 与えられた商品名と一致する商品が存在する場合はそれらの商品リストを返し、存在しない場合は空のリストを返します。
- 第1引数`c`は `sqlite3` データベースのカーソルオブジェクトが渡されます。
- 第2引数`params`はブラウザから送られてきたパラメータがそのまま渡されます。
- ユーザーが指定した商品名は`params['name']`で取り出すことができます。
- 商品情報は`items`というテーブルで管理されており、`name`というカラムに商品名が入っています。
​
このとき、以下の関数内の`#### CODE ####`に入る最も適切なコードを、選択肢の中から選んでください。
​
## 関数（Python3.x）

```Python
def get_items(c, params):
	name = params['name']
	#### CODE ####
	return c.fetchall()
```

## 選択肢

1. `c.execute(f'SELECT * FROM items WHERE name = "{name}"')`
2. `c.execute('SELECT * FROM items WHERE name = "' + name + '"')`
3. `c.execute('SELECT * FROM items WHERE name = ?', (name,))`
4. `c.execute('SELECT * FROM items WHERE name = "%s"' % name)`
5. `c.execute('SELECT * FROM items WHERE name = "name"')`
6. `c.execute('SELECT * FROM items WHERE name = ?', (re.escape(name),))`
