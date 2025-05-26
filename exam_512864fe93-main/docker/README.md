# ローカル開発用Docker環境

言語ごとに、採点環境に近い環境を再現したDockerfileを用意しています。開発のためにお使いください。

ただし、採点が実行される環境と全く同一の挙動であることは保証しません。

このリポジトリのトップをカレントディレクトリとして、以下のようにイメージをビルドして使用してください。

例（Goの場合）:
```
$ docker build --platform linux/amd64 -t local_tester -f docker/go/Dockerfile docker/go
$ docker run --rm -it -v $(pwd):/work -w /work local_tester

以降、docker内で必要な操作を行う
```


## Windowsユーザーの方へ

Windowsの場合、`$(pwd)`の代わりにカレントディレクトリの絶対パスをUNIX形式に変換したものを書いてください。

例：`c:¥Users¥user1¥src`のUNIX形式は`/c/Users/user1/src`になります。


## Apple Silicon MacでPythonを使用する方へ

ライブラリの互換性のため、Dockerfileが2通りに分かれています。次のようにイメージをビルドしてください。

### PyTorchを使わない場合

次のように、 `Dockerfile_mac` を使用して --platform を指定せずにビルドしてください。
```
$ docker build -t local_tester -f docker/python/Dockerfile_mac docker/python
```

この環境では、PyTorchは正常にインストールできないため除かれています。

### PyTorchを使う場合

次のように、 `Dockerfile_mac_torch` を使用してビルドしてください。
```
$ docker build --platform linux/amd64 -t local_tester -f docker/python/Dockerfile_mac_torch docker/python
```

この環境では、TensorFlowは正常に動作しないため除かれています。

amd64エミュレートでのビルドのため、実行が遅くなることに留意してください。
