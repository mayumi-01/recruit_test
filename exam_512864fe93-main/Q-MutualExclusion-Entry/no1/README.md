# 問1

それぞれのユーザがポイントを保持しており、ユーザ間でのポイントのやりとりができるようなポイント口座システムを考えます。どのユーザも、保持しているポイントは常に非負整数でなければなりません。

はじめに、ユーザのポイント口座を表すクラス `Account` と、所定の量のポイントをある口座から別の口座へ移す関数 `transfer` を以下のように定義しました。

```python
class Account:
    def __init__(self, initial_point: int):
        self.point = initial_point


def transfer(account_from: Account, account_to: Account, amount: int) -> bool:
    if account_from.point >= amount:
        account_from.point -= amount
        account_to.point += amount
        return True
    else:
        return False
```

実際にこれらを利用するシステムでは、複数のスレッドが `Account` のインスタンスを共有し、同時に `transfer` 関数を呼び出す可能性があります。このとき、以下の各問題に答えてください。

## 問題A

いま、2 つのポイント口座 `a` と `b` が次のように初期化されているとします。

```python
a = Account(80)
b = Account(0)
```

これに対し、2 つのスレッドが同時に実行を開始し、それぞれ以下のような処理を行います。

- スレッド 1: `transfer(a, b, 40)` を呼び出し、その戻り値を変数 `X` に保存する
- スレッド 2: `transfer(a, b, 50)` を呼び出し、その戻り値を変数 `Y` に保存する

両スレッドの処理が完了したあとの `X` や `Y` の値はスレッド間の処理の実行順序やタイミングによって変わることがありえます。組 `(X, Y)` としてありうるものを以下の選択肢から**すべて**選んでください。

1. `(False, False)`
2. `(False, True)`
3. `(True, False)`
4. `(True, True)`

## 問題B

現状の実装には、複数のスレッドが同時に `transfer` 関数を呼び出したときに制約 (どのユーザの保持するポイントも非負整数でなければならない) が満たされなくなるという問題があることがわかりました。そこで、`Account` の実装を次のように変更し、新たに `transfer_safe` 関数を定義しました。

```python
import threading


class Account:
    def __init__(self, initial_point: int):
        self.point = initial_point
        self.lock = threading.Lock()


def transfer_safe(account_from: Account, account_to: Account, amount: int) -> None:
    account_from.lock.acquire()
    account_to.lock.acquire()
    transfer(account_from, account_to, amount)
    account_to.lock.release()
    account_from.lock.release()
```

これらを利用するシステムでは旧来の `transfer` 関数を使わず、すべて `transfer_safe` 関数を使うことにしました。

これにより、口座の制約が満たされなくなるといった問題は回避することができました。しかし、新たに全体の処理が正常に進まなくなるような問題が起こりうることがわかりました。その起こりうる新たな問題として、上記のコードから読み取れる最も適切なものは以下のうちどれですか。

1. 競合状態 (レースコンディション)
2. デッドロック
3. ライブロック
4. スラッシング

## 問題C

問題を解決するため、`transfer_safe` 関数の実装を以下のように変更しました。

```python
import time


def transfer_safe(account_from: Account, account_to: Account, amount: int) -> None:
    account_from.lock.acquire()
    while not account_to.lock.acquire(blocking=False):
        account_from.lock.release()
        time.sleep(0.01)
        account_from.lock.acquire()
    transfer(account_from, account_to, amount)
    account_to.lock.release()
    account_from.lock.release()
```

残念ながら、この変更を行ったあとも、全体の処理が正常に進まなくなるような問題が起こりうることがわかりました。その起こりうる問題として、上記のコードから読み取れる最も適切なものは以下のうちどれですか。

1. 競合状態 (レースコンディション)
2. デッドロック
3. ライブロック
4. スラッシング
