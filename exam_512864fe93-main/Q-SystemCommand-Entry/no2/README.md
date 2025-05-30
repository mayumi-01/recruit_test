# 問2

以下の文章を読み、（A）〜（G）に当てはまるものを選択肢から選んでください。

あなたが運用しているシステムではユーザのイベントログを異なる2つの経路を通じてデータ基盤に転送しています。片方はメインデータとして別のシステムに利用されます。もう片方はバックアップデータとして保存されます。

メインデータとバックアップデータは理想的には同じ内容であるべきですが、通信エラーやシステム障害などの影響で両データともにデータ欠損が発生する可能性があり、稀に内容が異なることがあります。あなたはある時間枠に発生したイベントログを両データから抽出し、それらを比較することにしました。

抽出されたデータはそれぞれ、`main.txt`、`backup.txt`という名前のファイルに保存されています。これらのファイルにはログID（各イベントログに付与される一意なIDでアルファベットと数字のみから成り立つ文字列）のみが行区切りで出力されています。ファイル内には無駄な空行は含まれません。また、重複するログIDが複数行に出力されることはないとします。

まずあなたは2つのファイルの内容が同じであるかどうかチェックするために以下のコマンドを実行しました。

```
$ (A) main.txt backup.txt
```

その結果2つのファイルが異なることが分かったので、以下のコマンドを実行して2つのファイルの行数を比較することにしました。

```
$ (B) main.txt backup.txt
```

上記のコマンドを実行した結果、`backup.txt`の方が行数が多いことが分かりました。この時点であなたは (C) と判断しました。

さらに詳細な調査をするために以下のコマンドを実行し、メインデータにのみ含まれるログ、バックアップデータにのみ含まれるログ、両方に含まれるログのログIDを抽出することにしました。

```
$ cat main.txt main.txt backup.txt >tmp.txt
$ cat tmp.txt | (D) | (E) | awk '$1==2 {print $2}' > main_only.txt
$ cat tmp.txt | (D) | (E) | awk '$1==1 {print $2}' > backup_only.txt
$ cat tmp.txt | (D) | (E) | awk '(F) {print $2}' > both.txt
```

生成されたファイルを確認したところ、`main_only.txt`のみ空であることが分かりました。このことから、あなたは調査対象の時間枠においては (G) と判断しました。

#### 選択肢A
  1. `head`
  1. `cmp`
  1. `ls`
  1. `tail`

#### 選択肢B
  1. `wc -c`
  1. `cat -v`
  1. `cat -s`
  1. `wc -l`

#### 選択肢C
  1. メインデータではログの欠損は発生していない
  1. メインデータでログの欠損が発生している
  1. バックアップデータではログの欠損は発生していない
  1. バックアップデータでログの欠損が発生している

#### 選択肢D
  1. `sort`
  1. `grep 'id'`
  1. `diff`
  1. `awk '{print $1}'`

#### 選択肢E
  1. `cat -n`
  1. `diff`
  1. `awk '{print cnt[$1]}'`
  1. `uniq -c`

#### 選択肢F
  1. `$1==0`
  1. `$1==3`
  1. `$2==1`
  1. `$2==2`

#### 選択肢G
  1. メインデータのみでログの欠損が発生している
  1. バックアップデータのみでログの欠損が発生している
  1. メインデータでログの欠損が発生しているかどうかは断言できないが、バックアップデータではログの欠損は発生していない
  1. メインデータではログの欠損が発生しているが、バックアップデータでログの欠損が発生しているかどうかは断言できない