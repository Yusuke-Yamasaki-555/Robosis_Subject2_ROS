# Robosis_Subject2_ROS
---
## 概要
- このリポジトリは、ROSを用いて素数の倍数を探索・判定し出力するプログラムのパッケージです。対応している素数は２～２９までの、計１０個となっています。
---
## 動作確認環境
- 機種：Raspberry Pi 3B+
- OS：Ubuntu 20.04.3 LTS
- 容量：microSD 16GB
- ROS：noetic 1.15.13
---
## 実行手順
### 0.環境構築
- このパッケージは、ROS noetic上での動作を前提として作成されています。事前にROS noeticの環境を整えてください。
- (作成時の環境では、Ryuichi Ueda様から公開されている[こちらのインストーラ](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server)を使用しました)
- ROS noeticの環境が整い次第、ワークスペースの準備を行ってください。作成時の環境では、Ryuichi Ueda様から公開されている[こちら](https://github.com/Yusuke-Yamasaki-555/robosys2020/blob/master/md/ros.md#%E3%83%AF%E3%83%BC%E3%82%AF%E3%82%B9%E3%83%9A%E3%83%BC%E3%82%B9%E3%81%AE%E6%BA%96%E5%82%99)を参考に行いました。
- その後、このリポジトリをcloneしてください。
```bash
$ cd ~/catkin_ws/src/
$ git clone git@github.com:Yusuke-Yamasaki-555/Robosis_Subject2_ROS.git # ssh通信の場合
# $ git clone https://github.com/Yusuke-Yamasaki-555/Robosis_Subject2_ROS.git # https通信の場合
```
- clone後、コンパイル＆ターミナル初期化を行ってください。
```bash
$ cd ~/catkin_ws/
$ catkin_make
$ source ~/.bashrc
```
### 1.実行
- 以下のようにlaunchファイルを実行することで、プログラムを実行することが出来ます。
```bash
$ roslaunch robosis_subject2_ros start.launch
```
- 実行すると以下の画像のように、行に数字、列に素数が対応した表が永遠に出力されます。数字が素数の倍数となっていれば"●"が付くようになっています。

![image](https://user-images.githubusercontent.com/91410662/148417419-fcda2594-170c-4b53-b482-1a0460ac1fa4.png)

- 実際に実行した際の様子は[こちら](https://www.youtube.com/watch?v=RPXsHVRuDxc)(パッケージの名前が実際とは異なっていますが、実行内容に差異はありません)
- プログラムを終了する際は、Ctrl+Cを入力してください。
---
## ライセンスについて
- このリポジトリは、**MIT License**をライセンスとしています。詳細は**LICENSE**ファイルをご参照ください。
- このリポジトリに含まれるプログラムには、Ryuichi Ueda様から公開されている[こちら](https://github.com/Yusuke-Yamasaki-555/robosys2020/blob/master/md/ros.md)に記載されているプログラムコードを含んでいます。プログラムの著作権については、各プログラムの著作権表示と**package.xml**をご確認ください。
