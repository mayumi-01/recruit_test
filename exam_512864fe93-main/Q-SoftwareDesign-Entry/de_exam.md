適切なソフトウェアの設計について以下の問に答えてください。

---


地球上のさまざまな地点の座標が `input.txt` という名前のテキストファイルで与えられます。
`input.txt` には、1行につき1地点の緯度と経度が、下記のような形式で与えられています。
```file
36.112N139.1E
36.112N131.1W
10S97.332E
35N179.9E
35N179.9W
..
```
このとき、`"36.112N139.1E"` は、北緯36.112度、東経139.1度の地点を表します。
あなたは、この中からもっとも東京(北緯35.6度,東経139.7度)に近い点を探すプログラムを書こうと思っています。

二つの緯度と経度から距離を求める手法には球面三角法などが知られています。
あなたはこれを使って、まず下記のようなプログラムを書きました。

```python
import re
import math

def func1(input_file: str):
    with open(input_file, "r") as f:
        md = 100000000
        r = ""
        for line in f.readlines():
            reg = re.compile('([\d\.]+[NS])([\d\.]+[EW])')
            m = reg.match(line.strip())
            # 緯度を取り出す
            if m.group(1)[-1] == "N":
                latitude = float(m.group(1)[0:-1])
            else:
                latitude = -float(m.group(1)[0:-1])

            # 経度を取り出す
            if m.group(2)[-1] == "E":
                longitude = float(m.group(2)[0:-1])
            else:
                longitude = -float(m.group(2)[0:-1])

            # 東京との距離を計算する。地球が完全な球面であることを仮定している。
            # Haversine 公式を利用
            d = 6371 * 2 * math.asin(math.sqrt(
                math.sin((latitude * math.pi / 180 - 35.6 * math.pi / 180) / 2 )**2
                + math.cos(latitude * math.pi / 180) * math.cos(35.6 * math.pi / 180) * math.sin((longitude * math.pi / 180 - 139.7 * math.pi / 180) / 2)**2
            ))
            if d < md:
                md = d
                r = line
        return r

print(func1("input.txt"))
```

このコードを改善しようと思います。


## 問1

コードの問題点と、改善のための書き換え例について、可読性や保守性の観点から**適切でない**点をひとつ選んでください。

1. 地球の半径の値がハードコーディングされてしまっているため、意味合いが不明確になってしまっている。`EARTH_RADIUS=6371` といった変数に分離すべきである。
2. 度をラジアンに変換するために `math.pi / 180` という式が何度も記述されており、コードが冗長であるのみならず、無駄な計算を何度も行ってしまっている。事前に計算し `latitude = float(m.group(1)[0:-1]) * 0.017453844` のように書き換えることで簡潔に記述するべきである。
3. `md`という変数名, `func1` というメソッド名などが適切な名前にはなっていない。それぞれ `min_distance`, `find_nearest_point` のような名前に改めるべきである。
4. もっとも近い点の探索には距離の大小のみ分かればよく、実際の距離を算出する必要はないので、`6371 * 2 * ` の掛け算は削除しても正しく動作するが、その場合は"東京との距離を計算する"のコメントは改めるべきである。

## 問2

次に、問1のコードに手を加え、以下のように修正しました。
このコードを読み、以下の問に答えてください。

```python
import re
import math

def func2(lat1: float, long1: float):
    # 東京との距離を計算する。　地球が完全な球面であることを仮定している。
    # Haversine 公式を利用
    lat1 = func3(lat1)
    long1 = func3(long1)

    lat_tokyo = 35.6
    long_tokyo = 139.7
    lat2 = func3(lat_tokyo)
    long2 = func3(long_tokyo)
    return 6371 * 2 * math.asin(math.sqrt(
        math.sin((lat1 - lat2) / 2 )**2 + math.cos(lat1) * math.cos(lat2) * math.sin((long1 - long2) / 2)**2
    ))

def func3(x: float):
    return x * math.pi / 180.0

def func1(input_file: str):
    with open(input_file, "r") as f:
        md = 100000000
        r = ""
        for line in f.readlines():
            reg = re.compile('([\d\.]+[NS])([\d\.]+[EW])')
            m = reg.match(line.strip())
            # 緯度を取り出す
            if m.group(1)[-1] == "N":
                latitude = float(m.group(1)[0:-1])
            else:
                latitude = -float(m.group(1)[0:-1])

            # 経度を取り出す
            if m.group(2)[-1] == "E":
                longitude = float(m.group(2)[0:-1])
            else:
                longitude = -float(m.group(2)[0:-1])

            d = func2(latitude, longitude)
            if d < md:
                md = d
                r = line
        return r

print(func1("input.txt"))
```

可読性の観点から、いくつかの関数を適切な名前に改め、 関数の機能を過不足なく表すように改善したいと思います。

#### 問2-1
`func2` の適切な名前として最も適切であると考えられるものを次から選択してください。

1. `haversine_formula`
2. `get_distance`
3. `get_distance_from_tokyo`
4. `between_two_points`

#### 問2-2
`func3` の適切な名前として最も適切であると考えられるものを次から選択してください。

1. `get_degree`
2. `get_radian`
3. `times_pi_divided_by_180`

## 問3

問2のような書き換えを行う理由や、この書き換えによってもたらされる効果として適切なものを2つ選択してください。

1. 複雑な距離計算についての処理を関数に分離することで、距離計算の自動テストを記述しやすくなる効果がある。
2. 複雑な距離計算についての処理を関数に分離することで、`func1` の実装の詳細を隠蔽し、意図しない方法での`func1`の呼び出しを防ぐ効果がある。
3. 関数の平均的な長さが短くなるため、処理を高速化する効果がある。
4. 他の距離計算アルゴリズムに変更する際に、書き換えが容易になる効果がある。

## 問4

問2のコードに更に手を加え、ファイルを読み取る部分を `read_points` 関数に切り出し、下記のように書き換えることを考えます。
なおこのコード例において、問2における `func2`,`func3` およびimport文は省略されています。

```python
def read_points(input_file: str):
    result = []
    reg = re.compile('([\d\.]+[NS])([\d\.]+[EW])')
    with open(input_file, "r") as f:
        for line in f.readlines():
            m = reg.match(line.strip())
            if m.group(1)[-1] == "N":
                latitude = float(m.group(1)[0:-1])
            else:
                latitude = -float(m.group(1)[0:-1])

            if m.group(2)[-1] == "E":
                longitude = float(m.group(2)[0:-1])
            else:
                longitude = -float(m.group(2)[0:-1])
            result.append((line, latitude, longitude))
    return result

def func(input_file: str):
    r = ""
    md = 100000000
    for (line, latitude, longitude) in read_points(input_file):
        d = func2(latitude, longitude)
        if d < md or md is None:
            md = d
            r = line
    return r

print(func("input.txt"))
```

このような書き換えによってもたらされる効果として、**適切でない**ものをひとつ次から選んでください。

1. `re.compile` の行をforループの外側に出すことで処理が高速化される効果がある。
2. 緯度と経度を読み込む処理を `read_points` 関数に分離することで、今後入力ファイルフォーマットの仕様が変更された場合に、書き換えが容易になる効果がある。
3. ファイルの読み取り処理を関数に分離することで、`input.txt` に予期しない文字列が混ざっていた場合にもエラーが出にくくなる効果がある。
4. 経緯度の情報をすべてメモリに乗せるため、メモリ効率がやや悪化する効果がある。
