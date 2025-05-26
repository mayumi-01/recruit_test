# スキルチェックに関する注意事項
まずは下記の注意事項をお読みください。

## 最終提出
最終提出は最終提出ページにて、「提出する」ボタンを押していただくと完了します。  
※最終提出に関する詳細は、以下の [解答方法について](#解答方法について) をご覧ください。  
[最終提出ページへ](https://recruit-litmus.jp/r/submit?token=5949c862-8272-439e-a852-2678d08853d1)

## 解答いただく問題について
* どの問題に必須で解答いただくかは、ご希望の職種によって異なります。ご自身の強みを一番発揮できると思われる職種を選択してください。
* 職種の併願も可能ですので、その場合は各職種ごとで指定されている必須問題に全て解答するようにしてください。
* 各問題は、問題名に対応するディレクトリに格納されています。問題内容の詳細はそちらをご覧ください。

職種名 | 説明 | 必須問題
:---- | :----------------------- | :--------------
`MLE` | 機械学習エンジニア<br/>機械学習の予測モデル構築・実装が得意な方向け。<br/>Keyword：機械学習,自然言語処理,深層学習,予測,レコメンド | [`Q-StatisticalEvaluation-Entry`](Q-StatisticalEvaluation-Entry)<br/>[`Q-DefaultPrediction-Entry`](Q-DefaultPrediction-Entry)<br/>[`Q-AssociationAnalysis-Entry`](Q-AssociationAnalysis-Entry)<br/>[`Q-DataApplicationDesign-Entry`](Q-DataApplicationDesign-Entry)<br/>[`Q-MemoryLimited-Entry`](Q-MemoryLimited-Entry)<br/>[`Q-SystemCommand-Entry`](Q-SystemCommand-Entry)
`DE` | データエンジニア<br/>データパイプライン構築やデータプロダクト開発が得意な方向け。<br/>Keyword：アーキテクチャ設計,ネットワーク,セキュリティ,データ構造・アルゴリズム,データ指向アプリケーション,機械学習 | [`Q-DataApplicationDesign-Entry`](Q-DataApplicationDesign-Entry)<br/>[`Q-MemoryLimited-Entry`](Q-MemoryLimited-Entry)<br/>[`Q-SystemCommand-Entry`](Q-SystemCommand-Entry)<br/>[`Q-SecureProgramming-Entry`](Q-SecureProgramming-Entry)<br/>[`Q-MutualExclusion-Entry`](Q-MutualExclusion-Entry)<br/>[`Q-SoftwareDesign-Entry`](Q-SoftwareDesign-Entry)
`DS` | データサイエンティスト<br/>課題の定式化、数理モデルの構築が得意な方向け。<br/>Keyword：確率統計,数理最適化 | [`Q-StatisticalEvaluation-Entry`](Q-StatisticalEvaluation-Entry)<br/>[`Q-DefaultPrediction-Entry`](Q-DefaultPrediction-Entry)<br/>[`Q-AssociationAnalysis-Entry`](Q-AssociationAnalysis-Entry)<br/>[`Q-EstimationTheory-Entry`](Q-EstimationTheory-Entry)<br/>[`Q-Mathematics-Entry`](Q-Mathematics-Entry)


## 解答方法について

希望職種の必須問題に期限内に解答して `最終提出` してください。解答作成にあたり、Webや書籍などで調査を行っても構いません。

* `提出` : mainブランチへのpush、 または mainブランチへ向けた pull request をマージすること
* `提出物` : mainブランチにおける各問題ディレクトリ以下のファイル
  * 各問題で指定される通りのファイルを含めてください
* `採点` : `提出` のたびにシステムが `提出物` を評価すること
  * 回数に制限（連続する24時間で最大5回まで）がありますのでご注意ください
* `フィードバック` : `提出` 後にこのリポジトリに作成されるissueに対し、通常10分-1時間ほどで追加されるコメントのこと
  * `フィードバック` は、 `https://github.com/recruit-skillcheck/exam_512864fe93/issues` から確認できます。必要に応じて確認し解答を修正してください
  * 文面の詳細・意味は問題によるので、各問題文を参照してください
  * 締切直前はサーバーが混み合い `フィードバック` により長い時間がかかる可能性がありますので、余裕を持って `提出` いただくようお願いいたします
  * `提出` を行ったにも関わらず、`フィードバック` が5時間以上ない場合は、本スキルチェックの案内メールに記載されている問い合わせ先までご連絡ください
* `最終提出` : その時点で最終の `提出` を、スキルチェックの最終的な`提出物`として確定させること
  * `方法`: [こちらのリンク](https://recruit-litmus.jp/r/submit?token=5949c862-8272-439e-a852-2678d08853d1)から最終提出ページに遷移し、「提出する」ボタンを押していただくと完了します
  * `最終提出` 後、この`提出物`の`採点`が行われ、最終的な採点結果となります。この時の `採点` は、回数制限の影響は受けず、必ず1度行われます。
  * `最終提出` 以外の `提出` は、最終的な結果には影響ありません
  * `フィードバック`が作成される前でも`最終提出`は可能です
  * `採点` の結果とは別に、こちらのリポジトリの内容を参考資料として利用する場合があります
  * 一度 `最終提出` が完了すると、スキルチェック用のリポジトリは閲覧・変更できなくなりますので、十分確認のうえ実行してください
  * 期限内に `最終提出` が行われなかった場合は、最後の `提出` が `最終提出` とみなされます

### 提出するファイルの文字コード・改行コードについて

提出するファイルの文字コードはUTF-8、改行コードは `\n`(LF) としてください。
リポジトリ内に配置されたサンプルコードや解答フォーマットはいずれもこの文字コード、改行コードを使っていますが、
Windows OSをご利用の場合、自動的にOSやアプリケーションが他の文字コードや改行コードに変更してしまうことがありますのでご注意ください。
Windows OSをご利用の場合は最初に以下のコマンドを実行し、コミット時に CRLF を LF に変換する設定にすることを推奨します。
```sh
git config --global core.autocrlf input
```

### ファイルサイズの制限について

リポジトリには、解答に必要なファイルのみを追加するようにしてください。

リポジトリ内のファイルサイズの合計が 250MB を超えていた場合、 `提出` されても `採点` を行いません。
この値は十分余裕を持った制限であり、問題の想定する方法で解答を追加するのであれば、全く気にする必要はないものです。

### mainブランチへ push するためのコマンド例

```sh
git clone https://github.com/recruit-skillcheck/exam_512864fe93
cd exam_512864fe93

# 上のコマンドははじめに１度だけ行えば良い。修正して解答し直す場合には、修正したファイルについて以下のコマンドを実行する。
# 解答のファイルを作成・編集する
git add (作成・編集したファイルのパスをここに書く)
git add (作成・編集したファイルが複数ある場合は全てに対して git add を実行する)
git commit -m '解答追加'
git push origin main
```

## コードの実行環境について
コード実行環境の詳細は問題によるので、各問題ディレクトリ内を参照してください。

### 共通事項
* cpu: 2 vCPU
* インターネットには接続できません
* 1GB以上のストレージ領域は保証されません

### コンパイル方法

コードを提出する問題では、 `run.sh` というスクリプトでプログラムの実行コマンドを指定する形式になっています。

`build.sh` という名前のファイルを `run.sh` と同じディレクトリに置いておくと、 `run.sh` を実行する前に `build.sh` が実行されます。コンパイルする言語を使用する場合は、 `build.sh` でプログラムをコンパイルして、 `run.sh` でその生成物を使用するようにしてください。

複数のテストデータがある問題では `run.sh` が複数回実行されますが、 `build.sh` はその前に1度だけ実行されます。

例：C++を使う場合

`build.sh`
```sh
#!/bin/sh -eu

g++ -O2 -o main main.cpp
```

`run.sh`
```sh
#!/bin/sh -eu

./main
```

### 使用可能言語について
使用可能言語は下記の通りです。これ以外の言語でご解答いただいても採点ができませんのでご注意ください。
各言語の標準ライブラリが使用可能です。

* Python (3.11)
  * `python` コマンドが使用可能です
* C / C++ (gcc11)
  * `gcc`, `g++` コマンドが使用可能です
* Go (1.21)
  * `go` コマンドが使用可能です
* Java (21)
  * `javac`, `java` コマンドが使用可能です
* Ruby (3.3)
  * `ruby` コマンドが使用可能です
* Node.js (20)
  * `node` コマンドが使用可能です
* SQLite (3.40)
  * `sqlite3` コマンドが使用可能です

Pythonでは標準ライブラリに加え、次のライブラリが使用可能です。

<details><summary>Pythonライブラリ</summary>

* catboost (1.2.2)
* joblib (1.3.2)
* keras (2.14.0)
* lightgbm (4.3.0)
* numpy (1.26.3)
* optuna (3.5.0)
* pandas (2.2.0)
* pyyaml (5.3.1)
* scikit-learn (1.4.0)
* scipy (1.12.0)
* tensorflow-cpu (2.14.1)
* torch (2.2.0+cpu)
* werkzeug (3.0.1)
* xgboost (2.0.3)

</details>

[docker](docker/) ディレクトリ以下に言語ごとの Dockerfile を置いていますので、ローカル環境での動作確認に利用いただいてもかまいません。

詳細は [docker/README.md](docker/README.md) をご覧ください。


## 禁止事項
* 著作権違反・ライセンス違反となるようなコードの使用
* 外部への試験問題の流出・公開

## プライバシーポリシー

本スキルチェックのプライバシーポリシーは[こちら](https://recruit-litmus.jp/r/privacy_policy/51)からご確認いただけます。

## お問い合わせ
* ご案内した方法で提出ができない等不具合が生じた場合は、お手数ですが本スキルチェックの案内メールに記載されている問い合わせ先までご連絡ください
* 問題の内容について等、採点結果に影響するご質問にはお答えできませんのでご了承ください
