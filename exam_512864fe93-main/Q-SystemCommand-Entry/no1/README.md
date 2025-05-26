# 問1
`git` コマンドの使い方に関する以下の問題に答えてください。

## 小問A
`add/new_feature` というブランチを新たに作成し、カレントブランチを `add/new_feature` に切り替えたいときに使うコマンドとして適切なものを選択してください。

  1. `git checkout add/new_feature`
  1. `git fetch add/new_feature`
  1. `git checkout -b add/new_feature`
  1. `git branch -f add/new_feature`
   

## 小問B
カレントブランチの最新のコミットの変更内容を確認したいときに使うコマンドとして適切なものを選択してください。

  1. `git diff HEAD HEAD`
  1. `git diff`
  1. `git diff HEAD`
  1. `git diff HEAD^ HEAD`

## 小問C
`git commit --amend` に関する説明として正しいものを選択してください。

  1. ステージし忘れたファイルを追加することはできない。
  1. リモートレポジトリにプッシュ済みのコミットを修正することはできない。
  1. コミットメッセージだけを修正することはできない。
  1. 最新でない古いコミットを修正することはできない。

## 小問D
`issue/1` というブランチを `main` ブランチにマージする際の手順として適切なものを選択してください。

  1. `git checkout main` で `main` ブランチにチェックアウトした後、`git merge issue/1` を実行する。
  1. `git checkout issue/1` で `issue/1` ブランチにチェックアウトした後、`git merge main` を実行する。
  1. `git merge issue/1` を実行した後、`git checkout main` で `main` ブランチにチェックアウトする。
  1. `git merge main` を実行した後、`git checkout issue/1` で `issue/1` ブランチにチェックアウトする。
