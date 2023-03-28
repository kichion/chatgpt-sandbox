# 0. python 環境の準備

asdf を使って Python と pip をインストールする方法を説明します。まずは asdf をインストールし、Python プラグインを追加する必要があります。

## 1. asdf のインストール

asdf をインストールします。

refs: https://asdf-vm.com/

## 2. asdf plugin のインストール

以下のコマンドを使用して、Python プラグインを追加します。

```bash
$ asdf plugin add python
```

## 3. python インストール

利用したい Python バージョンをインストールするには、以下のコマンドを実行します。ここでは、Python 3.11.2 を例にします。

```bash
$ asdf install python 3.11.2
```

インストールした Python バージョンをデフォルトで使用するように設定するには、以下のコマンドを実行します。

```bash
$ asdf global python 3.11.2
```

## 4. pip の確認

Python が正しくインストールされ、pip が利用可能か確認するには、以下のコマンドを実行します。

```bash
$ python --version
$ pip --version
```

# 1. 実行ライブラリのインストール

Steamlit を使って、ChatGPT API を使用した自分用の ChatGPT を作成するための実装例を以下に示します。まずは必要なライブラリをインストールしてください。

```bash
$ pip install streamlit openai streamlit-chat
```

# 2. アプリケーション実行

OPENAI_API_KEY が環境変数から取得されます。環境変数に API キーを設定して、アプリを起動してください。


## a. インスタントチャットアプリ

文脈の指定と一つの質問に対して一つの回答のみを扱うアプリケーションです

```bash
$ OPENAI_API_KEY=sk-****************************** streamlit run instant.py
```

## b. ChatGPTライクアプリ

同じタイムラインにおいては文脈を続けてコミュニケーションするアプリケーションです（ChatGPTもどき）

```bash
$ OPENAI_API_KEY=sk-****************************** streamlit run engineer_chat.py
```
