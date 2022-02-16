# a_pinyin-data
<https://github.com/fm-elpac/a_pinyin-data>

[![build](https://github.com/fm-elpac/a_pinyin-data/actions/workflows/ci.yml/badge.svg)](https://github.com/fm-elpac/a_pinyin-data/actions)

A拼音 c1 核心的数据及相关工具.

+ 文档: <https://github.com/fm-elpac/a_pinyin>


## 下载内置数据库

此部分说明一般适用于普通用户.

TODO 下载 a_pinyin-apk 所需的内置数据库安装文件 `a_pinyin-2.zip`

TODO 尚未完成


## 编译运行

此部分说明一般适用于开发者.

+ 使用 [rustup](https://www.rust-lang.org/tools/install) (rust/cargo)

  ```sh
  rustup target add wasm32-wasi
  ```

+ 下载 Unicode 14.0 数据 (只需一次)

  ```sh
  make u14
  ```

+ 编译 (apd 工具及 a_pinyin-2.zip)

  ```sh
  make
  ```


## 目录结构

本仓库的目录结构安排如下:

```
+ a_pinyin-data/  本仓库根目录

  + apd/          数据处理工具 apd 的源代码 (rust)

  + data1/        一类数据, 比较靠谱
    + u14/          Unicode 14.0[1] 的原始数据, 直接下载
    + fix/          手动修复数据
    + raw/          由 apd 工具生成的重要中间数据

  + data2/        二类数据, 不靠谱
    + v1/           来自 A拼音 1.x 的数据

  + out/          生成的内置数据库文件 a_pinyin-2.zip
```

+ [1] [Unicode 14.0.0](https://www.unicode.org/versions/Unicode14.0.0/)


## apd 命令

数据处理工具 apd 的使用说明.
apd 具有以下命令:

+ `apd --版本` <br />
  `apd --version`

  显示工具版本号.

+ `apd --帮助` <br />
  `apd --help`

  显示命令行用法.

+ `apd 解析u14a`

  从 Unicode 14.0 中提取基础数据 (比如拼音数据, 汉字数据等),
  生成 `data1/raw` 相关文件.

+ `apd 解析u14b`

  从 Unicode 14.0 中提取数据, 用于 Unicode 小工具功能 (Unicode 内置数据库)

+ `apd 生成2db`

  组装生成 `a_pinyin-2.db` 内置数据库文件.

  注意: 进一步压缩生成 `a_pinyin-2.zip` 文件需要另外使用 `zip` 命令.

+ `apd 导入v1`

  导入 A拼音 1.x 的用户数据库, 尽量保留用户数据,
  生成 `a_pinyin-2u.db` 用户数据库.

+ `apd 合并2u`

  多设备同步之后的用户数据库合并, 生成 `2u_合并.db`.


## 友情链接

TODO


## LICENSE

[`CC-BY-SA 4.0+`](https://creativecommons.org/licenses/by-sa/4.0/)

本仓库的内容使用 创意共享-署名-相同方式共享 (CC-BY-SA 4.0) 许可证 (LICENSE).
This repository is released under Creative Common (CC-BY-SA 4.0) license.
